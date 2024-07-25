from sqlalchemy.orm import Mapped, declarative_base, mapped_column


Base = declarative_base()


class ItemModel(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    price: Mapped[float]
    amount: Mapped[int]
