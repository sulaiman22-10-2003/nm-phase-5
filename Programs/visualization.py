# visualization.py
# Module containing all visualization functions for energy analysis

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_consumption_by_region(data):
    # Bar plot for energy consumption across months and regions
    plt.figure(figsize=(12, 6))
    sns.barplot(data=data, x='Month', y='Consumption_kWh', hue='Region')
    plt.title('Monthly Energy Consumption by Region')
    plt.ylabel('Energy Consumption (kWh)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_losses_by_region(data):
    # Bar plot showing average loss percentage by region
    plt.figure(figsize=(10, 6))
    losses = data.groupby('Region')['Losses_Percent'].mean().reset_index()
    sns.barplot(data=losses, x='Region', y='Losses_Percent')
    plt.axhline(4.0, color='red', linestyle='--', label='Target Threshold')  # Reference line
    plt.title('Average Transmission & Distribution Losses by Region')
    plt.ylabel('Losses (%)')
    plt.legend()
    plt.show()

def plot_peak_vs_optimized(data):
    # Line plot comparing actual vs optimized peak load
    months = data['Month'].unique()
    peak = data.groupby('Month')['Peak_Load_kW'].mean()
    optimized = peak * np.random.uniform(0.7, 0.9, len(peak))  # Optimized is 70–90% of peak

    plt.figure(figsize=(10, 6))
    plt.plot(peak.index, peak.values, marker='o', label='Current Peak Load')
    plt.plot(peak.index, optimized, marker='s', label='Optimized Load')
    plt.fill_between(range(len(peak)), peak.values, optimized, alpha=0.3, color='green')  # Shaded area
    plt.xticks(ticks=range(len(months)), labels=months, rotation=45)
    plt.xlabel('Month')
    plt.ylabel('Load (kW)')
    plt.title('Peak Load vs Optimized Load Profile')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_correlation(data):
    # Heatmap to visualize correlation between energy metrics
    corr = data[['Consumption_kWh', 'Losses_Percent', 'Peak_Load_kW', 'Power_Factor']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Between Energy Metrics')
    plt.tight_layout()
    plt.show()
