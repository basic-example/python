import pytest
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import registry
from sqlalchemy.pool import QueuePool

Base = registry().generate_base()


def test_case():
    engine = create_engine(
        "sqlite://", poolclass=QueuePool, max_overflow=1, pool_size=1, pool_timeout=5
    )

    with pytest.raises(Exception) as exception:
        connections = []
        connections.append(engine.connect())
        connections.append(engine.connect())
        connections.append(engine.connect())
        connections.append(engine.connect())
        connections.append(engine.connect())
        connections.append(engine.connect())
        connections.append(engine.connect())

    assert exception.type == sqlalchemy.exc.TimeoutError
    assert (
        "QueuePool limit of size 1 overflow 1 reached, connection timed out, timeout 5.00"
        in str(exception.value)
    )
