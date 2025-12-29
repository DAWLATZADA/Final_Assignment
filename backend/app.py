from flask import Flask, jsonify
from flask_cors import CORS
import threading
import time
import random

app = Flask(__name__)

# ENABLE CORS
CORS(app)

TOTAL_SEATS = 5
available_seats = TOTAL_SEATS
lock = threading.Lock()


@app.route("/book_unsafe")
def book_unsafe():
    global available_seats
    if available_seats > 0:
        time.sleep(random.uniform(0.1, 0.5))
        available_seats -= 1
        return jsonify(status="SUCCESS", remaining_seats=available_seats)
    return jsonify(status="FAILED", message="No seats available")


@app.route("/book_safe")
def book_safe():
    global available_seats
    with lock:  # CRITICAL SECTION
        if available_seats > 0:
            time.sleep(random.uniform(0.1, 0.5))
            available_seats -= 1
            return jsonify(status="SUCCESS", remaining_seats=available_seats)
        return jsonify(status="FAILED", message="No seats available")


@app.route("/reset")
def reset():
    global available_seats
    available_seats = TOTAL_SEATS
    return jsonify(message="Seats reset", available_seats=available_seats)


if __name__ == "__main__":
    app.run(debug=True)
