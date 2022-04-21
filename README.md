# Author: Mimi Pieper
# Class: CS 356 Design Pattern
# Date: March 31, 2022

# Overview: 
This code provides the user with the ability to create or randomly generate an RPG character. It has a variety of species, jobs, and spells, along with the requisite stat modifiers accompaning each category. 

# Explanation of Classes Chosen:
The code is governed by interfaces for Jobs, Species, Spells, ect. It is a simple blank base format to allow each category to specify (like Species: Dwarf). 

Beneath each interface are subclasses with more specific headings and modifiers for each type.

The classes are called by the characterCreator.py file, which calls first the interface, then moves down to the specifc instances. 

The program begins in the main.py file, which contains all user/terminal interaction. From main.py characterCreator.py is called and begins the process of moving through classes.

The reason that this class structure was chosen was for ease of scalability and adaptability. The file and class format easily allow for additional Jobs, Species, ect to be added quickly, without having to change multiple instances of the information.
