"""All NBA models are defined here."""
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean, Text, Date, Table, UniqueConstraint, ForeignKeyConstraint, Constraint
from sqlalchemy.orm import relationship, backref

from backend.models.base import BaseModel
from backend.database.db import get_db

# Define the association table for the many-to-many relationship between teams and players
team_player_association = Table(
    "team_player_association",
    BaseModel.metadata,
    Column("team_id", Integer, ForeignKey("teams.id")),
    Column("player_id", Integer, ForeignKey("players.id")),
    UniqueConstraint("team_id", "player_id", name="team_player_uc"),
)

# Define the association table for the many-to-many relationship between teams and games
team_game_association = Table(
    "team_game_association",
    BaseModel.metadata,
    Column("team_id", Integer, ForeignKey("teams.id")),
    Column("game_id", Integer, ForeignKey("games.id")),
    UniqueConstraint("team_id", "game_id", name="team_game_uc"),
)

# Define the association table for the many-to-many relationship between players and games
player_game_association = Table(
    "player_game_association",
    BaseModel.metadata,
    Column("player_id", Integer, ForeignKey("players.id")),
    Column("game_id", Integer, ForeignKey("games.id")),
    UniqueConstraint("player_id", "game_id", name="player_game_uc"),
)

# Define the association table for the many-to-many relationship between teams and seasons
team_season_association = Table(
    "team_season_association",
    BaseModel.metadata,
    Column("team_id", Integer, ForeignKey("teams.id")),
    Column("season_id", Integer, ForeignKey("seasons.id")),
    UniqueConstraint("team_id", "season_id", name="team_season_uc"),
)

# Define the association table for the many-to-many relationship between players and seasons
player_season_association = Table(
    "player_season_association",
    BaseModel.metadata,
    Column("player_id", Integer, ForeignKey("players.id")),
    Column("season_id", Integer, ForeignKey("seasons.id")),
    UniqueConstraint("player_id", "season_id", name="player_season_uc"),
)

# Define the association table for the many-to-many relationship between games and seasons
game_season_association = Table(
    "game_season_association",
    BaseModel.metadata,
    Column("game_id", Integer, ForeignKey("games.id")),
    Column("season_id", Integer, ForeignKey("seasons.id")),
    UniqueConstraint("game_id", "season_id", name="game_season_uc"),
)


class Player(BaseModel):
    """A player model."""

    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    full_name = Column(String, index=True)
    is_active = Column(Boolean, default=False)
    birth_date = Column(Date)
    height = Column(Float)
    weight = Column(Float)
    position = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="players")
    games = relationship("Game", secondary=player_game_association, back_populates="players")
    seasons = relationship("Season", secondary=player_season_association, back_populates="players")


class Team(BaseModel):
    """NBA team model."""
    
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    name = Column(String)
    city = Column(String)
    abbreviation = Column(String, index=True)
    city = Column(String)
    state = Column(String)
    year_founded = Column(Integer)
    conference = Column(String)
    division = Column(String)
    players = relationship("Player", secondary=team_player_association, back_populates="team")
    games = relationship("Game", secondary=team_game_association, back_populates="teams")
    seasons = relationship("Season", secondary=team_season_association, back_populates="teams")


class Game(BaseModel):
    """NBA game model."""

    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    home_team_id = Column(Integer, ForeignKey("teams.id"))
    home_team = relationship("Team", backref="home_games", foreign_keys=[home_team_id])
    away_team_id = Column(Integer, ForeignKey("teams.id"))
    away_team = relationship("Team", backref="away_games", foreign_keys=[away_team_id])
    home_team_score = Column(Integer)
    away_team_score = Column(Integer)
    season_id = Column(Integer, ForeignKey("seasons.id"))
    season = relationship("Season", back_populates="games")
    players = relationship("Player", secondary=player_game_association, back_populates="games")
    teams = relationship("Team", secondary=team_game_association, back_populates="games")


