from datetime import date

from sqlalchemy import Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class PlayerTeam(Base):
    """
    Stores player transfer history.
    """

    __tablename__ = "player_teams"

    player_team_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    player_id: Mapped[int] = mapped_column(
        ForeignKey("players.player_id"),
        nullable=False,
    )

    team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.team_id"),
        nullable=False,
    )

    jersey_number: Mapped[int | None]

    start_date: Mapped[date]

    end_date: Mapped[date | None]

    is_current: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    player = relationship(
        "Player",
        back_populates="player_teams",
    )

    team = relationship(
        "Team",
        back_populates="player_teams",
    )