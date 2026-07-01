from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Team(Base):
    """
    Represents a football club or national team.
    """

    __tablename__ = "teams"

    team_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    player_teams = relationship(
    "PlayerTeam",
    order_by="PlayerTeam.start_date",
    back_populates="team",
)
    team_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    short_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    fifa_team_code: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        unique=True,
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    confederation: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    logo_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    flag_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )