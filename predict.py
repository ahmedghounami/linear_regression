#!/usr/bin/env python3

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

THETAS_FILE = "thetas.csv"


def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def load_thetas(filename):
    theta0 = 0.0
    theta1 = 0.0

    try:
        with open(filename, "r", newline="") as file: 
            reader = csv.DictReader(file) # reader is 
            row = next(reader, None)

            if row is None:
                return theta0, theta1

            theta0 = float(row["theta0"])
            theta1 = float(row["theta1"])

    except FileNotFoundError:
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
        theta0, theta1 = load_thetas(
            THETAS_FILE
        )
        mileage_X = read_mileage()


        estimated_price = estimate_price(
            mileage_X,
            theta0,
            theta1
        )

        print(
            f"Estimated price: "
            f"{estimated_price:.2f}"
        )

        
        df = pd.read_csv("data.csv")

        if "km" not in df.columns:
            raise ValueError(
                "The dataset must contain a 'km' column"
            )

        if "price" not in df.columns:
            raise ValueError(
                "The dataset must contain a 'price' column"
            )

        if df.empty:
            raise ValueError("The dataset is empty")

      
        mileage = df["km"].to_numpy(dtype=float)
        y = df["price"].to_numpy(dtype=float)

        predected = theta0 + theta1 * mileage

        plt.figure(figsize=(12, 8)) # 8
        plt.scatter(
            mileage,
            y,
            label="Data points",
        )
        plt.plot(
            mileage,
            predected,
            label="Regression line"
        )
        plt.xlabel("Mileage (km)")
        plt.ylabel("Price")
        plt.title("Linear Regression")
        plt.legend()
        plt.grid()
        plt.show()
        

    except ValueError as error:
        print(f"Error: {error}")

    except KeyboardInterrupt:
        print("\nProgram interrupted.")

    except EOFError:
        print("\nNo input received.")


if __name__ == "__main__":
    main()