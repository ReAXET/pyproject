"""Module that contains functions and classes for getting NBA data."""
import os
import sys

from pathlib import Path
from dotenv import load_dotenv

import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime
from typing import List, Dict, Union, Any

from nba_api.stats.endpoints import LeagueDashPlayerStats, LeagueDashTeamStats
from nba_api.stats.static import teams
from nba_api.stats.static import players


from loguru import logger

from backend.core.path_config import PKG_ROOT, DATA_PATH, NBA_DATA_PATH


log = logger.bind(name=__file__)


def stat_names() -> List[str]:
    """Return a list of the names of the stats that are available from the NBA API."""
    return LeagueDashPlayerStats().get_dict().get('resultSets')[0].get(
        'headers')


def wanted_stat_names() -> List[str]:
    """Return a list of the names of the stats that are wanted from the NBA API."""
    return [
        'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'AGE',
        'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A',
        'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV',
        'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'NBA_FANTASY_PTS',
    ]


#stat_names: ['PLAYER_ID', 'PLAYER_NAME', 'NICKNAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'AGE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'NBA_FANTASY_PTS', 'DD2', 'TD3', 'WNBA_FANTASY_PTS', 'GP_RANK', 'W_RANK', 'L_RANK',
             'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK', 'NBA_FANTASY_PTS_RANK', 'DD2_RANK', 'TD3_RANK', 'WNBA_FANTASY_PTS_RANK'] # type: ignore
