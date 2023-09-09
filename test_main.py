"""
Test case 1 :
Test case 2 : for scenario the user does not input correct path for the data

"""

from src.display_stat import descriptive_statistics
from io import StringIO
import sys


def test_no_numeric_columns_message():
    # Redirect standard output to a StringIO buffer
    sys.stdout = StringIO()

    csv_file_path = "datasets/cereal_text_only_columns.csv"  # Replace with the path to your CSV file
    selected_columns = None
    descriptive_statistics(csv_file_path, selected_columns)

    printed_message = sys.stdout.getvalue().strip()

    sys.stdout = sys.__stdout__

    assert printed_message == "No numeric columns found in the specified columns."


if __name__ == "__main__":
    test_no_numeric_columns_message()
