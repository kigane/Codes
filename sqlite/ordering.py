from main import User, Session, engine
from sqlalchemy import desc

local_session = Session(bind=engine)  # 创建会话

# users_asc = local_session.query(User).order_by(User.username).all()
# for user in users_asc:
#     print(user)

users_desc = local_session.query(User).order_by(desc(User.username)).all()
for user in users_desc:
    print(user)
