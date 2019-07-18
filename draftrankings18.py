from ffdata import *
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
Rob = {
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

print("Rob {}".format(get_Team_Position_Index(Rob)))
print("Matt {}".format(get_Team_Position_Index(Matt)))
print("Slaz {}".format(get_Team_Position_Index(Slaz)))
print("Krum {}".format(get_Team_Position_Index(Krum)))
print("Mike {}".format(get_Team_Position_Index(Mike)))
print("Sam {}".format(get_Team_Position_Index(Sam)))
print("Frank {}".format(get_Team_Position_Index(Frank)))
print("Zach {}".format(get_Team_Position_Index(Zach)))
