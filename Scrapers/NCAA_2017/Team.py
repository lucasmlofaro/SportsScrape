class Team:
    def __init__(self, name):
        self.name = name
        self.schedule = []
        self.record = [0, 0]
        self.game_stats = {'GP': 0, 'PPG': 0, 'RPG': 0, 'APG': 0, 'SPG': 0, 'BPG': 0, 'TPG': 0,
                      'FG%': 0.0, 'FT%': 0.0, '3P%': 0.0}
        self.season_stats = {'FGM': 0, 'FGA': 0, 'FTM': 0, 'FTA': 0, '3PM': 0, '3PA': 0,
                        'PTS': 0, 'REB': 0, 'AST': 0, 'TO': 0, 'STL': 0, 'BLK': 0,
                        'OFFR': 0, 'DEFR': 0}

    def win_percentage(self):
        return self.record[0] / (sum(self.record))
