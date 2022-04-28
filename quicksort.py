
def quick_sort(sequence):
    print("**************")
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    
    print(items_lower,items_greater,pivot)
     
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([0,9,3,8,2,7,5]))