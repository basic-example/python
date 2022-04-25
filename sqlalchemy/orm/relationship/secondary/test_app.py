from sqlalchemy import Column, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.orm import Session, registry, relationship

Base = registry().generate_base()


class Post_Tag(Base):
    __tablename__ = "post_tag"
    id = Column(Integer, primary_key=True)
    post_id = Column(ForeignKey("posts.id"))
    tag_id = Column(ForeignKey("tags.id"))


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    subject = Column(String)
    description = Column(Text)
    tags = relationship("Tag", secondary="post_tag", back_populates="posts")


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship("Post", secondary="post_tag", back_populates="tags")


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    tag1 = Tag(id=1, name="tech")
    tag2 = Tag(id=2, name="virtual")
    tag3 = Tag(id=3, name="metaverse")
    post1 = Post(id=1, subject="docker is great tool", description="...")
    post2 = Post(id=2, subject="metaverse is awesome", description="...")
    session.add(tag1)
    session.add(tag2)
    session.add(tag3)
    session.add(post1)
    session.add(post2)
    post1.tags.append(tag2)
    post2.tags.append(tag3)
    tag1.posts.append(post1)
    tag1.posts.append(post2)
    session.commit()
    post1 = session.query(Post).get(1)
    post1_tag_ids = [x.id for x in post1.tags]
    post2 = session.query(Post).get(2)
    post2_tag_ids = [x.id for x in post2.tags]

    assert tag1.id in post1_tag_ids
    assert tag2.id in post1_tag_ids
    assert tag1.id in post2_tag_ids
    assert tag3.id in post2_tag_ids
