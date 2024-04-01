import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Load data from CSV file
    df = pd.read_csv('epa-sea-level.csv')

    # Generate scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], s=10, c='black')

    # Create the first regression line
    slope, intercept = linregress(
        x=df['Year'], y=df['CSIRO Adjusted Sea Level'])[0:2]
    extended_years = np.arange(df['Year'].iloc[0], 2050)
    plt.plot(extended_years, intercept + slope * extended_years, 'r')

    # Create the second regression line
    mask = (df['Year'] >= 2000)
    slope, intercept = linregress(
        x=df.loc[mask, 'Year'],
        y=df.loc[mask, 'CSIRO Adjusted Sea Level'])[0:2]
    extended_years = np.arange(2000, 2050)
    plt.plot(extended_years, intercept + slope * extended_years, 'b')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save the plot and return the plot axis (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

