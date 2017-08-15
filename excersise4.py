# Subham Bhattacharjee
# 30/07/2017 10.59pm
# description: a text based adventure game.
import numpy as np;
import random;
import re

def adv():
    entry = input("Enter lenght and width (separated by commas): ");
    [n,m] = results = list(map(int, entry.split(',')))

    entry = input("Enter initial postion x,y separated by commas: ");
    [x,y] = results = list(map(int, entry.split(',')));
    [x_dash,y_dash] = x,y;
    dir = input("Enter move direction or q to quite: ");

    while (dir != 'q'):
        if(dir.isdigit()):
            dir = int(dir);
            if(dir == 8):
                y_dash += 1;
            elif(dir == 2):
                y_dash -= 1;
            elif(dir == 4):
                x_dash -=1;
            elif(dir == 6):
                x_dash += 1;
        else:
            print('wrong entry!');
        if(x_dash>n or x_dash<0 or y_dash >m or y_dash<0 ):
            [x_dash,y_dash] = [x,y]
            print('you cant go out of the map!');
        else:
            [x,y] = x_dash,y_dash;
            print("new position:" , [x,y]);
        dir = input('new entry: ');


