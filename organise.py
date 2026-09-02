print("================================")
print("smart notes organiser")
print("================================")
sample_notes =[
"Important: study\n",
"Todo: complete all homeworks\n",
"Note: read(n) review characters\n ",
"Important: submit work\n",
"skip: this line is note needed\n",
"note: readlines() stores lines in a list\n",
"Todo: practice loops with files\n"
]
file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()
print("sample file 'class-notes.txt' created")
print("\nPart 1: preview notes with read(n)")
file = open("class-notes.txt", "r")
preview = file.read(40)
file.close()
print("First 40 characters:")
print(preview)
print("\nPart 2: Read all lines with readlines()")
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
print("total lines in file:", len(lines))
for i in range (len(lines)):
    print(i + 1, "->", lines[i].strip())
print("\n Part 3: Loop through file line by line")
file = open("class-notes.txt", "r")
for line in file:
    print("Reading:",line.strip())
file.close()
print("\n Part 4: filter lines with conditions")
file = open("class-notes.txt", "r")
for line in file:
    if line.startswith("skip"):
        print("skipped:", line.strip())
    else:
        print("kept:", line.strip())
file.close()
print("\n part 5: copy selected lines to a new file")
file = open("class-notes.txt","r")
lines = file.readlines()
file.close()
output_file = open("organised-notes.txt", "r")
for line in lines:
    if line.startswith("Important") or line.startswith("Todo"):
        output_file.write(line)
output_file.close()
print("selected lines copied to 'organised-notes.txt' .")
print("\nOrganised notes:")
file = open("organised-notes.txt", "w")
for line in file:
    print("line.strip()")
file.close()
print("\n================================")
print("smart notes organiser summary")
print("================================")
print("read(n): previewed the first few characters.")
print("readlines(): stored all lines in a list.")
print("Loop: read the file line by line")
print("condition: skipped lines starting with skip.")
print("copy:saved Important and Todo lines into new file")
print("================================")