class Season(BaseModel):
    """NBA season model."""

    __tablename__ = "seasons"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Date, index=True)
    end_date = Column(Date, index=True)
    year = Column(Integer, index=True)
    games = relationship("Game", secondary=game_season_association, back_populates="season")
    teams = relationship("Team", secondary=team_season_association, back_populates="seasons")
    players = relationship("Player", secondary=player_season_association, back_populates="seasons")


class PlayerBasicStats(BaseModel):
    """NBA player basic stats model."""

    __tablename__ = "player_basic_stats"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    player = relationship("Player", backref="basic_stats")
    season_id = Column(Integer, ForeignKey("seasons.id"))
    season = relationship("Season", backref="basic_stats")
    games_played = Column(Integer)
    minutes_per_game = Column(Float)
    field_goals_made_per_game = Column(Float)
    field_goals_attempted_per_game = Column(Float)
    field_goal_percentage = Column(Float)
    three_point_field_goals_made_per_game = Column(Float)
    three_point_field_goals_attempted_per_game = Column(Float)
    three_point_field_goal_percentage = Column(Float)
    free_throws_made_per_game = Column(Float)
    free_throws_attempted_per_game = Column(Float)
    free_throw_percentage = Column(Float)
    offensive_rebounds_per_game = Column(Float)
    defensive_rebounds_per_game = Column(Float)
    total_rebounds_per_game = Column(Float)
    assists_per_game = Column(Float)
    steals_per_game = Column(Float)
    blocks_per_game = Column(Float)
    turnovers_per_game = Column(Float)
    personal_fouls_per_game = Column(Float)
    points_per_game = Column(Float)


class PlayerAdvancedStats(BaseModel):
    """NBA player advanced stats model."""

    __tablename__ = "player_advanced_stats"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    player = relationship("Player", backref="advanced_stats")
    season_id = Column(Integer, ForeignKey("seasons.id"))
    season = relationship("Season", backref="advanced_stats")
    true_shooting_percentage = Column(Float)
    effective_field_goal_percentage = Column(Float)
    three_point_attempt_rate = Column(Float)
    free_throw_attempt_rate = Column(Float)
    offensive_rebound_percentage = Column(Float)
    defensive_rebound_percentage = Column(Float)
    total_rebound_percentage = Column(Float)
    assist_percentage = Column(Float)
    steal_percentage = Column(Float)
    block_percentage = Column(Float)
    turnover_percentage = Column(Float)
    usage_percentage = Column(Float)
    offensive_win_shares = Column(Float)
    defensive_win_shares = Column(Float)
    win_shares = Column(Float)
    win_shares_per_48_minutes = Column(Float)
    offensive_box_plus_minus = Column(Float)
    defensive_box_plus_minus = Column(Float)
    box_plus_minus = Column(Float)
    value_over_replacement_player = Column(Float)


class PlayerShootingStats(BaseModel):
    """NBA player shooting stats model."""

    __tablename__ = "player_shooting_stats"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    player = relationship("Player", backref="shooting_stats")
    season_id = Column(Integer, ForeignKey("seasons.id"))
    season = relationship("Season", backref="shooting_stats")
    two_point_field_goals_made_per_game = Column(Float)
    two_point_field_goals_attempted_per_game = Column(Float)
    two_point_field_goal_percentage = Column(Float)
    two_point_field_goals_assisted_percentage = Column(Float)
    two_point_field_goals_dunk_percentage = Column(Float)
    two_point_field_goals_layup_percentage = Column(Float)
    three_point_field_goals_made_per_game = Column(Float)
    three_point_field_goals_attempted_per_game = Column(Float)
    three_point_field_goal_percentage = Column(Float)
    three_point_field_goals_assisted_percentage = Column(Float)
    three_point_field_goals_dunk_percentage = Column(Float)
    three_point_field_goals_layup_percentage = Column(Float)
    free_throws_made_per_game = Column(Float)
    free_throws_attempted_per_game = Column(Float)
    free_throw_percentage = Column(Float)
    free_throws_assisted_percentage = Column(Float)
    free_throws_dunk_percentage = Column(Float)
    free_throws_layup_percentage = Column(Float)                                                                                                                                                                                                                                                  