# DAY 03

with open('advent03.txt') as input_file: # get each wire input as a seperate list
    wire_a_list = [x.strip() for x in input_file.readline().split(',')]
    wire_b_list = [x.strip() for x in input_file.readline().split(',')]
    
def graph(input_wire): # create a list of segments that represent the wire

    x = 0
    y = 0
    segments = []
    for segment in input_wire:
        direction = segment[0]
        distance = int(segment[1:])
        initial_point = (x,y)
        if direction == 'U':
            delta = (0, distance)
        elif direction == 'D':
            delta = (0, -distance)
        elif direction == 'L':
            delta = (-distance, 0)
        elif direction == 'R': 
            delta = (distance, 0)
        end_point = (initial_point[0] + delta[0], initial_point[1] + delta[1])
        x = end_point[0]
        y = end_point[1]
        segments.append((initial_point, end_point))
    return segments
graph_a = graph(wire_a_list)
graph_b = graph(wire_b_list)

'''
an intersection is when the coordinates between two points are between two other points
0,0 -> 0, 10

if x1->x2 is between x3->x4 and y1->y2 is between y3->y4
'''

intersection_points = []

for segment_a in graph_a: # for each segment, determine if the wire fits within the range of the of the segment (thus intersecting)
    lower_x_a = min(segment_a[0][0], segment_a[1][0])
    lower_y_a = min(segment_a[0][1], segment_a[1][1])
    upper_x_a = max(segment_a[0][0], segment_a[1][0])
    upper_y_a = max(segment_a[0][1], segment_a[1][1])
    for segment_b in graph_b:
        lower_x_b = min(segment_b[0][0], segment_b[1][0])
        lower_y_b = min(segment_b[0][1], segment_b[1][1])
        upper_x_b = max(segment_b[0][0], segment_b[1][0])
        upper_y_b = max(segment_b[0][1], segment_b[1][1])
        
        if lower_x_b >= lower_x_a and upper_x_b <= upper_x_a and lower_y_b <= lower_y_a and upper_y_b >= upper_y_a: # intersection
            intersection_points.append((segment_b[0][0], segment_a[0][1]))
        if lower_x_b <= lower_x_a and upper_x_b >= upper_x_a and lower_y_b >= lower_y_a and upper_y_b <= upper_y_a: # other intersection
            intersection_points.append(((segment_a[0][0], segment_b[0][1])))

distances = []
for i in intersection_points:
    distances.append(abs(i[0]) + abs(i[1]))
distances.sort()
print(distances)
print(intersection_points)

# for each step in drawing the graph, check if it instersects with one of the interection points
import math

def dist(a, b): # distance formula
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def graph_with_intersections(input_wire, intersections): # graph, but it keeps track of the distance, and has knowledge of the list of all intersections
    x = 0
    y = 0
    travel_time = 0
    intersection_travel = {}
    for segment in input_wire:
        direction = segment[0]
        distance = int(segment[1:])
        
        initial_point = (x,y)
        if direction == 'U':
            delta = (0, distance)
        elif direction == 'D':
            delta = (0, -distance)
        elif direction == 'L':
            delta = (-distance, 0)
        elif direction == 'R': 
            delta = (distance, 0)
        end_point = (initial_point[0] + delta[0], initial_point[1] + delta[1]) 
        x = end_point[0]
        y = end_point[1]
        for intersection in intersections:
            if (dist(initial_point, intersection) + dist(end_point, intersection) == dist(initial_point, end_point)): # if intersects
                intersection_travel[intersection] = int(dist(initial_point, intersection) + travel_time) # find intersection distance
        travel_time += distance
    return intersection_travel

a_travel = graph_with_intersections(wire_a_list, intersection_points)
b_travel = graph_with_intersections(wire_b_list, intersection_points)

combined_list = []
for point in a_travel:
    combined_list.append(a_travel[point] + b_travel[point])
combined_list.sort()
combined_list