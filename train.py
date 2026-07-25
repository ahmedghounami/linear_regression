#!/usr/bin/env python3

import numpy as np
import pandas as pd


DATA_FILE = "data.csv"

LEARNING_RATE = 0.1
ITERATIONS = 100000
PRINT_INTERVAL = 1000


def gradient_descent(
    x,
    y,
    theta0,
    theta1,
    learning_rate,
    iterations
):
    n = len(y)

    for iteration in range(iterations):

        y_pred = theta0 + theta1 * x

        errors = y_pred - y
        

        errors_times_x = errors * x

        sum_errors_times_x = np.sum(errors_times_x)


        da = (1 / n) * sum_errors_times_x


        sum_errors = np.sum(errors)


        db = (1 / n) * sum_errors


        movement_theta0 = learning_rate * db

        movement_theta1 = learning_rate * da


        theta0 = theta0 - movement_theta0

        theta1 = theta1 - movement_theta1

    return theta0, theta1


def main():
    print("Gradient descent — simple linear regression")

    try:
       
        df = pd.read_csv(DATA_FILE)

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

        if not np.all(np.isfinite(mileage)):
            raise ValueError(
                "The 'km' column contains invalid values"
            )

        if not np.all(np.isfinite(y)):
            raise ValueError(
                "The 'price' column contains invalid values"
            )

        mileage_min = np.min(mileage)

   
        mileage_max = np.max(mileage)

        mileage_range = mileage_max - mileage_min

        if mileage_range == 0:
            raise ValueError(
                "All mileage values are identical"
            )

     
        mileage_normalized = (mileage - mileage_min) / mileage_range

        normalized_theta0 = 0.0
        normalized_theta1 = 0.0

        normalized_theta0, normalized_theta1 = gradient_descent(
            mileage_normalized,
            y,
            normalized_theta0,
            normalized_theta1,
            LEARNING_RATE,
            ITERATIONS
        )

        theta1 = normalized_theta1 / mileage_range

        theta0 = (
            normalized_theta0 - (normalized_theta1 * mileage_min / mileage_range)
        )

        
        with open("thetas.csv", "w") as file:
            file.write(f"theta0,theta1\n")
            file.write(f"{theta0},{theta1}\n")

        print("\nTraining completed")

        print(f"\ntheta0 = {theta0}")
        print(f"theta1 = {theta1}")
    except FileNotFoundError:
        print(f"Error: '{DATA_FILE}' was not found")

    except PermissionError:
        print(
            f"Error: permission denied while reading "
            f"'{DATA_FILE}'"
        )

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()