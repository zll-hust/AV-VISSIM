import matplotlib.pyplot as plt
import numpy as np

# Data from the table
scenarios = ["Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4"]
measurements = [
    "Average Travel Time",
    "Average Speed",
    "Average Delay Time per Vehicle",
    "Average Number of Stops per Vehicle",
]
public_data = np.array([
    [11.775, 11.285, 10.690, 10.220],  # Average Travel Time
    [16.551, 18.049, 19.932, 20.842],  # Average Speed
    [4.263, 3.590, 2.943, 2.849],      # Average Delay Time per Vehicle
    [9.500, 7.400, 6.300, 6.100],      # Average Number of Stops per Vehicle
])

private_data = np.array([
    [9.714, 6.507, 5.583, 4.844],     # Average Travel Time
    [19.221, 23.831, 27.760, 29.206],  # Average Speed
    [4.662, 2.680, 2.219, 2.114],      # Average Delay Time per Vehicle
    [13.177, 12.229, 11.210, 10.494],  # Average Number of Stops per Vehicle
])


# Plot settings
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 25

def plot_measurement_changes(scenarios, public_data, private_data, measurements):
    # Calculate percentage changes relative to Scenario 1
    public_percent_change = (public_data / public_data[:, 0].reshape(-1, 1) - 1) * 100
    private_percent_change = (private_data / private_data[:, 0].reshape(-1, 1) - 1) * 100

    for i, measurement in enumerate(measurements):
        plt.figure(figsize=(8, 6))
        plt.plot(scenarios, public_percent_change[i], 'r-', label="Public")
        plt.plot(scenarios, private_percent_change[i], 'b--', label="Private")
        plt.title(measurement)
        # plt.xlabel("Scenarios")
        plt.ylabel("Percentage Change (%)")
        # plt.legend()
        plt.tight_layout()
        # Save the figure
        plt.savefig(f"measurement_{i+1}.png", dpi=300)
        plt.close()

def plot_relative_improvement(scenarios, public_data, private_data, measurements):
    # Calculate pairwise relative improvement
    public_relative_improvement = (public_data[:, 1:] / public_data[:, :-1] - 1) * 100
    private_relative_improvement = (private_data[:, 1:] / private_data[:, :-1] - 1) * 100

    # Adjust scenarios for pairwise improvement (e.g., "2 vs 1", "3 vs 2", "4 vs 3")
    pairwise_scenarios = [f"{scenarios[i]} vs {scenarios[i-1]}" for i in range(1, len(scenarios))]

    for i, measurement in enumerate(measurements):
        plt.figure(figsize=(8, 6))
        plt.plot(
            pairwise_scenarios, public_relative_improvement[i], 'r-o', label="Public", linewidth=2, markersize=8
        )
        plt.plot(
            pairwise_scenarios, private_relative_improvement[i], 'b--s', label="Private", linewidth=2, markersize=8
        )
        plt.xlabel("Scenario Comparisons", fontsize=20)
        plt.ylabel("Relative Improvement (%)", fontsize=20)
        plt.title(measurement, fontsize=20)
        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)
        plt.legend(fontsize=16)
        plt.tight_layout()
        # Save the figure
        plt.savefig(f"pairwise_relative_improvement_{i+1}.png", dpi=300)
        plt.close()


# Data from the provided tables for Scenario 2 and Scenario 3
measurements = [
    "Average Travel Time",
    "Average Speed",
    "Average Delay Time per Vehicle",
    "Average Number of Stops per Vehicle",
]

scenario_1 = {
    "Public": [11.775, 16.551, 4.263, 9.5],
    "Private": [9.714, 19.221, 4.662, 13.177],
}

scenario_2 = {
    "Public (AV)": [11.285, 18.049, 3.590, 9.4],
    "Private (HV)": [6.630, 23.433, 2.745, 13.046],
    "Private (AV)": [6.218, 24.761, 2.529, 10.295],
}

scenario_3 = {
    "Public (CAV)": [10.690, 19.932, 2.943, 6.3],
    "Private (AV)": [5.854, 27.270, 2.242, 11.233],
    "Private (CAV)": [4.951, 28.903, 2.166, 11.156],
}


