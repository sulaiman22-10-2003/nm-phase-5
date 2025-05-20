# Module to create and return synthetic energy data

import numpy as np
import pandas as pd

def generate_energy_data(seed=42):
    # Set seed for reproducibility
    np.random.seed(seed)

    # Define months and regions
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    regions = ['North', 'South', 'East', 'West', 'Central']

    # Create a DataFrame with synthetic/random values
    data = pd.DataFrame({
        'Month': np.repeat(months, len(regions)),  # Each month repeated for all regions
        'Region': regions * len(months),           # Regions repeated for each month
        'Consumption_kWh': np.random.randint(5000, 15000, len(months) * len(regions)),  # Energy consumption
        'Losses_Percent': np.random.uniform(2.0, 8.0, len(months) * len(regions)),      # Transmission losses
        'Peak_Load_kW': np.random.randint(500, 2000, len(months) * len(regions)),       # Peak load in kW
        'Power_Factor': np.random.uniform(0.8, 0.98, len(months) * len(regions))        # Power factor
    })

    # Calculate cost savings based on consumption and losses
    data['Cost_Savings'] = data['Consumption_kWh'] * data['Losses_Percent'] * 0.01 * 0.15

    return data
