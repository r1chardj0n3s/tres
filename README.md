# tres
Typed resolver (dependency container) for Python

It provides a dependency container for you to use in typed dependency resolution.

That's all. Very type resolution. Much wow.

Inspired by the dependency container in [tsyringe](https://www.npmjs.com/package/tsyringe), but more Pythonic.

## Usage:

```python
from tres import container, InjectionToken

def a(n: int) -> str:
    return str(n)


def b(a: int, b: int) -> int:
    return a + b


a_token = InjectionToken[Callable[[int], str]]()
b_token = InjectionToken[Callable[[int, int], int]]()

container.register(a_token, a)
container.register(b_token, b)
container.register(b_token, a)  # type error


def c(f: Callable[[int], str]):
    print(f(1))


c(container[a_token])
c(container[b_token])  # type error
```

## A longer example registering a Protocol

```python

# application logic

from typing import Protocol, Iterable

class OrdersProtocol(Protocol):
    def byId(self, id) -> Order:
        ...

    def getLines(self, id) -> Iterable[OrderLine]:
        ...

OrdersStoreToken = tres.InjectionToken[OrdersProtocol]()

def calculate_total(orders_store: OrdersProtocol, order_id):
    order = orders_store.byId(order_id)
    lines = orders_store.getLines(order_id)
    return sum(line.price for line in lines) + order.shipping


# implementation

from config import URL from domain import Order, OrderLine
from application import OrdersProtocol, OrdersStoreToken

class OrdersStore(OrdersProtocol):
    def __init__(self, url):
        self.url = url

    def byId(self, id):
        return map(Order, requests.get(f'{self.url}/order/{id}').json())

    def getLines(self, id):
        return map(OrderLine, requests.get(f'{self.url}/order/{id}/lines').json())

tres.container.register(OrdersStoreToken, OrdersStore(URL))


# consumer

from application import calculate_total, OrdersStoreToken

def order_view(order_id):
    orders_store = tres.container[OrdersStoreToken]
    order = orders_store.byId(order_id)
    total = calculate_total(orders_store, order_id)
    return f'{order.id} - {order.date}: {total}'
```
