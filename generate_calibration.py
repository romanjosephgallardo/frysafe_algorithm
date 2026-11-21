
import pandas as pd
import json
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).parent

CSV_FILE = BASE_DIR / "data" / "frysafe_dummy_experimental_data.csv"
OUTPUT_FILE = BASE_DIR / "calibration" / "calibration.json"

# Read experimental data
df = pd.read_csv(CSV_FILE)

# Sensor columns
sensor_columns = [
    "red_frequency_hz",
    "green_frequency_hz",
    "blue_frequency_hz",
    "turbidity_voltage_mv"
]

# Calculate mean readings for Cycle 0 and Cycle 5
baseline = (
    df[df["cycle_number"] == 0][sensor_columns]
    .mean()
)

maximum = (
    df[df["cycle_number"] == 5][sensor_columns]
    .mean()
)

# Prepare calibration data
calibration = {
    "calibration_method": "Three-trial mean",
    "reference_cycles": {
        "baseline": 0,
        "maximum": 5
    },
    "baseline": {
        "red": float(baseline["red_frequency_hz"]),
        "green": float(baseline["green_frequency_hz"]),
        "blue": float(baseline["blue_frequency_hz"]),
        "turbidity": float(baseline["turbidity_voltage_mv"])
    },
    "maximum": {
        "red": float(maximum["red_frequency_hz"]),
        "green": float(maximum["green_frequency_hz"]),
        "blue": float(maximum["blue_frequency_hz"]),
        "turbidity": float(maximum["turbidity_voltage_mv"])
    }
}

# Create calibration directory if needed
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# Save as JSON
with open(OUTPUT_FILE, "w") as file:
    json.dump(calibration, file, indent=4)

print("Calibration successfully generated!")
print(f"Saved to: {OUTPUT_FILE}")
