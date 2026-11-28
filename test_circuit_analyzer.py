#Basic calculation and history checks for the circuit analyzer.

from circuit_calculations import analyzeCircuit
from circuit_insights import (
    analyzeCircuitBehavior,
    analyzeCurrent,
    analyzeEngineeringRecommendations,
    analyzeResistance,
    analyzeVoltage,
    generateInsights,
)
from circuit_history import appendHistory


def checkValue(name, actual, expected):
    if actual == expected:
        print("PASS:", name)
    else:
        print("FAIL:", name, "- expected", expected, "but got", actual)


def checkSeriesCircuit():
    result = analyzeCircuit("series", [10, 10], 20)
    checkValue("series equivalent resistance", result["equivalent resistance"], 20)
    checkValue("series total current", result["total current"], 1)
    checkValue("series first resistor voltage", result["resistors"][0]["voltage"], 10)
    checkValue("series total power", result["total power"], 20)


def checkParallelCircuit():
    result = analyzeCircuit("parallel", [10, 10], 20)
    checkValue("parallel equivalent resistance", result["equivalent resistance"], 5)
    checkValue("parallel total current", result["total current"], 4)
    checkValue("parallel first resistor current", result["resistors"][0]["current"], 2)
    checkValue("parallel total power", result["total power"], 80)


def checkZeroVoltage():
    result = analyzeCircuit("series", [10], 0)
    checkValue("zero-voltage current", result["total current"], 0)
    checkValue("zero-voltage power", result["total power"], 0)


def checkHistory():
    history = []
    result = analyzeCircuit("series", [10], 20)
    appendHistory(history, result)
    checkValue("history calculation count", len(history), 1)
    checkValue(
        "history calculation resistance",
        history[0]["equivalent resistance"],
        10,
    )


def checkSeriesInsights():
    result = analyzeCircuit("series", [10, 20, 30], 12)
    resistanceInsights = analyzeResistance(result)
    voltageInsights = analyzeVoltage(result)
    currentInsights = analyzeCurrent(result)
    behaviorInsight = analyzeCircuitBehavior(result)
    recommendationInsights = analyzeEngineeringRecommendations(result)
    allInsights = generateInsights(result)

    checkValue("series highest resistance identified", "R3" in resistanceInsights[0], True)
    checkValue("series lowest resistance identified", "R1" in resistanceInsights[1], True)
    checkValue("series highest voltage drop identified", "R3" in voltageInsights[0], True)
    checkValue("series current explanation", "same current" in currentInsights[0], True)
    checkValue("series open component breaks entire path", "entire circuit" in behaviorInsight, True)
    checkValue("series recommendations are provided", len(recommendationInsights) >= 3, True)
    checkValue("all five insight categories generated", len(allInsights), 5)


def checkParallelInsights():
    result = analyzeCircuit("parallel", [10, 20, 40], 12)
    resistanceInsights = analyzeResistance(result)
    voltageInsights = analyzeVoltage(result)
    currentInsights = analyzeCurrent(result)
    behaviorInsight = analyzeCircuitBehavior(result)

    checkValue("parallel highest resistance identified", "R3" in resistanceInsights[0], True)
    checkValue("parallel lowest resistance identified", "R1" in resistanceInsights[1], True)
    checkValue("parallel equal voltage explanation", "same voltage" in voltageInsights[0], True)
    checkValue("parallel highest current branch identified", "R1" in currentInsights[0], True)
    checkValue("parallel open branch leaves other branches operating", "other intact branches" in behaviorInsight, True)



checkSeriesCircuit()
checkParallelCircuit()
checkZeroVoltage()
checkHistory()
checkSeriesInsights()
checkParallelInsights()
