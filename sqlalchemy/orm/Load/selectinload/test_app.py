import logging
import re

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Query, Session, registry, relationship, selectinload

Base = registry().generate_base()


class Basket(Base):
    __tablename__ = "baskets"
    id = Column(Integer, primary_key=True)
    package_id = Column(Integer, ForeignKey("packages.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    package = relationship("Package", foreign_keys=[package_id], back_populates="baskets")
    product = relationship("Product", foreign_keys=[product_id], back_populates="baskets")


class Package(Base):
    __tablename__ = "packages"
    id = Column(Integer, primary_key=True)
    payment_id = Column(Integer, ForeignKey("payments.id"))
    address = Column(String)
    baskets = relationship("Basket")
    payment = relationship("Payment", foreign_keys=[payment_id], back_populates="packages")


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    method = Column(String)
    packages = relationship("Package")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    baskets = relationship("Basket")


class StreamHandler(logging.StreamHandler):

    def emit(self, record):
        if re.match("^SELECT", record.msg):
            message = "".join(str(record.msg).splitlines())
            messages.append(message)


messages = []
logging.basicConfig()
logging.getLogger("sqlalchemy").setLevel(logging.DEBUG)
logging.getLogger("sqlalchemy").addHandler(StreamHandler())


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(Product(id=1, name="aaa"))
    session.add(Product(id=2, name="bbb"))
    session.add(Product(id=3, name="ccc"))
    session.add(Payment(id=1, method="card"))
    session.add(Payment(id=2, method="cash"))
    session.add(Package(id=1, payment_id=1, address="seoul"))
    session.add(Package(id=2, payment_id=1, address="busan"))
    session.add(Package(id=3, payment_id=2, address="seoul"))
    session.add(Package(id=4, payment_id=2, address="busan"))
    session.add(Basket(id=1, package_id=1, product_id=1, quantity=10))
    session.add(Basket(id=2, package_id=2, product_id=2, quantity=20))
    session.add(Basket(id=3, package_id=1, product_id=2, quantity=30))
    session.add(Basket(id=4, package_id=2, product_id=3, quantity=40))
    session.commit()

    query = Query(Payment).with_session(session)
    query = query.filter_by(method="card")
    query = query.options(
        selectinload(Payment.packages).selectinload(Package.baskets)
    )
    result = query.all()

    assert len(result) == 1
    assert re.search("FROM packages WHERE packages.payment_id IN ", messages[1])
    assert re.search("FROM baskets WHERE baskets.package_id IN ", messages[2])
