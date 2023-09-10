
## Pandas Descriptive statistics 
This repository contains code for displaying descriptive statistics of specified columns from any CSV file. A user has to provide the dataset name as an argument and specify the columns they want to analyze. If no columns are specified, the code will default to displaying statistics for all numeric columns.

### `src` directory contains:
1. `display_stat.py` This script defines a function that reads a CSV file, calculates descriptive statistics for specified or all numeric columns, and prints the results. If the file doesn't exist, it handles the FileNotFoundError.
2. `visualise_utils.py` Defines a function for creating scatter plots with Seaborn, allowing for customization of plot appearance and optionally coloring data points by a categorical variable. It also saves the plot as a PNG file in a "plots" folder with an `assumption` its already created

### Test script:
1. `test_main.py` It test cases to help ensure that the descriptive_statistics function behaves as expected when given different inputs, handling both incorrect data paths and valid numeric columns appropriately.

Illustrated execution of the tests are below: 
![Tests](/images/tests.png?raw=true)

### Visualisation: 
1. `visualisation.py` This script reads a dataset, creates scatter plots to visualize the relationship between two variables/columns passed by the user, and optionally differentiates data points by color options using a categorical column. It helps users explore and understand the data through these visualizations. The visualisations are saved on `plots` folder

### Infrastructure scripts:
`.devcontainer`
1. `devcontainer.json` Sets up a development environment. It also includes settings for Docker for VS Code or GitHub Codespace. 
2. `Dockerfile` Dockerfile set up a development environment with Python 3.8


`Makefile` Streamlines development workflows and ensuring code quality and consistency.

`setup.sh` Activates a virtual environment
