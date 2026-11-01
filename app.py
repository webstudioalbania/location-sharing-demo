from flask import Flask, render_template, request, jsonify
from datetime import datetime, timezone
from threading import Lock

app = Flask(__name__)
latest_location = None
lock = Lock()

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/share-location")
def share_location():
    data = request.get_json(silent=True) or {}
    try:
        lat, lon = float(data["latitude"]), float(data["longitude"])
        accuracy = float(data.get("accuracy", 0))
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            raise ValueError()
    except (KeyError, TypeError, ValueError):
        return jsonify({"ok": False, "error": "Invalid coordinates"}), 400
    global latest_location
    with lock:
        latest_location = {"latitude": lat, "longitude": lon, "accuracy_m": accuracy,
                           "received_at": datetime.now(timezone.utc).isoformat()}
    print("Visitor-approved location received:", latest_location, flush=True)
    return jsonify({"ok": True})

@app.get("/latest")
def latest():
    with lock:
        return jsonify(latest_location or {"message": "No location shared yet."})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
