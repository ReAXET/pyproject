### Notes for CSV Files located in this folder

- NBA_API_Players.csv is just the static data from the NBA API for all players
    - endpoint: None (static data) imported as such
        - from nba_api.stats.static import players as static_players, teams as static_teams
        - players = static_players.get_players()
        - players = pd.DataFrame(players)

- NBA_Players.csv is the data from CommonAllPlayers
    - endpoint: commonallplayers
        - from nba_api.stats.endpoints import commonallplayers
        - players = commonallplayers.CommonAllPlayers(is_only_current_season=1)
        - players = players.get_data_frames()[0]

- NBA_Team_Info.csv is basic data from the NBA API for all teams
    - endpoint: CommonTeamInfo
        - from nba_api.stats.endpoints import commonteamroster
        - teams = commonteamroster.CommonTeamRoster(team_id=1610612737)
        - teams = teams.get_data_frames()[0]

- NBA_Team_Roster.csv is data from CommonTeamRoster
    - endpoint: commonteamroster
        - from nba_api.stats.endpoints import commonteamroster
        - teams = commonteamroster.CommonTeamRoster(team_id=1610612737)
        - teams = teams.get_data_frames()[0]

- PlayerNameIDMap.csv is 2 columns of player names and their respective player ids
    - endpoint: None (static data) imported as such
        - from nba_api.stats.static import players as static_players, teams as static_teams
        - players = static_players.get_players()
        - players = pd.DataFrame(players)


====================================================================================================