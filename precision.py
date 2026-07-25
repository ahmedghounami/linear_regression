#!/usr/bin/env python3

import sys

import numpy as np
import pandas as pd


DATA_FILE = "data.csv"
THETAS_FILE = "thetas.csv"


def main():
    try:
        data = pd.read_csv(DATA_FILE)

        if "km" not in data.columns or "price" not in data.columns:
            raise ValueError(
                "data.csv must contain 'km' and 'price' columns."
            )

        mileage = data["km"].to_numpy(dtype=float)
        real_prices = data["price"].to_numpy(dtype=float)

        thetas = pd.read_csv(THETAS_FILE)

        if "theta0" not in thetas.columns or "theta1" not in thetas.columns:
            raise ValueError(
                "thetas.csv must contain 'theta0' and 'theta1' columns."
            )

        theta0 = float(thetas["theta0"].iloc[0])
        theta1 = float(thetas["theta1"].iloc[0])

        predicted_prices = theta0 + theta1 * mileage

        errors = predicted_prices - real_prices

        mae = np.mean(np.abs(errors)) # mean absolute error

        mse = np.mean(errors ** 2) # mean squared error

        rmse = np.sqrt(mse) # root mean squared error

        print(f"Theta0: {theta0}")
        print(f"Theta1: {theta1}")
        print()

        print("Prediction results:")

        for km, real, predicted, error in zip(
            mileage,
            real_prices,
            predicted_prices,
            errors
        ):
            print(
                f"Mileage: {km:.0f} km | "
                f"Real price: {real:.2f} | "
                f"Predicted price: {predicted:.2f} | "
                f"Error: {error:.2f}"
            )

        print()
        print(f"MAE:  {mae:.2f}")
        print(f"MSE:  {mse:.2f}")
        print(f"RMSE: {rmse:.2f}")

    except FileNotFoundError as error:
        print(f"Error: file not found: {error.filename}")
        sys.exit(1)

    except (ValueError, TypeError, IndexError) as error:
        print(f"Error: {error}")
        sys.exit(1)

    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()