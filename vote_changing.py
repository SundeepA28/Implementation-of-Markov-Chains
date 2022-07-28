import numpy as np
states =["X","Y","Z"] #Names of political parties are A , B , C
transitionName = [["XX","XY","XZ"],["YX","YY","YZ"],["ZX","ZY","ZZ"]]
if len(transitionName) == 3:
    pass
else:
    print("Error,some transitions are missing")
def vote_change(elections):
    # Choose the starting state
    Startstate = "A"
    print("Start state: " + Startstate)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    activityList = [Startstate]
    i = 0
    while i != elections:
        if Startstate == "A":
            change = np.random.choice(transitionName[0],replace=True)
            if change == "AA":
                activityList.append("A")
                pass
            elif change == "AB" :
                Startstate = "B"
                activityList.append("B")
            else:
                Startstate = "C"
                activityList.append("C")
        elif Startstate == "B":
            change = np.random.choice(transitionName[1],replace=True)
            if change == "BB":
                activityList.append("B")
                pass
            elif change == "BC" :
                Startstate = "C"
                activityList.append("C")
            else:
                Startstate = "A"
                activityList.append("A")
        elif Startstate == "C":
            change = np.random.choice(transitionName[2],replace=True)
            if change == "CC":
                activityList.append("C")
                pass
            elif change == "CA" :
                Startstate = "A"
                activityList.append("A")
            else:
                Startstate = "B"
                activityList.append("B")
        i += 1
    print("Possible states reach: " + str(activityList))
    print("After "+ str(elections) + " elections the votes were changed to party : "+Startstate)
vote_change(2)
  