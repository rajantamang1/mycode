#!/usr/biin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
for animals in farms[0]['agriculture']:
    
        print(animals)

userInput =input("Choose a farm, NE Farm or W Farm or SE Farm: ")


