#!/bin/bash
source venv/bin/activate
echo "Running ETL process"
python3 run_etl.py
echo "ETL process completed"
deactivate
