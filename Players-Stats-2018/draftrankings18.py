from functions18 import *
import pandas as pd
import numpy as np
from collections import OrderedDict

Sam=OrderedDict()
Sam["Ezekiel Elliott"]="RB"
Sam["Keenan Allen"]="WR"
Sam["Jordan Howard"]="RB"
Sam["Derrick Henry"]="RB"
Sam["Larry Fitzgerald"]="WR"
Sam["Marvin Jones"]= "WR"
Sam["Jamaal Williams"]="RB"
Sam["Delanie Walker"]="TE"
Sam["Chris Hogan"]="WR"
Sam["Emmanuel Sanders"]="WR"
Sam["Carson Wentz"]="QB"
Sam["Kelvin Benjamin"]="WR"
Sam["Jamison Crowder"]="WR"
Sam["Sterling Shepard"]="WR"
Sam["Pittsburgh Steelers"]="DST"
Sam["Chris Boswell"]="K"

Slaz = OrderedDict()
Slaz["Todd Gurley"] = "RB"
Slaz["Joe Mixon"] = "RB"
Slaz["Davante Adams"] = "WR"
Slaz["Kenyan Drake"] = "RB"
Slaz["Amari Cooper"] = "WR"
Slaz["Chris Thompson"] = "RB"
Slaz["Marquise Goodwin"] = "WR"
Slaz["Evan Engram"] = "TE"
Slaz["Kerryon Johnson"] = "RB"
Slaz["Robby Anderson"] = "WR"
Slaz["Andrew Luck"] = "QB"
Slaz["Peyton Barber"] = "RB"
Slaz["D.J. Moore"] = "WR"
Slaz["Cameron Meredith"] = "WR"
Slaz["Baltimore Ravens"] = "DST"
Slaz["Daniel Carlson"] = "K"

Zach = {
    "QB": ["Cam Newton"],
    "RB": ["Kareem Hunt","Jerick McKinnon","LeSean McCoy","Jay Ajayi","Dion Lewis"],
    "WR": ["Odell Beckham Jr.","JuJu Smith-Schuster","Demaryius Thomas","Alshon Jeffery","Randall Cobb","Will Fuller","Marqise Lee"],
    "TE": ["Rob Gronkowski"],
    "K": ["Greg Zuerlein"],
    "DST": ["Philadelphia Eagles"]
}
Krum = {
    "QB": ["Russell Wilson","Drew Brees"],
    "RB": ["Le'Veon Bell","Alex Collins","Mark Ingram","Isaiah Crowell","Frank Gore"],
    "WR": ["Michael Thomas","A.J. Green","Adam Thielen","Sammy Watkins","Kenny Stills","Robert Woods"],
    "TE": ["Greg Olsen",],
    "K": ["Justin Tucker"],
    "DST": ["Los Angeles Chargers"]
}
Frank = {
    "QB": ["Kirk Cousins"],
    "RB": ["David Johnson","Dalvin Cook","Melvin Gordon","Lamar Miller","Marlon Mack","Marshawn Lynch"],
    "WR": ["Tyreek Hill","Josh Gordon","Devin Funchess","Devante Parker","Dez Bryant","Corey Davis"],
    "TE": ["Zach Ertz"],
    "K": ["Wil Lutz"],
    "DST": ["Houston Texans"]
}
RobTeam = {
    "QB": ["Deshaun Watson"],
    "RB": ["Saquon Barkley","Alvin Kamara","Sony Michel","James Conner","Latavius Murray"],
    "WR": ["Doug Baldwin","Mike Evans","Golden Tate","Jarvis Landry","Nelson Agholor","Calvin Ridley"],
    "TE": ["Kyle Rudolph","Jordan Reed"],
    "K": ["Jake Elliot"],
    "DST": ["Minnesota Vikings"]
}
Mike = {
    "QB": ["Tom Brady"],
    "RB": ["Ronald Jones","Devonta Freeman","Royce Freeman","Rashaad Penny","Tevin Coleman","Tarik Cohen"],
    "WR": ["Antonio Brown","Julio Jones","Stefon Diggs","Brandin Cooks","Pierre Garcon","Jordy Nelson"],
    "TE": ["David Njoku"],
    "K": ["Giorgio Tavecchio"],
    "DST": ["Los Angeles Rams"]
}
Matt = {
    "QB": ["Aaron Rodgers"],
    "RB": ["Leonard Fournette","Christian McCaffrey","Nick Chubb","Rex Burkhead","Carlos Hyde","C.J. Anderson"],
    "WR": ["DeAndre Hopkins","T.Y. Hilton","Allen Robinson","Michael Crabtree","Cooper Kupp"],
    "TE": ["Travis Kelce"],
    "K": ["Stephen Gostkowski","Graham Gano"],
    "DST": ["Jacksonville Jaguars"]
}

RobDraft = OrderedDict()
RobDraft["Saquon Barkley"] = "RB"
RobDraft["Alvin Kamara"]= "RB"
RobDraft["Doug Baldwin"]= "WR"
RobDraft["Mike Evans"]= "WR"
RobDraft["Golden Tate"]= "WR"
RobDraft["Kyle Rudolph"]= "TE"
RobDraft["Deshaun Watson"]= "QB"
RobDraft["Jarvis Landry"]= "WR"
RobDraft["Nelson Agholor"]="WR"
RobDraft["Sony Michel"]="RB"
RobDraft["James Conner"]="RB"
RobDraft["Minnesota Vikings"]="DST"
RobDraft["Latavius Murray"]= "RB"
RobDraft["Jordan Reed"]= "TE"
RobDraft["Jake Elliot"]="K"
RobDraft["Calvin Ridley"]="WR"



#print(get_Player_Position_Index("RB","Melvin Gordon"))

print("Rob {}".format(get_Draft_Rank(RobDraft)))
#print("Matt {}".format(get_Team_Position_Rank(Matt)))
#print("Slaz {}".format(get_Team_Position_Rank(Slaz)))
#print("Krum {}".format(get_Team_Position_Rank(Krum)))
#print("Mike {}".format(get_Team_Position_Rank(Mike)))
print("Sam {}".format(get_Draft_Rank(Sam)))
print("Slaz {}".format(get_Draft_Rank(Slaz)))
#print("Frank {}".format(get_Team_Position_Rank(Frank)))
#print("Zach {}".format(get_Team_Position_Rank(Zach)))
