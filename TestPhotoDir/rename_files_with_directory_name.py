import os
import sys

def is_leaf_directory(path:str) -> bool:
    return(all([ os.path.isfile(os.path.join(path, f)) for f in os.listdir(path)]))

def rename_file(path:str, do_it:bool) -> None:
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    if len(files) > 1:
        print(f"Skipped. More than 1 file in {path}")
    elif len(files) == 1:
        tokens = files[0].split(".")

        if len(tokens) != 2:
            print(f"Skipped. Failed to work out the extension for {files[0]}")
        else:
            extension = tokens[-1]
            target_name = os.path.basename(path) + "." + extension
            print(f"renaming {os.path.join(path,files[0])} to {target_name}")
            if do_it:
               os.rename(os.path.join(path,files[0]), os.path.join(path, target_name)) 
    
def rename_leaf_files(path:str, do_it:bool) -> None:
    if is_leaf_directory(path):
        rename_file(path, do_it)
    else:
        dirs = [ d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        
        for d in dirs:
            rename_leaf_files(os.path.join(path, d), do_it)

rename_leaf_files(os.path.dirname(__file__), "--really_do_it" in sys.argv)