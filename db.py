from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from configuration import CONNECTION_ROW
import sqlalchemy as db


Model = declarative_base(name='Model')
# engine = create_engine(CONNECTION_ROW, echo=True)
engine = create_engine(CONNECTION_ROW)

"""create data in db"""
# metadata = MetaData()
#
# films = db.Table(
#     'films', metadata,
#     db.Column('film_id', db.Integer, primary_key=True),
#     db.Column('status', db.String(50), nullable=False),
#     db.Column('title', db.String(100), nullable=False),
#     db.Column('is_premiere', db.Boolean, nullable=False),
# )
#
# metadata.create_all(bind=engine)
#
# engine.execute(
#     films.insert(),
#     {
#         'title': 'The Hobbit',
#         'status': 'John R. R. Tolkien',
#         'is_premiere': False
#     }
# )


Session = sessionmaker(engine, autoflush=False)
# session = Session()
