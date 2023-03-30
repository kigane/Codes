from main import User, Session, engine

local_session = Session(bind=engine)  # 创建会话

user_to_update = local_session.query(User).filter(User.username=='jolin').first()
user_to_update.username = 'jojo'
user_to_update.email = 'jojo@spdwg.com'
local_session.commit()