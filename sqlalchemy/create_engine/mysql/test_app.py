import os
import time
from time import sleep

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, registry

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


def test_case():

    os.system("docker compose up -d")

    while True:
        try:
            engine = create_engine("mysql://root:1234@localhost/test")
            Base.metadata.create_all(engine)
        except:
            print("connection failed")
            time.sleep(1)
        else:
            break

    session = Session(engine)
    session.query(User).delete()
    session.add(User(id=1, name="yoo"))
    session.add(User(id=2, name="lee"))
    session.add(User(id=3, name="park"))
    session.commit()
    data = session.query(User).all()

    assert len(data) == 3
