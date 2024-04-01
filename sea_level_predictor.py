# We first import modules <- Pandas, matplotlib, numpy and scipy
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
    We are then defining a plotting function: 
        -> This plots sea level data over time 
        -> We want to use this to make predictions about the sea level in 2050, by performing a linear 
            regression analysis 

    We first import the data:
        -> This is data which shows the global sea level for a given year 
        -> We are provided this data in a CSV file and are importing it in 
        -> This is loaded into a `df` variable, using the `read_csv` method 

    Then generating a scatter plot from this:
        -> We do this using the .scatter method 
        -> We are plotting the time on the x and the sea level on the y 
        -> We were told to do this in the project instructions
        -> At the end of the plotting function, we are also defining the values for the x and y axes of the 
            plot, and for its title 

    Saving the plot:
        -> Since this is a plotting function, we want it to save the plot and output it 
        -> When the function is called, this will return our plot 
        -> This is saved as sea_level_plot.png, using the savefig method 
        -> The .gca method is used (get current axis), in case we want to change the axes for example before 
            the plot is saved when calling the function 
        -> Our plotting function is internally keeping track of the coordinate system and returning the axis 
            object 

    Drawing regression lines:
        -> We want two regression lines, which are each added in with the third and fourth block in this code 
        -> linregress <- We are using this to calculate the slope and intercept for these regression lines
        -> We are doing this for the input data which is plotted
        -> The first line uses all of the data as the input <- and then extends the slope until 2050, using iloc 
    -> The second line uses the data from 2,000 onwards and creates a boolean mask to do this 
        -> We are again using the linregress function to calculate the gradient and intercept of the slope 

    The overall stages of defining this plotting function are:
        -> Importing data
        -> Creating the time series plot 
        -> Adding a regression line to the plot
        -> Adding a second regression line to the plot <- This uses the same approach as the first one, just with a 
            different date range
                -> We are creating lines of best fit to predict the gobal sea level rise at 2050 - using two different 
                    data ranges 
        -> Adding axis titles to the plot 
        -> Saving and returning the plot 
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Load data from CSV file <- IMPORTING DATA
    df = pd.read_csv('epa-sea-level.csv')

    # Generate scatter plot <- CREATE THE PLOT 
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], s=10, c='black')

    # Create the first regression line <- REGRESSION LINE 1
        # Calculate the slope and intercept for the first regression line 
    slope, intercept = linregress(
        x=df['Year'], y=df['CSIRO Adjusted Sea Level'])[0:2]
        # Extend the linear regression line to the year 2050
    extended_years = np.arange(df['Year'].iloc[0], 2050)
        # Plot the linear regression line
    plt.plot(extended_years, intercept + slope * extended_years, 'r')

    # Create the second regression line <- REGRESSION LINE 2
    mask = (df['Year'] >= 2000)
        # Calculate the slope and intercept for the second regression line
        # This time, run the calculation from the year 2,000 onwards
    slope, intercept = linregress(
        x=df.loc[mask, 'Year'],
        y=df.loc[mask, 'CSIRO Adjusted Sea Level'])[0:2]
        # Extend the linear regression line to the year 2050
    extended_years = np.arange(2000, 2050)
        # Plot the linear regression line
    plt.plot(extended_years, intercept + slope * extended_years, 'b')

    # Add labels and title <- AXIS TITLES
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save the plot and return the plot axis (DO NOT MODIFY) <- SAVE THE PLOT 
    plt.savefig('sea_level_plot.png')
    return plt.gca()