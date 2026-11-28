#Console-based analyzer for ideal resistor series and parallel circuits.

from circuit_calculations import analyzeCircuit
from circuit_insights import generateInsights
from circuit_history import appendHistory


def readNumber(prompt, allowZero):
    #Ask until the user enters an acceptable number.
    validNumber = False

    while validNumber == False:
        try:
            number = float(input(prompt))
            if allowZero:
                if number >= 0:
                    validNumber = True
                else:
                    print("  Enter a number that is zero or greater.")
            else:
                if number > 0:
                    validNumber = True
                else:
                    print("  Enter a number greater than zero.")
        except ValueError:
            print("  Please enter a valid number.")

    return number


def readResistorCount():
    #Ask for a positive whole number of resistors.
    validCount = False

    while validCount == False:
        try:
            count = int(input("Number of resistors: "))
            if count > 0:
                validCount = True
            else:
                print("  Enter a number greater than zero.")
        except ValueError:
            print("  Please enter a whole number.")

    return count


def printResult(result):
    #Display the circuit totals and a table of resistor values.
    print()
    print("=" * 66)
    print("  " + result["mode"].upper() + " CIRCUIT RESULTS")
    print("=" * 66)
    print(f"  Supply voltage       : {result['supply voltage']:.2f} V")
    print(f"  Equivalent resistance: {result['equivalent resistance']:.2f} ohm")
    print(f"  Total current        : {result['total current']:.2f} A")
    print(f"  Total power          : {result['total power']:.2f} W")
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


def printInsights(result):
    #Display the five engineering insight categories for a calculation.
    insights = generateInsights(result)

    print("\n" + "=" * 66)
    print("  ENGINEERING ANALYSIS & INSIGHTS")
    print("=" * 66)

    for category, observations in insights.items():
        print(f"\n  {category.upper()}")
        for observation in observations:
            print("  - " + observation)

    print("\n" + "=" * 66)


def askForInsights():
    #Ask whether the user wants to view optional engineering insights.
    while True:
        print("\n" + "=" * 66)
        print("Would you like to view the engineering analysis and insights?")
        print("[Y] Yes   [N] No")
        print("=" * 66)
        choice = input("Select an option: ").strip().lower()

        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("  Please enter Y or N.")


def printHistory(history):
    #Display calculations saved during this run.
    if not history:
        print("\n  No calculations saved during this run yet.\n")
        return

    print("\n  CALCULATIONS FROM THIS RUN")
    number = 0
    for result in history:
        number = number + 1
        print("  Calculation", number)
        printResult(result)


def displayHeader():
    #Display the main screen in the requested console layout.
    line = "=" * 66

    print(line)
    print("PARALLEL & SERIES CIRCUIT ANALYZER".center(66))
    print(line)
    print()
    print("Calculate equivalent resistance, voltage, current, and power.")
    print("Enter resistance in ohms and supply voltage in volts.")
    print()
    print(line)


def run():
    displayHeader()
    running = True
    history = []
    while running:
        print("[1] Series circuit   [2] Parallel circuit   [H] History   [Q] Quit")
        print("=" * 66)
        choice = input("Select an option: ").lower()

        if choice == "q":
            print("\n  Goodbye.")
            running = False
        elif choice == "h":
            printHistory(history)
        elif choice == "1" or choice == "2":
            if choice == "1":
                mode = "series"
            else:
                mode = "parallel"

            print("\nChosen Circuit: " + mode.capitalize())
            print("-" * 66)
            resistorCount = readResistorCount()
            resistances = []
            number = 0

            for index in range(resistorCount):
                number = index + 1
                prompt = "Resistance of resistor " + str(number) + " in ohms: "
                resistance = readNumber(prompt, False)
                resistances.append(resistance)

            supplyVoltage = readNumber("Supply voltage in volts: ", True)

            try:
                result = analyzeCircuit(mode, resistances, supplyVoltage)
                printResult(result)
                if askForInsights():
                    printInsights(result)
                appendHistory(history, result)
                print("  Calculation added to this run's history.\n")
            except ZeroDivisionError:
                print("  These values are too large or small to calculate.")
        else:
            print("  Choose 1, 2, H, or Q.")


run()