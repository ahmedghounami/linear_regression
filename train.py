#!/usr/bin/env python3

import csv


DATA_FILE = "data.csv"
THETAS_FILE = "thetas.csv"

LEARNING_RATE = 1e-12
ITERATIONS = 2

def load_data(filename):
    mileages = []
    prices = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("The dataset has no header")

        if "km" not in reader.fieldnames:
            raise ValueError("The dataset must contain a 'km' column")

        if "price" not in reader.fieldnames:
            raise ValueError("The dataset must contain a 'price' column")

        for row in reader:
            mileage = float(row["km"])
            price = float(row["price"])

            mileages.append(mileage)
            prices.append(price)

    if len(mileages) == 0:
        raise ValueError("The dataset is empty")

    return mileages, prices


def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def loss_function(mileages, prices, theta0, theta1):
    total_loss = 0.0
    m = len(mileages)

    for i in range(m):
        prediction = estimate_price(
            mileages[i],
            theta0,
            theta1
        )

        error = prediction - prices[i]
        total_loss += error ** 2

    return total_loss / m


def gradient_descent(
    mileages,
    prices,
    theta0,
    theta1,
    learning_rate
):
    m = len(mileages)

    theta0_gradient = 0.0
    theta1_gradient = 0.0

    for i in range(m):
        prediction = estimate_price(
            mileages[i],
            theta0,
            theta1
        )

        error = prediction - prices[i]
        print(f"Prediction: {prediction}, Actual: {prices[i]}, Error: {error}")
        theta0_gradient += error
        theta1_gradient += error * mileages[i]
        print(f"theta0_gradient: {theta0_gradient}, theta1_gradient: {theta1_gradient}")

    tmp_theta0 = learning_rate * theta0_gradient / m
    tmp_theta1 = learning_rate * theta1_gradient / m

    new_theta0 = theta0 - tmp_theta0
    new_theta1 = theta1 - tmp_theta1
    
    return new_theta0, new_theta1


def save_thetas(filename, theta0, theta1):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["theta0", "theta1"])
        writer.writerow([theta0, theta1])


def main():
    try:
        mileages, prices = load_data(DATA_FILE)

        theta0 = 0.0
        theta1 = 0.0

        for iteration in range(ITERATIONS):
            theta0, theta1 = gradient_descent(
                mileages,
                prices,
                theta0,
                theta1,
                LEARNING_RATE
            )

            current_loss = loss_function(
                mileages,
                prices,
                theta0,
                theta1
            )
            # print(f"Iteration {iteration}: Loss = {current_loss}, theta0 = {theta0}, theta1 = {theta1}")

            if iteration % 10000 == 0:
                print(
                    f"Iteration {iteration}: "
                    f"Loss = {current_loss}, "
                    f"theta0 = {theta0}, "
                    f"theta1 = {theta1}"
                )

        save_thetas(
            THETAS_FILE,
            theta0,
            theta1
        )

        print("\nTraining completed.")
        print(f"theta0 = {theta0}")
        print(f"theta1 = {theta1}")
        print(f"Parameters saved in '{THETAS_FILE}'.")

    except FileNotFoundError:
        print(f"Error: '{DATA_FILE}' was not found.")

    except PermissionError:
        print("Error: permission denied.")

    except (ValueError, KeyError) as error:
        print(f"Error: invalid dataset: {error}")

    except OSError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()