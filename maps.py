def get_owner(team_id):
    team_map = {1: "Daniel", 2: "Travis", 3: "Mike", 4: "Omid", \
                5: "Dilkarn", 6: "Liam", 7: "Gurkirat"}
    return team_map.get(team_id)

def get_position(lineup_id):
    lineup_map = {0: 'C', 1: 'LW', 2: 'RW', 3: 'F', 4: 'D', \
                  5: 'G', 6: 'UTIL', 7: 'BE', 8: 'IR'}
    return lineup_map.get(lineup_id)

def get_stat_name(stat_id):
    stat_map = {0: 'GS', 1: 'W', 2: 'L', 3: 'SA', 4: 'GA', 5: 'ENGA', 6: 'SV', \
                7: 'SO', 8: 'TOI(G)', 9: 'OTL', 10: 'GAA', 11: 'SV%', 12: 'GW%', \
                13: 'G', 14: 'A', 15: '+/-', 16: 'P', 17: 'PIM', 18: 'PPG', \
                19: 'PPA', 20: 'SHG', 21: 'SHA', 22: 'GWG', 23: 'FOW', 24: 'FOL', \
                25: 'SHF', 26: 'TOI(S)', 27: 'ATOI', 28: 'HT', 29: 'SOG', \
                30: 'GP', 31: 'HIT', 32: 'BLK', 33: 'DPTS', 34: 'GP(S)', \
                35: 'STG', 36: 'STA', 37: 'STP', 38: 'PPP', 39: 'SHP'}
    return stat_map.get(stat_id)