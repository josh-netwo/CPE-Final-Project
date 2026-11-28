#Rule-based engineering insights for ideal resistor circuits.

def analyzeResistance(result):
    #Explain the resistor values and their relationship to equivalent resistance.
    resistors = result["resistors"]
    resistances = [resistor["resistance"] for resistor in resistors]
    highestResistance = max(resistances)
    lowestResistance = min(resistances)
    mode = result["mode"]
    equivalentResistance = result["equivalent resistance"]

    highestNumbers = [
        str(index + 1)
        for index, resistance in enumerate(resistances)
        if resistance == highestResistance
    ]
    lowestNumbers = [
        str(index + 1)
        for index, resistance in enumerate(resistances)
        if resistance == lowestResistance
    ]

    if mode == "series":
        relationship = (
            "In a series circuit, the equivalent resistance is the sum of all "
            "resistor values. Each resistor adds to the total resistance."
        )
    elif len(resistances) == 1:
        relationship = (
            "With only one resistor, the equivalent resistance is equal to "
            "that resistor's resistance."
        )
    else:
        relationship = (
            "In a parallel circuit, the equivalent resistance is lower than "
            "the lowest individual branch resistance because adding parallel "
            "paths reduces the circuit's total resistance."
        )

    return [
        f"Highest resistance: R{', R'.join(highestNumbers)} at {highestResistance:.2f} ohms.",
        f"Lowest resistance: R{', R'.join(lowestNumbers)} at {lowestResistance:.2f} ohms.",
        f"Equivalent resistance: {equivalentResistance:.2f} ohms.",
        relationship,
    ]


def analyzeVoltage(result):
    #Explain voltage drops in series and parallel circuits.
    resistors = result["resistors"]
    mode = result["mode"]

    if mode == "series":
        highestVoltage = max(resistor["voltage"] for resistor in resistors)
        highestNumbers = [
            str(index + 1)
            for index, resistor in enumerate(resistors)
            if resistor["voltage"] == highestVoltage
        ]
        return [
            f"Highest voltage drop: R{', R'.join(highestNumbers)} at {highestVoltage:.2f} V.",
            "In a series circuit, the supply voltage is divided among the resistors. "
            "The voltage drop across each resistor depends on its resistance; "
            "a higher resistance has a higher voltage drop when the same current flows.",
        ]

    supplyVoltage = result["supply voltage"]
    return [
        f"Each parallel branch has the same voltage as the supply: {supplyVoltage:.2f} V.",
        "In a parallel circuit, voltage is equal across all branches, regardless "
        "of the resistance in each branch.",
    ]


def analyzeCurrent(result):
    #Explain current behavior in series and parallel circuits.
    resistors = result["resistors"]
    mode = result["mode"]

    if mode == "series":
        totalCurrent = result["total current"]
        return [
            f"Every resistor carries the same current: {totalCurrent:.2f} A.",
            "In a series circuit, there is only one path for charge to flow, "
            "so the current is equal through every component.",
        ]

    highestCurrent = max(resistor["current"] for resistor in resistors)
    highestNumbers = [
        str(index + 1)
        for index, resistor in enumerate(resistors)
        if resistor["current"] == highestCurrent
    ]
    return [
        f"Highest branch current: R{', R'.join(highestNumbers)} at {highestCurrent:.2f} A.",
        "In a parallel circuit, current divides among the branches. The branch "
        "with the lowest resistance carries the highest current when the branch "
        "voltages are equal.",
    ]


def analyzeCircuitBehavior(result):
    #Describe the theoretical effect of an open component or branch.
    if result["mode"] == "series":
        return (
            "If any component becomes open or disconnected in a series circuit, "
            "the single current path is broken. Current stops throughout the "
            "entire circuit, so all components lose their operating current."
        )

    return (
        "If one branch becomes open or disconnected in a parallel circuit, "
        "current stops only in that branch. The other intact branches can "
        "continue operating because they have separate paths to the supply."
    )


def analyzeEngineeringRecommendations(result):
    #Give practical checks based on the calculated electrical values.
    recommendations = []
    resistors = result["resistors"]
    highestPower = max(resistor["power"] for resistor in resistors)
    highestPowerNumbers = [
        str(index + 1)
        for index, resistor in enumerate(resistors)
        if resistor["power"] == highestPower
    ]

    recommendations.append(
        f"Check the power rating of R{', R'.join(highestPowerNumbers)} first. "
        f"It has the highest calculated power dissipation at {highestPower:.2f} W. "
        "Its rated power must be suitable for the actual operating conditions "
        "and include an appropriate safety margin."
    )
    recommendations.append(
        f"Verify that each resistor's power rating is adequate for its own "
        f"calculated power dissipation, not just the circuit's total power "
        f"of {result['total power']:.2f} W."
    )
    recommendations.append(
        f"Check that the power supply can safely provide {result['supply voltage']:.2f} V "
        f"and the calculated total current of {result['total current']:.2f} A."
    )
    recommendations.append(
        "Use resistors with suitable resistance and power specifications, "
        "and check component datasheets and operating limits before building "
        "a physical circuit."
    )
    return recommendations


def generateInsights(result):
    #Generate all five insight categories for a completed circuit calculation.
    return {
        "Resistance Analysis": analyzeResistance(result),
        "Voltage Analysis": analyzeVoltage(result),
        "Current Analysis": analyzeCurrent(result),
        "Circuit Behavior": [analyzeCircuitBehavior(result)],
        "Engineering Recommendations": analyzeEngineeringRecommendations(result),
    }
