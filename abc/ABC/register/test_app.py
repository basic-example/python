from abc import ABC, abstractmethod


class Parent(ABC):
    @abstractmethod
    def add(self, x, y):
        pass


class Child:
    pass


Parent.register(Child)  # virtual sub-class register


def test_case():
    assert issubclass(Child, Parent)
