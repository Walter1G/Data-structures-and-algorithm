def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[: midpoint], target)


def verify(result):
    if result:
        print("Target found: ", result)
    else:
        print("Target not found: ", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
results1 = recursive_binary_search(numbers, 5)
results2 = recursive_binary_search(numbers, 20)
verify(results1)
verify(results2)
