#!/bin/bash

mkdir url_data hosp_data
python get_hosp_url.py
python get_hosp_data.py
