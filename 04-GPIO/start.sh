#!/bin/bash

./dht_csv.py > data.csv &
./dht_pandas_page.py
