from sqlalchemy import Column, ForeignKey, Integer, create_engine
from sqlalchemy.orm import Session, registry, relationship

Base = registry().generate_base()


class Node(Base):
    __tablename__ = "nodes"
    id = Column(Integer, primary_key=True)
    depth = Column(Integer)
    parents = relationship(
        "Node",
        secondary="node_node",
        primaryjoin="Node_Node.child_id == Node.id",
        secondaryjoin="Node.id == Node_Node.parent_id",
        back_populates="childs",
    )
    childs = relationship(
        "Node",
        secondary="node_node",
        primaryjoin="Node_Node.parent_id == Node.id",
        secondaryjoin="Node.id == Node_Node.child_id",
        back_populates="parents",
    )


class Node_Node(Base):
    __tablename__ = "node_node"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("nodes.id"))
    child_id = Column(Integer, ForeignKey("nodes.id"))


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    node1 = Node(id=1, depth=1)
    node2 = Node(id=2, depth=2)
    node3 = Node(id=3, depth=2)
    node4 = Node(id=4, depth=3)
    node5 = Node(id=5, depth=3)
    node6 = Node(id=6, depth=3)
    node_node1 = Node_Node(parent_id=1, child_id=2)
    node_node2 = Node_Node(parent_id=1, child_id=3)
    node_node3 = Node_Node(parent_id=2, child_id=4)
    node_node4 = Node_Node(parent_id=2, child_id=5)
    node_node5 = Node_Node(parent_id=2, child_id=6)
    node_node6 = Node_Node(parent_id=3, child_id=6)
    session.add(node1)
    session.add(node2)
    session.add(node3)
    session.add(node4)
    session.add(node5)
    session.add(node6)
    session.add(node_node1)
    session.add(node_node2)
    session.add(node_node3)
    session.add(node_node4)
    session.add(node_node5)
    session.add(node_node6)
    session.commit()

    assert len(node2.childs) == 3
    assert len(node2.parents) == 1
    assert len(node6.childs) == 0
    assert len(node6.parents) == 2
    assert isinstance(node2.childs[0], Node)
    assert 4 in [x.id for x in node2.childs]
    assert 5 in [x.id for x in node2.childs]
    assert 6 in [x.id for x in node2.childs]
    assert 1 in [x.id for x in node2.parents]
    assert 2 in [x.id for x in node6.parents]
    assert 3 in [x.id for x in node6.parents]
