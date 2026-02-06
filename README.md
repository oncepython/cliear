# cliear
Simple Python library for building CLI tools.
Pure Python.
Extremely easy to use, designed to be a modern alternative to argparse.
It is still under development.

## Quick start
Clone the repo:
```bash
git clone https://github.com/oncepython/cliear.git
cd cliear
```
Then execute this:
```bash
python examples/example.py subcommand1 --test-bool --test-str name --test-int 10 --test-list 1 2 3 -- file.txt
```
It should output:
```
subcommand 1
True
name
10
[1, 2, 3]
file.txt
```
Still developing.