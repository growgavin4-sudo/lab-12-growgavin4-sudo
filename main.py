# SearchSortLab.py
# Name:
# Date:
# Assignment: Lab 13 – Searching and Sorting


def linearSearch(data, target):
    """Return the index of target if found, otherwise return -1."""
    
    # TODO: implement linear search
    
    return -1


def bubbleSort(data):
    """Sort the list using bubble sort and return the sorted list."""
    
    # TODO: implement bubble sort
    
    return data


def main():
    # Test lists
    sortedList = [1, 2, 3, 4, 5]
    reversedList = [5, 4, 3, 2, 1]
    randomList = [3, 1, 4, 2, 5]

    # Test linear search
    print("Search for 4 in randomList:", linearSearch(randomList, 4))
    print("Search for 10 in randomList:", linearSearch(randomList, 10))

    # Test sorting
    print("Sorted list:", bubbleSort(sortedList.copy()))
    print("Reversed list sorted:", bubbleSort(reversedList.copy()))
    print("Random list sorted:", bubbleSort(randomList.copy()))


if __name__ == "__main__":
    ##answers to reflection questions 
    #1. the already sorted listed (1,2,3,4,5) because the bubble sort doesnt need to swap anything.
    #2. reversed list required the most work. because every element is out of the place so bubble sort has to make the most swaps to move them into the right place.
    #3. sorting is useful because it can be faster.
    #4.linear may be useful when the list is small
    main()
