from sqlalchemy import (
    Column,
    Index,
    ForeignKey,
    Integer,
    Text,
    create_engine,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    relationship,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

engine = create_engine('postgresql://postgres:password@localhost:5432/VeLauz')
DBSession.configure(bind=engine)
Base.metadata.bind = engine

class User(Base):
    __tablename__ = 'user'
    __table_args__ = ({'schema': 'public', 'autoload': True})
    userID = Column('userID', Integer, primary_key=True)

query = DBSession.query(User).all()
for q in query:
    print q.userID
