#!/bin/bash

# create python virtual env
python3 -m venv local_lib; source local_lib/bin/activate 

# pip version
pip --version

# install path.py
if pip install --target=./local_lib --upgrade git+https://github.com/jaraco/path.git --log install.log; then
    # execute python script if install successful
    python3 my_program.py
fi