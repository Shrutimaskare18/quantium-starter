import pandas as pd

def test_output_csv_has_correct_columns():
    df = pd.read_csv('output.csv')
    assert 'sales' in df.columns
    assert 'date' in df.columns
    assert 'region' in df.columns

def test_output_csv_not_empty():
    df = pd.read_csv('output.csv')
    assert len(df) > 0

def test_only_valid_regions():
    df = pd.read_csv('output.csv')
    valid_regions = ['north', 'east', 'south', 'west']
    assert df['region'].isin(valid_regions).all()