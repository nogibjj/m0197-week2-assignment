"""
Plot the visualisations 

"""

from src.visualise_utils import visualize_data
import pandas as pd

# read the dataset
data = pd.read_csv("datasets/cereal.csv")

visualize_data(data, x_col="rating",
                y_col="calories",
                title=" calories and ratings", 
                x_label="Item Ratings", 
                y_label="Calories")

visualize_data(data, x_col="rating",
                y_col="calories",
                title=" Calories and ratings by mfr", 
                x_label="Item Ratings", 
                y_label="Calories", 
                color_by="mfr"
                )
