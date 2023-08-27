import os
import sys

import yaml


def addNumbers(a, b):
    result = a + b
    return result


if __name__ == "__main__":
    try:
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        print("Config file not found")
        sys.exit(1)
    num1 = config.get("num1", 0)
    num2 = config.get("num2", 0)
    sum = addNumbers(num1, num2)
    print(f"Sum of {num1} and {num2} is {sum}")
