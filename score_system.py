import json


class ScoreSystem:
    def __init__(self):
        self.file_path = "high_scores.json"
        self.high_scores = self.load_high_scores()

    def save_high_scores(self):
        with open(self.file_path, "w") as file:
            json.dump(self.high_scores, file, indent=2)

    def load_high_scores(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def add_score(self, score):
        self.high_scores.append({"score": score})
        self.high_scores = sorted(self.high_scores, key=lambda x: x["score"], reverse=True)[:10]
        self.save_high_scores()

    def get_high_scores(self):
        return self.high_scores
