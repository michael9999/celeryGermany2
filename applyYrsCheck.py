    # Choose query via variable
import sys
import requests, json

    # 31/07/2019

# split string up based on how site returns data
# valueToCheck = data we are searching in
# listToCheck = data we are looking for
# returns "found" or "not found"

def applyYrsCheck(targetYrs, currYrs, pointsComp):

    
    targetYrs = 10
    currentYrs = 12

    if(targetYrs == currentYrs) or (targetYrs == currentYrs +2) or (targetYrs == currentYrs -2):
  
        print("yrs experience works")
        pointsComp = 1
  
    else:
        print("yrs don't matach")


    return pointsComp
