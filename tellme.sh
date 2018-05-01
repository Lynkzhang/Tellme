#!/bin/bash

datetime=$(date +%Y%m%d-%H%M%S)
touch log.$datetime.out
python sendtest.py $datetime
python slack.py
