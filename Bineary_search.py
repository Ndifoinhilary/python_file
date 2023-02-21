def bineary_search(list , target):
    first = 0
    last = len(list)-1
    while first <= last:
        midpoitn = (first + last)//2
        if list[midpoitn] == target:
            return midpoitn
        elif list[midpoitn] > target:
            last = midpoitn-1
        else:
            first= midpoitn+1

list = [i for i in range(20) if i%2==0]
target= eval(input("Enter your element to search  : "))
print(bineary_search(list,target))
