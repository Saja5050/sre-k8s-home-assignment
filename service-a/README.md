# 📈 Bitcoin Price Tracker

This is a lightweight Flask-based web application that tracks the current Bitcoin price in USD using the CoinGecko API. The app fetches the price every minute, displays it live on a webpage, and logs a rolling 10-minute average every 10 minutes.

It's designed to be production-ready with a clean structure, Dockerized setup, and optional health checks.

---

## 🚀 Features

- 💰 Live Bitcoin price updates (every minute)
- 📊 10-minute average based on last 10 prices
- 🧪 `/health` endpoint for container readiness
- 🐳 Dockerfile includes `HEALTHCHECK`
- 🔒 Clean, modular, and testable codebase
- 📄 Console logging for both current and average prices

---

## 🛠 How to Run

### 🔧 Locally (Python)

1. Clone the repository:

```bash
git clone https://github.com/Saja5050/bitcoin-app.git
cd bitcoin-tracker
Install dependencies:

```bash
pip install -r requirements.txt
```
Run the app:

```bash
python app.py
```
Open http://localhost:5000 in your browser.

### 🐳 Run with Docker

Build the Docker image:

```bash
docker build -t bitcoin-tracker .
```
Run the container:

```bash
docker run -p 5000:5000 bitcoin-tracker
```
Optional: Check health manually

```bash
curl http://localhost:5000/health
```
The app will be available at: http://localhost:5000

## 📁 Project Structure

```
bitcoin-tracker/
├── app.py                  # Flask app with route definitions
├── tracker.py              # Core logic for fetching & computing prices
├── requirements.txt        # Python production dependencies
├── dev-requirements.txt    # Development dependencies (tests etc.)
├── Dockerfile              # Container definition
├── .gitignore              # Files ignored by Git
├── templates/
│   └── index.html          # Web frontend
```

## 👤 Author

Developed by **Saja Abu Krenat**, Software Engineer

## 📜 License

MIT License – feel free to use, modify, and build upon this project.