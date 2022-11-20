#!/bin/bash
echo "Start"
python3 /app/nt_import/nt_importd.py /app/nt_import/logs/run/nt_importd.pid /app/nt_import/logs/nt_importd.log  start
tail -n 10 /app/nt_import/logs/nt_importd.log
