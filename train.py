seat_numbers = [100, 102, 104, 107, 110, 113, 116, 120, 122, 124, 125, 130]
target_seat = 110
print("================================")
print("my train seat finder")
print("available seats:", seat_numbers)
print("seat to find:", target_seat)
def binary_search(seats, target):
    low = 0
    high = len(seats)- 1
    steps = 0
    while low <= high:
        steps = steps + 1
        mid = (low + high) //2
        print("checking middle seat:", seats[mid])
        if seats [mid] == target:
            return mid, steps
        elif target < seats[mid]:
            high = mid -1
        else:
            low = mid + 1
    return -1, steps
index, steps = binary_search(seat_numbers, target_seat)
print("binary search result:")
if index != -1:
    print("seat found at index")
else:
    print("seat not found")
print("steps taken:", steps)
print("Time complexity: O(log n)")
print("space complexity: O(1)")
def recursive_binary_search(seats, target, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    print("recursive_check:", seats[mid])
    if seats[mid]== target:
        return mid
    elif target < seats[mid]:
        return recursive_binary_search(seats, target, low, high, mid -1)
    else:
        return recursive_binary_search(seats, target, mid + 1, high)
recursive_index = recursive_binary_search(seat_numbers,target_seat,0,len(seat_numbers) -1)
print("Recursive binary search result:")
if recursive_index != -1:
    print("seat found at index:", recursive_index)
else:
    print("seat not found")
print("recursive time complexity: O(log n)")
print("space complexity: O(log n) because of the call stack")
print("================================")
print("complexity ladder")
print("================================")
print("O(1): Directly checking one fixed seat")
print("O(log n): Binary search by cutting the first list in half")
print("O(n): checking every seat one by one")
print("O(n^2): comparing every seat with every other seat") 
print("================================")
print("summary")
print("Binary search is faster than checking seats one by one")
print("it works only when the seat is sorted")
print("recursive binary search also uses O(log n) time")
print("However, recursion uses extra soace in the call stack")