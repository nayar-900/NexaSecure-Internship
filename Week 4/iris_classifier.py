from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("--- Day 28: Mini Project 6 (Iris Flower Classifier) ---")
print("Loading dataset...")
iris = load_iris()
X, y = iris.data, iris.target

print("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training the Random Forest AI Model...")
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

print("Testing the model...")
predictions = clf.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"\n AI Model Accuracy: {accuracy * 100:.2f}%")
print("The AI successfully learned how to classify the flowers!")