# CS461-Best-First-Search-Path-Finder
This is my submission for program 1, my implementation of best first search. 


# General Information
- The program to run is Program1.py.
	- Adjacencies.txt and coordinates.txt have to be in the same directory as the file for it to run correctly.
- There has been a change to coordinates.txt 
	- South Haven has been updated to have the coordinates (37.0497874 -97.4052061) instead of it's original (7.0497874 -97.4052061). 
	- Reguardless I beleve south haven is south enough that it shouldn't make a differnce if either coordinate is being used.
	- If you would like to use the original coordinates.txt file that is also fine, testing has just been done with this text file in the repo. 
- When inputting data into the python program.
	- When the program prompts the user for the start and goal cities, captalization and the number of spaces before and after the city should not have an impact as long as the city is in adjacencies.txt
	- Safest practice however should still be to spell cities as accuratly as possible.
		- i.e) Anthony, Bluff_City, Wichita
	- If a city is entered incorrectly, meaning mispelled, the program will terminate and print an error message asking you to check your input to make sure your input is spelled correctly.
- Based on the assignment description, I have made my heuristic value calculate distance from the starting node (meaning if Anthony was your first city, every distance is calculated from itself to Anthony) and we evaluate the nodes in that order. This was my interpretation of the program which I conferred with our professor before this assignment was due. 
	- i.e) If Anthony is our starting node and our goal node is on the other side of the map. We first examine Anthony, and find all of it's neighbors. We calculate all the neighbors distance from Anthony, and sort them by which neighbor is closest based on distance. If Harper is closer than Bluff_City even though Bluff_City may get us closer to our goal, we first evaluate Harper and then Bluff_City if it is next in line, and Harper doesn't have any neighbor nodes that are also closer to Anthony. 
	- And also mentioned in the doc. [To make things a bit less complex for this problem, we’re going to go one step back and implement a  best-first search, you’ll order the cities you can get to (but haven’t visited yet) by distance from your starting point.]

# Sample Run
![Program1](https://user-images.githubusercontent.com/63514033/221990611-ae756a27-65cc-4871-8288-1734877791e7.gif)
