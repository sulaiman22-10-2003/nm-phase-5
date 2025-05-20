# Main script to run the full energy efficiency analysis

from data_preprocessing import generate_energy_data
from visualization import (
    plot_consumption_by_region,
    plot_losses_by_region,
    plot_peak_vs_optimized,
    plot_correlation
)

def main():
    # Step 1: Generate the data
    data = generate_energy_data()

    # Step 2: Call all visualization functions
    plot_consumption_by_region(data)
    plot_losses_by_region(data)
    plot_peak_vs_optimized(data)
    plot_correlation(data)

# Entry point
if __name__ == "__main__":
    main()
