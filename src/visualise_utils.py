"""
 Visualize data using a scatter plot with Seaborn

    Parameters:
    - data: DataFrame containing the data.
    - x_col: Column name for the x-axis.
    - y_col: Column name for the y-axis.
    - title: Title of the plot.
    - x_label: Label for the x-axis.
    - y_label: Label for the y-axis.
    - color_by: Column name for categorical variable 
"""

import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(data, x_col, y_col, title, x_label, y_label, color_by=None):
    
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x=x_col, y=y_col, hue=color_by, data=data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if color_by is not None:
        plt.legend(title=color_by)
    # assuming plots folder exists
    plot_name = f"plots/{title}.png"
    plt.savefig(plot_name)
    #plt.show()