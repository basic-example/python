from datetime import datetime

from pytz import timezone


def test_case():
    assert timezone("Asia/Seoul").localize(datetime.utcnow())
