from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def test_case():
    assert datetime.utcnow().astimezone(ZoneInfo("Asia/Seoul"))
