#!/usr/bin/env bash

poetry shell
`which python` -m pytest --cov=sample_tdd --cov-report=html --html=reports/test/results.html --self-contained-html
