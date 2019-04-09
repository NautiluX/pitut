#!/bin/bash

python plot.py &
python dht_print.py > data.csv
python -m SimpleHTTPServer 8080

