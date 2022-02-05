from sqlalchemy import (
    Column,
    ForeignKey,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
    String,
    create_engine,
)
from sqlalchemy.orm import Session, registry, relationship

Base = registry().generate_base()


class Account(Base):
    __tablename__ = "accounts"
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String)
    email = Column(String)
    user = relationship("User", foreign_keys=[user_id], back_populates="accounts")
    photos = relationship("Photo", back_populates="account")
    __table_args__ = (PrimaryKeyConstraint("user_id", "type"),)


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    type = Column(String)
    path = Column(String)
    account = relationship("Account", back_populates="photos")
    __table_args__ = (
        ForeignKeyConstraint(
            ["user_id", "type"], ["accounts.user_id", "accounts.type"]
        ),
    )


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    accounts = relationship("Account")


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    user = User(id=1, name="yoo")
    account1 = Account(user_id=1, type="google", email="admin1@example.com")
    account2 = Account(user_id=1, type="facebook", email="admin2@example.com")
    account3 = Account(user_id=2, type="google", email="admin3@example.com")
    photo1 = Photo(id=1, user_id=1, type="google", path="aaa/bbb/ccc.jpg")
    photo2 = Photo(id=2, user_id=1, type="google", path="xxx/yyy/zzz.jpg")
    photo3 = Photo(id=3, user_id=1, type="facebook", path="xxx/yyy/zzz.jpg")
    photo4 = Photo(id=4, user_id=2, type="google", path="xxx/yyy/zzz.jpg")
    session.add(user)
    session.add(account1)
    session.add(account2)
    session.add(account3)
    session.add(photo1)
    session.add(photo2)
    session.add(photo3)
    session.add(photo4)
    session.commit()

    assert len(account1.photos) == 2
    assert len(account2.photos) == 1
    assert len(account3.photos) == 1
    assert list(account1.photos)[0].id == 1
    assert list(account1.photos)[1].id == 2
    assert list(account2.photos)[0].id == 3
    assert list(account3.photos)[0].id == 4
