#!/usr/bin/env python

import math
import numpy as np
import random
import matplotlib.pyplot as plt
import pdb

def f(x):
    return x**3

def integrate(f, a, b, n = 100):

    try:
        curve = 0
        width = (float(b - a)/ float(n))
        for i in range(n):
            curve = f(float(a) + width*i)*width + curve
        return abs(curve)

    except:
        print "Enter numbers as input"



def integrate_mc(f, a, b, (c,d), n=1000):

    if a > b:
        #a , b are bounds of integral
        low_list = []
        for i in np.arange(a,b,-0.6):
            x = f(i)
            low_list.append(x)

        c = min(low_list)
        d = max(low_list)
        #c is the lower bound
        #d is the upper bound

        #Area of rectangle
        Area = (b-a)*(d-c)

        #Take random darts and check if they are inside or out
        count = 0
        for i in range(n):
            numb_x = random.uniform(a,b)
            numb_y = random.uniform(c,d)
            if f(numb_x) > numb_y:
                count  = count + 1

        Total_area = (Area*count)/n

        #monte carlo integration
        Integral = abs(a - b)*c + Total_area
        return abs(2*Integral)


    else:
        low_list = []
        for i in np.arange(a, b, 0.05):
            x = f(i)
            low_list.append(x)

        c = min(low_list)
        d = max(low_list)
        # c is the lower bound
        # d is the upper bound

        # Area of rectangle
        Area = (b - a) * (d - c)

        # Take random darts and check if they are inside or out
        count = 0
        for i in range(n):
            numb_x = random.uniform(a, b)
            numb_y = random.uniform(c, d)
            if f(numb_x) > numb_y:
                count = count + 1

        Total_area = (Area * count) / n

        # monte carlo integration
        Integral = abs(a - b) * c + Total_area
        return abs(Integral)


def approximate_pi(n):
    #The center is at 0,0 and we know it is a unit circle. So, a = -1, b =1, c = -1, d = 1
    
    Area = (2)*2.0   #square is from -1,1 so here (b-a) = 2 and (d-c) = 2

    #Take random darts and check if they are inside or out
    count = 0
    for i in range(n):
        numb_x = random.uniform(-1,1)
        numb_y = random.uniform(-1,1)
        if ((numb_x)**2 + (numb_y)**2) < 1:
            count  = count + 1

    pi_value = (Area*count)/n
    return pi_value


# -------------------------Plotting---------------------------
def plot():
    actual_answer = 156.25
    intervals = [10, 100, 500, 1000, 5000]

    error_rie = []
    error_mc = []
    for i in intervals:
        absolute_error = abs(actual_answer - integrate(f, 0, 5, i))
        error = abs(actual_answer - integrate_mc(f,0,5,(2,3),i))
        error_rie.append(absolute_error)
        error_mc.append(error)

    plt.plot(intervals, error_rie, label = 'Riemann integral')
    plt.plot(intervals, error_mc, label = 'Monte-carlo integral')
    plt.title("Absolute Errors in approximation")
    plt.xlabel("Number of intervals")
    plt.ylabel("Error value")
    plt.legend(loc = 'best')
    plt.show()

if __name__ == '__main__':
    print integrate(f, 2, 5, 1000)
    print integrate_mc(f,2,5,(2,3),1000)
    print approximate_pi(100)
    plot()