# Created on: 06-02-2024
# This program used enums, transformation functions, and closures.

from enum import Enum

class EasternConference(Enum):
    CELTICS = 1
    KNICKS = 2
    BUCKS = 3
    CAVALIERS = 4
    MAGIC = 5
    PACERS = 6
    SIXERS = 7
    HEAT = 8
    BULLS = 9
    HAWKS = 10
    NETS = 11
    RAPTORS = 12
    HORNETS = 13
    WIZARDS = 14
    PISTONS = 15

class WesternConference(Enum):
    THUNDER = 1
    NUGGETS = 2
    TIMBERWOLVES = 3
    CLIPPERS = 4
    MAVERICKS = 5
    SUNS = 6
    LAKERS = 7
    PELICANS = 8
    KINGS = 9
    WARRIORS = 10
    ROCKETS = 11
    JAZZ = 12
    GRIZZLIES = 13
    SPURS = 14
    BLAZERS = 15

def check_nba_season_information(transformation_function):
    '''
    This function returns an inner function to check NBA playoff team information.

    Parameters:
        transformation_function (function): A function that transforms team information.

    Returns:
        function: A function that takes a team as input and applies the transformation function to it.
                  If the team did not make the playoffs, raises a ValueError message.

    Examples:
    >>> get_home_status = check_nba_season_information(check_home_status)
    >>> get_home_status(WesternConference.MAVERICKS)
    {'Team': 'Mavericks', 'Rank': 5, 'Home': 'No'}

    >>> get_opponent_name = check_nba_season_information(check_opponent_name)
    >>> get_opponent_name(WesternConference.MAVERICKS)
    {'Team': 'Mavericks', 'Rank': 5, 'Opponent': 'Clippers', 'Opponent Rank': 4}
    '''
    teams = []

    def check_nba_playoff_information(team):
        if team.value <= 8:
            teams.append(team.name.title())
            return transformation_function(team)
        raise ValueError(f"{team.name.title()}: missed playoffs")
    
    def get_teams():
        return teams

    check_nba_playoff_information.get_teams = get_teams
        
    return check_nba_playoff_information

# Transformation functions
def check_home_status(team):
    return {
        "Team": team.name.title(),
        "Rank": team.value,
        "Home": "Yes" if (team.value <= 4) else "No", 
    }

def check_opponent_name(team):
    opponent_rank = 9 - team.value
    opponent_name = (EasternConference if team in EasternConference else WesternConference)(opponent_rank).name.title()
    return {
        "Team": team.name.title(),
        "Rank": team.value,
        "Opponent": opponent_name,
        "Opponent Rank": opponent_rank,
    }

# Applying transformations
get_home_status = check_nba_season_information(check_home_status)
get_opponent_name = check_nba_season_information(check_opponent_name)

print(get_home_status(WesternConference.MAVERICKS))
print(get_home_status(WesternConference.SUNS))
print(get_opponent_name(EasternConference.KNICKS))
print(get_opponent_name(EasternConference.BUCKS))

# Accessing the teams list via closure
print("Teams checked for home court:", get_home_status.get_teams())
print("Teams checked for opponent:", get_opponent_name.get_teams())