#!/usr/bin/env bash

export PATH=`poetry env info --path`/bin:$PATH
find . -type d -name .venv -prune -o -type f -name "*.py" -exec `which python` -m autopep8 --in-place {} \;

