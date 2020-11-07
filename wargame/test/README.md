# Test Directory

This directory contains the unit test scripts. The following table is the total coverage of the tests:

| name | Stmts | Miss | Cover | 
| ---- | ----- | ---- | ----- | 
| abstractgameunit.py  | 39 | 4 | 90% | 
| attackoftheorcs.py | 75 | 16 | 79% | 
| gameuniterror.py | 10 | 8 | 20% | 
| gameutils.py | 15 | 6 | 60% | 
| hut.py | 17 | 1 | 94% | 
| knight.py | 44 | 11 | 75% | 
| orcrider.py | 10 | 1 | 90% | 
| test/__init__.py | 0 | 0 | 100% | 
| test/test_wargame.py |  56 | 6 | 89% | 
| ---- | ----- | ---- | ----- |
| TOTAL | 266 | 53 | 80% | 

Fell free to help full coverage :)

### How to run the coverage test?

First install the coverage package:

```sh
$ pip install coverage
```
Then go the wargame directory:

```sh
$ cd wargame
```
and run:

```sh
$ converage run -m test.test_wargame && coverage report
```
