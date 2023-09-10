"""
A function to display descriptive statistics for any file and specified or
 non specified columns
"""
import pandas as pd


def descriptive_statistics(csv_file_path, selected_columns=None):
    try:
        df = pd.read_csv(csv_file_path)

        if selected_columns is None:
            numeric_columns = df.select_dtypes(include=["number"])
        else:
            numeric_columns = df[selected_columns]

        if not numeric_columns.empty:
            for col in numeric_columns:
                result = df[col].agg(["mean", "median", "std"])
                result = result.round(2)
                print("Mean:", result["mean"], "Median:", 
                    result["median"], "SD:", result["std"])
        else:
            print("No numeric columns found in the specified columns.")

    except FileNotFoundError:
        print("The file was not found.")