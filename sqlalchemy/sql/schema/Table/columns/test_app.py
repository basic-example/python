from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import registry

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)

    assert ["id", "name"] == [c.name for c in User.__table__.columns]
