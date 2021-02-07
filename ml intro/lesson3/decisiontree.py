from sklearn.tree import DecisionTreeRegressor
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

# Fit model
predict_price_model.fit(X, y)


# Making predictions
print("Making predictions for the following 5 houses:")
print(house_data.head()["Price"], end="\n\n")
print("The predictions are")
print(predict_price_model.predict(X.head()))
