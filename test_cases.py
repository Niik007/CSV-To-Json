import pytest
from pathlib import Path
import pandas as pd

data_csv = 'data.csv'
json_file = 'new_output.json'
data_path = Path(data_csv)
json_path = Path(json_file)


def test_datafile():
    if data_path.is_file():
        assert True


def test_jsonfile():
    if json_path.is_file():
        assert True


def test_columns_size():
    df = pd.read_csv(file)
    columns = df.shape[1]
    if columns == 10:
        assert True
