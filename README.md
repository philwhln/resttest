# resttest

[![Build Status](https://travis-ci.org/philwhln/resttest.svg?branch=master)](https://travis-ci.org/philwhln/resttest) [![Docker Hub](https://img.shields.io/badge/docker-ready-blue.svg)](https://hub.docker.com/r/philwhln/resttest/)

## Run application

Use `make run` to run the application.

```
> make run

2013-12-12        $-227.35        $-227.35
2013-12-13       $-1229.58       $-1456.93
2013-12-15          $-5.39       $-1462.32
2013-12-16       $-4575.53       $-6037.85
2013-12-17       $10686.28        $4648.43
2013-12-18       $-1841.29        $2807.14
2013-12-19       $19753.31       $22560.45
2013-12-20       $-4054.60       $18505.85
2013-12-21         $-17.98       $18487.87
2013-12-22        $-110.71       $18377.16

                           TOTAL $18377.16
```

## Run tests

Use `make test` to run the tests.

```
> make test

py.test --flake8 --cov=resttest
======================================== test session starts ========================================
platform darwin -- Python 3.6.0, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /Users/phil/src/bench/resttest, inifile:
plugins: flake8-0.8.1, cov-2.4.0
collected 10 items

app.py s
resttest/__init__.py .
resttest/display.py .
resttest/transactions.py .
tests/test_transactions.py s.....

---------- coverage: platform darwin, python 3.6.0-final-0 -----------
Name                       Stmts   Miss  Cover
----------------------------------------------
resttest/__init__.py          11      9    18%
resttest/display.py            4      2    50%
resttest/transactions.py      39      1    97%
----------------------------------------------
TOTAL                         54     12    78%


================================ 8 passed, 2 skipped in 2.51 seconds ================================
```

## Assumptions

- We cannot guarantee how many items are returned on each page. Therefore, we cannot proactively determine how many pages there will be.
- Transactions come in arbitrary order.

## Improvements

- Add pageSize to `http://resttest.bench.co/transactions/*.json`

## Docker usage

### Build

Build the application with `make docker-build`.

### Run

Run the application with `make docker-run`

### Test

Test the application with `make docker-test`

This builds a 2nd docker container that builds on the application container, 
adding the unit tests and testing dependencies.
