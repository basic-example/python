from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.orm import registry
from sqlalchemy.sql.expression import Select

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


def to_string(query):
    return "".join(str(query).splitlines())


def test_case():
    query = select(User).get_final_froms()[0]

    assert "users" == to_string(query)
