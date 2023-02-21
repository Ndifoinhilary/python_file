def linear_search(list,target):
    for i in  range(len(list)):
        if list[i] == target:
            return i
        else:
            None
list = [i for i in range(1,20) if i%2==0]
print(linear_search(list,2))