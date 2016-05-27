#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-23 07:07:48
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: 




## import python`s own lib
import os

## import third party lib
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

## import local lib

# import matplotlib
# matplotlib.use('MacOSX')

DATA_DIR = "../season_1_sad/" # only change this dir to change the operate dir

TRAIN_FLAG = True
CONCRETE_DIR = "training_data" if TRAIN_FLAG else "test_set_1"


TRAFFIC_SHEET_DIR = "traffic_data"


# tj_level1_count  tj_level2_count  tj_level3_count tj_level4_count
# week  date  time  district
# Axes3D.scatter(xs, ys, zs=0, zdir='z', s=20, c='b', *args, **kwargs)
def plot_single_day_traffic(df):
    y_tj_l1 = df["tj_level1_count"]
    y_tj_l2 = df["tj_level2_count"]
    y_tj_l3 = df["tj_level3_count"]
    y_tj_l4 = df["tj_level4_count"]

    x_time = df["time_slices"]
    x_district = df["district"]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_time, x_district, y_tj_l1)
    # ax.plot_surface(x_time, x_district, y_tj_l1)
    print(plt.get_backend())
    #plt.show()
    plt.savefig("plot_traffic.png")
    

def plot_single_day_district_traffic(df, district_num, save_dir):
    single_district = df[df.district == district_num]

    fig = plt.figure()
    # show tj_level1_count 
    tj1_y = single_district["tj_level1_count"]
    time_x = single_district["time_slices"]
    tj1_p = fig.add_subplot(411)
    tj1_p.set_title("date: " + str(single_district.date.unique()[0]) +"," + " district: " + str(district_num))
    tj1_p.axis([0, 145, 0, max(tj1_y) + 50])
    tj1_p.set_ylabel("tj_level1_count")
    tj1_p.scatter(time_x, tj1_y)


    # show tj_level1_count 
    tj2_y = single_district["tj_level2_count"]
    time_x = single_district["time_slices"]
    tj2_p = fig.add_subplot(412)
    tj2_p.axis([0, 145, 0, max(tj2_y) + 50])
    tj2_p.set_ylabel("tj_level2_count")
    tj2_p.scatter(time_x, tj2_y)

    # show tj_level1_count 
    tj3_y = single_district["tj_level3_count"]
    time_x = single_district["time_slices"]
    tj3_p = fig.add_subplot(413)
    tj3_p.axis([0, 145, 0, max(tj3_y) + 50])
    tj3_p.set_ylabel("tj_level3_count")
    tj3_p.scatter(time_x, tj3_y)

    # show tj_level1_count 
    tj4_y = single_district["tj_level4_count"]
    time_x = single_district["time_slices"]
    tj4_p = fig.add_subplot(414)
    tj4_p.axis([0, 145, 0, max(tj4_y) + 50])
    tj4_p.set_ylabel("tj_level4_count")
    tj4_p.set_xlabel("time slice")
    tj4_p.scatter(time_x, tj4_y)
    
    save_file_name = "district: "+ str(district_num) + ".png"
    plt.savefig(os.path.join(save_dir, save_file_name))
    plt.close()

def plot_traffic():
    traffic_dir = os.path.join(DATA_DIR, CONCRETE_DIR, TRAFFIC_SHEET_DIR)
    print("plotting: ", traffic_dir)
    if not os.path.isdir(traffic_dir) or not os.path.exists(traffic_dir):
        raise IOError("Not a dir or not existed")
    for file in os.listdir(traffic_dir):
        if ".csv" in file:
            file_path = os.path.join(DATA_DIR, CONCRETE_DIR, TRAFFIC_SHEET_DIR, file)
            df = pd.read_csv(file_path)
            current_date = str(df["date"].unique()[0])
            current_date_plot_dir = os.path.join(DATA_DIR, CONCRETE_DIR, TRAFFIC_SHEET_DIR,\
                                                 current_date + "--plot")
            if not os.path.exists(current_date_plot_dir):
                os.mkdir(current_date_plot_dir)
            for dis_num in df.district.unique():
                plot_single_day_district_traffic(df, dis_num, current_date_plot_dir)





if __name__ == '__main__':
    file = "traffic_data_2016-01-01.csv"
    path = os.path.join(DATA_DIR, CONCRETE_DIR, TRAFFIC_SHEET_DIR, file)
    df = pd.read_csv(path)
    # print(df)
    # plot_single_day_traffic(df)
    # plot_single_day_district_traffic(df, 5)
    plot_traffic()