# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:42:11 2023

@author: eddie
"""

def search(list1,key):
    flag=False
    list2=[]
    for i in range (len(list1)):
        if key==list1[i]:
            flag=True
            list2.append(i)
            
    if flag==True:
        print("element found at index:")
        for i in list2:
            print(i)
            
    else:
        print("Element not found")
        
list1=[78,89,12,34,56,34,34]
print(list1)
key=int(input("Enter the element:"))
search(list1, key)

            