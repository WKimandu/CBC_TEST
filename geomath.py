import os
import sys
import json
from collections import OrderedDict
import drawio
import drawio
#Generate a Python script that performs the following tasks:

#Generate a Python script that performs the following tasks:

def read_data(file):
    # Read the data from the file
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append(line.strip().split('\t'))
    return data

def calculate_properties(data):
    # Calculate the properties of each rectangle
    properties = []
    for row in data:
        height = float(row[0])
        width = float(row[1])
        x = float(row[2])
        y = float(row[3])
        color = row[4]
        name = row[5]
        area = height * width
        perimeter = 2 * (height + width)
        aspect_ratio = width / height
        diagonal_length = (height**2 + width**2)**0.5
        properties.append([name, height, width, x, y, color, area, perimeter, aspect_ratio, diagonal_length])
    return properties

def visualize_rectangles(properties, output_file):
    # Visualize the rectangles and save the image
    canvas = drawio.Canvas()
    for prop in properties:
        name, height, width, x, y, color, area, perimeter, aspect_ratio, diagonal_length = prop
        rect = drawio.Rectangle(x, y, width, height, color)
        canvas.add(rect)
        canvas.add(drawio.Text(name, x + width/2, y + height/2))
        canvas.add(drawio.Text("Area: {:.2f}".format(area), x + width/2, y + height/2 + 10))
        canvas.add(drawio.Text("Perimeter: {:.2f}".format(perimeter), x + width/2, y + height/2 + 20))
        canvas.add(drawio.Text("Aspect Ratio: {:.2f}".format(aspect_ratio), x + width/2, y + height/2 + 30))
        canvas.add(drawio.Text("Diagonal Length: {:.2f}".format(diagonal_length), x + width/2, y + height/2 + 40)
)
    canvas.save(output_file)

def main(input_file, output_file):
    data = read_data(input_file)
    # Skip the first line (column headers)
    data = data[1:]
    properties = calculate_properties(data)
    visualize_rectangles(properties, output_file)

if __name__ == "__main__":
    main("rectangles.txt", "output.png")

# Run the script with the provided example data and verify that the output image file is