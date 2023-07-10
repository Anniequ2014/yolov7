import json
import os

def convert_plan_file(plan_file_path, output_file_path):
    # Read the plan file
    with open(plan_file_path, 'r') as plan_file:
        plan_data = json.load(plan_file)
    
    # Extract the waypoints from the plan data
   # xwaypoints = [(item['LatLng']['Lat'], item['LatLng']['Lng'], item['Altitude']) for item in plan_data['MissionItems']]
    waypoints = [(item['params'][4], item['params'][5], item['params'][6]) for item in plan_data['mission']['items']]    
    # Convert the waypoints to a string representation
    #waypoints_str = '\n'.join([f"{waypoint['lat']},{waypoint['lng']},{waypoint['relative_alt']}" for waypoint in waypoints])
    waypoints_str = '\n'.join([f"{waypoint[0]},{waypoint[1]},{waypoint[2]}" for waypoint in waypoints])    
    # Write the waypoints string to the output TXT file
    with open(output_file_path, 'w') as output_file:
        output_file.write(waypoints_str)

# Specify the path to the plan file and the desired output TXT file
plan_file_path = '/home/annie/Desktop/dev/yolov7/mission/mission1.plan'
output_file_path = '/home/annie/Desktop/dev/yolov7/mission/mission1wp.txt'

# Call the conversion function
convert_plan_file(plan_file_path, output_file_path)
