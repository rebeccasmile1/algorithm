'''
Description

There are Infinite People Standing in a row, indexed from 1.A person having index 'i' has strength of (i*i).You have Strength 'P'. You need to tell what is the maximum number of People You can Kill With your Strength P.You can only Kill a person with strength 'X' if P >= 'X' and after killing him, Your Strength decreases by 'X'.


Input

First line contains an integer 'T' - the number of testcases,Each of the next 'T' lines contains an integer 'P'- Your Power.Constraints:1<=T<=100001<=P<=1000000000000000


Output



'''

import math
def killx():
    num=int(input())
    if num<1 or num>100001:
        return
    for i in range(num):
        P=int(input())
        if P<1 or P>1000000000000000:
            break

        for j in range(1,P):
            sum=(j*(j+1)*(2*j+1)//6)
            # print(j)
            if sum>P:
                break
        print(j-1)

if __name__ == '__main__':
    killx()