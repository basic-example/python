class AAA:
    x = 1
    y = 2


def test_case():
    assert "{}, {}, {}".format("a", "b", "c") == "a, b, c"
    assert "{0}, {1}, {2}".format("a", "b", "c") == "a, b, c"
    assert "{0}, {1}, {0}".format("a", "b", "c") == "a, b, a"
    assert "{1}, {0}, {2}".format("a", "b", "c") == "b, a, c"
    assert "{1}, {0}, {2}".format(*"abc") == "b, a, c"
    assert "{a}, {b}, {c}".format(a="aaa", b="bbb", c="ccc") == "aaa, bbb, ccc"
    assert "{0.x}, {0.y}".format(AAA()) == "1, 2"
    assert "{1:>7}".format("aaa", "bbb") == "    bbb"
    assert "{1:<7}".format("aaa", "bbb") == "bbb    "
    assert "{1:^7}".format("aaa", "bbb") == "  bbb  "
    assert "{1:*^7}".format("aaa", "bbb") == "**bbb**"
    assert "{1:=^7}".format("aaa", "bbb") == "==bbb=="
    assert (
        "int:{0:d}; hex:{0:x}; oct:{0:o}; bin:{0:b}".format(42)
        == "int:42; hex:2a; oct:52; bin:101010"
    )
    assert "{0:.3%}".format(12.3) == "1230.000%"  # 123.4 * 100.000
    assert "{0:,}".format(123456789) == "123,456,789"
