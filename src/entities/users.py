from sqlalchemy import Column, String, Integer
from src.config import Base

class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    def __repr__(self):
        return f"Users (id={self.id}, nome={self.nome})"
