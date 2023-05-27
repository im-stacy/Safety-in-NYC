import pandas as pd
import math

# Load the dataset
df = pd.read_csv('dataset.csv', delimiter=',')

# Extract X and Y coordinates
x_coordinates = df['Latitude']
y_coordinates = df['Longitude']

# Save coordinates to a JavaScript file

with open('data.js', 'w') as f:
    x_truncated = [round(coord, 6) for coord in x_coordinates if not math.isnan(coord)]
    y_truncated = [round(coord, 6) for coord in y_coordinates if not math.isnan(coord)]
    
    f.write(f'var xCoordinates = {x_truncated};\n')
    f.write(f'var yCoordinates = {y_truncated};\n')
