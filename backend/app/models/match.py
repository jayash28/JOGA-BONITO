from datetime import datetime

from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Match(Base):
    """
    Represents a football match.
    """

    __tablename__ = "matches"

    match_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    competition_id: Mapped[int] = mapped_column(
        ForeignKey("competitions.competition_id"),
        nullable=False,
    )

    season_id: Mapped[int] = mapped_column(
        ForeignKey("seasons.season_id"),
        nullable=False,
    )

    venue_id: Mapped[int] = mapped_column(
        ForeignKey("venues.venue_id"),
        nullable=False,
    )

    home_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.team_id"),
        nullable=False,
    )

    away_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.team_id"),
        nullable=False,
    )

    kickoff_time: Mapped[datetime]

    status: Mapped[str]

    attendance: Mapped[int | None]

    referee: Mapped[str | None]

    home_score: Mapped[int] = mapped_column(default=0)

    away_score: Mapped[int] = mapped_column(default=0)

    winner: Mapped[str | None]

    went_to_extra_time: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    went_to_penalties: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    home_penalty_score: Mapped[int | None]

    away_penalty_score: Mapped[int | None]

    competition = relationship("Competition")

    season = relationship("Season")

    venue = relationship("Venue")

    home_team = relationship(
        "Team",
        foreign_keys=[home_team_id],
    )

    away_team = relationship(
        "Team",
        foreign_keys=[away_team_id],
    )