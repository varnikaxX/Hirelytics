import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Load the cleaned dataset
data = pd.read_csv('E:/codei/GDG/cleaned_d.csv')

# 2. Separate Features (X) and Target (y)
# Features: CGPA, Internships, Projects, Workshops,Aptitude, SoftSkills, Training
X = data.drop(['Placed','Student ID'], axis=1) 
y = data['Placed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(f"✅ Model Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")


joblib.dump(model, 'placement_model.pkl')

print("📂 Model saved as placement_model.pkl in the foler")

