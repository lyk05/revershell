#!/usr/bin/env python3
from itertools import permutations 
from itertools import combinations
def findNo(n,lenOfno):
    l=[]
    comb = permutations(n, lenOfno) 
    for i in comb:
        if(i[0]!= 0):
            l.append(i[0]+i[1])
        else:
            l.append(i[1])
    print(l)    







N=int(input())
num_str=input()
nums=num_str.split(" ")
if N == len(nums):
    lenOfno=int(input())
    findNo(nums,lenOfno)
