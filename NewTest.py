import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, Dropdown

# Sample data
np.random.seed(0)
x_values = np.random.randn(100)
y_values1 = 2 * x_values + np.random.randn(100)
#y_values2 = 3 * x_values + np.random.randn(100)

# Create dropdown widgets for selecting variables
#x_dropdown = Dropdown(options=['x_values', 'y_values1', 'y_values2'], description='X-axis:')
#y_dropdown = Dropdown(options=['x_values', 'y_values1', 'y_values2'], description='Y-axis:')

x_dropdown = Dropdown(options=['x_values', 'y_values1'], description='X-axis:')
y_dropdown = Dropdown(options=['x_values', 'y_values1'], description='Y-axis:')

# Define function to update scatter plot based on dropdown selections
def update_plot(x_var, y_var):
    #plt.figure(figsize=(8, 6))
    plt.scatter(eval(x_var), eval(y_var))
    plt.xlabel(x_var)
    plt.ylabel(y_var)
    plt.title(f'Scatter Plot ({x_var} vs {y_var})')
    plt.grid(True)
    plt.show()

# Create interactive plot using ipywidgets interact function
interact(update_plot, x_var=x_dropdown, y_var=y_dropdown)
print("The End")
