from sqlalchemy import create_engine
from sqlalchemy.orm import registry
from sqlalchemy.pool import StaticPool

Base = registry().generate_base()


def test_case():
    engine = create_engine("sqlite://", poolclass=StaticPool)

    assert (
        engine.connect()._dbapi_connection.connection
        == engine.connect()._dbapi_connection.connection
    )
