#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-20 03:06:21
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: load train first!!! Then test data


## import python`s own lib
import os
import shutil

## import third party lib
import pandas as pd

## import local lib
from operate_file import *
from operate_day import *
from operate_file_style import operate_file_style
from operate_load_poi_data import extract_poi_data_normally

# the path work for csj
LOAD_DATA_DIR = "../season_1/"
SAVE_DATA_DIR = "../season_1_sad/"


TRAIN_FLAG = True
CONCRETE_DIR = "training_data" if TRAIN_FLAG else "test_set_1"



## all the data dir we want to solve
CLUSTER_MAP_SHEET_DIR = "cluster_map"
ORDER_SHEET_DIR = "order_data"
TRAFFIC_SHEET_DIR = "traffic_data"
WEATHER_SHEET_DIR = "weather_data"
POI_SHEET_DIR = "poi_data"


def cluster_map_sheet_pre():
    print("------ load cluster_map data ----------")
    cluster_map_sheet_path = os.path.join(LOAD_DATA_DIR, CONCRETE_DIR, CLUSTER_MAP_SHEET_DIR)
    print("load data from: ", cluster_map_sheet_path)
    save_path = os.path.join(SAVE_DATA_DIR, CONCRETE_DIR, CLUSTER_MAP_SHEET_DIR)
    print("save data to: ", save_path)
    file = "cluster_map"

    cluster_sheet = os.path.join(cluster_map_sheet_path, file)
    data = pd.read_csv(cluster_sheet,header=-1)
    data.columns = ["raw"]
    data["district_hash"] = data["raw"].map(lambda x: x.split("\t")[0])
    data["district_map"] = data['raw'].map(lambda x: x.split("\t")[1])

    del data["raw"]
    
    save_df_to_file(data, save_path, file)


# handle the order_info sheet
def order_sheet_pre():
    
    print("\n------ load order data ----------")
    order_sheet_path = os.path.join(LOAD_DATA_DIR, CONCRETE_DIR, ORDER_SHEET_DIR)
    print("load data from: " + order_sheet_path)
    save_path = os.path.join(SAVE_DATA_DIR, CONCRETE_DIR, ORDER_SHEET_DIR)
    print("save data to: " + save_path)

    for file in os.listdir(order_sheet_path):
        if "order_data_" in file:
            data = pd.read_csv(os.path.join(order_sheet_path,file),header=-1)
            
    #processing data and slice time
            data.columns = ['raw']
            data['order_id'] = data['raw'].map(lambda x: x.split("\t")[0])
            data['driver_id'] = data['raw'].map(lambda x: x.split("\t")[1])
            data['passenger_id'] = data['raw'].map(lambda x: x.split("\t")[2])
            data['start_district_hash'] = data['raw'].map(lambda x: x.split("\t")[3])
            data['dest_district_hash'] = data['raw'].map(lambda x: x.split("\t")[4])
            data['price'] = data['raw'].map(lambda x: x.split("\t")[5])
            data['Time'] = data['raw'].map(lambda x: x.split("\t")[6])

            t = pd.to_datetime(data['Time'])
            data['Time']=t.map(lambda x:deal_the_day(x))

            data["week"] = data["Time"].map(lambda x: pd.to_datetime(x[:10]).weekday()+1)
            data["date"] = data["Time"].map(lambda x: x[:10])
            data["time_slices"] = data["Time"].map(lambda x: x[11:])
            del data['raw']#del useless column
            #del data['Time']

    #save as the specific dir
            save_df_to_file(data, save_path, file)



def poi_sheet_pre():
    print("\n------ load poi data ----------")
    poi_sheet_path = os.path.join(LOAD_DATA_DIR, CONCRETE_DIR, POI_SHEET_DIR)
    print("load data from: " + poi_sheet_path)
    save_path =os.path.join(SAVE_DATA_DIR, CONCRETE_DIR, POI_SHEET_DIR)
    print("save data to: " + save_path)
    data = pd.read_csv(os.path.join(poi_sheet_path,"poi_data"),header=-1)
    normal_poi_df = extract_poi_data_normally(data)

    file = "poi_data"
    save_df_to_file(normal_poi_df, save_path, file)

