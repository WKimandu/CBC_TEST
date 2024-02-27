import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to read the tabular data
def read_data(filepath):
    """
    Reads the rectangle data from a CSV file.
    """
    return pd.read_csv(filepath)

# Function to calculate rectangle properties
def calculate_properties(df):
    """
    Calculates area, perimeter, aspect ratio, and diagonal length for each rectangle.
    """
    df['area'] = df['height_cm'] * df['width_cm']
    df['perimeter'] = 2 * (df['height_cm'] + df['width_cm'])
    df['aspect_ratio'] = df['width_cm'] / df['height_cm']
    df['diagonal_length'] = np.sqrt(df['height_cm']**2 + df['width_cm']**2)
    return df

# New function to arrange rectangles in a grid
def arrange_rectangles_in_grid(df):
    """
    Arranges rectangles in a grid layout, updating their x and y positions.
    """
    current_x, current_y = 0, 0
    max_row_height = 0
    for index, row in df.iterrows():
        if current_x + row['width_cm'] > 100:  # Assuming a max width of 100 units for each row
            current_x = 0
            current_y += max_row_height
            max_row_height = row['height_cm']
        df.at[index, 'x'] = current_x
        df.at[index, 'y'] = current_y
        current_x += row['width_cm']
        max_row_height = max(max_row_height, row['height_cm'])
    return df

# Function to visualize rectangles
def visualize_rectangles(df):
    """
    Visualizes each rectangle with specified properties on a single canvas.
    """
    fig, ax = plt.subplots()
    # Set a larger figure size for better visibility
    fig.set_size_inches(12, 8)
    
    for _, row in df.iterrows():
        rect = patches.Rectangle((row['x'], row['y']), row['width_cm'], row['height_cm'], linewidth=1, edgecolor='r', facecolor=row['color'], label=row['name'])
        ax.add_patch(rect)
        plt.text(row['x'] + row['width_cm']/2, row['y'] + row['height_cm']/2, f"{row['name']}", ha='center', va='center', fontsize=8, color='white')

    plt.xlim(0, df['x'].max() + df['width_cm'].max() + 10)
    plt.ylim(0, df['y'].max() + df['height_cm'].max() + 10)
    plt.axis('off')  # Hide axes for a cleaner look
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Function to save the visualization
def save_visualization(df, filename):
    """
    Saves the visualization as a PNG file.
    """
    visualize_rectangles(df)
    plt.savefig(filename, format='png', bbox_inches='tight')
    plt.close()  # Close the plot to free up memory

# Main function to orchestrate the steps
def main(filepath, output_filename):
    """
    Main function to read data, calculate properties, arrange in a grid, visualize, and save the image.
    """
    df = read_data(filepath)
    df = calculate_properties(df)
    df = arrange_rectangles_in_grid(df)  # Arrange the rectangles in a grid
    save_visualization(df, output_filename)

if __name__ == "__main__":
    filepath = 'rectangles.csv'  # Update this to your CSV file path
    output_filename = 'rectangles_visualization.png'
    main(filepath, output_filename)
# The main function reads the data from the CSV file, calculates the properties of each rectangle, arranges the rectangles in a grid layout, visualizes the rectangles, and saves the visualization as a PNG file. The visualization includes the name of each rectangle and the calculated properties. The visualization is saved as a PNG file with the specified filename.