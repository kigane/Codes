import os
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = os.path.realpath('results/db')

connection_str = 'sqlite:///' + os.path.join(BASE_DIR, 'record.db')
engine = create_engine(connection_str, echo=True)

Base = declarative_base()
Session = sessionmaker()


class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    config = Column(String(), nullable=False, unique=True)
    result = Column(String(), nullable=False, unique=True)
    desc = Column(String(), default='无')
    date = Column(DateTime(), default=datetime.utcnow)


class RecordData(BaseModel):
    id: int
    name: str
    config: str
    result: str
    desc: str
    data: datetime

    class Config():
        orm_mode = True


class RecordSession():

    def __init__(self) -> None:
        Base.metadata.create_all(engine)
        self.session: Session = Session(bind=engine)

    def add_record(self, **kwargs):
        new_user = Record(**kwargs)
        self.session.add(new_user)
        self.session.commit()

    def del_record(self, id):
        candidate = self.session.query(Record).filter(Record.id == id).first()
        self.session.delete(candidate)
        self.session.commit()

    def del_record(self, name):
        candidate = self.session.query(Record).filter(
            Record.name == name).first()
        self.session.delete(candidate)
        self.session.commit()

    def update_record(self, id, desc):
        candidate = self.session.query(Record).filter(Record.id == id).first()
        candidate.desc = desc
        self.session.commit()
