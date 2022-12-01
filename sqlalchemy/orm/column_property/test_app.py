from sqlalchemy import Column, Integer, String, create_engine, inspect
from sqlalchemy.orm import Session, column_property, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    name = column_property(last_name + " " + first_name)


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(User(id=1, first_name="Min su", last_name="Park"))
    session.commit()

    assert session.query(User).first().name == "Park Min su"
