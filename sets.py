l1=[2,3,4,5,6,7,8,9]
l2=[1,3,5,7,9,11,13]
def union(l1,l2):
    ul=l1+l2
    ul=set(ul)
    ul=list(ul)
    return print("union of l1 and l2 is",ul)
def intersection(l1,l2):
    for i in range(len(l1)):
        il=set(l1)&set(l2)
        il=list(il)
    return print("intersection of l1 and l2 is",il)
def difference(l1,l2):
    dl=list(set(l1)-set(l2))+list(set(l2)-set(l1))
    return print("difference of l1 and l2 is",dl)
def symdiff(l1,l2):
    a=set(l1)
    b=set(l2)
    sdl=list(a.symmetric_difference(b))
    return print("symmetrical difference of l1 and l2 is",sdl)
union(l1,l2)
intersection(l1,l2)
difference(l1,l2)
symdiff(l1,l2)
