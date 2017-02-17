# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:28:18 2016

@author: Zach
"""




def what_grade_do_I_need():
    try:
        total=0
        categories=int(input("number of grading categories already graded:"))
        progression=0
        while progression<categories:
            grade= float(input("what grade did you get?: "))
            percent=float(input("what percent of the class is that worth?: "))
            weight=grade*percent
            total+=weight
            progression+=1
        actual_total=total*.01
        a= float(input("what grade do you want?: "))
        b=float(input("what percentage is the final worth?: "))
        goodgrade= (a-actual_total)/b
        print( goodgrade*100)
    except ValueError:
        print("Please make sure the number of categories is an integer, and all inputs are numbers")
    except ZeroDivisionError:
        print("the final cannot be worth 0 percent")
    
go_again='yes'  
    
while go_again!='no':
    what_grade_do_I_need()
    go_again=input("do you want to do another calculation?:")



