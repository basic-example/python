from sqlalchemy import Column, Integer, String, Table, Text, create_engine
from sqlalchemy.orm import Query, Session, deferred, registry

Base = registry().generate_base()


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True)
    path = Column(String)
    data = deferred(Column(Text))


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    photo = Photo(id=1, path="xxx/yyy/zzz.jpg", data="abcdefgh")
    session.add(photo)
    session.commit()
    photoQuery = Query(Photo).with_session(session)
    photo = photoQuery.first()

    assert (
        "".join(str(photoQuery).splitlines())
        == "SELECT photos.id AS photos_id, photos.path AS photos_path FROM photos"
    )
    assert photo.data == "abcdefgh"
