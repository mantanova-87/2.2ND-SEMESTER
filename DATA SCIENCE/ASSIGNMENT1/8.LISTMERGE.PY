'''Write a function merge_and_sort(list1, list2) that merges two lists and returns the sorted list 
in ascending order.'''
def merge_and_sort(list1,list2):
    L3=list1+list2
    L4=sorted(L3)
    print("THE MERGED AND SORTED LIST IN ASCENDING ORDER IS: ",L4)

LIST1=eval(input("ENTER THE NUMBERS SEPARATED BY COMMAS FOR LIST 1: "))
LIST2=eval(input("ENTER THE NUMBERS SEPARATED BY COMMAS FOR LIST 2: "))
L1,L2=list(LIST1),list(LIST2)
merge_and_sort(L1,L2)
