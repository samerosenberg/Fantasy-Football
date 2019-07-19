from functions18 import *
import pandas as pd
import numpy as np


Sam ={
    "QB": ["Carson Wentz"],
    "RB": ["Ezekiel Elliott","Jordan Howard","Jamaal Williams","Derrick Henry"],
    "WR": ["Keenan Allen","Larry Fitzgerald","Marvin Jones","Chris Hogan","Emmanuel Sanders","Kelvin Benjamin","Jamison Crowder","Sterling Shepard"],
    "TE": ["Delanie Walker"],
    "K": ["Chris Boswell"],
    "DST": ["Pittsburgh Steelers"]
}
Slaz = {
    "QB": ["Andrew Luck"],
    "RB": ["Todd Gurley","Joe Mixon","Kenyan Drake","Chris Thompson","Kerryon Johnson","Peyton Barber"],
    "WR": ["Davante Adams","Amari Cooper","Marquise Goodwin","Robby Anderson","D.J. Moore","Cameron Meredith"],
    "TE": ["Evan Engram"],
    "K": ["Daniel Carlson"],
    "DST": ["Baltimore Ravens"]
}
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

RobDraft={
    "Saquon Barkley": "RB",
    "Alvin Kamara": "RB",
    "Doug Baldwin": "WR",
    "Mike Evans": "WR",
    "Golden Tate": "WR",
    "Kyle Rudolph": "TE",
    "Deshaun Watson": "QB",
    "Jarvis Landry": "WR",
    "Nelson Agholor":"WR",
    "Sony Michel":"RB",
    "James Conner":"RB",
    "Minnesota Vikings":"DST",
    "Latavius Murray": "RB",
    "Jordan Reed": "TE",
    "Jake Elliot":"K",
    "Calvin Ridley":"WR"
}

print("Rob {}".format(get_Draft_Rank(RobDraft)))
print("Matt {}".format(get_Team_Position_Rank(Matt)))
print("Slaz {}".format(get_Team_Position_Rank(Slaz)))
print("Krum {}".format(get_Team_Position_Rank(Krum)))
print("Mike {}".format(get_Team_Position_Rank(Mike)))
print("Sam {}".format(get_Team_Position_Rank(Sam)))
print("Frank {}".format(get_Team_Position_Rank(Frank)))
print("Zach {}".format(get_Team_Position_Rank(Zach)))
