from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class InjectionToken(Generic[T]):
    ...


class DependencyContainer(dict):
    def register(self, token: InjectionToken[T], value: T):
        if token in self:
            raise KeyError(f"token {token} already registered")
        self[token] = value

    def __getitem__(self, token: InjectionToken[T]) -> T:
        return super().__getitem__(token)


container = DependencyContainer()
