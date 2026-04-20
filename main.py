# I write this to make a easy python script painful xD

from dataclasses import dataclass

CHILD: int = 5
TEENAGER: int = 10
ADULT: int = 15

@dataclass
class Player:
    name: str
    age: int
    game_score: float
    is_member: bool

    # ask user for inputs
    def ask(self) -> None:
        self.name = input("Enter your name:\n")

        while True:
            age = input("Enter your age:\n")
            try:
                self.age = int(age)
                break
            except ValueError:
                print(f"Expect integer, find {type(age)}")

        while True:
            game_score = input("Enter your game score:\n")
            try:
                self.game_score = float(game_score)
                break
            except ValueError:
                print(f"Expect float, find {type(game_score)}")

        member_input = input("Are you a member? Enter Yes/No\n")
        match member_input:
            case member_input if member_input == "Yes":
                self.is_member = True
            case _:
                self.is_member = False

    # check the ability to continue
    def check_ablitiy(self) -> bool:
        if self.age <= 0:
            print(f"Expect age, find negative {self.age}")
            return False
        if self.game_score < 0 or self.game_score > 100:
            print(f"Expect 0-100, find out of scope {self.game_score}")
            return False
        return True

    # This function only print and won't change any `self.`
    def check_tournament(self) -> bool:
        if self.age >= 13 and self.game_score >= 50.0:
            print("You qualify for the tournament!")
            if self.game_score >= 80.0:
                print("Advanced division.")
                return True
            else:
                print("Standard division.")
                return True
        else:
            print("You do not qualify for the tournament yet.")
            return False

    def calc_fee(self) -> int:
        # if is member, store value as constant inline
        child = CHILD - 2
        teen = TEENAGER - 2
        adult = ADULT - 2
        if self.is_member:
            match self.age:
                case self.age if self.age < 13:
                    return child
                case self.age if self.age >= 13 and self.age <= 17:
                    return teen
                case _:
                    return adult
        else:
            match self.age:
                case self.age if self.age < 13:
                    return CHILD
                case self.age if self.age >= 13 and self.age <= 17:
                    return TEENAGER
                case _:
                    return ADULT

def initialize_player():
    player = Player("", 0, 0.0, False)
    player.ask()
    return player

def main():
    player = initialize_player()

    if not player.check_ablitiy():
        print("aborting for previous errors")
        return
    
    fee = player.calc_fee()

    # display
    print(f"\n\n\n\n-----------\nPlayer: {player.name}")
    if player.check_tournament():
        print(f"Entry fee: {fee}\nThanks for playing!")


if __name__ == "__main__":
    main()
