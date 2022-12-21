from operator import attrgetter


class Image:
    url: str

    def __init__(self, url=None):
        self.url = url


class User:
    name: str
    image: Image

    def __init__(self, name=None, image=None):
        self.name = name
        self.image = image


def test_case():
    assert attrgetter("name")(User(name="aaa")) == "aaa"
    assert (
        attrgetter("image.url")(
            User(name="aaa", image=Image(url="http://x.com/y")),
        )
        == "http://x.com/y"
    )
    assert attrgetter("name", "image.url")(
        User(name="aaa", image=Image(url="http://x.com/y")),
    ) == ("aaa", "http://x.com/y")
