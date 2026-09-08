n = 5
print("================================")
print("my running lap tracker")
print("================================")
print("number of laps:", n)
print()
formula_total = n * (n+1)//2
print("solution 1: formula method")
print("total running points:", formula_total)
print("Time complexity: O(1)")
print("space complexity: O(1)")
print()
loop_total = 0
steps_loop = 0
for lap in range(1, n +1):
    loop_total = loop_total + lap
    steps_loop = steps_loop + 1
    print("solution 2: loop method")
    print("total running points:", loop_total)
    print("steps taken:", steps_loop)
    print("Time complexity: O(n)")
    print("Space complexity: O(1)")
    print()
    nested_total = 0
    steps_nested = 0
    for lap in range (1, n +1):
        for point in range (1, lap + 1):
            nested_total = nested_total + 1
            steps_nested = steps_nested + 1
print("solution 3: nested method")
print("total running points:", nested_total)
print("steps taken:", steps_nested)
print("Time complexity O(n^2)")
print("Space complexity O(1)")
print()
print("================================")
print("algorithim efficiency comparison")
print("================================")
print("formula method: fastest as it uses only 1 calculation")
print("loop method: slower as it repeats once every loopf")
print("nested loop method: slowest as it uses a loop within another loop")
print()
print("best method: formula")
print("Reason: it has O(1) time complexity, keeping it fast even as laps increase")
print("================================")