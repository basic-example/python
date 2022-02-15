def test_case():
    assert "hello world".endswith("world")
    assert "hello world".endswith("world", 8) == False
    assert "hello world".endswith("hello", 0, 5)
    assert "hello world".endswith("hello") == False
