"""
Test case 1 :for scenario the user does not input correct path for the data
Test case 2 : When  a User enter valid numeric column(s)

"""

from src.display_stat import descriptive_statistics
from io import StringIO
import sys


def test_no_numeric_columns_message():
    # Redirect standard output to a StringIO buffer
    sys.stdout = StringIO()
    # Replace with the path to your CSV file
    csv_file_path = "datasets/cereal_text_only_columns.csv"  
    selected_columns = None
    descriptive_statistics(csv_file_path, selected_columns)

    printed_message = sys.stdout.getvalue().strip()

    sys.stdout = sys.__stdout__

    assert printed_message == "No numeric columns found in the specified columns."


def test_numeric_message():
    sys.stdout = StringIO()

    csv_file_path = "datasets/cereal.csv"
    selected_columns = ["calories"]
    descriptive_statistics(csv_file_path, selected_columns)

    printed_message = sys.stdout.getvalue().strip()

    sys.stdout = sys.__stdout__

    expected_output = 'Mean: 105.54 Median: 110.0 SD: 18.44'

    assert printed_message == expected_output


if __name__ == "__main__":
    test_no_numeric_columns_message()
    test_numeric_message()
