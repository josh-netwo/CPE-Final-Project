"""Functions for calculating ideal resistor series and parallel circuits."""


def analyzeCircuit(mode, resistances, supplyVoltage):
    """Return the circuit totals and a list of results for each resistor."""
    if mode == "series":
        equivalentResistance = 0
        for resistance in resistances:
            equivalentResistance = equivalentResistance + resistance
    else:
        reciprocalTotal = 0
        for resistance in resistances:
            reciprocalTotal = reciprocalTotal + (1 / resistance)
        equivalentResistance = 1 / reciprocalTotal

    totalCurrent = supplyVoltage / equivalentResistance
    totalPower = supplyVoltage * totalCurrent
    resistorResults = []

    for resistance in resistances:
        if mode == "series":
            current = totalCurrent
            voltage = current * resistance
        else:
            voltage = supplyVoltage
            current = voltage / resistance

        resistorResult = {
            "resistance": resistance,
            "voltage": voltage,
            "current": current,
            "power": voltage * current,
        }
        resistorResults.append(resistorResult)

    return {
        "mode": mode,
        "equivalent resistance": equivalentResistance,
        "supply voltage": supplyVoltage,
        "total current": totalCurrent,
        "total power": totalPower,
        "resistors": resistorResults,
    }
