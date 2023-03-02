# Henry Fundenberger
# Student ID: 16251041
# CS 461
# Spring 2023 Project 1

#---------------------------------#
# Reading from files: adjacencies.txt and coordinates.txt
with open("adjacencies.txt") as f:
    adjacencies = f.read().splitlines()

with open("coordinates.txt") as f:
    coordinates = f.read().splitlines()


adjacenciesDict = {}

# Create dictionary of adjacencies
# Key: city name
# Value: list of adjacent cities
# This is also allows us to have case insensitive input
adjacenciesDict = {}
for line in adjacencies:
    line = line.split()
    line[0] = line[0].lower()
    for i in range(1, len(line)):
        line[i] = line[i].lower()
    if line[0] not in adjacenciesDict:
        adjacenciesDict[line[0]] = []
    for i in range(1, len(line)):
        if line[i] not in adjacenciesDict:
            adjacenciesDict[line[i]] = []
        adjacenciesDict[line[0]].append(line[i])
        adjacenciesDict[line[i]].append(line[0])


# Create dictionary of coordinates
coordinatesDict = {}
# Reading in coordinates from coordinates.txt
# And creating a dictionary of coordinates
# Key: city name
# Value: list of coordinates
for line in coordinates:
    line = line.split()
    line[0] = line[0].lower()
    # set the city name as the key and the coordinates as the value (we do line[2] first because the coordinates are in the format (x, y)
    coordinatesDict[line[0]] = [line[2], line[1]]



# This helps in us the case where a city is not in coordinates.txt but is in adjacencies.txt
# So we may not know exactly where the city is, but we know it's somewhere near its neighbors
# Such as Hays and Salina, we don't know where Hays is, but we know it's somewhere near Salina
for city in adjacenciesDict:
    if city not in coordinatesDict:
        for neighbor in adjacenciesDict[city]:
            if neighbor in coordinatesDict:
                coordinatesDict[city] = coordinatesDict[neighbor]
                break

