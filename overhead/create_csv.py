import pandas as pd
# import turtle

with open("states.txt") as fp:
    states = [state[:-1] for state in fp.readlines()]

with open("x.txt") as fp:
    x = [float(num) for num in fp.readlines()]

with open("y.txt") as fp:
    y = [float(num) for num in fp.readlines()]

pd.DataFrame({
    "states" : states,
    "x" : x,
    "y" : y
}).to_csv("..\states.csv")