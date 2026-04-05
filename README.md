# HIRELYTICS

**Placement Prediction System using Machine Learning**

## Overview

Hirelytics is an end-to-end machine learning web application that predicts a student’s placement probability based on academic performance and professional experience. It integrates a trained Random Forest model with a Flask backend to deliver real-time predictions through a modern web interface.

## Features

* Real-time placement probability prediction
* Machine Learning model integration (Random Forest)
* Clean and responsive UI
* REST API using Flask
* Lightweight data handling (no database required)
* Custom preprocessing using C++

## Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask (Python)
* **Machine Learning:** Scikit-learn, Pandas, Joblib
* **Data Processing:** C++

## Input Parameters

The model uses the following inputs:

* CGPA
* Internships
* Projects
* Workshops
* Aptitude Test Score
* Soft Skills Rating
* Placement Training (Yes/No)

## Project Structure

```
├── app.py
├── placement_model.pkl
├── index.html
├── result.html
├── data_cleaning.cpp
```

## How It Works

1. User enters details in the web form
2. Data is sent to Flask backend via API
3. Backend processes input and feeds it to the ML model
4. Model returns placement probability
5. Result is displayed on the frontend

## Setup & Installation

1. Clone the repository

```
git clone https://github.com/your-username/hirelytics.git
cd hirelytics
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the application

```
python app.py
```

4. Open in browser

```
http://127.0.0.1:5000/
```

## Future Improvements

* Add database support
* Improve model accuracy with larger datasets
* Deploy on cloud (AWS/GCP)
* Add authentication system

## Contributing

Contributions are welcome. Feel free to open issues or submit pull requests.

---

