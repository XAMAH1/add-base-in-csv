from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class UserBaseModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    user_id: Mapped[str] = mapped_column(
        nullable=False,
    )
    login: Mapped[str] = mapped_column(
        nullable=False,
    )
    password: Mapped[str] = mapped_column(
        nullable=False,
    )

    # server_default=text("TIMEZONE('utc', now() + INTERVAL '1 year')",),
