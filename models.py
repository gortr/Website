from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

# Declaring Instances and/or Variables
Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	email = Column(String(250), nullable = False)
	picture = Column(String)

	@property
	def serialize(self):
		return {
			'name': self.name,
			'id': self.id,
		}

# Declaring Blog Posts and/or Content
class Posts(Base):
	__tablename__ = 'posts'

	id = Column(Integer, primary_key = True)
	title = Column(String(80), nullable = False)
	content = Column(String(1500))
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'content': self.content,
			'user_id': self.user_id
		}

####### insert at end of file ######

engine = create_engine('sqlite:///website.db', echo=True)
Base.metadata.create_all(engine)
