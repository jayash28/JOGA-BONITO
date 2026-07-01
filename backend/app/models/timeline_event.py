from sqlalchemy import Float, ForeignKey, String
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.enums.event_type import EventType
from app.db.base import Base


class TimelineEvent(Base):
    """
    Represents a single football event occurring during a match.
    """

    __tablename__ = "timeline_events"

    event_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    match_id: Mapped[int] = mapped_column(
        ForeignKey("matches.match_id"),
        nullable=False,
    )

    team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.team_id"),
        nullable=False,
    )

    player_id: Mapped[int | None] = mapped_column(
        ForeignKey("players.player_id"),
        nullable=True,
    )

    related_player_id: Mapped[int | None] = mapped_column(
        ForeignKey("players.player_id"),
        nullable=True,
    )

    minute: Mapped[int]

    second: Mapped[int]

    period: Mapped[str] = mapped_column(
        String(20),
    )

    event_type: Mapped[EventType] = mapped_column(
        SQLEnum(EventType),
        nullable=False,
    )

    event_subtype: Mapped[str | None] = mapped_column(
        String(50),
    )

    outcome: Mapped[str | None] = mapped_column(
        String(50),
    )

    x_coordinate: Mapped[float | None] = mapped_column(
        Float,
    )

    y_coordinate: Mapped[float | None] = mapped_column(
        Float,
    )

    short_description: Mapped[str | None] = mapped_column(
        String(255),
    )

    detailed_description: Mapped[str | None] = mapped_column(
        String(1000),
    )

    provider_event_id: Mapped[str | None] = mapped_column(
        String(100),
    )

    source: Mapped[str] = mapped_column(
        String(50),
        default="FIFA",
    )

    importance_score: Mapped[float | None] = mapped_column(
        Float,
    )

    sentiment_shift: Mapped[float | None] = mapped_column(
        Float,
    )

    raw_reference: Mapped[str | None] = mapped_column(
        String(255),
    )

    match = relationship("Match")

    team = relationship("Team")

    player = relationship(
        "Player",
        foreign_keys=[player_id],
    )

    related_player = relationship(
        "Player",
        foreign_keys=[related_player_id],
    )