#!/bin/bash
source /home/gabriel/repos/etl_api_to_sql/venv/bin/activate
echo "Running ETL process"
/usr/bin/python3 /home/gabriel/repos/etl_api_to_sql/run_etl.py
echo "ETL process completed"
deactivate
