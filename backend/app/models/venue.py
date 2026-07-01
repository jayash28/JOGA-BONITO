from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Venue(Base):
    """
    Represents a football stadium.
    """

    __tablename__ = "venues"

    venue_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    stadium_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    capacity: Mapped[int]

    latitude: Mapped[float] = mapped_column(Float)

    longitude: Mapped[float] = mapped_column(Float)