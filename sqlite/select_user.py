from main import Session, User, engine

local_session = Session(bind=engine)  # 创建会话

# select * from users
users = local_session.query(User).all()
for user in users:
    print(user)

# select one from users where user.username = one
jolin = local_session.query(User).filter(User.username=='jolin').first()
print(jolin)
