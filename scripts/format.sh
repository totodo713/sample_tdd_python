#!/usr/bin/env bash

export PATH=`poetry env info --path`/bin:$PATH
find . -type f -name "*.py" -exec `which python` -m autopep8 --in-place {} \;

