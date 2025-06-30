from flask import Flask, render_template, jsonify
from tracker import BitcoinPriceTracker
import threading

app = Flask(__name__)
tracker = BitcoinPriceTracker()

@app.route("/service-a/")
def index():
    return render_template("index.html")

@app.route("/service-a/data")
def data():
    return jsonify(tracker.get_data())

@app.route("/service-a/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    threading.Thread(target=tracker.run, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
