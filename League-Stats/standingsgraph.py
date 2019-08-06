import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Stan2018 = pd.read_csv("2018Standings.csv",index_col="TEAM")
Stan2017 = pd.read_csv("2017Standings.csv",index_col="TEAM")
Stan2016 = pd.read_csv("2016Standings.csv",index_col="TEAM")
Stan2015 = pd.read_csv("2015Standings.csv",index_col="TEAM")

Leaguestats=[Stan2015,Stan2016,Stan2017,Stan2018]

#print(Stan2015.loc["Slaz","PF"])

SlazPF = [year.loc["Slaz","PF"] for year in Leaguestats]
FrankPF = [year.loc["Frank","PF"] for year in Leaguestats]
SamPF = [year.loc["Sam","PF"] for year in Leaguestats]
ZachPF = [year.loc["Zach","PF"] for year in Leaguestats]
MikePF = [year.loc["Mike","PF"] for year in Leaguestats]
KrumPF = [year.loc["Krum","PF"] for year in Leaguestats]
RobPF = [year.loc["Rob","PF"] for year in Leaguestats]

PF= pd.DataFrame({
    "Slaz" :SlazPF,
    "FRank":FrankPF,
    "Sam":SamPF,
    "Zach":ZachPF,
    "Mike":MikePF,
    "Krum":KrumPF,
    "Rob": RobPF},index=["2015","2016","2017","2018"])

sns.lineplot(data=PF, dashes=False)
print(plt.show())



Standings = pd.DataFrame({
    "Slaz":[6,5,3,1],
    "Frank":[3,1,4,4],
    "Sam":[8,4,5,5],
    "Matt":[None,None,7,2],
    "Rob":[2,6,2,3],
    "Mike":[7,7,6,7],
    "Krum":[4,3,8,8],
    "Zach":[5,2,1,6],
    "Liam":[1,8,None,None],
    }, index=["2015","2016","2017","2018"])



#print(Standings.head())
# plt.figure(figsize=(14,6))
# sns.lineplot(data=Standings, dashes=False)
#print(plt.show())
