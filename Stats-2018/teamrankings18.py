from ffdata import *

Slaz = {
    "QB": ["Russell Wilson","Andrew Luck"],
    "RB": ["Joe Mixon","Jamaal Williams","Derrick Henry","Todd Gurley","Kenyan Drake","Phillip Lindsay"],
    "WR": ["Davante Adams","Amari Cooper","Josh Reynolds","D.J. Moore"],
    "TE": ["Evan Engram", "Cameron Brate"],
    "K": ["Justin Tucker"],
    "DST":["Cleveland Browns"]
}
Slazstarters={
    "QB": ["Russell Wilson"],
    "RB": ["Joe Mixon","Todd Gurley","Derrick Henry"],
    "WR": ["Davante Adams","Amari Cooper"],
    "TE": ["Evan Engram"],
    "K": ["Justin Tucker"],
    "DST": ["Cleveland Browns"]
}

Matt={
    "QB": ["Jared Goff", "Aaron Rodgers"],
    "RB": ["Christian McCaffrey","Jaylen Samuels","Tarik Cohen","Leonard Fournette","Sony Michel","James White"],
    "WR": ["DeAndre Hopkins","T.Y. Hilton","Tyler Lockett","Tyler Boyd"],
    "TE": ["Travis Kelce"],
    "K": ["Stephen Gostkowski"],
    "DST":["Chicago Bears","Los Angeles Chargers"]
}

Mattstarters={
    "QB":["Aaron Rodgers"],
    "RB": ["Christian McCaffrey","James White"],
    "WR": ["DeAndre Hopkins","T.Y. Hilton", "Tyler Lockett"],
    "TE":["Travis Kelce"],
    "K": ["Stephen Gostkowski"],
    "DST": ["Chicago Bears"]
}

positions = ["QB","RB","WR","TE","K","DST"]

#Slaz Rankings

print("All positions rankings\n")

get_Team_Overall_Index(Slazstarters)

print("Individual Position rankings\n")

get_Team_Position_Index(Slazstarters)

#Matt rankings

print("All positions rankings\n")

get_Team_Overall_Index(Mattstarters)

print("Individual Position rankings\n")

get_Team_Position_Index(Mattstarters)
