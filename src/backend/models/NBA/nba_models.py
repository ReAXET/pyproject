import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
import polars as pl
import numpy as np
import requests
import json
from datetime import datetime
from typing import List, Dict, Union, Any
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, MetaData, DateTime, func
from nba_api.stats.endpoints import LeagueDashPlayerStats, LeagueDashTeamStats, CommonTeamRoster, CommonPlayerInfo, PlayerGameLog, TeamGameLog, CommonAllPlayers, CommonTeamYears, TeamInfoCommon
from nba_api.stats.static import teams, players
from loguru import logger
from backend.core.path_config import PKG_ROOT, DATA_PATH, NBA_DATA_PATH
from backend.models.base import BaseModel


log = logger.bind(name=__file__)


class NBA_Player(BaseModel):
    """Model for the NBA player table.

       Uses the CommonAllPlayers endpoint from the NBA API to get the data.

       # Note # 
         The CommonAllPlayers endpoint returns all players that have played in the NBA.
         Also the player_id is the same as the person_id from the CommonPlayerInfo endpoint.
    """

    __tablename__ = 'nba_player'  # type: ignore

    player_id = Column(Integer, nullable=False, primary_key=True)
    player_name = Column(
        String, nullable=False
    )  # The name of the player and the column name from the NBA API is DISPLAY_FIRST_LAST
    roster_status = Column(String, nullable=False)
    from_year = Column(Integer)
    to_year = Column(Integer)
    player_code = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey('nba_team.team_id'))
    team = relationship('NBA_Team', backref='players')

    def __repr__(self):
        """
        Return a string representation of the NBA_Player object.
        Example: NBA_Player(player_id=203518, player_name='Al-Farouq Aminu')"""

        return f'NBA_Player(player_id={self.player_id}, player_name={self.player_name})'

    @classmethod
    def get_all_players(cls) -> List[Dict[str, Union[str, int]]]:
        """Return a list of all the players that have played in the NBA."""
        all_players = CommonAllPlayers().get_dict()
        return all_players.get('resultSets')[0].get('rowSet')

    @classmethod
    def get_player_info(cls, player_id: int) -> Dict[str, Union[str, int]]:
        """Return the player info for the given player_id."""
        player_info = CommonPlayerInfo(player_id=player_id).get_dict()
        return player_info.get('resultSets')[0].get('rowSet')[0]

    @classmethod
    def get_player_game_log(cls, player_id: int) -> List[Dict[str, Union[str, int]]]:
        """Return the game log for the given player_id."""
        game_log = PlayerGameLog(player_id=player_id).get_dict()
        return game_log.get('resultSets')[0].get('rowSet')
