from main import Base, User, engine

# create table that do not exist.
Base.metadata.create_all(engine)
