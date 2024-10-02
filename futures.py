import concurrent.futures
import datetime as dt
from typing import List
import pandas as pd
import matplotlib.pyplot as plt
import ast

# Base class for all operation nodes
class OperationNode:
    def __add__(self, other):
        if not isinstance(other, OperationNode):
            other = ValueNode(other)
        return AddNode(self, other)

    def __radd__(self, other):
        if not isinstance(other, OperationNode):
            other = ValueNode(other)
        return AddNode(other, self)

    def __sub__(self, other):
        if not isinstance(other, OperationNode):
            other = ValueNode(other)
        return SubNode(self, other)

    def __rsub__(self, other):
        if not isinstance(other, OperationNode):
            other = ValueNode(other)
        return SubNode(other, self)

    def __mul__(self, other):
        if not isinstance(other, OperationNode):
            other = ValueNode(other)
        return MulNode(self, other)

    def __rmul__(self, other):
        if not isinstance(other, OperationNode):
            other = ValueNode(other)
        return MulNode(other, self)

    def __truediv__(self, other):
        if not isinstance(other, OperationNode):
            other = ValueNode(other)
        return DivNode(self, other)

    def __rtruediv__(self, other):
        if not isinstance(other, OperationNode):
            other = ValueNode(other)
        return DivNode(other, self)

    def evaluate(self):
        raise NotImplementedError("Subclasses should implement this!")

class ValueNode(ast.Expr, OperationNode):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def evaluate(self):
        if isinstance(self.value, concurrent.futures.Future):
            return self.value.result()
        return self.value

class AddNode(ast.BinOp, OperationNode):
    def __init__(self, left, right):
        super().__init__(left=left, op=ast.Add(), right=right)

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

class SubNode(ast.BinOp, OperationNode):
    def __init__(self, left, right):
        super().__init__(left=left, op=ast.Sub(), right=right)

    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

class MulNode(ast.BinOp, OperationNode):
    def __init__(self, left, right):
        super().__init__(left=left, op=ast.Mult(), right=right)

    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

class DivNode(ast.BinOp, OperationNode):
    def __init__(self, left, right):
        super().__init__(left=left, op=ast.Div(), right=right)

    def evaluate(self):
        return self.left.evaluate() / self.right.evaluate()

class MarketDataSpec:
    def __init__(self, asset: str, date: dt.date):
        self.asset = asset
        self.date = date

class MarketDataResolver:
    def get(self, requests: List[MarketDataSpec]):
        print(f"Resolving some prices...")
        return (self._get_price(req.asset, req.date) for req in requests)

    def _get_price(self, asset: str, date: dt.date):
        if asset in ['a', 'c', 'e']:
            return 100. + (date - dt.date(2019, 1, 1)).days * 0.01
        if asset in ['b', 'd']:
            return 100. + (date - dt.date(2019, 1, 1)).days * (-0.005)

class MarketDataContext:
    def __init__(self, batch_size=10):
        self.executor = None
        self.price_requests = []
        self.ast_nodes = []
        self.batch_size = batch_size

    def __enter__(self):
        #self.executor = concurrent.futures.ThreadPoolExecutor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass #self.executor.shutdown()

    def get_price(self, asset: str, date: dt.date):
        future = concurrent.futures.Future()
        value_node = ValueNode(future)
        self.price_requests.append({"value_node":value_node, "spec":MarketDataSpec(asset, date)})
        self.ast_nodes.append(value_node)
        if len(self.price_requests) >= self.batch_size:
            self.resolve()
        return value_node

    def get_return(self, asset: str, date: dt.date):
        return -1 + (self.get_price(asset, date) / self.get_price(asset, date - dt.timedelta(days=1)))

    def resolve(self):

        resolved_data = MarketDataResolver().get((f["spec"] for f in self.price_requests))
        for (req, data) in zip(self.price_requests, resolved_data):
            req["value_node"].value.set_result(data)

        for node in self.ast_nodes:
            node.evaluate()

        self.price_requests = []
        self.ast_nodes = []

def evaluate_index_value(end_date: dt.date):
    index_value = ValueNode(100)
    cur_dt = dt.date(2020, 1, 1)
    index_level_history = pd.Series(dtype=object)
    index_level_history[cur_dt] = index_value.evaluate()

    with MarketDataContext(50) as market_data_context:
        while cur_dt < end_date:
            print(cur_dt)
            weights = iselect_weights(cur_dt)
            returns = [market_data_context.get_return(k, cur_dt) * v for k, v in weights.items()]
            index_value = index_value * (1. + sum(returns))
            #index_level_history[cur_dt] = index_value.evaluate()
            cur_dt += dt.timedelta(days=1)

        market_data_context.resolve()  # Ensure all price requests are resolved
        final_value = index_value.evaluate()  # This should trigger the computation of all prices
        index_level_history.plot()
        plt.show()
        print(f"final_level={final_value}")

def iselect_weights(date: dt.date):
    if date < dt.date(2020, 1, 1):
        return {}
    
    if date >= dt.date(2020, 1, 1) and date < dt.date(2021, 1, 1):
        return {'a':.25, 'b':.25, 'c':.25, 'd':0}

    if date >= dt.date(2021, 1, 1) and date < dt.date(2022, 1, 1):
        return {'a':.25, 'b':.25, 'c':0, 'd':0, 'e':.5}
    
# Example usage
def main():
    try:
        evaluate_index_value(dt.date(2022, 1, 1))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()