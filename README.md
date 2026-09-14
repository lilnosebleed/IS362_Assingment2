# IS362_Assingment2
## hel
# Data Compression 
## Project Overview
This repos contains my Week 2 assignment focusing on data structures and introductory data management techniques. 
When processing information, storing long, repeating strings requires a significant amount of memory. One core method of data compression is categorical encoding. By using a dictionary data structure in Python, we can easily map long text strings to short, unique integers. 

## Included Files
code.py: this file contains the Python script demonstrating the compression logic.

## How the Code Works
The script utilizes a dictionary acting as a compression key. It takes a list of standard text data (such as academic majors) and uses a list comprehension to replace the text with corresponding integers. 
Output:
1. The original list of uncompressed text strings.
2. The final compressed list of integers.
