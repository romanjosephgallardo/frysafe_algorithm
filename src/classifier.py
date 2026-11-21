
def classify_odi(odi):
    """
    Classify the FrySafe Oil Degradation Index (ODI).

    Classification:
        0 <= ODI < 25   : Low Degradation
        25 <= ODI < 50  : Moderate Degradation
        50 <= ODI < 75  : High Degradation
        75 <= ODI <= 100: Very High Degradation

    Parameters:
        odi (float): Computed Oil Degradation Index.

    Returns:
        str: Corresponding degradation classification.
    """

    odi = float(odi)

    if not 0 <= odi <= 100:
        raise ValueError(
            f"Invalid ODI value: {odi}. Expected a value from 0 to 100."
        )

    if odi < 25:
        return "Low Degradation"

    elif odi < 50:
        return "Moderate Degradation"

    elif odi < 75:
        return "High Degradation"

    else:
        return "Very High Degradation"


if __name__ == "__main__":

    # Sample ODI values for testing
    sample_values = [25.00, 35.00, 52.50, 87.50]

    print("\nFrySafe Rule-Based Classification")
    print("---------------------------------")

    for odi in sample_values:
        classification = classify_odi(odi)

        print(f"ODI: {odi:.2f} | Classification: {classification}")
