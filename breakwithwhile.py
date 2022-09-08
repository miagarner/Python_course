#write a while loop that stops appending items to the new list as soon as it encounters an empty string: "". And prints "There is an empty string and returns the new list."
lst=["Sam", "", "Ben", "Olivia", "Alicia"]
def name_adder(lst):
    i=0
    new_list=[]
    while i<len(lst):
        if lst[i]!="":
            new_list.append(lst[i])
        else:
            break
        i=i+1
    return new_list
print(name_adder(lst))
    