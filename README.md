## Code

```python
> cat main.py
from typing import AnyStr


def some_func(test_str: AnyStr):
    cmdline: str | int = test_str
```

## Reproduce steps

```sh
python3 -m venv venv
. venv/bin/activate

pip install 'mypy<0.800'
mypy main.py
```

## Facts

- reproducible code uses `Union operation`, PEP604
  - https://www.python.org/dev/peps/pep-0604/
- `mypy<0.800` doesn't support union operation
  - https://mypy-lang.blogspot.com/2021/01/mypy-0800-released.html
- failure only happens when importing `AnyStr`
  - even when union operation is used, error doesn't occur without importing `AnyStr`


## Assumption

Some malicious code exists in AnyStr implementation, which somehow try to utilize union operation.
