"""Console-based analyzer for ideal resistor series and parallel circuits."""

from circuit_calculations import analyze_circuit


def read_number(prompt, allow_zero):
    """Ask until the user enters an acceptable number."""
    valid_number = False

    while valid_number == False:
        try:
            number = float(input(prompt))
            if allow_zero:
                if number >= 0:
                    valid_number = True
                else:
                    print("  Enter a finite number that is zero or greater.")
            else:
                if number > 0:
                    valid_number = True
                else:
                    print("  Enter a finite number greater than zero.")
        except ValueError:
            print("  Please enter a valid number.")

    return number


def read_resistor_count():
    """Ask for a positive whole number of resistors."""
    valid_count = False

    while valid_count == False:
        try:
            count = int(input("Number of resistors: "))
            if count > 0:
                valid_count = True
            else:
                print("  Enter a number greater than zero.")
        except ValueError:
            print("  Please enter a whole number.")

    return count


def print_result(result):
    """Display the circuit totals and a table of resistor values."""
    print()
    print("=" * 66)
    print("  " + result["mode"].upper() + " CIRCUIT RESULTS")
    print("=" * 66)
    print(f"  Supply voltage       : {result['supply_voltage']:.2f} V")
    print(f"  Equivalent resistance: {result['equivalent_resistance']:.2f} ohm")
    print(f"  Total current        : {result['total_current']:.2f} A")
    print(f"  Total power          : {result['total_power']:.2f} W")
    print("-" * 66)
    print(f"  {'#':>2}  {'Resistance':>14}  {'Voltage':>14}  {'Current':>14}  {'Power':>12}")
    print(f"      {'(ohm)':>14}  {'(V)':>14}  {'(A)':>14}  {'(W)':>12}")
    print("-" * 66)

    number = 0
    for resistor in result["resistors"]:
        number = number + 1
        print(
            f"  {number:>2}  {resistor['resistance']:>14.2f}  "
            f"{resistor['voltage']:>14.2f}  {resistor['current']:>14.2f}  "
            f"{resistor['power']:>12.2f}"
        )

    print("=" * 66)
    print("  Assumes ideal resistors and wires.")
    print()


def run():
    print("=" * 62)
    print("           PARALLEL & SERIES CIRCUIT ANALYZER")
    print("=" * 62)
    print("  Calculate equivalent resistance, voltage, current, and power.")
    print("  Enter resistance in ohms and supply voltage in volts.")

    running = True
    while running:
        print("\n  [1] Series circuit   [2] Parallel circuit   [Q] Quit")
        choice = input("  Select an option: ").lower()

        if choice == "q":
            print("\n  Goodbye.")
            running = False
        elif choice == "1" or choice == "2":
            resistor_count = read_resistor_count()
            resistances = []
            number = 0

            for index in range(resistor_count):
                number = index + 1
                prompt = "Resistance of resistor " + str(number) + " in ohms: "
                resistance = read_number(prompt, False)
                resistances.append(resistance)

            supply_voltage = read_number("Supply voltage in volts: ", True)

            if choice == "1":
                mode = "series"
            else:
                mode = "parallel"

            try:
                result = analyze_circuit(mode, resistances, supply_voltage)
                print_result(result)
            except ZeroDivisionError:
                print("  These values are too large or small to calculate.")
        else:
            print("  Choose 1, 2, or Q.")


run()