def binary_search(list, target):
    first = 0
    last = len(list) - 1
    print("Target: ", target)

    while first <= last:
        print("First: ", first)
        print("Last: ", last)
        midpoint = (first + last)//2
        print("midpoint: ", midpoint)

        if list[midpoint] == target:
            print("list = midpoint")
            return midpoint
        elif list[midpoint] < target:
            print("midpoint < target")
            first = midpoint + 1
        else:
            print("midpoint > target")
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 6)
print(result)

verify(result)
