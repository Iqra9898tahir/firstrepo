#while and for loops
#while loops
# x=0
# while (x<5):
#  print(x)
#  x=x+1
 #for loop
# for x in range(5,10):
#      print(x)
#array
days=["mon",'tues',"wed","thur","fri","sat","sun"]
for d in days:
    # if (d=="fri"):break #loop stops
    if(d=="fri"):continue #skips d
    print(d)
