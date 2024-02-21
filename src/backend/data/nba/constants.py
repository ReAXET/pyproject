"""Constants for the NBA data module including the team_id list and 
team_id to team_abbrv mapping."""
# Team IDs
TEAM_ID_LIST = [
    1610612737, 1610612738, 1610612739, 1610612740, 1610612741, 1610612742,
    1610612743, 1610612744, 1610612745, 1610612746, 1610612747, 1610612748,
    1610612749, 1610612750, 1610612751, 1610612752, 1610612753, 1610612754,
    1610612755, 1610612756, 1610612757, 1610612758, 1610612759, 1610612760,
    1610612761, 1610612762, 1610612763, 1610612764, 1610612765, 1610612766
]

# Team ID to Team Abbreviation Mapping
TEAM_ID_TO_TEAM_ABBRV = {
    1610612737: 'ATL',
    1610612738: 'BOS',
    1610612739: 'CLE',
    1610612740: 'NOP',
    1610612741: 'CHI',
    1610612742: 'DAL',
    1610612743: 'DEN',
    1610612744: 'GSW',
    1610612745: 'HOU',
    1610612746: 'LAC',
    1610612747: 'LAL',
    1610612748: 'MIA',
    1610612749: 'MIL',
    1610612750: 'MIN',
    1610612751: 'BKN',
    1610612752: 'NYK',
    1610612753: 'ORL',
    1610612754: 'IND',
    1610612755: 'PHI',
    1610612756: 'PHX',
    1610612757: 'POR',
    1610612758: 'SAC',
    1610612759: 'SAS',
    1610612760: 'OKC',
    1610612761: 'TOR',
    1610612762: 'UTA',
    1610612763: 'MEM',
    1610612764: 'WAS',
    1610612765: 'DET',
    1610612766: 'CHA'
}

# Team Abbreviation to Team ID Mapping

TEAM_ABBRV_TO_TEAM_ID = {
    'ATL': 1610612737,
    'BOS': 1610612738,
    'CLE': 1610612739,
    'NOP': 1610612740,
    'CHI': 1610612741,
    'DAL': 1610612742,
    'DEN': 1610612743,
    'GSW': 1610612744,
    'HOU': 1610612745,
    'LAC': 1610612746,
    'LAL': 1610612747,
    'MIA': 1610612748,
    'MIL': 1610612749,
    'MIN': 1610612750,
    'BKN': 1610612751,
    'NYK': 1610612752,
    'ORL': 1610612753,
    'IND': 1610612754,
    'PHI': 1610612755,
    'PHX': 1610612756,
    'POR': 1610612757,
    'SAC': 1610612758,
    'SAS': 1610612759,
    'OKC': 1610612760,
    'TOR': 1610612761,
    'UTA': 1610612762,
    'MEM': 1610612763,
    'WAS': 1610612764,
    'DET': 1610612765,
    'CHA': 1610612766
}

TEAM_BASIC_STATS = [
    'min', 'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a', 'fg3_pct', 'ftm', 'fta',
    'ft_pct', 'oreb', 'dreb', 'reb', 'ast', 'stl', 'blk', 'to', 'pf', 'pts'
]

TEAM_ADVANCED_STATS = [
    'off_rating', 'def_rating', 'net_rating', 'ast_pct', 'ast_to', 'ast_ratio',
    'oreb_pct', 'dreb_pct', 'reb_pct', 'tm_tov_pct', 'efg_pct', 'ts_pct',
    'usg_pct', 'pace', 'pie'
]

team_misc_stats = [
    'pts_off_tov', 'pts_2nd_chance', 'pts_fb', 'opp_pts_off_tov',
    'opp_pts_2nd_chance', 'opp_pts_fb', 'poss', 'opp_poss', 'opp_pts', 'pts'
]

team_scoring_stats = [
    'fast_break_pts', 'second_chance_pts', 'points_in_paint', 'efficiency'
]

team_defense_stats = [
    'defensive_rating', 'opp_pts_off_tov', 'opp_pts_2nd_chance', 'opp_pts_fb',
    'opp_pts_paint', 'defensive_rebounds', 'opp_second_chance_pts',
    'opp_fast_break_pts', 'opp_points_in_paint', 'opp_efficiency'
]

team_tracking_stats = [
    'speed', 'distance', 'avg_speed', 'dist', 'avg_dist', 'off_dist',
    'def_dist', 'def_dist_avg', 'dist_off', 'dist_def', 'avg_dist_off',
    'avg_dist_def'
]

