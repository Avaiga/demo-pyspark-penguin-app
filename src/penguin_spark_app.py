### app/penguin_spark_app.py
import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input-csv-path", required=True, help="Path to the input penguin CSV file.")
parser.add_argument("--output-csv-path", required=True, help="Path to save the output CSV file.")
args = parser.parse_args()

import pyspark.pandas as ps
from pyspark.sql import SparkSession


def read_penguin_df(csv_path: str):
    penguin_df = ps.read_csv(csv_path)
    return penguin_df


def clean(df: ps.DataFrame) -> ps.DataFrame:
    return df[df.sex.isin(["male", "female"])].dropna()


def process(df: ps.DataFrame) -> ps.DataFrame:
    """The mean of measured penguin values, grouped by island and sex."""

    mean_df = df.groupby(by=["species", "island", "sex"]).agg("mean").drop(columns="year").reset_index()
    return mean_df


if __name__ == "__main__":
    spark = SparkSession.builder.appName("Mean Penguin").getOrCreate()

    penguin_df = read_penguin_df(args.input_csv_path)
    cleaned_penguin_df = clean(penguin_df)
    processed_penguin_df = process(cleaned_penguin_df)
    processed_penguin_df.to_pandas().to_csv(args.output_csv_path, index=False)

    sys.exit(os.EX_OK)
