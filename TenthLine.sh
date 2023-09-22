#Given a text file file.txt, print just the 10th line of the file.

#Example:

#Assume that file.txt has the following content:

#Line 1
#Line 2
#Line 3
#Line 4
#Line 5
#Line 6
#Line 7
#Line 8
#Line 9
#Line 10
#Your script should output the tenth line, which is:

#Line 10
#Note:
#1. If the file contains less than 10 lines, what should you output?
#2. There's at least three different solutions. Try to explore all possibilities.
#!/bin/bash
# read the file into a parameter
filename="file.txt"
# check to see if there is a value in spot 10 of the file. Print out the line associated with that line.
awk '{if(NR==10) print $0}' "$filename"
