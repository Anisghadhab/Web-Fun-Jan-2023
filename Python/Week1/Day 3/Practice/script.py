class Player:
    def __init__(self, players_info):
        self.name = players_info["name"]
        self.age = players_info["age"]
        self.position = players_info["position"]
        self.team = players_info["team"]
        print(self.name)


# kevin = {
#     "name": "Kevin Durant",
#     "age": 34,
#     "position": "small forward",
#     "team": "Brooklyn Nets",
# }
# jason = {
#     "name": "Jason Tatum",
#     "age": 24,
#     "position": "small forward",
#     "team": "Boston Celtics",
# }
# kyrie = {
#     "name": "Kyrie Irving",
#     "age": 32,
#     "position": "Point Guard",
#     "team": "Brooklyn Nets",
# }

# players_info1 = Player(kyrie)
# players_info2 = Player(jason)
# players_info3 = Player(kevin)

# print(players_info1.name)


players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers",
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls",
    },
]

new_team = []

for players_info in players:
    list_player = Player(players_info)
    # print(players_info["name"])
    new_team.append(list_player) 
print(new_team[1])

# Create your Player instances here!
# player_jason = ???
