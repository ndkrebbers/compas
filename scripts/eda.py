import pandas as pd
import numpy as np

def main(import_path: str):
    df = pd.read_csv(import_path)

    pass


if __name__ == "__main__":
    file_path = "../data/raw/cox-violent-parsed_filt.csv"
    main(file_path)
