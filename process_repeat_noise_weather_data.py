#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-24 19:24:37
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: 




## import python`s own lib
import os

## import third party lib
import pandas as pd

## import local lib



def process_repeat_noise_weather_dir(needed_map_dir):
    if not os.path.isdir(needed_map_dir) or not os.path.exists(needed_map_dir):
        raise IOError("ERROR: " + needed_map_dir + " not existed or its not a dir")
    print("changeing all the weather... in " + needed_map_dir)
    for file in os.listdir(needed_map_dir):
        if ".csv" in file:
            file_path = os.path.join(needed_map_dir, file)
            #print(file)
            # map all the district into concrete value
            mapped_data_frame = process_weather(pd.read_csv(file_path))
            # change the file
            mapped_data_frame.to_csv(file_path, index = False)

def process_weather(data):
    data = data.drop_duplicates(["time_slices"])
    data.reset_index(drop=True,inplace=True)


    dict1 = dict(zip(data.time_slices,data.weather))
    dict2 = dict(zip(data.time_slices,data["PM2.5"]))
    dict3 = dict(zip(data.time_slices,data["temperature"]))
    
    #print(dict1)
    df = pd.DataFrame(columns=["date", "time_slices","weather","PM2.5"])
    df["date"] = data["date"]
    df["Time"] = data["Time"]
    df["week"] = data["week"]
    df["time_slices"]=pd.Series(range(1,145))
    df["weather"]=0
    df["PM2.5"]=0
    df["temperature"]=0
    default_wea = 0
    default_pm = 0
    default_tem = 0

    for x in df["time_slices"]:
        default_wea = dict1.get(x,default_wea)
        default_pm = dict2.get(x,default_pm)
        default_tem = dict3.get(x,default_tem)

        df["weather"] = df["weather"].set_value(int(x)-1,default_wea)
        df["PM2.5"] = df["PM2.5"].set_value(int(x)-1,default_pm)
        df["temperature"] =  df["temperature"].set_value(int(x)-1,default_tem)



    for x in df["time_slices"]:
        if(x>2 and x<143):
      
            s1=df["weather"][int(x)-1]
            s2=df["weather"][int(x)+1]
            if(s1 == s2):
                df["weather"][x]=s1
            else:
                pass
        else:
            pass

    return df