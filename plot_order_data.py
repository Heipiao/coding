#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-28 18:35:57
# @Author  : chensijia (2350543676@qq.com)
# @Version : 0.0.0
# @Style   : Python3.4
#
# @Description: 

import os


## import python`s own lib
import os 

## import third party lib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

## import local lib


DATA_DIR = "../season_1_sad/"

TRAIN_FLAG = True
CONCRETE_DIR = "training_data" if TRAIN_FLAG else "test_set_1"


ORDER_SHEET_DIR = "order_data"


def plot_missed_time_slice(missed_sta):
    plot_saved_dir = os.path.join(DATA_DIR, CONCRETE_DIR, ORDER_SHEET_DIR, 
                                    "plot_missed_time_slice")
    x = range(1, 67)
    xmajorLocator = MultipleLocator(10) #将x主刻度标签设置为10的倍数
    xmajorFormatter = FormatStrFormatter('%d') #设置x轴标签文本的格式 
    xminorLocator = MultipleLocator(5) #将x轴次刻度标签设置为1的倍数  
    for k, v in missed_sta.items():
        y = np.zeros(66)
        for missed_dis, missed_time_slices in v.items():
            y[missed_dis - 1] = len(missed_time_slices)

        plt.scatter(x, y)
        ax = plt.gca()
        ax.set_title("missed time slice statistic:")
        ax.set_xlabel("district")
        ax.xaxis.set_major_locator(xmajorLocator)
        ax.xaxis.set_minor_locator(xminorLocator)
        ax.xaxis.set_minor_formatter(xmajorFormatter)
        ax.xaxis.grid(True, which='minor') #x坐标轴的网格使用次刻度
        ax.set_xlim(0, 66)
        ax.set_ylabel("missed time slices count")
        
        detail = "plot_district_slices"
        plt.savefig(os.path.join(plot_saved_dir, detail,  str(k) + ".png"))
        plt.close()


def plot_missed_time_slice_district(missed_sta):
    plot_saved_dir = os.path.join(DATA_DIR, CONCRETE_DIR, ORDER_SHEET_DIR, 
                                "plot_missed_time_slice")
    x = range(1, 22)
    xmajorLocator = MultipleLocator(1) #将x主刻度标签设置为10的倍数
    dates = list()
    for k, v in missed_sta.items():
        dates.append(k)
    print(dates)

    for i in range(1, 67):        
        y = list()
        for k in dates:
            if i in missed_sta[k].keys():
                y.append(len(missed_sta[k][i]))
            else:
                y.append(0)

        # print(len(y))
        plt.scatter(x, y)
        ax = plt.gca()
        ax.set_title("district: " + str(i) + " time slices missed ")
        ax.set_xlabel("date")
        ax.xaxis.set_major_locator(xmajorLocator)
        ax.xaxis.grid(True, which='major') #x坐标轴的网格使用主刻度
        ax.set_xlim(0, 22)
        #ax.set_xticklabels(dates)
        ax.set_ylabel("missed time slices count")
        
        detail = "plot_date_district"
        plt.savefig(os.path.join(plot_saved_dir, detail, "district_" + str(i) + ".png"))
        plt.close()