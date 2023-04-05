from typing import Protocol
from abc import ABCMeta, abstractmethod


class Comparable(Protocol):

    def less_than(y):
        ...


class AbstractEvent(metaclass=ABCMeta):

    @abstractmethod
    def execute(AbstractSimulator):
        ...


class AbstractSimulator(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.events = OrderedSet()

    def insert(self, e):
        self.events.add(e)

    def cancel(self, e):
        raise NotImplementedError("Not implement yet")


class OrderedSet(metaclass=ABCMeta):

    def insert(x: Comparable) -> None:
        ...

    def remove_first() -> Comparable:
        ...

    def size() -> int:
        ...

    def remove(x: Comparable) -> Comparable:
        ...
