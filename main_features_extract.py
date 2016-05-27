#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-25 20:33:18
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: 




## import python`s own lib
import os
import shutil

## import third party lib
import pandas as pd

## import local lib
from features_order_data import features_order_data_dir


LOAD_DATA_DIR = "../season_1_sad/" # only change this dir to change the operate dir
SAVE_DATA_DIR = "../season_1_upset/"

TRAIN_FLAG = True
CONCRETE_DIR = "training_data" if TRAIN_FLAG else "test_set_1"

## all the data dir we want to solve
CLUSTER_MAP_SHEET_DIR = "cluster_map"
ORDER_SHEET_DIR = "order_data"
TRAFFIC_SHEET_DIR = "traffic_data"
WEATHER_SHEET_DIR = "weather_data"
POI_SHEET_DIR = "poi_data"


#### Note: 
shutil.copytree(LOAD_DATA_DIR, SAVE_DATA_DIR)


########################################################################
####################### Order features #################################

def features_order():
    order_data_dir = os.path.join(SAVE_DATA_DIR, CONCRETE_DIR, ORDER_SHEET_DIR)
    features_order_data_dir(order_data_dir)



if __name__ == '__main__':
    features_order()