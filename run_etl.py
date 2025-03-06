from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data


def run_etl():
    df = extract_data()
    cleaned_df = transform_data(df)
    load_data(cleaned_df)


if __name__ == "__main__":
    run_etl()
