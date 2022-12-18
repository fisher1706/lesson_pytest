from db import session
import tables
from sqlalchemy.sql.expression import desc


# result = session.query(tables.Films.film_id, tables.Films.title).first()
# result = session.query(tables.Films.film_id, tables.Films.title).all()

# result = session.query(
#     tables.Films.film_id, tables.Films.title).\
#     filter(
#         tables.Films.film_id > 1,
#         tables.Films.film_id < 3)\
#     .one_or_none()


# film_ids = session.query(tables.Films.film_id).filter(tables.Films.film_id > 1).subquery()
# result = session.query(tables.Films.title).filter(tables.Films.film_id.in_(film_ids)).all()

# film_ids = session.query(tables.Films.film_id).order_by(tables.Films.film_id).all()
film_ids = session.query(tables.Films.film_id).order_by(desc(tables.Films.film_id)).all()

data = session.query(tables.Films).first()


if __name__ == '__main__':
    # print(result)
    print(film_ids)

    print(data.title)
