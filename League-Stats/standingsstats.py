import pandas as pd
import numpy as np

Stan2018 = pd.read_csv("2018Standings.csv")
Stan2017 = pd.read_csv("2017Standings.csv")
Stan2016 = pd.read_csv("2016Standings.csv")
Stan2015 = pd.read_csv("2015Standings.csv")
#Stan2014 = pd.read_csv("2014Standings.csv")
#print(Stan2018.head())


Leaguestats=[Stan2018,Stan2017,Stan2016,Stan2015]

Slaz={
        "PF":0,
        "PA":0,
        "PF/G":0,
        "PA/G":0
}
Liatt={
        "PF":0,
        "PA":0,
        "PF/G":0,
        "PA/G":0
}
Sam={
        "PF":0,
        "PA":0,
        "PF/G":0,
        "PA/G":0
}
Rob={
        "PF":0,
        "PA":0,
        "PF/G":0,
        "PA/G":0
}
Frank={
        "PF":0,
        "PA":0,
        "PF/G":0,
        "PA/G":0
}
Zach={
        "PF":0,
        "PA":0,
        "PF/G":0,
        "PA/G":0
}
Krum={
        "PF":0,
        "PA":0,
        "PF/G":0,
        "PA/G":0
}
Mike={
        "PF":0,
        "PA":0,
        "PF/G":0,
        "PA/G":0
}


Stats={"TEAM","REC","PF","PA","PF/G","PA/G","DIFF","MOVES"}

print(Stan2018.loc[Stan2018.TEAM=="Slaz","PF"][0])


def get_All_Time_Stats(team):
        totalpf=0
        totalpa=0
        totalpfg=0
        totalpag=0
        totalmoves=0
        for year in Leaguestats:
                index = np.where(year["TEAM"]==team)[0][0]
                totalpf+= year["PF"][index]
                totalpa+= year["PA"][index]
                totalpfg+= year["PF/G"][index]
                totalpag+= year["PA/G"][index]
                totalmoves+=year["MOVES"][index]
        return totalpf/len(Leaguestats),totalpa/len(Leaguestats),totalpfg/len(Leaguestats),totalpag/len(Leaguestats),totalmoves/len(Leaguestats)



Slaz["PF"],Slaz["PA"],Slaz["PF/G"],Slaz["PA/G"],moves = get_All_Time_Stats("Slaz")
Liatt["PF"],Liatt["PA"],Liatt["PF/G"],Liatt["PA/G"],moves = get_All_Time_Stats("Liatt")
Sam["PF"],Sam["PA"],Sam["PF/G"],Sam["PA/G"],moves = get_All_Time_Stats("Sam")
Rob["PF"],Rob["PA"],Rob["PF/G"],Rob["PA/G"],moves = get_All_Time_Stats("Rob")
Frank["PF"],Frank["PA"],Frank["PF/G"],Frank["PA/G"],moves = get_All_Time_Stats("Frank")
Zach["PF"],Zach["PA"],Zach["PF/G"],Zach["PA/G"],moves = get_All_Time_Stats("Zach")
Krum["PF"],Krum["PA"],Krum["PF/G"],Krum["PA/G"],moves = get_All_Time_Stats("Krum")
Mike["PF"],Mike["PA"],Mike["PF/G"],Mike["PA/G"],moves = get_All_Time_Stats("Mike")

print("PF Rankings")
print("{} \tPF: {:.2f} ".format("Frank",Frank["PF"]))
print("{} \tPF: {:.2f} ".format("Slaz",Slaz["PF"]))
print("{} \tPF: {:.2f} ".format("Sam",Sam["PF"]))
print("{} \tPF: {:.2f} ".format("Zach",Zach["PF"]))
print("{} \tPF: {:.2f} ".format("Liatt",Liatt["PF"]))
print("{} \tPF: {:.2f} ".format("Krum",Krum["PF"]))
print("{} \tPF: {:.2f} ".format("Rob",Rob["PF"]))
print("{} \tPF: {:.2f} ".format("Mike",Mike["PF"]))

print("\nPA Rankings")
print("{} \tPA: {:.2f} ".format("Mike",Mike["PA"]))
print("{} \tPA: {:.2f} ".format("Slaz",Slaz["PA"]))
print("{} \tPA: {:.2f} ".format("Liatt",Liatt["PA"]))
print("{} \tPA: {:.2f} ".format("Sam",Sam["PA"]))
print("{} \tPA: {:.2f} ".format("Frank",Frank["PA"]))
print("{} \tPA: {:.2f} ".format("Krum",Krum["PA"]))
print("{} \tPA: {:.2f} ".format("Zach",Zach["PA"]))
print("{} \tPA: {:.2f} ".format("Rob",Rob["PA"]))
