#
#
#      0===========================================================0
#      |    TP1 Basic structures and operations on point clouds    |
#      0===========================================================0
#
#
# ------------------------------------------------------------------------------------------
#
#      First script of the practical session. Transformation of a point cloud
#
# ------------------------------------------------------------------------------------------
#
#      Hugues THOMAS - 13/12/2017
#


# ------------------------------------------------------------------------------------------
#
#          Imports and global variables
#      \**********************************/
#


# Import numpy package and name it "np"
import numpy as np

# Import functions to read and write ply files
from utils.ply import write_ply, read_ply


# ------------------------------------------------------------------------------------------
#
#           Functions
#       \***************/
#
#
#   Here you can define useful functions to be used in the main
#


# ------------------------------------------------------------------------------------------
#
#           Main
#       \**********/
#
# 
#   Here you can define the instructions that are called when you execute this file
#

if __name__ == '__main__':

    # Load point cloud
    # ****************
    #

    # Path of the file
    file_path = '../data/bunny.ply'

    # Load point cloud
    data = read_ply(file_path)

    # Concatenate x, y, and z in a (N*3) point matrix
    points = np.vstack((data['x'], data['y'], data['z'])).T

    # Concatenate R, G, and B channels in a (N*3) color matrix
    colors = np.vstack((data['red'], data['green'], data['blue'])).T

    # Get the scalar field which represent density as a vector
    density = data['scalar_density']

    # Transform point cloud
    # *********************
    #
    #   Follow the instructions step by step
    #

    # Replace this line by your code
    centroid = points.mean(axis=0)
    centered_points = points - centroid
    scaled_points = centered_points / 2

    rotation_matrix = np.array([[0, -1, 0],
                                [1, 0, 0],
                                [0, 0, 1]])
    
    rotated_points = scaled_points @ rotation_matrix

    recentered_points = rotated_points + centroid

    recentered_points[:, 1] -= 0.1

    transformed_points = recentered_points

    # Save point cloud
    # *********************
    #
    #   Save your result file
    #   (See write_ply function)
    #

    # Save point cloud
    write_ply('../little_bunny.ply', [transformed_points, colors, density], ['x', 'y', 'z', 'red', 'green', 'blue', 'density'])

    print('Done')
