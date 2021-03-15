#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:00:44 2021

@author: aaronnadell
"""
import random as random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from mpl_toolkits import mplot3d
#from mpl_toolkits.mplot3d.axes3d import Axes3D

def Translator(nrow, connections):
    
    colors = ["blue", "red", "brown", "darkorange", "crimson",
          "aqua", "aquamarine", "goldenrod", "gold", 'm', 'fuchsia', 
          'greenyellow', 'g','k','cyan', 'purple', 'dodgerblue', 'hotpink',
          'deepskyblue', 'coral', 'maroon', 'khaki']
    colors = colors * random.randint(1, nrow)
    #Useful Functions
    def jitter():
        jitter = []
        jitter =  jitter + [random.random()/random.randrange(1,4, 1)]
        return(jitter)
    
    def ReduceConnections(connlist):
        for i in range(0,len(connlist)):    #for every element
            for k in range(0,len(connlist[i])): #for every sub-element
                remover = connlist[i][k]    #row it's connected to
                for j in connlist[remover]: #for subelements in the element that needs to be reduced
                    if j == i:              #if the initial element matches the value of the second element
                        connlist[j][k] = j  #replace the value to be removed with the element number so it references itself
        return(connlist)
    
    def connector(nrow, deg_connect):   #generates string with embeded strings
        connect = [None]*nrow           #initialize string
        for i in range(0, nrow):        #for every element in the string
            ran_int = random.sample(range(nrow), deg_connect) #random integers sampled deg_connect times
            connect[i] = ran_int        #give element the random integers
        return(connect)
    
    #Create the dataframe to be referenced
    x = np.linspace(0, 100, nrow)
    
    connections = ReduceConnections(connector(nrow, connections))
    d = {'x': x, 
     'y': np.tan(x), 
     'z': 2*x,
     'connections':connections
         }
    df = pd.DataFrame(data = d)
    
    nrow = len(df.index)
    
    ####################### Plot in 3D ###########################
    ax = plt.axes(projection='3d')
    
    
    zline = df.loc[:,'z']
    xline = df.loc[:,'x']
    yline = df.loc[:,'y']
    ax.plot3D(xline, yline, zline, 'red')
    
    zdata = df.loc[:,'z']
    xdata = df.loc[:,'x']
    ydata = df.loc[:,'y']
    ax.scatter3D(xdata, ydata, zdata);
    plt.show()
    
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    
    for i in range(0, nrow): #for each row
        for j in range(0, len(df.loc[i, 'connections'])): #for the elements in connection
                x = []
                y = []
                z = []
                k= 0
                while k < len(df.loc[i, 'connections'])-1:
                    grab_row_val = df.loc[i, 'connections'][j]
                    x = x +[df.loc[i,'x'], df.loc[grab_row_val,'x']]
                    y = y +[df.loc[i,'y'], df.loc[grab_row_val,'y']]
                    z = z +[df.loc[i,'z'], df.loc[grab_row_val,'z']]
                    k = k + 1
                    ax.plot(x, y, z, color = colors[i])
    plt.show()
    
    ####################### Plot in 2D ###########################
    
    # x axis values 
    x = df.loc[:,'x']
    # y axis values 
    y = df.loc[:,'y']
      
    plt.plot(x, y, 'o') 
    
    
    
    for i in range(0, nrow): #for each row
        for j in range(0, len(df.loc[i, 'connections'])): #for the elements in connection
                x = []
                y = []
                k= 0
                while k < len(df.loc[i, 'connections'])-1:
                    grab_row_val = df.loc[i, 'connections'][j]
                    x = x +[df.loc[i,'x'], df.loc[grab_row_val,'x']] 
                    y = y +[df.loc[i,'y'], df.loc[grab_row_val,'y']]
                    k = k + 1
                    plt.plot(x, y, color = colors[i])
    
    plt.xlabel('x - axis') 
    plt.ylabel('y - axis') 
    plt.title('2D Representation')            
    plt.show()
