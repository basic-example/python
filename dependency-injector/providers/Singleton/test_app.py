from dependency_injector import containers, providers


class Connection:
    config: dict

    def __init__(self, config={}) -> None:
        self.config = config

    def getConfig(self, config):
        return self.config


class Query:
    def __init__(self, connection) -> None:
        self.connection = connection

    def get_connection(self):
        return self.connection


class Container(containers.DeclarativeContainer):
    connection = providers.Singleton(Connection)
    query = providers.Factory(Query, connection)


def test_case():
    container = Container()
    query1 = container.query()
    query2 = container.query()

    assert query1 != query2
    assert query1.get_connection() == query2.get_connection()
