# Using while loop, if statement and str() function; iterate through the list and if there is a 100, print it with its index number
i=0
lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
while i<len(lst):
    if lst[i]==100:
        print("There is a 100 at index number"+ str(i))
    i=i+1