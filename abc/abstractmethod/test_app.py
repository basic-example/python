from abc import ABC, abstractmethod


class Parent(ABC):
    @abstractmethod
    def add(self, x, y):
        pass


class Child(Parent):
    def add(self, x, y):
        return x + y


def test_case():
    child = Child()
    assert child.add(1, 2) == 3
