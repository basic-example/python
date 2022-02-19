from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta

Base = declarative_base()


def test_case():
    assert isinstance(Base, DeclarativeMeta)
