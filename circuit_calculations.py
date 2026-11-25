"""Functions for calculating ideal resistor series and parallel circuits."""


def analyze_circuit(mode, resistances, supply_voltage):
    """Return the circuit totals and a list of results for each resistor."""
    if mode == "series":
        equivalent_resistance = 0
        for resistance in resistances:
            equivalent_resistance = equivalent_resistance + resistance
    else:
        reciprocal_total = 0
        for resistance in resistances:
            reciprocal_total = reciprocal_total + (1 / resistance)
        equivalent_resistance = 1 / reciprocal_total

    total_current = supply_voltage / equivalent_resistance
    total_power = supply_voltage * total_current
    resistor_results = []

    for resistance in resistances:
        if mode == "series":
            current = total_current
            voltage = current * resistance
        else:
            voltage = supply_voltage
            current = voltage / resistance

        resistor_result = {
            "resistance": resistance,
            "voltage": voltage,
            "current": current,
            "power": voltage * current,
        }
        resistor_results.append(resistor_result)

    return {
        "mode": mode,
        "equivalent_resistance": equivalent_resistance,
        "supply_voltage": supply_voltage,
        "total_current": total_current,
        "total_power": total_power,
        "resistors": resistor_results,
    }
