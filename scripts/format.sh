#!/usr/bin/env bash

find . -type f -name "*.py" -exec `which python` -m autopep8 --in-place {} \;

