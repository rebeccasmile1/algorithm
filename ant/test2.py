#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def COUTING_SORT(A):
    i = 0;
    # 这里需要将使B的长度是A的长度加1，因为在第一步时，记录的位置每一个都往后移了一格
    B = [0] * (len(A)+1)
    C = [0] * (max(A)+1)
    while i < len(A):
        C[A[i]] = C[A[i]]+1
        i += 1

    i = 0;
    while i < len(C)-1:
        C[i+1] = C[i] + C[i+1]
        i += 1


    for i in range(len(A)):
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1
        i -= 1

    print(B[1:])

A = [7,5,3,0,2,3,0,3]
COUTING_SORT(A)