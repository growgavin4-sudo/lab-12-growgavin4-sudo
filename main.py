# SearchSortLab.py
# Name:Gavin Grow
# Date:4/24/26
# Assignment: Lab 13 – Searching and Sorting


def linearSearch(data, target):
    """Return the index of target if found, otherwise return -1."""

    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def bubbleSort(data):
    """Return a sorted copy of the list using bubble sort."""

    sorted_data = data.copy()
    n = len(sorted_data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_data[j] > sorted_data[j + 1]:
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
    return sorted_data


def run_tests():
    assert linearSearch([1, 2, 3, 4, 5], 4) == 3
    assert linearSearch([1, 2, 3, 4, 5], 10) == -1
    assert bubbleSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubbleSort([3, 1, 4, 2, 5]) == [1, 2, 3, 4, 5]
    assert bubbleSort([]) == []


def main():
    # Test lists
    sortedList = [1, 2, 3, 4, 5]
    reversedList = [5, 4, 3, 2, 1]
    randomList = [3, 1, 4, 2, 5]

    # Test linear search
    print("Search for 4 in randomList:", linearSearch(randomList, 4))
    print("Search for 10 in randomList:", linearSearch(randomList, 10))

    # Test sorting
    print("Sorted list:", bubbleSort(sortedList))
    print("Reversed list sorted:", bubbleSort(reversedList))
    print("Random list sorted:", bubbleSort(randomList))


if __name__ == "__main__":
    run_tests()
    main()


if __name__ == "__main__":
    ##answers to reflection questions 
    #1. the already sorted listed (1,2,3,4,5) because the bubble sort doesnt need to swap anything.
    #2. reversed list required the most work. because every element is out of the place so bubble sort has to make the most swaps to move them into the right place.
    #3. sorting is useful because it can be faster.
    #4.linear may be useful when the list is small
    main()
