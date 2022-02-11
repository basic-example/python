import sqlite3


def check_sql(sql):
    assert sql == 'select ?'

def test_version():
    connection = sqlite3.connect(':memory:')
    sqlite3.enable_callback_tracebacks(True)
    connection.set_trace_callback(check_sql)
    connection.execute("select ?", ('1'))
