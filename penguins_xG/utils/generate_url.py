url_base_team = 'https://moneypuck.com/moneypuck/playerData/careers/gameByGame/regular/teams'
url_teams_all = 'https://moneypuck.com/moneypuck/playerData/seasonSummary/2023/regular/teams.csv'


def generate_url_teams_all():
    return url_teams_all

def generate_url_team(team):
    return f'{url_base_team}/{team}.csv'
