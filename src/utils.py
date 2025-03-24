import json
import os

class GameUtils:
    @staticmethod
    def load_leaderboard(filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except:
            return []

    @staticmethod
    def save_leaderboard(data, filename):
        with open(filename, "w") as f:
            json.dump(data, f)

    @staticmethod
    def calculate_score(time, difficulty, hints_used):
        # Score calculation logic
        pass
