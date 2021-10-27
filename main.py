class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        return round((self.weight_kg * 2.20462262), 2)

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

game = input("Do you wanna enter A) footbal player data or B) basketball player data?")

if game.upper() == "A":
    f_name = input("Enter football player's first name: ")
    l_name = input("Enter football player's last name: ")
    height = input("Enter football player's height: ")
    weight = input("Enter football player's weight: ")
    goals = input("Enter the number of football player's goals: ")
    y_cards = input("Enter the number of football player's yellow cards: ")
    r_cards = input("Enter the number of football player's red cards: ")

    new_player = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
                                goals=int(goals), yellow_cards=int(y_cards), red_cards=int(r_cards))

    with open("football_players.json", "w") as football_file:
        football_file.write(str(new_player.__dict__))

    print("Player successfully entered!")
    print("Player's data: {0}".format(new_player.__dict__))

elif game.upper() == "B":
    f_name = input("Enter basketball player's first name: ")
    l_name = input("Enter basketball player's last name: ")
    height = input("Enter basketball player's height: ")
    weight = input("Enter basketball player's weight: ")
    points = input("Enter the number of basketball player's points: ")
    rebounds = input("Enter the number of basketball player's rebounds: ")
    assists = input("Enter the number of basketball player's assists: ")

    new_player = BasketballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
                                points=int(points), rebounds=int(rebounds), assists=int(assists))

    with open("basketball_players.json", "w") as basketball_file:
        basketball_file.write(str(new_player.__dict__))

    print("Player successfully entered!")
    print("Player's data: {0}".format(new_player.__dict__))