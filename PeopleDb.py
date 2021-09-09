# %%
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pydantic import BaseModel

# configure Session class with desired options
Session = sessionmaker()

Base = declarative_base()
engine = create_engine("sqlite:///my_db.db")
Session.configure(bind=engine)


class Person(Base):
    __tablename__ = "people_info"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    height = Column(Float)
    weight = Column(Float)


class PersonRequest(BaseModel):
    first_name: str
    last_name: str
    height: float
    weight: float
    id: int = None


Base.metadata.create_all(engine)


def map_request_person_to_sql_person(person: PersonRequest):
    person_sql_model = Person(
        first_name=person.first_name,
        last_name=person.last_name,
        height=person.height,
        weight=person.weight,
    )

    return person_sql_model


def get_all():
    session = Session()
    query = session.query(Person)
    result = query.all()
    return result


def add_new_person(person: PersonRequest):
    session = Session()
    person_sql_model = map_request_person_to_sql_person(person)

    session.add(person_sql_model)
    session.commit()
    return person_sql_model


def update_person(person: PersonRequest):
    session = Session()

    query = session.query(Person).filter(Person.id == person.id)
    person_from_db = query.first()

    person_from_db.first_name = person.first_name
    person_from_db.last_name = person.last_name
    person_from_db.height = person.height
    person_from_db.weight = person.weight

    result = session.commit()
    return person_from_db


if __name__ == "__main__":
    result = get_all()
    print(result)
