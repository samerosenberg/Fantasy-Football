from data18 import *
import numpy as np
import pandas as pd


positions = ["QB","RB","WR","TE","K","DST"]


def get_Player_Overall_Index(player):
    try:
        return alldata.loc[alldata["Player"].str.startswith(player,na=False)].index[0]+1
    except IndexError as error:
        print(player)
        return 526

def get_Player_Position_Index(position,player):
    if(position == "QB"):
        try:
            return qbdata.loc[qbdata["Player"].str.startswith(player,na=False)].index[0]+1
        except IndexError as error:
            return 157
    elif(position == "RB"):
        try:
            return rbdata.loc[rbdata["Player"].str.startswith(player,na=False)].index[0]+1
        except IndexError as error:
            return 334
    elif(position == "WR"):
        try:
            return wrdata.loc[wrdata["Player"].str.startswith(player,na=False)].index[0]+1
        except IndexError as error:
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
    numqb, numte, numwr, numrb, numdst,numk=0,0,0,0,0,0
    for player in team.keys():
        index = get_Player_Position_Index(team[player],player)+1
        if team[player]=="QB":
            numqb+=1
            rank= index*(1/numqb)
        elif team[player]=="RB":
            numrb+=1
            rank= index*(1/numrb)
        elif team[player]=="WR":
            numwr+=1
            rank= index*(1/numwr)
        elif team[player]=="TE":
            numte+=1
            rank= index*(1/numte)
        elif team[player]=="DST":
            numdst+=1
            rank= index*(1/numdst)
        elif team[player]=="K":
            numk+=1
            rank= index*(1/numk)
        totalrank+= rank
        players+=1
        print("{}\t : {}\t : {}\t : \t{}".format(player,players,index ,rank))
    return totalrank/players
