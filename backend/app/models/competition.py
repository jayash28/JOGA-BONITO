from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Competition(Base):
    """
    Represents a football competition.
    """

    __tablename__ = "competitions"

    competition_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    competition_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    competition_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    organizer: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )