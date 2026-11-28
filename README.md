# Parallel & Series Circuit Analyzer

A console program for calculating ideal resistor circuits. Choose series or
parallel, enter the number of resistors, then enter each resistance in ohms and
the supply voltage in volts. Results include equivalent resistance, total
current and power, each resistor's voltage, current, and power, and five
automatically generated engineering insight categories: resistance, voltage,
current, circuit behavior, and engineering recommendations.

## Run

```text
python circuit_analyzer.py
```

Choose `Q` to quit. The project separates circuit calculations (`circuit_calculations.py`) from
rule-based engineering insights (`circuit_insights.py`). It uses Python's
built-in features and does not require external packages. The code uses basic variables, lists, dictionaries,
input/output, conditionals, loops, functions, and `try`/`except`.

Successful calculations are kept in a history list while the program is
running. Choose `H` from the menu to view them. The history clears when you
quit because this version uses only the course topics and does not write files.

## Engineering insights

After each successful calculation, the program identifies the highest and
lowest resistance values, analyzes voltage and current behavior, explains the
theoretical effect of an open component or branch, and provides practical
component and power-rating checks. Open-circuit behavior is explained
theoretically; the program does not simulate a physically disconnected part.
Power-rating recommendations are reminders to compare calculated dissipation
with actual component datasheets because resistor ratings are not user inputs.

## Run the calculation checks

```text
python test_circuit_analyzer.py
```
