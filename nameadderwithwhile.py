#Using while loop and an if statement write a function named name_adder which appends all the elements in a list to a new list unless the element is an empty string: "".

lst=["Joe", "Sarah", "Mike", "Jess", "", "Matt","", "Greg"]
def name_adder(lst):
    i=0
    new_list=[]
    while i<len(lst):
        if lst[i]!="":
            new_list.append(lst[i])
        i=i+1
    return new_list
print(name_adder(lst))