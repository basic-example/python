from datetime import datetime
from string import Formatter


class AAA:
    x = 1
    y = 2


def test_case():
    assert Formatter().format("{}, {}, {}", "a", "b", "c") == "a, b, c"
    assert Formatter().format("{0}, {1}, {2}", "a", "b", "c") == "a, b, c"
    assert Formatter().format("{0}, {1}, {0}", "a", "b", "c") == "a, b, a"
    assert Formatter().format("{1}, {0}, {2}", "a", "b", "c") == "b, a, c"
    assert Formatter().format("{1}, {0}, {2}", *"abc") == "b, a, c"
    assert (
        Formatter().format("{a}, {b}, {c}", a="aaa", b="bbb", c="ccc")
        == "aaa, bbb, ccc"
    )
    assert Formatter().format("{0.x}, {0.y}", AAA()) == "1, 2"
    assert Formatter().format("{1:>7}", "aaa", "bbb") == "    bbb"
    assert Formatter().format("{1:<7}", "aaa", "bbb") == "bbb    "
    assert Formatter().format("{1:^7}", "aaa", "bbb") == "  bbb  "
    assert Formatter().format("{1:*^7}", "aaa", "bbb") == "**bbb**"
    assert Formatter().format("{1:=^7}", "aaa", "bbb") == "==bbb=="
    assert (
        Formatter().format("int:{0:d}; hex:{0:x}; oct:{0:o}; bin:{0:b}", 42)
        == "int:42; hex:2a; oct:52; bin:101010"
    )
    assert Formatter().format("{0:.3%}", 12.3) == "1230.000%"  # 123.4 * 100.000
    assert Formatter().format("{0:,}", 123456789) == "123,456,789"
    assert (
        Formatter().format("{0:%Y-%m-%d %H:%M:%S}", datetime(2010, 7, 4, 12, 15, 58))
        == "2010-07-04 12:15:58"
    )
