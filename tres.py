from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class InjectionToken(Generic[T]):
    ...


class DependencyContainer(Generic[T]):
    def __init__(self):
        self.__container = {}

    def register(self, token: InjectionToken[T], value: T):
        if token in self.__container:
            raise KeyError(f"token {token} already registered")
        self.__container[token] = value

    def __getitem__(self, token: InjectionToken[T]) -> T:
        return self.__container[token]


container = DependencyContainer()
