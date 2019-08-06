from data17 import *
import numpy as np
import pandas as pd


positions = ["QB","RB","WR","TE","K","DST"]


def get_Player_Overall_Index(player):
    try:
        return np.where(alldata["Player"]==player)[0][0]+1
    except IndexError as error:
        print(player)
        return 526

def get_Player_Position_Index(position,player):
    if(position == "QB"):
        for row in qbdata["Player"]:
            if row.startswith(player):
                return np.where(qbdata["Player"]==row)[0][0]+1
    elif(position == "RB"):
        return rbdata.loc[rbdata["Player"]==player].index[0]+1
        #for row in rbdata["Player"]:
        #    try:
        #        if row.startswith(player):
        #            return np.where(rbdata["Player"]==row)[0][0]+1
        #    except AttributeError as error:
                #print(player)
        #        return 334
    elif(position == "WR"):
        for row in wrdata["Player"]:
            try:
                if row.startswith(player):
                    return np.where(wrdata["Player"]==row)[0][0]+1
            except AttributeError as error:
                #print(player)
                return 502
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

def get_Team_Overall_Rank(team):
    players=0
    totalrank = 0
    for position in positions:
        for player in team[position]:
            index = get_Player_Overall_Index(player)+1
            #print("{} {}".format(index,player))
            totalrank+=index
            players+=1
    return totalrank/players

def get_Team_Position_Rank(team):
    players=0
    totalrank = 0
    for position in positions:
        for player in team[position]:
            index = get_Player_Position_Index(position, player)+1
            #print("{} {}".format(index,player))
            totalrank+=index
            players+=1
    return totalrank/players

def get_Draft_Rank(team):
    players =0
    totalrank =0
    for player in team:
        index = get_Player_Position_Index(team[player],player)+1
        totalrank+=index
        players+=1
    return totalrank/players
