from datetime import date

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Season(Base):
    """
    Represents a competition season.
    """

    __tablename__ = "seasons"

    season_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    competition_id: Mapped[int] = mapped_column(
        ForeignKey("competitions.competition_id"),
        nullable=False,
    )

    season_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    start_date: Mapped[date]

    end_date: Mapped[date]

    is_active: Mapped[bool] = mapped_column(
        default=False,
    )

    competition = relationship("Competition")