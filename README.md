# Parallel & Series Circuit Analyzer

A console program for calculating ideal resistor circuits. Choose series or
parallel, enter the number of resistors, then enter each resistance in ohms and
the supply voltage in volts. Results include equivalent resistance, total
current and power, and each resistor's voltage, current, and power.

## Run

```text
python circuit_analyzer.py
```

Choose `Q` to quit. The project uses Python's built-in features and does not
require external packages. The code uses basic variables, lists, dictionaries,
input/output, conditionals, loops, functions, and `try`/`except`.

Successful calculations are kept in a history list while the program is
running. Choose `H` from the menu to view them. The history clears when you
quit because this version uses only the course topics and does not write files.

## Run the calculation checks

```text
python test_circuit_analyzer.py
```
