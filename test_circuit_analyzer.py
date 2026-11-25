"""Basic calculation checks for the circuit analyzer."""

from circuit_calculations import analyze_circuit


def check_value(name, actual, expected):
    if actual == expected:
        print("PASS:", name)
    else:
        print("FAIL:", name, "- expected", expected, "but got", actual)


def check_series_circuit():
    result = analyze_circuit("series", [10, 10], 20)
    check_value("series equivalent resistance", result["equivalent_resistance"], 20)
    check_value("series total current", result["total_current"], 1)
    check_value("series first resistor voltage", result["resistors"][0]["voltage"], 10)
    check_value("series total power", result["total_power"], 20)


def check_parallel_circuit():
    result = analyze_circuit("parallel", [10, 10], 20)
    check_value("parallel equivalent resistance", result["equivalent_resistance"], 5)
    check_value("parallel total current", result["total_current"], 4)
    check_value("parallel first resistor current", result["resistors"][0]["current"], 2)
    check_value("parallel total power", result["total_power"], 80)


def check_zero_voltage():
    result = analyze_circuit("series", [10], 0)
    check_value("zero-voltage current", result["total_current"], 0)
    check_value("zero-voltage power", result["total_power"], 0)


check_series_circuit()
check_parallel_circuit()
check_zero_voltage()
