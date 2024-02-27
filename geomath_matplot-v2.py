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

# Function to visualize rectangles and save the visualization directly
def save_visualization(df, filename):
    """
    Visualizes each rectangle with specified properties on a single canvas and saves the visualization as a PNG file.
    """
    fig, ax = plt.subplots()
    # Set a larger figure size for better visibility
    fig.set_size_inches(12, 8)
    
    # Determine plot limits
    x_min, x_max = df['x'].min(), df['x'].max() + df['width_cm'].max()
    y_min, y_max = df['y'].min(), df['y'].max() + df['height_cm'].max()
    ax.set_xlim(x_min - 10, x_max + 10)
    ax.set_ylim(y_min - 10, y_max + 10)

    for _, row in df.iterrows():
        rect = patches.Rectangle((row['x'], row['y']), row['width_cm'], row['height_cm'], linewidth=1, edgecolor='r', facecolor=row['color'], alpha=0.5)  # Added alpha for overlap visibility
        ax.add_patch(rect)
        plt.text(row['x'] + row['width_cm']/2, row['y'] + row['height_cm']/2, f"{row['name']}", ha='center', va='center', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')  # Turn off the axis for a cleaner look

    # Save the figure without displaying it
    plt.savefig(filename, format='png', bbox_inches='tight')
    plt.close(fig)  # Close the plot to free up memory

# Main function to orchestrate the steps
def main(filepath, output_filename):
    """
    Main function to read data, calculate properties, and save the visualization.
    """
    df = read_data(filepath)
    df = calculate_properties(df)
    save_visualization(df, output_filename)

if __name__ == "__main__":
    filepath = 'rectangles.csv'  # Update this to your CSV file path
    output_filename = 'rectangles_visualization.png'
    main(filepath, output_filename)
