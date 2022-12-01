from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import registry

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    @hybrid_property
    def name(self):
        return self.last_name + " " + self.first_name


def test_case():
    user1 = User(id=1, first_name="Min su", last_name="Park")

    assert user1.name == "Park Min su"
