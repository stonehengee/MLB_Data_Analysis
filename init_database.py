if input("Running this will clear the database. Are you sure you want to proceed? (Y/N)").lower() == "y":
    pass
else:
    quit()


import sqlalchemy as alchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, ForeignKeyConstraint, Boolean
from sqlalchemy.ext.declarative import declarative_base
import os
if os.path.isfile("app.db"):
    os.remove("app.db")
Base = declarative_base()
engine = create_engine('sqlite:///app.db')

metadata = MetaData()


class Records(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    team_id = Column(String)
    league = Column(String)
    wins = Column(Integer)
    losses = Column(Integer)
    org_founded = Column(Integer)
    expansion = Column(Boolean)


# class Franchises(Base):
#     __tablename__ = 'franchises'

#     id = Column(Integer, primary_key=True)
#     team_id = Column(String, ForeignKey('records.team_id'))


class Alt_Names(Base):
    __tablename__ = 'alt_names'

    alternate_name = Column(String, primary_key=True)
    team_id = Column(String, ForeignKey('records.team_id'))


if __name__ == "__main__":
    Base.metadata.create_all(engine)