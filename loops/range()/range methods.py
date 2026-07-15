#method 1 :
for i in range(10): #stop ,default start from 0 and end at 9 (range (stop))
    print(i)
'''output :
0
1
2
3
4
5
6
7
8
9'''

#method 2 :
for i in range(3,10): # here we gave start and stop (range(start,stop))
    print(i)
'''output:
3
4
5
6
7
8
9'''


#method 3 :
for i in range(2,10,2): #range(start,stop,step) here "step" means increase the value with 
    print(i)
'''output :
2
4
6
8'''