import gc
import logging
import re
import time

import psutil
from sqlalchemy import Column, Integer, String, Text, create_engine, select
from sqlalchemy.engine import ChunkedIteratorResult
from sqlalchemy.orm import Query, Session, registry

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
    session.add(Photo(id=1, path="a.jpg", data="a" * 1024 * 1024 * 300))
    session.add(Photo(id=2, path="b.jpg", data="b" * 1024 * 1024 * 300))
    session.add(Photo(id=3, path="c.jpg", data="c" * 1024 * 1024 * 300))
    session.add(Photo(id=4, path="d.jpg", data="d" * 1024 * 1024 * 300))
    session.add(Photo(id=5, path="e.jpg", data="e" * 1024 * 1024 * 300))
    session.add(Photo(id=6, path="f.jpg", data="f" * 1024 * 1024 * 300))
    session.add(Photo(id=7, path="g.jpg", data="g" * 1024 * 1024 * 300))
    session.add(Photo(id=8, path="h.jpg", data="h" * 1024 * 1024 * 300))
    session.add(Photo(id=9, path="i.jpg", data="i" * 1024 * 1024 * 300))
    session.add(Photo(id=10, path="j.jpg", data="j" * 1024 * 1024 * 300))
    session.add(Photo(id=11, path="k.jpg", data="k" * 1024 * 1024 * 300))
    session.add(Photo(id=12, path="l.jpg", data="l" * 1024 * 1024 * 300))
    session.add(Photo(id=13, path="m.jpg", data="m" * 1024 * 1024 * 300))
    session.add(Photo(id=14, path="n.jpg", data="n" * 1024 * 1024 * 300))
    session.commit()
    infos = {}

    for i in [3, 1, 7, 5]:
        engine.connect().execution_options(stream_results=True)
        query = select(Photo)
        result = session.execute(query)
        info = None
        for row in result.yield_per(i):
            info = psutil.Process().memory_info()
        infos[i] = info
        gc.collect()

    assert infos[3].rss > infos[1].rss
    assert infos[5].rss > infos[3].rss
    assert infos[7].rss > infos[5].rss
