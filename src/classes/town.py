class Town:
    def __init__(self, name, region):
        self.name = name
        self.region = region


towns = [Town("балашиха", "мо"), Town("химки", "мо"), Town("тула", "тульская область")]


def find(towns, region):
    return (town.name for town in towns if town.region == region)


if __name__ == "__main__":
    print([town for town in find(towns, "мо")])
