#!/bin/bash
source venv/bin/activate &&
rm -rf migrations/versions/* &&
python dropdb.py
