from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.db.base import Base


class Player(Base):
    """
    Represents a football player.
    """

    __tablename__ = "players"
    player_teams = relationship(
    "PlayerTeam",
    back_populates="player",
    
    )
    player_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    short_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    date_of_birth: Mapped[date]

    nationality: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    height: Mapped[int]

    weight: Mapped[int]

    preferred_foot: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    profile_image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )
    