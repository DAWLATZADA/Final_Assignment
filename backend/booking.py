import threading
import time
import random
from typing import Dict, Any

class BookingSystem:
    def init(self):
        self.available_seats = 5
        self.lock = threading.Lock()
        self.history = []           # for demo purposes

    def reset(self):
        """Reset state for new demo"""
        self.available_seats = 5
        self.history = []

    def book_without_lock(self, customer_id: int) -> Dict[str, Any]:
        result = {"customer": customer_id, "success": False, "remaining": self.available_seats}

        if self.available_seats > 0:
            time.sleep(random.uniform(0.1, 0.5))  # simulate delay / processing
            self.available_seats -= 1
            result["success"] = True
            result["remaining"] = self.available_seats
            self.history.append(f"Customer {customer_id} booked (NO LOCK) → {self.available_seats} left")
        else:
            self.history.append(f"Customer {customer_id} failed (NO LOCK) → no seats")

        return result

    def book_with_lock(self, customer_id: int) -> Dict[str, Any]:
        result = {"customer": customer_id, "success": False, "remaining": self.available_seats}

        with self.lock:
            if self.available_seats > 0:
                time.sleep(random.uniform(0.1, 0.5))
                self.available_seats -= 1
                result["success"] = True
                result["remaining"] = self.available_seats
                self.history.append(f"Customer {customer_id} booked (WITH LOCK) → {self.available_seats} left")
            else:
                self.history.append(f"Customer {customer_id} failed (WITH LOCK) → no seats")

        return result

    def get_state(self) -> Dict[str, Any]:
        return {
            "available_seats": self.available_seats,
            "history": self.history[-15:],  # last 15 actions
        }