class BaseballPlayer:
    def __init__(self, name: str, hits: int, at_bats: int):
        self.name = name
        self.hits = hits
        self.at_bats = at_bats

    def calculate_batting_average(self) -> float:
        if self.at_bats == 0:
            return 0.0
        return self.hits / self.at_bats