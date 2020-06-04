#!/bin/sh -e

echo   Executing the Test---
flake8 cart tests --max-line-length=149
python -m pytest --cov=cart --cov-report=term-missing --tb=short;
