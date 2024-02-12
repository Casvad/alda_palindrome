# About this repo

Project with 3 palindrome algorithms

## Iterative

Time complexity: `O(n)`

## Recursive

Time complexity: `O(n)`

## Reverse

Time complexity: `O(n)`

---

# Python version
Python 3.11.0

# Running locally and testing

```
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

# Check coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. 
Then run `coverage run -m unittest discover` and after that run `coverage report` to get the following table:

```shell
Name                               Stmts   Miss  Cover
------------------------------------------------------
base/__init__.py                       0      0   100%
base/test/__init__.py                  0      0   100%
iterative/__init__.py                  0      0   100%
iterative/algorithm.py                 5      0   100%
iterative/test/__init__.py             0      0   100%
iterative/test/test_algorithm.py      11      1    91%
recursive/__init__.py                  0      0   100%
recursive/algorithm.py                 6      0   100%
recursive/test/__init__.py             0      0   100%
recursive/test/test_algorithm.py      11      1    91%
reverse/__init__.py                    0      0   100%
reverse/algorithm.py                   5      0   100%
reverse/test/__init__.py               0      0   100%
reverse/test/test_algorithm.py        11      1    91%
utils/__init__.py                      0      0   100%
utils/constants_test.py                2      0   100%
------------------------------------------------------
TOTAL                                 51      3    94%

```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.

# Searching performance


