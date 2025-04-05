# HW1:
In future assignments, we expect you to create the README. (Either a
README.txt, a README.md, or a README (no file extension).) We are expecting the
following three sections minimum. Please answer the questions from the
directions below.

## Usage:
- python3 hw1.py seed count max

## Examples:
- python3 hw1.py 1 100 10
- python3 hw1.py 2 100 10
- python3 hw1.py 3 1000 50

## Program description
This program performs various string functions on the text Frankenstein.

## Questions
1. What is a python list?
- A python list allows for a variable to store multiple items as data. It is zero-indexed and each item can be accessed directly with [0] after the name of the list variable: list[0] will be provide the first entry in the list. Lists are changeable, allow for duplicate values, and in python, allow for a mixture of data types. 

2. What is the time complexity of each of the following operations on a List: insertion, deletion, get
- Insert O(n), Delete O(n), Get 0(1)

3. What is a Python Dictionary?
- Dictionaries are used to store values in key:value pairs. They are changable, but do not allow duplicates, and in python versions 3.7+, they are ordered. Values are accessed with brackets: myDict['myKey'] will provide the value for the key myKey.

4. What is the time complexity of each of the following operations on a Dictionary: insertion, deletion,
get
- Insert O(1), Delete O(1), Get O(1); however worst cases can be up to O(n)