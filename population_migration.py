import numpy as np
state =["S", "T"]
transitionName = [["SS","ST"],["TS","TT"]]
transitionMatrix = [[0,400],[500,0]]
if len(transitionMatrix) == 2:
    pass
else:
    print("Error,some transitions are missing")
def pop_mig(transition):
    # Choose the starting state
    activityToday = "S"
    print("Start state: " + activityToday)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    activityList = [activityToday]
    i = 0
    prob = 0
    while i != transition:
        if activityToday == "S":
            change = np.random.choice(transitionName[0],replace=True)
            if change == "SS":
                prob = prob +0
                activityList.append("S")
                pass
            else :
                prob = prob + 400
                activityToday = "ST"
                activityList.append("T")
        elif activityToday == "T":
            change = np.random.choice(transitionName[1],replace=True)
            if change == "TS":
                prob = prob + 500
                activityList.append("S")
                pass
            else:
                prob = prob + 0
                activityToday = "TT"
                activityList.append("T")
        else:
            return -1;
        i += 1
    print("Possible states: " + str(activityList))
    print("End state after migration after "+ str(transition) + " transition: " +activityToday+" and now the population in "+ str(transition)+ " is "+ str(prob) )
pop_mig(3)