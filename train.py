import csv

def load_data(filename):
    mileages = []
    prices = []

    # with: used to close the file automatically
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            mileages.append(float(row["km"]))
            prices.append(float(row["price"]))

    return mileages, prices

def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def normalize_data(mileages):
    max_mileage = max(mileages)
    print(max_mileage)
    normalized = []

    i = 0
    for km in mileages:
        normalized.append(km / max_mileage)
        print(normalized[i])
        i += 1

    return normalized, max_mileage

def train_one_step(mileages, prices, theta0, theta1, learning_rate):
    m = len(mileages)

    sum_error_theta0 = 0
    sum_error_theta1 = 0

    for i in range(m):
        prediction = estimate_price(mileages[i], theta0, theta1)
        error = prediction - prices[i]

        sum_error_theta0 += error
        sum_error_theta1 += error * mileages[i]

    tmp_theta0 = learning_rate * (1 / m) * sum_error_theta0
    tmp_theta1 = learning_rate * (1 / m) * sum_error_theta1

    new_theta0 = theta0 - tmp_theta0
    new_theta1 = theta1 - tmp_theta1

    return new_theta0, new_theta1
def train(mileages, prices, learning_rate, epochs):
    theta0 = 0
    theta1 = 0

    for _ in range(epochs):
        theta0, theta1 = train_one_step(
            mileages,
            prices,
            theta0,
            theta1,
            learning_rate
        )

    return theta0, theta1

    # ------------------- #

mileages, prices = load_data("data.csv")

print("Mileages:", mileages)
print("Prices:", prices)
# print(estimate_price(100000, 0, 0))
# print(estimate_price(100000, 10000, -0.05))

normalized_mileages, max_mileage = normalize_data(mileages)

# print("Max mileage:", max_mileage)
# print("Normalized:", normalized_mileages)

theta0 = 0
theta1 = 0
learning_rate = 0.1

theta0, theta1 = train_one_step(
    normalized_mileages,
    prices,
    theta0,
    theta1,
    learning_rate
)

# print("theta0:", theta0)
# print("theta1:", theta1)


# theta0, theta1 = train(normalized_mileages, prices, 0.1, 10000)

# print("Final theta0:", theta0)
# print("Final theta1:", theta1)

# test_km = 100000
# normalized_test_km = test_km / max_mileage

# predicted_price = estimate_price(normalized_test_km, theta0, theta1)

# print("Prediction for", test_km, "km:", predicted_price)