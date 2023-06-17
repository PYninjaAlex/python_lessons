import json
import random
from typing import NoReturn

with open("historical_events.json", "r", encoding="utf-8") as file:
    historical_events = json.load(file)


class Question:
    def __init__(self):
        self.choice = random.choice([x for x in range(len(historical_events))])
        self.theme = historical_events[self.choice]["тема"]
        self.year = historical_events[self.choice]["год"]
        self.place = historical_events[self.choice]["место"]

    def __call__(self, name: str) -> NoReturn:
        print(
            f"Привет, {name}! Сегодня я расскажу тебе про {self.theme}! Оно произошло в {self.year}. Место где происходило {self.theme} - {self.place}.",
            sep="")


question_object_1 = Question()
question_object_1("Alex")
