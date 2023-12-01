# Advent of Code 2023

## Pytest

Experiements with dynamic tests, using fixtures or parameterzed:

### Parameterized test

- Good: Separate tests for each example
- Bad: Ugly test names

```python
@pytest.mark.parametrize("test_input,expected", test_a)
def test_solve_a(test_input, expected):
    assert solve_a(test_input) == expected
```

### Test using fixture

- Good: Pretty test names
- Bad: One test for all examples
- ?: How does it work with if fixture is empty list?
- ?: How to access fixture values?

```python
@pytest.fixture
def fix_b():
    return test_a

def test_solve_b(fix_b):
    if fix_b:
        assert solve_b(fix_b[0][0]) == fix_b[0][1]
```
