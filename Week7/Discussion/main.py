from batting_average import BaseballPlayer

def main():
    player = BaseballPlayer(name="John Doe", hits=50, at_bats=150)
    batting_average = player.calculate_batting_average()
    print(f"{player.name}'s batting average is {batting_average:.3f}")

if __name__ == "__main__":
    main()