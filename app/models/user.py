from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class User(Base):
	__tablename__ = "users"

	id: Mapped[int] = mapped_column(primary_key=True, index=True)
	email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
	full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
	password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

	exercises: Mapped[list["Exercise"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
	workouts: Mapped[list["WorkoutSession"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
	workout_plans: Mapped[list["Workout"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
	goals: Mapped[list["Goal"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
	progress_entries: Mapped[list["Progress"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
