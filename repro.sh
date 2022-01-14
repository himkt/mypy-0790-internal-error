#!/bin/sh

python3 -m venv venv
. venv/bin/activate

pip install 'mypy<0.800'
mypy main.py
