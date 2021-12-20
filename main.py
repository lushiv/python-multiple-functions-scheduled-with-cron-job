import os, sys
from os.path import dirname, join, abspath
from crontabs import Cron,Tab


def func_1():
    try:
        print("This is the Function 1 : Run :- every 30 second")
    except Exception as e:
        error =  (sys, e)
        print(error)

def func_2():
    try:
        print("This is the Function: 2 : RUN in every 1 minutes")
    except Exception as e:
        error =  (sys, e)
        print(error)


def func_3():
    try:
        print("This is the Function: 3 : RUN in every 2 minutes")
    except Exception as e:
        error =  (sys, e)
        print(error)


def func_4():
    try:
        print("This is the Function: 4 : RUN in every 3 minutes")
    except Exception as e:
        error =  (sys, e)
        print(error)
    
Cron().schedule(
    Tab(name='Fun_1').every(seconds=30).run(func_1),
    Tab(name='Fun_2').every(minutes=1).run(func_2),
    Tab(name='Fun_3').every(minutes=2).run(func_3),
    Tab(name='Fun_4').every(minutes=3).run(func_4),

).go()
