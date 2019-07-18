from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd


qbdata = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_QB.csv")
rbdata = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_RB.csv")
wrdata = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_WR.csv")
tedata = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_TE.csv")
kdata = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_K.csv")
dstdata = pd.read_csv("FantasyPros_Fantasy_Football_Statistics_DST.csv")
alldata = pd.read_csv("FantasyPros_Fantasy_Football_Points.csv")

positions = ["QB","RB","WR","TE","K","DST"]

#print(alldata.head())
#print(qbdata.head())
#print(wrdata.head())

def get_Player_Overall_Index(player):
    return np.where(alldata["Player"]==player)[0][0]+1

def get_Player_Position_Index(position,player):
    if(position == "QB"):
        for row in qbdata["Player"]:
            if row.startswith(player):
                return np.where(qbdata["Player"]==row)[0][0]+1
    elif(position == "RB"):
        for row in rbdata["Player"]:
            if row.startswith(player):
                return np.where(rbdata["Player"]==row)[0][0]+1
    elif(position == "WR"):
        for row in wrdata["Player"]:
            if row.startswith(player):
                return np.where(wrdata["Player"]==row)[0][0]+1
    elif(position == "TE"):
        for row in tedata["Player"]:
            if row.startswith(player):
                return np.where(tedata["Player"]==row)[0][0]+1
    elif(position == "K"):
        for row in kdata["Player"]:
            if row.startswith(player):
                return np.where(kdata["Player"]==row)[0][0]+1
    elif(position == "DST"):
        for row in dstdata["Player"]:
            if row.startswith(player):
                return np.where(dstdata["Player"]==row)[0][0]+1

def get_Team_Overall_Index(team):
    totalrank = 0
    for position in positions:
        for player in team[position]:
            index = get_Player_Overall_Index(player)
            print("{} {}".format(index,player))
            totalrank+=index
    print(totalrank/9)

def get_Team_Position_Index(team):
    totalrank = 0
    for position in positions:
        for player in team[position]:
            index = get_Player_Position_Index(position, player)
            print("{} {}".format(index,player))
            totalrank+=index
    print(totalrank/9)
