quiz_scores =[91, 45, 87, 60, 67, 98, 69, 82]
print("================================")
print("quiz result researcher")
print("================================")
print("Quie scores:", quiz_scores)
first_score = quiz_scores[0]
print("Part 1: Direct access")
print("first student score:", first_score)
print("Time complexity: O(1)")
print("Theta rotatioc: Theta(1)")
print("Reason : direct access takes more than one step")
target_score = 87
steps = 0
found = False
print("part 2: linear search")
print("searching for score", target_score)
for score in quiz_scores:
    steps = steps + 1
    if score == target_score:
        found = True
        print("score found:", score)
        print("steps taken:", steps)
        break
if found == False:
    print("score not found")
    print("steps taken:", steps)
print("Best case: Omega(1)")
print("Average: O(n)")
print("Worst case: O(n)")
print("Reason: the program may need to check many scores")
print("part 3 : pair comparison")
pair_steps = 0
for scores1 in quiz_scores:
    for scores2 in quiz_scores:
        pair_steps = pair_steps + 1
print("Total pair checks:", pair_steps)
print("Time complexity O(n^2)")
print("Reason: a nested loop compares every score with every other score")
print("part 4: case comparison")
best_case_score = 45
average_case_score = 67
worst_case_score = 91
print("Best case target:", best_case_score, "-Found near the beginning")
print("Average case score:", average_case_score, "-Found around the middle")
print("Worst case score:", worst_case_score, "-Found near the end")
print("================================")
print("Asymptotic analysis summary")
print("================================")
print("O(1) direct access is faster")
print("O(n) linear search grows with the number of scores")
print("O(n^2) nested loops grow much faster")
print("Omega(1): Best case for search when the target is found first")
print("Theta(1): direct access always takes constant time")
print("Big-O shows the upper/worst-case growth")
print("================================")