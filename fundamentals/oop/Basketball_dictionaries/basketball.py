

from sys import displayhook


class Player:

    def __init__(self, dict):
        self.name = dict['name']
        self.age = dict['age']
        self.position = dict['position']
        self.team = dict['team']

    def __repr__(self):
        display = f"Name: {self.name}  Age: {self.age}  Pos: {self.position}  Team: {self.team}"
        return display




players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# Create your Player instances here!
Kevin = Player(kevin)
Jason = Player(jason)
Kyrie = Player(kyrie)

print(Kevin.name)
# player_jason = ???

new_team = []
for playerdict in players:
    new_team.append(playerdict)

print(new_team)
print(Kevin)
print(Jason)
print(Kyrie)