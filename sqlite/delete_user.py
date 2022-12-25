from main import User, Session, engine

local_session = Session(bind=engine)  # 创建会话

user_to_delete = local_session.query(User).filter(User.username=='jojo').first()

local_session.delete(user_to_delete)
local_session.commit()