from sqlalchemy.orm import Mapped, mapped_column

from app.db_sqla.schemas.base import Base


class UserDB(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(  # noqa: A003
        init=False, primary_key=True, index=True
    )
    email: Mapped[str]
    password: Mapped[str]
