from sqlalchemy import Column, BIGINT, REAL, TEXT
from src.models.sqlite.settings.base import Base

class JuridicalPersonTable(Base):
    __tablename__ = "juridical_person"

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    revenue = Column(REAL, nullable=False)
    age = Column(BIGINT)
    trade_name = Column(TEXT)
    mobile = Column(TEXT)
    corporate_email = Column(TEXT)
    category = Column(TEXT)
    balance = Column(REAL)

    def __repr__(self):
        return (
            f"\nJuridical Person [Id={self.id}, trade_name={self.trade_name}, " \
            f"revenue={self.revenue}, balance={self.balance} age={self.age}]"
        )
