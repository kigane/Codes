import os
from datetime import datetime

from pydantic import BaseModel, constr
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_str = 'sqlite:///' + os.path.join(BASE_DIR, 'user.db')
print(connection_str)

Base = declarative_base()
Session = sessionmaker()

engine = create_engine(connection_str, echo=True) # 连接数据库

# TABLE
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(5), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'User(id={self.id}, username={self.username}, email={self.email}, date_created={self.date_created})'
    
class UserModel(BaseModel):
    id: int
    username: constr(max_length=5)
    email: constr(max_length=80)
    date_created: datetime
    class Config():
        orm_mode = True


if __name__ == '__main__':
    new_user = User(id=1, username='melin', email='fingerwitch@golden.tree', date_created=datetime.utcnow())
    user_model = UserModel.from_orm(new_user)
    # print(User.__tablename__)
    # print(f'{User.__table__!r}')
    print(user_model)
    print(user_model.json())
