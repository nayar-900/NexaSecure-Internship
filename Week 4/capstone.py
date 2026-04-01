import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("--- Day 23: Data Preparation ---")
# Creating a simple dataset: Study Hours vs. Marks
data = {
    'Study_Hours': [1, 2, 3, 4, 4.5, 5, 6, 7, 8, 9],
    'Marks': [40, 50, 60, 65, 70, 75, 85, 90, 95, 98]
}
df = pd.DataFrame(data)
print("Dataset Head:")
print(df.head())

print("\n--- Day 24 & 25: Build and Test Model ---")
X = df[['Study_Hours']] # Input feature
y = df['Marks']         # Output target

# Split data into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)
print(" Model Trained Successfully!")

# Test the model and make a prediction
test_hours = 5.5
predicted_mark = model.predict([[test_hours]])
print(f"\n AI Prediction: If a student studies for {test_hours} hours, their predicted marks are: {predicted_mark[0]:.2f}")

print("\n--- Day 26 & 27: Visualize Results ---")
# Plotting the regression line
plt.scatter(X, y, color='blue', label='Actual Student Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='AI Prediction Line')
plt.title('AI Capstone: Study Hours vs Predicted Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.legend()
plt.grid(True)
plt.show() # TAKE SCREENSHOT OF THIS GRAPH!