print(coordinatesDict)
# Class for a node in the graph
# Each node has a name, coordinates, start coordinates, parent, visited, and f value (where the f value is the distance from the node to the start node)
class Node:
    def __init__(self, name, coordinates, startCoordinates):
        self.name = name
        self.coordinates = coordinates
        self.startCoordinates = startCoordinates
        self.parent = None
        self.visited = False
        self.f = 0

    # Overriding the equals operator
    # Two nodes are equal if they have the same name
    def __eq__(self, other):

        return self.name == other.name

    # Overriding the less than operator
    # Two nodes are less than if they have a lower f value (lower f means closer to start node)
    def __lt__(self, other):
        return self.f < other.f

    # Overriding the string representation of the node
    # Just prints the name of the node
    def __repr__(self):
        return (slef.name )

    # Calculates the distance from the node to the goal node (in this case, the start node)
    # Uses the distance formula
    def calcGoalDistance(self):
        x1 = float(self.coordinates[0])
        y1 = float(self.coordinates[1])
        x2 = float(self.startCoordinates[0])
        y2 = float(self.startCoordinates[1])
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def bestFirstSearch():

    # Initialize OPEN and CLOSED lists
    # OPEN list is a priority queue, so we use a list and sort it 
    # (newOPEN is used to remove duplicates)
    # CLOSED list is a regular list
    OPEN = []
    newOPEN = []
    CLOSED = []

    # Get user input for start and goal cities (case insensitive )
    try: 
        startCity = input("Enter the start city: ")
        goalCity = input("Enter the goal city: ")

        # Stripping whitespace
        startCity = startCity.strip().lower()
        goalCity = goalCity.strip().lower()

        # Create start and goal nodes
        startNode = Node(startCity, coordinatesDict[startCity], coordinatesDict[startCity])
        goalNode = Node(goalCity, coordinatesDict[goalCity], coordinatesDict[startCity])

        # Add start node to OPEN list
        OPEN.append(startNode)

        # if a node in open has the same name as another node in open, remove the one with the higher f value
        for node in OPEN:
            if node not in newOPEN:
                newOPEN.append(node)
        OPEN = newOPEN



    # Error case, if the user enters a city that is not in the coordinates.txt file
    # Still if the city does not exist in the adjacencies.txt file, we can't do anything, so the program will exit
    except:

        # case if start city is in coordinates
        if startCity in adjacenciesDict and goalCity in adjacenciesDict:
            if startCity in coordinatesDict:
                startNode = Node(startCity, coordinatesDict[startCity], coordinatesDict[startCity])
                OPEN.append(startNode)
                if goalCity in coordinatesDict:
                    goalNode = Node(goalCity, coordinatesDict[goalCity], coordinatesDict[startCity])
                else:
                    goalNode = Node(goalCity, [0,0], coordinatesDict[startCity])
            # Error case, this should never happen but incase it does
            # We just assume we know nothing about the city and set its coordinates to 0,0
            else:
                # case if start city is not in coordinates but we have the adjacencies
                startNode = Node(startCity, [0,0], [0,0])
                OPEN.append(startNode)
                if goalCity in coordinatesDict:
                    goalNode = Node(goalCity, coordinatesDict[goalCity], [0,0])
           



    # Repeat until OPEN list is empty
    # OPEN list is a priority queue, so we sort it by f value every time we add a node to it
    while len(OPEN) > 0:
        newOPEN = []
        # Sort OPEN list by f value
        OPEN.sort()

        # Process of removing duplicates
        for node in OPEN:
            if node not in newOPEN:
                newOPEN.append(node)
        OPEN = newOPEN


        # Get first node in OPEN list
        currentNode = OPEN.pop(0)

        # If current node is goal node, return the currentNode (goal node) and the startNode
        if currentNode == goalNode:

            return currentNode, startNode



        # Add current node to CLOSED list
        # if a node is put
        CLOSED.append(currentNode)

        # If current node is goal node, return True

        # Expand current node to get its neighbors
        # Add neighbors to OPEN list and skip if they are already in CLOSED list
        for neighbor in adjacenciesDict[currentNode.name]:
            # case if start city is in coordinates

            try:
                # If the neighbor is in the coordinatesDict, create a node for it and add it to the OPEN list
                if neighbor in coordinatesDict:
                    # Create a node for the neighbor
                    neighborNode = Node(neighbor, coordinatesDict[neighbor], coordinatesDict[startCity])
                    # Set the parent of the neighbor node to the current node (so we can trace the path later)
                    neighborNode.parent = currentNode
                    # Calculating the heuristic value for the neighbor node (distance from neighbor to start node)
                    neighborNode.f = neighborNode.calcGoalDistance()
                    # add neighbor node to OPEN list
                    OPEN.append(neighborNode)

            except:
                pass

        
        # Make sure we don't add a node to OPEN list if it's already in CLOSED list
        for node in CLOSED:
            if node in OPEN:
                OPEN.remove(node)

    return False

# Main function to run the program
def main():
    try:
        # Call bestFirstSearch function
        goalNode, startNode = bestFirstSearch()
        # If goal node is found, print path
        if goalNode:
            print("Made it to goal node")
            path = []
            # start at goal node and work backwards to start node
            currentNode = goalNode
            while currentNode != startNode:
                # Add each node to the path list (in reverse order)
                path.append(currentNode.name)
                # Move to the parent node and repeat
                currentNode = currentNode.parent
            # Add start node to path list
            path.append(startNode.name)
            # Reverse the path list so it's in the correct order
            path.reverse()
            print("Path: ", end="")
            # For all but the last city in the path, print the city name and a comma
            for city in path[:-1]:
                print(city.title() + " -> ", end=" ")
            # For the last city in the path, print the city name and a period
            print(path[-1].title() + ".")
            print()
        # If goal node is not found, print error message
        else:
            print("No path found")
    # If an error occurs anywhere in the program that cannot be handled, print error message and exit
    except:
        print("Program terminated")
        print("Check that cities are spelled correctly or exist, capitalization does not matter")

if __name__ == "__main__":

    main()