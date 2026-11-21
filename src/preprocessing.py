
def classify_odi(odi):
    """
    Classify the FrySafe Oil Degradation Index (ODI).

    ODI Reading Range Interpretation:

        0.00 to below 25.00  : Low Degradation
        25.00 to below 50.00 : Moderate Degradation
        50.00 to below 75.00 : High Degradation
        75.00 to 100.00      : Very High Degradation

    Returns:
        str: Corresponding degradation classification.
    """

    odi = float(odi)

    if not 0.0 <= odi <= 100.0:
        raise ValueError(
            f"Invalid ODI value: {odi}. "
            "ODI must be between 0.00 and 100.00."
        )

    if odi < 25.00:
        return "Low Degradation"

    elif odi < 50.00:
        return "Moderate Degradation"

    elif odi < 75.00:
        return "High Degradation"

    else:
        return "Very High Degradation"


if __name__ == "__main__":

    # Sample ODI values for testing
    sample_values = [
        0.00,
        24.99,
        25.00,
        49.99,
        50.00,
        74.99,
        75.00,
        100.00
    ]

    print("\nFRYSAFE RULE-BASED CLASSIFICATION")
    print("--------------------------------")

    for odi in sample_values:
        classification = classify_odi(odi)

        print(
            f"ODI: {odi:.2f} | "
            f"Interpretation: {classification}"
        )
