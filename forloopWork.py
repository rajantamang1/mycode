#!/usr/bin/env python3

room=["biscuit", "cracker", "popcorn","biscuit"]
for biscuit in room:
    if biscuit=='biscuit':
        print("I am going to slap you")

hallway = ["toy", "tablet", "flip flop"]

for toy in hallway:
    if toy == 'toy':
        hallway.remove('toy')
        print("I am going to throw it away")

report =["A", "A", "B", "A"]
videogame=[]
version =0
for A in report:
    if A =='A':
        version +=1
        videogame.append('need for speed')
        print(f"I am going to give you videogame for your {videogame}")
