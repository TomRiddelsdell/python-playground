'''
We want to simulate requesting batches of market data as the requirements arise. 
A batch should be triggered only we hit the equivalent of a purple child.'
We should be careful that we can capture all known dependencies at any point in time, including those in the future.


A good case is the iSelect case. Here we have a dep on each of the underliers unless their weight is zero.
We only know the weight on day T
'''
import datetime as dt
import concurrent.futures
import pandas as pd
from random import random
import ast
import operator
import time
import astpretty
import matplotlib.pyplot as plt

    

# Function to simulate a long-running task
def resolve_future_value(x):
    time.sleep(2)  # Simulate a time-consuming operation
    return x * 2

# Base class for all operation nodes
class OperationNode(ast.AST):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    # Overload operators for operation nodes
    def __add__(self, other):
        if isinstance(other, OperationNode):
            return AdditionNode(self, other)
        return AdditionNode(self, ValueNode(other))

    def __sub__(self, other):
        if isinstance(other, OperationNode):
            return SubtractionNode(self, other)
        return SubtractionNode(self, ValueNode(other))

    def __mul__(self, other):
        if isinstance(other, OperationNode):
            return MultiplicationNode(self, other)
        return MultiplicationNode(self, ValueNode(other))

    def __truediv__(self, other):
        if isinstance(other, OperationNode):
            return DivisionNode(self, other)
        return DivisionNode(self, ValueNode(other))

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rtruediv__(self, other):
        return 1 / self.__truediv__(other)

# Class to represent an addition node in the AST
class AdditionNode(OperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

# Class to represent a multiplication node in the AST
class MultiplicationNode(OperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

# Class to represent a subtraction node in the AST
class SubtractionNode(OperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

# Class to represent a division node in the AST
class DivisionNode(OperationNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() / self.right.evaluate()

# Class to represent a leaf node that holds a future or a constant value
class ValueNode(ast.AST):
    def __init__(self, future_or_value):
        self.future_or_value = future_or_value

    def evaluate(self):
        # If it's a future, resolve it; otherwise, return the value directly
        if isinstance(self.future_or_value, concurrent.futures.Future):
            return self.future_or_value.result()  # Block until future is resolved
        return self.future_or_value

    # Overload operators for ValueNode
    def __add__(self, other):
        if isinstance(other, ValueNode):
            return AdditionNode(self, other)
        return AdditionNode(self, ValueNode(other))

    def __sub__(self, other):
        if isinstance(other, ValueNode):
            return SubtractionNode(self, other)
        return SubtractionNode(self, ValueNode(other))

    def __mul__(self, other):
        if isinstance(other, ValueNode):
            return MultiplicationNode(self, other)
        return MultiplicationNode(self, ValueNode(other))

    def __truediv__(self, other):
        if isinstance(other, ValueNode):
            return DivisionNode(self, other)
        return DivisionNode(self, ValueNode(other))


'''though I've written this fn as if all weights are known, I'm using dt to change the return information to simulate 
new rebalances coming in over time.
'''
def iselect_weights(date: dt.date):
    if date < dt.date(2020, 1, 1):
        return {}
    
    if date >= dt.date(2020, 1, 1) and date < dt.date(2021, 1, 1):
        return {'a':.25, 'b':.25, 'c':.25, 'd':0}

    if date >= dt.date(2021, 1, 1) and date < dt.date(2022, 1, 1):
        return {'a':.25, 'b':.25, 'c':0, 'd':0, 'e':.5}
    
#simulate 2 asset prices that grown linearly over time
def get_price(asset: str, date: dt.date):
    if(asset == 'a' or asset == 'c' or asset == 'e'):
        return ValueNode(100. + (date - dt.date(2019, 1, 1)).days * 0.01)
    if(asset == 'b' or asset == 'd'):
        return ValueNode(100. + (date - dt.date(2019, 1, 1)).days * (-0.005))

def r1(asset, date: dt.date):
    return -1 + get_price(asset, date) / get_price(asset, date - dt.timedelta(days=1))

def evaluate_index_value(end_date: dt.date):
    index_value = 100
    cur_dt = dt.date(2020, 1, 1)
    index_level_history = pd.Series()#dtype=object)
    index_level_history[cur_dt] = index_value

    with concurrent.futures.ThreadPoolExecutor() as executor:

        while cur_dt < end_date:
            weights = iselect_weights(cur_dt)
            prices = {k: executor.submit(get_price, k, cur_dt) for k in weights.keys()}
            index_value = index_value * (1 + sum([r1(k, cur_dt) * v for k, v in weights.items()]))

            index_level_history[cur_dt] = index_value.evaluate()

            cur_dt += dt.timedelta(days=1)

        astpretty.pprint(index_value)
        final_value = index_value.evaluate() # this should trigger the computation of all prices
        index_level_history.plot()
        plt.show()
        #print the index_level_history to see the values of the index at each date after the future have completed
        print(f"final_level={final_value} and the AST is\n")

def main():
    evaluate_index_value(dt.date(2022, 1, 1))

if __name__ == "__main__":
    main()
