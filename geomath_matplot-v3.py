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

# Adjusted function to arrange rectangles in a grid with gutters
def arrange_rectangles_in_grid(df, gutter=2):
    """
    Arranges rectangles in a grid layout with gutters between them, updating their x and y positions.
    """
    current_x, current_y = 0, 0
    max_row_height = 0
    for index, row in df.iterrows():
        if current_x + row['width_cm'] + gutter > 100:  # Assuming a max width of 100 units for each row
            current_x = 0
            current_y += max_row_height + gutter
            max_row_height = row['height_cm']
        df.at[index, 'x'] = current_x
        df.at[index, 'y'] = current_y
        current_x += row['width_cm'] + gutter
        max_row_height = max(max_row_height, row['height_cm'])
    return df

# Enhanced function to visualize rectangles with labels for properties
def visualize_rectangles(df):
    """
    Visualizes each rectangle with specified properties on a single canvas, including labels for each rectangle's properties.
    """
    fig, ax = plt.subplots()
    fig.set_size_inches(12, 8)
    
    for _, row in df.iterrows():
        rect = patches.Rectangle((row['x'], row['y']), row['width_cm'], row['height_cm'], linewidth=1, edgecolor='r', facecolor=row['color'], alpha=0.5)
        ax.add_patch(rect)
        label_text = f"{row['name']}\nL: {row['width_cm']}cm, H: {row['height_cm']}cm\nArea: {row['area']}cm²\nPerim: {row['perimeter']}cm\nAspect: {row['aspect_ratio']:.2f}\nDiag: {row['diagonal_length']:.2f}cm"
        plt.text(row['x'] + row['width_cm']/2, row['y'] + row['height_cm']/2, label_text, ha='center', va='center', fontsize=8, color='black', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

    plt.xlim(0, df['x'].max() + df['width_cm'].max() + 10)
    plt.ylim(0, df['y'].max() + df['height_cm'].max() + 10)
    plt.axis('off')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Function to save the visualization
def save_visualization(df, filename):
    """
    Saves the visualization as a PNG file.
    """
    visualize_rectangles(df)
    plt.savefig(filename, format='png', bbox_inches='tight')
    plt.close()

# Main function to orchestrate the steps
def main(filepath, output_filename):
    """
    Main function to read data, calculate properties, arrange in a grid with gutters, visualize, and save the image.
    """
    df = read_data(filepath)
    df = calculate_properties(df)
    df = arrange_rectangles_in_grid(df)  # Arrange the rectangles in a grid with gutters
    save_visualization(df, output_filename)

if __name__ == "__main__":
    filepath = 'rectangles.csv'  # Update this to your CSV file path
    output_filename = 'rectangles_visualization.png'
    main(filepath, output_filename)
