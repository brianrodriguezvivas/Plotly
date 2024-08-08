# my_project/main.py

import polars as pl

def main():
    df = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    print("Hola mundo")

if __name__ == "__main__":
    main()
