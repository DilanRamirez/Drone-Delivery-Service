"""
CS 2302 - Data Structures
Instructor: Dr. Olac Fuentes
TA: Ismael Villanueva-Miranda
Laboratory 5 - Search Algorithms
Author: Dilan Ramirez
Description:
    A company wants to establish a drone service to deliver packages from city to city. Your task is to implement
    algorithms to help them plan the set of flights that will be needed to make sure packages can be delivered from
    every city to every other city they serve while minimizing flight distances. The file cities.xlsx contains the names
    of the cities to be served and the flight distance from each pair of cities from which it is feasible to fly a drone; if
    flying a drone between two cities is not feasible, the distance appears as -1. For example, the ”drone distance”
    from El Paso to Austin is 851, from Dallas to Las Vegas it’s 1700, and it is not feasible to fly a drone from
    Laredo to San Antonio
Last Modification: Jul 30, 2019
Lab Report Link: https://drive.google.com/open?id=1XIbAf2tEQ3WEIRN2_8_agIGFESvgZEO4
"""

import disjoint_set_forest as dsf
import numpy as np
import matplotlib.pyplot as plt
import math 

def parent(i):
    return (i-1)//2

def leftChild(i):
    return 2*i + 1

def rightChild(i):
    return 2*i + 2

def HeapInsert(H,item):
    H.append(item)
    i = len(H)-1
    while i>0 and item[-1] < H[parent(i)][-1]:
        H[i] = H[parent(i)]
        i = parent(i)
    H[i] = item
        
def ExtractMin(H):
    if len(H) <1:
        return None
    if len(H) ==1:
        return H.pop()
    root = H[0]
    p = H.pop()
    i = 0
    while True:
        L = np.zeros(3)+math.inf
        L[0] = p[-1]
        if leftChild(i) <len(H):
            L[1] = H[leftChild(i)][-1]
            if rightChild(i) <len(H):
                L[2] = H[rightChild(i)][-1]
        m = np.argmin(L)
        if m == 0: #  Parent is smaller that both children
            H[i] = p
            break
        elif m == 1:
            H[i] = H[leftChild(i)]
            i = leftChild(i)
        else:
            H[i] = H[rightChild(i)] 
            i = rightChild(i)
    return root   

def kruskal(G): # O(|E| log |E|)
    MST = [[] for i in range(len(G))]
    H=[]
    #Insert all edges in heap
    for i in range(len(G)):
        for eg in G[i]:
            if i<eg[0]:
                HeapInsert(H,[i,eg[0],eg[1]]) 
    S = dsf.dsf(len(G))
    n = 0
    while True:
        eg = ExtractMin(H)
        u = dsf.union(S,eg[0],eg[1])
        #print(eg)
        if u==1: # eg does not create a cycle
            MST[eg[0]].append([eg[1],eg[2]])
            MST[eg[1]].append([eg[0],eg[2]])
        n+=u
        if n == len(G)-1:
            return MST
        if len(H)==0:
            return None

        
        
if __name__ == "__main__":  
    plt.close("all")   


    