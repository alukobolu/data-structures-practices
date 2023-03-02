def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped=True
        if not swapped:
            break
def bubble_sort_dict(elements,key):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j][key] > elements[j+1][key]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped=True
        if not swapped:
            break

if __name__ =='__main__':
    #elements = [5,9,2,1,67,34,88,34]
    elements =[
        {'name':'bolu','transaction_amount':1000 ,'device':'iphone'},
        {'name':'aluko','transaction_amount':400 ,'device':'cloudiby'},
        {'name':'michael','transaction_amount':9200 ,'device':'samsung'}
    ]

    bubble_sort_dict(elements,'device')
    print(elements)