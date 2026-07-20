#!/usr/bin/env python3

import csv


THETAS_FILE = "thetas.csv"


def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def load_thetas(filename):
    theta0 = 0.0
    theta1 = 0.0

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            row = next(reader, None)

            if row is None:
                return theta0, theta1

            theta0 = float(row["theta0"])
            theta1 = float(row["theta1"])

    except FileNotFoundError:
        # Before training, both values must be zero.
        pass

    except (ValueError, KeyError):
        print(
            "Warning: invalid parameter file. "
            "Using theta0 = 0 and theta1 = 0."
        )

        theta0 = 0.0
        theta1 = 0.0

    return theta0, theta1


def read_mileage():
    value = input("Enter a mileage: ").strip()

    mileage = float(value)

    if mileage < 0:
        raise ValueError("Mileage cannot be negative")

    return mileage


def main():
    try:
        mileage = read_mileage()

        theta0, theta1 = load_thetas(
            THETAS_FILE
        )

        estimated_price = estimate_price(
            mileage,
            theta0,
            theta1
        )

        print(
            f"Estimated price: "
            f"{estimated_price:.2f}"
        )

    except ValueError as error:
        print(f"Error: {error}")

    except KeyboardInterrupt:
        print("\nProgram interrupted.")

    except EOFError:
        print("\nNo input received.")


if __name__ == "__main__":
    main()