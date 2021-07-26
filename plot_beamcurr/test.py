# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os 
import math
import japanize_matplotlib
import matplotlib.ticker as ptick
from matplotlib.pyplot import figure
from matplotlib.backends.backend_pdf import PdfPages

def write_all():
    csv_file=os.listdir('csv/')
    pp = PdfPages('test.pdf')
    
    for i in range(len(csv_file)):
        file = pd.read_csv('csv/' + str(csv_file[i]) ,usecols=[0,1], skiprows=2, names=["B40電流", "電流値"], encoding="")    
        
        fig = plt.figure(num=None, figsize=(15, 6))#グラフのサイズ
        plt.xticks(np.arange(2, 8+1, 0.3))
        plt.yticks(np.arange(-5e-6, 5e-4, 3e-6))
        plt.xlabel('B40電流', fontsize=15)
        plt.ylabel('電流値', fontsize=15)
        plt.xlim([2,8])
        plt.grid(True)
        plt.title(csv_file[i])
        plt.plot(file["B40電流"], file["電流値"])    
        ax = plt.gca()#axesの取得
        ax.ticklabel_format(style="sci",  axis="y",scilimits=(-6,-6))#y軸指数表記
        pp.savefig(fig)
    pp.close()

def plot(csv_file):
    file = pd.read_csv('csv/' + str(csv_file) ,usecols=[0,1], skiprows=2, names=["B40電流", "電流値"], encoding="")  

    #グラフの作成
    figure(num=None, figsize=(15, 6))#グラフのサイズ
    #軸のメモリ幅
    plt.xticks(np.arange(2, 8+1, 0.5))
    plt.yticks(np.arange(-5e-6, 5e-4, 5e-6))
    #軸ラベル
    plt.xlabel('B40電流', fontsize=15)
    plt.ylabel('電流値', fontsize=15)
    plt.xlim([2,8])#x軸の範囲
    plt.grid(True)
    plt.plot(file["B40電流"], file["電流値"])    
    ax = plt.gca()#axesの取得
    ax.ticklabel_format(style="sci",  axis="y",scilimits=(-6,-6))#y軸指数表記
    
def multi_plot(csv_file1, csv_file2):
    file1 = pd.read_csv('csv/' + str(csv_file1) ,usecols=[0,1], skiprows=2, names=["B40電流", "電流値"], encoding="")  
    file2 = pd.read_csv('csv/' + str(csv_file2) ,usecols=[0,1], skiprows=2, names=["B40電流", "電流値"], encoding="")  
    
    #グラフ重ねて表示
    figure(num=None, figsize=(15, 6))#グラフのサイズ
    #軸のメモリ幅
    plt.xticks(np.arange(2, 8+1, 0.5))
    plt.yticks(np.arange(-4e-6, 4e-4, 4e-6))
    #軸ラベル
    plt.xlabel('B40電流', fontsize=15)
    plt.ylabel('電流値', fontsize=15)
    plt.xlim([2,8])#x軸の範囲
    plt.grid(True)
    plt.plot(file1["B40電流"], file1["電流値"])
    ax = plt.gca()#axesの取得
    ax.ticklabel_format(style="sci",  axis="y",scilimits=(-6,-6))#y軸指数表記
    plt.plot(file2["B40電流"], file2["電流値"])

def plot_graph(Hcurr):
    #表の作成
    ion_name=['H+','H2+ C6+ N7+ O8+','B5+','O7+','N6+','C5+','O6+','B4+','N5+'
              ,'C4+','O5+','10B3+','N4+','B3+','C3+ O4+','N3+','10B2+','O3+','B2+','C2+','N2+','O2+']
    ion_mass=[1,2,2.2,2.28,2.33,2.4,2.66,2.75,2.8,3,3.2,3.33,3.5,3.66,4,4.66,5,5.33,5.5,6,7,8]
    ion_curr=[math.sqrt(i)*Hcurr for i in ion_mass]

    #原子質量と電流値を小数点2桁に変更
    for j in range(len(ion_mass)):
        ion_mass[j]="{:.2f}".format(ion_mass[j])
    for j in range(len(ion_curr)):
        ion_curr[j]="{:.2f}".format(ion_curr[j])

    list = [
        ion_mass, 
        ion_curr
    ]

    custom_style = [
        {
            'selector': 'th', #表のヘッダーのスタイルを変更
            'props':[
                ('border', 'solid black 1px'), #ボーダーを実線、黒色、太さ1pxに設定
                ('text-align', 'center'), #中央揃え
            ]
        },
        {
            'selector': 'td', #各セルのスタイルを変更
            'props':[
                ('border', 'solid black 1px'), #ボーダーを実線、黒色、太さ1pxに設定
                ('text-align', 'center'), #中央揃え
            ]
        }
    ]
    df = pd.DataFrame(list)
    df.index = ['B40電流','電流値']#列要素の設定
    df.columns =ion_name#行要素の設定
    display(df.style.set_table_styles(custom_style))
