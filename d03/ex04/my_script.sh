#!/bin/bash

# create python virtual env
python3 -m venv django_venv

source django_venv/bin/activate

# install from .txt file
pip install -r requirement.txt
