from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, User, Posts

engine = create_engine('sqlite:///website.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
user1 = User(name="Rygol", email="warriorbambino23@gmail.com", picture="https://cdn2.iconfinder.com/data/icons/happy-users/100/users09-512.png")
session.add(user1)
session.commit()

# Create category #1 and add items to the category
posts1 = Posts(title="Overlord", user_id=1,
                        description="It's a great anime series!")
session.add(posts1)
session.commit()
