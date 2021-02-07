from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split  # use to split data into train and test
from sklearn.metrics import mean_absolute_error
import pandas as pd

data_path = "..\\lesson2\\input\\melbourne-housing-snapshot\\melb_data.csv"

house_data = pd.read_csv(data_path)

# dropna drops missing values (think of na as "not available")
house_data.dropna(axis=0)

# Selecting The Prediction Target
y = house_data["Price"]

# Choosing Features
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

# By convention, "features" is called X
X = house_data[features]

print(X.describe(), end="\n\n")
print(X.head(), end="\n\n")

# Define model. Specify a number for random_state to ensure same results each run
predict_price_model = DecisionTreeRegressor(random_state=69)

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=69)

# Fit model
predict_price_model.fit(X_train, y_train)


# Making predictions
predictions = predict_price_model.predict(X_test)

# Mean absolute error
print(mean_absolute_error(y_test, predictions))

