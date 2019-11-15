
def winner(balls):
    red, black, jack = [], [], []


    for ball in balls:
        if ball["type"] == "red":
            red.append(ball["distance"][0])
            red.append(ball["distance"][-1])
        elif ball["type"] == "black":
            black.append(ball["distance"][0])
            black.append(ball["distance"][-1])
        else:
            jack.append(ball["distance"][0])
            jack.append(ball["distance"][-1])
    if abs(jack[0] - red[0]) < abs(jack[0] - black[0]):
        if jack[1] < 0 and red[1] < 0 or jack[1] > 0 and red[1] > 0:
            return "red", 1
    elif abs(jack[0] - black[0]) < abs(jack[0] - red[0]):
        if jack[1] < 0 and black[1] < 0 or jack[1] > 0 and black[1] > 0:
            return "black", 1
    else:
        return None


if __name__=="__main__":
    value = winner([{"type":"black","distance":[80,-1]},{"type":"red","distance":[85,-1]},{"type":"jack","distance":[180, 5]}])
    if value == None:
        print("No Points Scored")
    else:
        print(f"{value[0]} scores {value[1]}")