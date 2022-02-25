from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Query, Session, registry, relationship

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = Query(User).with_session(session)
    query = query.slice(100, 120)

    assert (
        "".join(
            str(
                query.statement.compile(compile_kwargs={"literal_binds": True})
            ).splitlines()
        )
        == "SELECT users.id, users.name FROM users LIMIT 20 OFFSET 100"
    )
