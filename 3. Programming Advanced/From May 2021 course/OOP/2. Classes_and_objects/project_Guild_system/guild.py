from project_Guild_system.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player not in self.players:
            if player.guild == "Unaffiliated":
                self.players.append(player)
                player.guild = self.name
                return f'Welcome player {player.name} to the guild {self.name}'
            else:
                return f'Player {player.name} is in another guild.'

        return f'Player {player.name} is already in the guild.'

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f'Player {player.name} has been removed from the guild.'

        return f'Player {player.name} is not in the guild.'

    def guild_info(self):
        result = ""
        result += f'Guild: {self.name}\n'
        for player in self.players:
            result += f'{player.player_info()}'
        return result




player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())


