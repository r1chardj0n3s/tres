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
