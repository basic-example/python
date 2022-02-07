import gc

import psutil
from sqlalchemy import Column, Integer, String, Text, create_engine, select
from sqlalchemy.orm import Session, registry

Base = registry().generate_base()


class Photo(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    path = Column(String)
    data = Column(Text)


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(Photo(id=1, path="a.jpg", data="a" * 1024 * 1024 * 100))
    session.add(Photo(id=2, path="b.jpg", data="b" * 1024 * 1024 * 100))
    session.add(Photo(id=3, path="c.jpg", data="c" * 1024 * 1024 * 100))
    session.add(Photo(id=4, path="d.jpg", data="d" * 1024 * 1024 * 100))
    session.add(Photo(id=5, path="e.jpg", data="e" * 1024 * 1024 * 100))
    session.add(Photo(id=6, path="f.jpg", data="f" * 1024 * 1024 * 100))
    session.add(Photo(id=7, path="g.jpg", data="g" * 1024 * 1024 * 100))
    session.add(Photo(id=8, path="h.jpg", data="h" * 1024 * 1024 * 100))
    session.add(Photo(id=9, path="i.jpg", data="i" * 1024 * 1024 * 100))
    session.commit()
    records = {}

    for i in [3, 1, 7, 5]:
        engine.connect().execution_options(stream_results=True)
        query = select(Photo)
        result = session.execute(query)
        max_value = 0
        for row in result.yield_per(i):
            info = psutil.Process().memory_info()
            if max_value < info.rss:
                max_value = info.rss
        records[i] = max_value
        gc.collect()

    assert records[3] > records[1]
    assert records[5] > records[3]
    assert records[7] > records[5]
