from maps import get_owner, get_position
import pickle
import requests
import sys

class EspnFantasyApi:
    BASE_URL = 'http://fantasy.espn.com/apis/v3/games/fhl/seasons/2019/segments/0/leagues/{}'

    def __init__(self, league_id):
        self.url = self.BASE_URL.format(league_id)

    def get_roster(self, scoring_period):
        params = {'view': 'mRoster', 'scoringPeriodId': scoring_period}
        return requests.get(self.url, params=params).json()
    
    def get_latest_scoring_period(self):
        params = {'view': 'mRoster'}
        return requests.get(self.url, params=params).json()['status']['latestScoringPeriod']

gp_totals = {}
def add_to_map(posiiton, gp, owner):
    if owner not in gp_totals:
        gp_totals[owner] = {'F': 984, 'D': 492, 'G': 164, 'UTIL': 82, 'Total': 0}
    gp_totals[owner][posiiton] -= gp
    gp_totals[owner]['Total'] += gp

efs = EspnFantasyApi(sys.argv[1])
current_scorint_period = efs.get_latest_scoring_period() + 1
for i in range(1, current_scorint_period):
    teams = efs.get_roster(i)['teams']
    for team in teams:
        owner_name = get_owner(team['id'])
        data = team['roster']['entries']
        for player in data:
            lineup_slot = get_position(player['lineupSlotId'])
            if lineup_slot == 'BE' or lineup_slot == 'IR':
                # This player wasn't in a spot that accumulates games played.
                continue

            stats_list = player['playerPoolEntry']['player']['stats']
            for stats in stats_list:
                if stats['scoringPeriodId'] == i:
                    if stats['stats'] == {}:
                        continue
                    games_played = int(stats['stats']['30'])

                    if games_played != 0:
                        add_to_map(lineup_slot, games_played, owner_name)

for team in gp_totals:
    print('\n' + team)
    print('F', gp_totals[team]['F'], 'games remaining')
    print('D', gp_totals[team]['D'], 'games remaining')
    print('G', gp_totals[team]['G'], 'games remaining')
    print('UTIL', gp_totals[team]['UTIL'], 'games remaining')
    print('Total', gp_totals[team]['Total'])



        

