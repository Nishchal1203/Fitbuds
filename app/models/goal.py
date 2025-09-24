from datetime import date
from sqlalchemy import String, ForeignKey, Date, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class Goal(Base):
	__tablename__ = "goals"

	id: Mapped[int] = mapped_column(primary_key=True, index=True)
	title: Mapped[str] = mapped_column(String(255), nullable=False)
	description: Mapped[str | None] = mapped_column(Text, nullable=True)
	target_date: Mapped[date | None] = mapped_column(Date, nullable=True)
	is_completed: Mapped[bool] = mapped_column(default=False, nullable=False)

	owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False)
	owner: Mapped["User"] = relationship(back_populates="goals")
