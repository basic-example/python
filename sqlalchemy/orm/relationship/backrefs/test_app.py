from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session, relationship, registry

Base = registry().generate_base()


class StockLog(Base):

    __tablename__ = "stock_logs"

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer)

    user = relationship(
        "User",
        secondary="log_user",
        primaryjoin="and_(StockLog.id == foreign(LogUser.related_id), LogUser.related_type == 'stock_log')",
        secondaryjoin="User.id == foreign(LogUser.user_id)",
        backref="stock_log",
        viewonly=True,
    )


class ProductLog(Base):

    __tablename__ = "product_logs"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)

    user = relationship(
        "User",
        secondary="log_user",
        primaryjoin="and_(ProductLog.id == foreign(LogUser.related_id), LogUser.related_type == 'product_log')",
        secondaryjoin="User.id == foreign(LogUser.user_id)",
        backref="product_log",
        viewonly=True,
    )


class LogUser(Base):

    __tablename__ = "log_user"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    related_id = Column(Integer)
    related_type = Column(String(255))


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))


engine = create_engine("sqlite://")
session = Session(engine)
Base.metadata.create_all(engine)

session.add(User(id=1, username="abcd", password="1234"))
session.add(User(id=2, username="bcde", password="2345"))
session.flush()
session.add(ProductLog(id=1, product_id=1))
session.add(StockLog(id=1, stock_id=1))
session.add(LogUser(id=1, user_id=1, related_id=1, related_type="product_log"))
session.add(LogUser(id=2, user_id=2, related_id=1, related_type="stock_log"))
session.commit()


def test_app():
    assert session.query(ProductLog).get(1).user
    assert session.query(StockLog).get(1).user
    assert session.query(User).get(1).product_log
    assert not session.query(User).get(2).product_log
    assert session.query(User).get(2).stock_log
    assert not session.query(User).get(1).stock_log
