# 🌦️ Weather Forecast Dashboard on Google Cloud Platform

This project is a serverless, automated weather monitoring and visualization system using **OpenWeatherMap API** and **Google Cloud Platform** services. It collects current weather data periodically, stores it in BigQuery, and displays it on an interactive Looker Studio dashboard.

---

## 🌐 Live Demo

🔗 https://lookerstudio.google.com/embed/u/0/reporting/c1d5a902-3fc0-4ff4-b123-b48f60afb67c/page/y6WPF

---

## 🚀 Features

- Fetches weather data from OpenWeatherMap for multiple cities
- Automatically runs every 30 minutes via Cloud Scheduler
- Uses Cloud Functions and Pub/Sub for serverless data processing
- Stores weather data in BigQuery for querying and analytics
- Visualizes data using Looker Studio (Google Data Studio)
- Supports PDF export and scheduled email reports

---

## 🧰 Tech Stack

- **GCP Services:**
1. **Google Cloud Functions** – Fetch weather data
2. **Cloud Scheduler** – Schedule periodic function calls
3. **Cloud Pub/Sub** – Transmit data to BigQuery
4. **BigQuery** – Store and query weather data
5. **Looker Studio** – Dashboard and reporting
- **OpenWeatherMap API** – Weather data provider

---

## 🧱 Architecture

```plaintext
Cloud Scheduler (cron job)
        ↓
Cloud Function (Python)
        ↓
OpenWeatherMap API → JSON Weather Data
        ↓
Cloud Pub/Sub
        ↓
BigQuery Table (weather_data.city_weather)
        ↓
Looker Studio Dashboard

```
---

## 📁 Project Structure

```

weather-forecast-dashboard/
│
├── main.py                # Cloud Function to fetch and publish weather data
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation (this file)

````

---

## 🔑 Prerequisites

- Google Cloud Platform account (with billing enabled)
- OpenWeatherMap API key (https://openweathermap.org/api)
- Python 3.11+ installed (for local testing)

---

## 🛠️ GCP Setup

### 1. Creating GCP Project and Enabling Services

* Create a new project and enable the following APIs:
  * Cloud Functions
  * Cloud Scheduler
  * BigQuery
  * Pub/Sub
  * Cloud Logging

### 2. Set Up BigQuery

* Create a **dataset** (eg. weather_data) and **table** (eg. city_weather) with schema:

```text
city: STRING
country: STRING
temperature: FLOAT
humidity: INTEGER
description: STRING
timestamp: TIMESTAMP
```

### 3. Set Up Pub/Sub

* Create a topic (eg. weather-topic)
* Create a **BigQuery subscription** to push data to the `city_weather` table

### 4. Deploying the Cloud Function

```bash
gcloud functions deploy fetch_weather \
  --runtime python311 \
  --trigger-http \
  --allow-unauthenticated \
  --set-env-vars OPENWEATHER_API_KEY=your_api_key,GCP_PROJECT=your_project_id
```

### 5. Set Up Cloud Scheduler

* Create a job to call the Cloud Function every 30 minutes:
  * Frequency: `*/30 * * * *`
  * Target: HTTP
  * Auth: Use OIDC with Cloud Function’s service account

### 6. Building the Looker Studio Dashboard

* Create a new report and add your BigQuery table (`weather_data.city_weather`) as a data source
* Create charts:
  * Table of latest weather
  * Line chart (temperature over time)
  * Bar chart (average humidity)
  * Filters for city and date

### 7. Automating PDF Reports
* In Looker Studio:
  * Click `Share > Schedule email delivery`
  * Set up daily/weekly report to your email

---
