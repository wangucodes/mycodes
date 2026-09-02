import os

print("================================")
print("study notes organiser")
print("================================")
science_notes = [
    "plants need carbon dioxide and water",
    "The earth moves around the sun",
    "Saturn is a gas planet"
]
math_notes = [
    "addition means finding the total",
    "subtraction means taking away",
    "multiplication is repeated addition"
]
with open("science-notes.txt", "w") as f:
    f.writelines(science_notes)
with open("math-notes.txt", "w") as f:
    f.writelines(math_notes.txt)
print("simple notes files created successfully")
print("Part 1:science notes" )
with open("science-notes.txt", "r") as f:
    for line in f:
        print(line.strip)
print("part 2: word count in math notes")
with open("math-notes.txt", "r") as f:
    for line in f:
        words = line.split()
        print(len(words), "words->", line.strip())
merged_file = "all-study-notes.txt"
print("part 3: checking merged file")
if os.path.exists(merged_file):
    print(merged_file, "already exists")
else:
    print(merged_file, "does not exist")
print("part 4: remove old file")
if os.path.exists(merged_file):
    os.remove(merged_file)
    print("merged file has been removed")
else:
    print("no old merged file to remove")
print("part 5: merging files")
with open(merged_file, "w") as output:
    output.write("===science notes===")
    with open("science-notes.txt", "r") as science:
        output.write(science.read())
    output.write("===maths notes===")
    with open("maths-notes.txt", "r") as maths:
        output.write(maths.read()) 
print("science and maths notes merged successfully")
print("merged study notes:")
with open(merged_file, "r") as f:
    for line in f:
        print(line.strip())
print("================================")
print("study notes organiser summary")
print("with open() as f: used for safe file handling")
print("split(): used to count words in each line")
print("os.path.exists():used to check if the file exists")
print("os.remove(): used to delete an old file")
print("file merge: science and math notess combined to one file")
print("================================")