# Plot individual bar charts for each measurement and scenario
def plot_bar_comparisons(measurements, scenario_2, scenario_3):
    for i, measurement in enumerate(measurements):
        # Scenario 2 data
        values_scenario_2 = [
            scenario_2["Public (AV)"][i],
            scenario_2["Private (HV)"][i],
            scenario_2["Private (AV)"][i],
        ]
        categories_scenario_2 = ["Public (AV)", "Private (HV)", "Private (AV)"]

        # Plot for Scenario 2
        plt.figure(figsize=(8, 6))
        plt.bar(categories_scenario_2, values_scenario_2, color=['lightcoral', 'lightgreen', 'lightskyblue'])
        # plt.xlabel("Categories", fontsize=20)
        plt.ylabel(measurement)
        plt.xticks()
        plt.yticks()
        plt.tight_layout()
        plt.savefig(f"{measurement.replace(' ', '_')}_Scenario_2.png", dpi=300)
        plt.close()

        # Scenario 3 data
        values_scenario_3 = [
            scenario_3["Public (CAV)"][i],
            scenario_3["Private (AV)"][i],
            scenario_3["Private (CAV)"][i],
        ]
        categories_scenario_3 = ["Public (CAV)", "Private (AV)", "Private (CAV)"]

        # Plot for Scenario 3
        plt.figure(figsize=(8, 6))
        plt.bar(categories_scenario_3, values_scenario_3, color=['lightcoral', 'lightgreen', 'lightskyblue'])
        # plt.xlabel("Categories", fontsize=20)
        plt.ylabel(measurement)
        plt.xticks()
        plt.yticks()
        plt.tight_layout()
        plt.savefig(f"{measurement.replace(' ', '_')}_Scenario_3.png", dpi=300)
        plt.close()


def plot_changes(scenarios, public_data, private_data, measurements):
    plt.rcParams["font.size"] = 25

    differences = public_data - private_data

    plt.figure(figsize=(12, 8))
    for i, measurement in enumerate(measurements):
        plt.plot(
            scenarios,
            differences[i],
            marker="o",
            label=measurement
        )

    # plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)
    # plt.title("Differences Between Public and Private Data")
    # plt.xlabel("Scenarios")
    plt.ylabel("Difference")
    # plt.legend()
    # plt.grid(True, linestyle="-", alpha=0.7)
    plt.tight_layout()
    plt.savefig("difference.png")
    plt.close()

# Function to calculate improvement percentage
def calculate_improvement(new_values, base_values):
    return [(new - base) / base * 100 for new, base in zip(new_values, base_values)]

# Function to plot improvement comparison
def plot_improvement_comparisons(measurements, scenario_1, scenario_2, scenario_3):
    for i, measurement in enumerate(measurements):
        # Calculate improvements for Scenario 2
        public_improvement_scenario_2 = calculate_improvement(
            [scenario_2["Public (AV)"][i]], [scenario_1["Public"][i]]
        )[0]

        private_improvement_scenario_2 = calculate_improvement(
            [scenario_2["Private (HV)"][i], scenario_2["Private (AV)"][i]],
            [scenario_1["Private"][i], scenario_1["Private"][i]],
        )

        # Plot bar chart for Scenario 2
        categories_scenario_2 = [
            "Public (AV)",
            "Private (HV)",
            "Private (AV)",
        ]
        values_scenario_2 = [
            public_improvement_scenario_2,
            private_improvement_scenario_2[0],
            private_improvement_scenario_2[1],
        ]

        plt.figure(figsize=(8, 6))
        plt.bar(
            categories_scenario_2,
            values_scenario_2,
            color=["lightcoral", "lightgreen", "lightskyblue"],
            width=0.5,
        )
        plt.title(f"{measurement}")
        plt.ylabel("Percentage Change (%)")
        plt.xticks()
        plt.tight_layout()
        plt.savefig(f"{measurement.replace(' ', '_')}_Scenario_2_Improvement.png", dpi=300)
        plt.close()

        # Calculate improvements for Scenario 3
        public_improvement_scenario_3 = calculate_improvement(
            [scenario_3["Public (CAV)"][i]], [scenario_1["Public"][i]]
        )[0]

        private_improvement_scenario_3 = calculate_improvement(
            [scenario_3["Private (AV)"][i], scenario_3["Private (CAV)"][i]],
            [scenario_1["Private"][i], scenario_1["Private"][i]],
        )

        # Plot bar chart for Scenario 3
        categories_scenario_3 = [
            "Public (CAV)",
            "Private (AV)",
            "Private (CAV)",
        ]
        values_scenario_3 = [
            public_improvement_scenario_3,
            private_improvement_scenario_3[0],
            private_improvement_scenario_3[1],
        ]

        plt.figure(figsize=(8, 6))
        plt.bar(
            categories_scenario_3,
            values_scenario_3,
            color=["lightcoral", "lightskyblue", "lightgreen"],
            width=0.5,
        )
        plt.title(f"{measurement}")
        plt.ylabel("Percentage Change (%)")
        plt.xticks()
        plt.tight_layout()
        plt.savefig(f"{measurement.replace(' ', '_')}_Scenario_3_Improvement.png", dpi=300)
        plt.close()

def main():
    # plot_relative_improvement(scenarios, public_data, private_data, measurements)
    # plot_measurement_changes(scenarios, public_data, private_data, measurements)
    # plot_bar_comparisons(measurements, scenario_2, scenario_3)
    # plot_changes(scenarios, public_data, private_data, measurements)
    plot_improvement_comparisons(measurements, scenario_1, scenario_2, scenario_3)

if __name__ == "__main__":
    main()