def traffic_sheet_pre():
#set filename and input data
    print("\n------ load traffic data ----------")
    traffic_sheet_path = os.path.join(LOAD_DATA_DIR, CONCRETE_DIR, TRAFFIC_SHEET_DIR)
    print("load data from: " + traffic_sheet_path)
    save_path =os.path.join(SAVE_DATA_DIR, CONCRETE_DIR, TRAFFIC_SHEET_DIR)
    print("save data to: " + save_path)

    for file in os.listdir(traffic_sheet_path):
        if "traffic_data_" in file:
            data = pd.read_csv(os.path.join(traffic_sheet_path,file),header=-1)
            
    #processing data and slice time 
            data.columns = ['raw']
            data['district_hash'] = data['raw'].map(lambda x: x.split("\t")[0])
            data['tj_level1_count'] = data['raw'].map(lambda x: x.split("\t")[1][2:])
            data['tj_level2_count'] = data['raw'].map(lambda x: x.split("\t")[2][2:])
            data['tj_level3_count'] = data['raw'].map(lambda x: x.split("\t")[3][2:])
            data['tj_level4_count'] = data['raw'].map(lambda x: x.split("\t")[4][2:])
            data['Time'] = data['raw'].map(lambda x: x.split("\t")[5])
            t = pd.to_datetime(data['Time'])
            data['Time']=t.map(lambda x:deal_the_day(x))

            data["week"] = data["Time"].map(lambda x: pd.to_datetime(x[:10]).weekday()+1)
            data["date"] = data["Time"].map(lambda x: x[:10])
            data["time_slices"] = data["Time"].map(lambda x: x[11:])
            del data['raw']#del useless column
            #del data['Time']

    #save as the specific dir
            
            save_df_to_file(data, save_path, file)


def weather_sheet_pre():
#set filename and input data
    print("\n------ load weather data ----------")
    weather_sheet_path = os.path.join(LOAD_DATA_DIR, CONCRETE_DIR, WEATHER_SHEET_DIR)
    print("load data from: " + weather_sheet_path)
    save_path =os.path.join(SAVE_DATA_DIR, CONCRETE_DIR, WEATHER_SHEET_DIR)
    print("save data to: " + save_path)

    for file in os.listdir(weather_sheet_path):
        if "weather_data_" in file:
            data = pd.read_csv(os.path.join(weather_sheet_path,file),header=-1)
            
    #processing data and slice time 
            data.columns = ['raw']
            data['Time'] = data['raw'].map(lambda x: x.split("\t")[0])
            t = pd.to_datetime(data['Time'])
            data['Time']=t.map(lambda x:deal_the_day(x))
            data['weather'] = data['raw'].map(lambda x: x.split("\t")[1])
            data['temperature'] = data['raw'].map(lambda x: x.split("\t")[2])
            data['PM2.5'] = data['raw'].map(lambda x: x.split("\t")[3])

            data["week"] = data["Time"].map(lambda x: pd.to_datetime(x[:10]).weekday()+1)
            data["date"] = data["Time"].map(lambda x: x[:10])
            data["time_slices"] = data["Time"].map(lambda x: x[11:])
            del data['raw']#del useless column
            # del data['Time']

    #save as the specific dir
            save_df_to_file(data, save_path, file)


if __name__ == '__main__':
    if os.path.exists(SAVE_DATA_DIR) and TRAIN_FLAG:
        shutil.rmtree(SAVE_DATA_DIR)
    cluster_map_sheet_pre()
    order_sheet_pre()
    poi_sheet_pre()
    traffic_sheet_pre()
    weather_sheet_pre()
    operate_file_style(is_add = True, bases_dir = "../season_1_sad/")
    print("Done...")