team_hustle_stats = [
    'screen_assists', 'deflections', 'loose_balls_recovered', 'charges_drawn',
    'contested_shots', 'box_outs'
]

team_player_stats = [
    'player_id', 'team_id', 'min', 'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a',
    'fg3_pct', 'ftm', 'fta', 'ft_pct', 'oreb', 'dreb', 'reb', 'ast', 'stl',
    'blk', 'to', 'pf', 'pts'
]

team_player_advanced_stats = [
    'player_id', 'team_id', 'off_rating', 'def_rating', 'net_rating',
    'ast_pct', 'ast_to', 'ast_ratio', 'oreb_pct', 'dreb_pct', 'reb_pct',
    'tm_tov_pct', 'efg_pct', 'ts_pct', 'usg_pct', 'pace', 'pie'
]

player_basic_stats = [
    'min', 'fgm', 'fga', 'fg_pct', 'fg3m', 'fg3a', 'fg3_pct', 'ftm', 'fta',
    'ft_pct', 'oreb', 'dreb', 'reb', 'ast', 'stl', 'blk', 'to', 'pf', 'pts'
]

player_advanced_stats = [
    'off_rating', 'def_rating', 'net_rating', 'ast_pct', 'ast_to', 'ast_ratio',
    'oreb_pct', 'dreb_pct', 'reb_pct', 'tm_tov_pct', 'efg_pct', 'ts_pct',
    'usg_pct', 'pace', 'pie'
]

player_misc_stats = [
    'pts_off_tov', 'pts_2nd_chance', 'pts_fb', 'opp_pts_off_tov',
    'opp_pts_2nd_chance', 'opp_pts_fb', 'poss', 'opp_poss', 'opp_pts', 'pts'
]

player_scoring_stats = [
    'fast_break_pts', 'second_chance_pts', 'points_in_paint', 'efficiency'
]

player_defense_stats = [
    'defensive_rating', 'opp_pts_off_tov', 'opp_pts_2nd_chance', 'opp_pts_fb',
    'opp_pts_paint', 'defensive_rebounds', 'opp_second_chance_pts',
    'opp_fast_break_pts', 'opp_points_in_paint', 'opp_efficiency'
]

player_tracking_stats = [
    'speed', 'distance', 'avg_speed', 'dist', 'avg_dist', 'off_dist',
    'def_dist', 'def_dist_avg', 'dist_off', 'dist_def', 'avg_dist_off',
    'avg_dist_def'
]

player_hustle_stats = [
    'screen_assists', 'deflections', 'loose_balls_recovered', 'charges_drawn',
    'contested_shots', 'box_outs'
]

player_bio_stats = [
    'player_id', 'team_id', 'player_name', 'player_height', 'player_weight',
    'player_position', 'player_dob', 'player_age', 'player_exp',
    'player_college'
]

player_game_stats = [
    'player_id', 'team_id', 'game_id', 'min', 'fgm', 'fga', 'fg_pct', 'fg3m',
    'fg3a', 'fg3_pct', 'ftm', 'fta', 'ft_pct', 'oreb', 'dreb', 'reb', 'ast',
    'stl', 'blk', 'to', 'pf', 'pts'
]

player_game_advanced_stats = [
    'player_id', 'team_id', 'game_id', 'off_rating', 'def_rating',
    'net_rating', 'ast_pct', 'ast_to', 'ast_ratio', 'oreb_pct', 'dreb_pct',
    'reb_pct', 'tm_tov_pct', 'efg_pct', 'ts_pct', 'usg_pct', 'pace', 'pie'
]

player_game_misc_stats = [
    'player_id', 'team_id', 'game_id', 'pts_off_tov', 'pts_2nd_chance',
    'pts_fb', 'opp_pts_off_tov', 'opp_pts_2nd_chance', 'opp_pts_fb', 'poss',
    'opp_poss', 'opp_pts', 'pts'
]

player_game_scoring_stats = [
    'player_id', 'team_id', 'game_id', 'fast_break_pts', 'second_chance_pts',
    'points_in_paint', 'efficiency'
]

player_game_defense_stats = [
    'player_id', 'team_id', 'game_id', 'defensive_rating', 'opp_pts_off_tov',
    'opp_pts_2nd_chance', 'opp_pts_fb', 'opp_pts_paint', 'defensive_rebounds',
    'opp_second_chance_pts', 'opp_fast_break_pts', 'opp_points_in_paint',
    'opp_efficiency'
]
