from main import Session, User, engine

local_session = Session(bind=engine) # 创建会话

users = [
    {
        'username': 'jack',
        'email': 'jack@tree.com'
    },
    {
        'username': 'jonason',
        'email': 'jonason@tree.com'
    },
    {
        'username': 'jolin',
        'email': 'jolin@tree.com'
    },
    {
        'username': 'malina',
        'email': 'malina@tree.com'
    },
]

# for user in users:
#     new_user = User(**user)
#     local_session.add(new_user)

new_user = User(
    username='VGG12', email="""
        id: 7
        n_epochs: 3
        batch_size: 64
        lr: 1.0e-4
    """)
local_session.add(new_user)

local_session.commit()
print('Done!!!')

users = local_session.query(User).all()
for user in users:
    print(user)
