from sqlalchemy import Column, BIGINT, REAL, TEXT
from src.models.sqlite.settings.base import Base


class NaturalPersonTable(Base):
    __tablename__ = "natural_person"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    monthly_income = Column(REAL, nullable=False)
    age = Column(BIGINT, nullable=False)
    full_name = Column(TEXT, nullable=False)
    mobile = Column(TEXT, nullable=False)
    email = Column(TEXT, nullable=False)
    category = Column(TEXT, nullable=False)
    balance = Column(REAL, nullable=False)

    def __repr__(self):
        return (
            f"\nNatural Person [full_name={self.full_name}, " \
            f"monthly_income={self.monthly_income}, age={self.age}]"
        )
