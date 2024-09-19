import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original data')

    # Create first line of best fit
    slope_all, intercept_all, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extend_all = pd.Series(range(1880, 2051))
    sea_level_pred_all = intercept_all + slope_all * years_extend_all

    plt.plot(years_extend_all, sea_level_pred_all, label='Best fit line (all data)', color='red')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    years_extend_recent = pd.Series(range(2000, 2051))
    sea_level_pred_recent = intercept_recent + slope_recent * years_extend_recent

    plt.plot(years_extend_recent, sea_level_pred_recent, label='Best fit line (from 2000)', color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add a legend
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()