import string

from dependency_injector import containers, providers


class Query:
    def all():
        return {}


class User:
    attrs: dict

    def __init__(self, attrs) -> None:
        self.attrs = attrs

    def getAttributes(self):
        return self.attrs


class Repository:
    query: Query

    def __init__(self, query: Query):
        self.query = query

    def get_query(self):
        return self.query


class Container(containers.DeclarativeContainer):

    user = providers.Factory(User)
    repository = providers.Factory(Repository, Query)


def test_case():
    container = Container()

    user1 = container.user({"id": 1, "name": "yoo"})
    user2 = container.user({"id": 2, "name": "lee"})
    repository = container.repository()

    assert user1.getAttributes() == {"id": 1, "name": "yoo"}
    assert user2.getAttributes() == {"id": 2, "name": "lee"}
    assert repository.get_query().all() == {}
