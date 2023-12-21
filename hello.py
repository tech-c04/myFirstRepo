x = float (input ("Enter value of x :")) #float value ae like 4.09
n = int (input ("Enter value of n :")) #integer value input
s = 0     #s for calculating sum
a=0
while a<(n + 1) : # a loop 
     s += x**a    #sum of series element will be done in this line loop
     a=a+1
print ("Sum of series", s)