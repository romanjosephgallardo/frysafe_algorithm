
import json
import math
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
CALIBRATION_FILE = BASE_DIR / "calibration" / "calibration.json"

REQUIRED_SENSORS = ["red", "green", "blue", "turbidity"]


def load_calibration():
    """Load baseline and maximum values from calibration.json."""

    if not CALIBRATION_FILE.exists():
        raise FileNotFoundError(
            f"Calibration file not found: {CALIBRATION_FILE}"
        )

    with open(CALIBRATION_FILE, "r") as file:
        calibration = json.load(file)

    return calibration


def normalize_value(value, baseline, maximum):
    """
    Normalize a sensor reading using calibration references.

    Formula:
        N = (X - baseline) / (maximum - baseline)

    Output is restricted to the range 0.0 to 1.0.
    """

    value = float(value)
    baseline = float(baseline)
    maximum = float(maximum)

    if not all(math.isfinite(v) for v in [value, baseline, maximum]):
        raise ValueError("Sensor readings and calibration values must be finite.")

    denominator = maximum - baseline

    if denominator == 0:
        raise ValueError(
            "Invalid calibration: baseline and maximum are equal."
        )

    normalized = (value - baseline) / denominator

    return max(0.0, min(1.0, normalized))


def normalize_readings(readings):
    """Normalize all four FrySafe sensor readings."""

    calibration = load_calibration()

    baseline = calibration["baseline"]
    maximum = calibration["maximum"]

    normalized_readings = {}

    for sensor in REQUIRED_SENSORS:

        if sensor not in readings:
            raise ValueError(f"Missing sensor reading: {sensor}")

        if sensor not in baseline or sensor not in maximum:
            raise ValueError(f"Missing calibration reference: {sensor}")

        normalized_readings[sensor] = normalize_value(
            readings[sensor],
            baseline[sensor],
            maximum[sensor]
        )

    return normalized_readings


if __name__ == "__main__":

    # Sample readings for software testing only
    sample_readings = {
        "red": 850,
        "green": 750,
        "blue": 650,
        "turbidity": 2500
    }

    results = normalize_readings(sample_readings)

    print("\nFRYSAFE NORMALIZATION RESULTS")
    print("--------------------------------")

    for sensor, value in results.items():
        print(f"{sensor.capitalize()}: {value:.4f}")
