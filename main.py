
from src.normalization import normalize_readings
from src.odi import compute_odi
from src.classifier import classify_odi


def run_frysafe_algorithm(sensor_readings):
    """
    Execute the complete FrySafe algorithm.

    Process:
        1. Sensor Data Acquisition
        2. Data Normalization
        3. ODI Computation
        4. Rule-Based Classification

    Parameters:
        sensor_readings (dict): Raw sensor readings.

    Returns:
        dict: Complete FrySafe algorithm results.
    """

    # Step 1: Normalize sensor readings
    normalized_readings = normalize_readings(sensor_readings)

    # Step 2: Compute Oil Degradation Index
    odi = compute_odi(normalized_readings)

    # Step 3: Classify ODI
    classification = classify_odi(odi)

    # Step 4: Compile results
    results = {
        "raw_readings": sensor_readings,
        "normalized_readings": normalized_readings,
        "odi": odi,
        "classification": classification
    }

    return results


def display_results(results):
    """Display the complete FrySafe algorithm results."""

    print("\n========================================")
    print("          FRYSAFE ALGORITHM")
    print("========================================")

    print("\nRAW SENSOR READINGS")
    print("----------------------------------------")

    for sensor, value in results["raw_readings"].items():
        print(f"{sensor.capitalize():<15}: {value}")

    print("\nNORMALIZED SENSOR READINGS")
    print("----------------------------------------")

    for sensor, value in results["normalized_readings"].items():
        print(f"{sensor.capitalize():<15}: {value:.4f}")

    print("\nODI COMPUTATION")
    print("----------------------------------------")
    print(f"Oil Degradation Index: {results['odi']:.2f}")

    print("\nODI INTERPRETATION")
    print("----------------------------------------")
    print(f"Classification: {results['classification']}")

    print("\n========================================")


if __name__ == "__main__":

    # Sample sensor readings for software testing only
    sample_readings = {
        "red": 850,
        "green": 750,
        "blue": 650,
        "turbidity": 2500
    }

    # Execute FrySafe algorithm
    results = run_frysafe_algorithm(sample_readings)

    # Display results
    display_results(results)
