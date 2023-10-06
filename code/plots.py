
import matplotlib
import matplotlib.pyplot as plt
import contextily as cx
import geopandas as gpd
import pandas as pd
import numpy as np
from mycolorpy import colorlist as mcp
from matplotlib import colors as mcolors
from math import pi, ceil, floor
import matplotlib.lines as mlines
import seaborn as sns






# Create function to plot radar chart of cluster centroid
def plot_radar_centroid(cl_centroid, average_centroid):

    '''
    Plot radar chart of cluster centroid

    :param cl_centroid: df of cluster centroids
    :return the radar chart of cluster centroid
    '''

    # Number of variables
    var = cl_centroid.columns
    n_var = len(var)

    # Angle of axis
    angles = [n / float(n_var) * 2 * pi for n in range(n_var)]
    angles += angles[:1]

    # Initialise the spider plot
    fig, ax = plt.subplots(figsize=(15,15))
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw ylabels
    y_min = floor(min(cl_centroid.min()))
    y_max = ceil(max(cl_centroid.max()))
    plt.ylim(y_min, y_max)

    # Plot average
    values = list(average_centroid)
    values += values[:1]
    ax.plot(angles, values, linewidth=4, color='dimgrey',
            linestyle=':', label="Average")
    
    # Plot cluster centroid
    
    colors=mcp.gen_color(cmap='viridis',n=len(cl_centroid))
    for cl in range(len(cl_centroid)):
        values = cl_centroid.iloc[cl].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values,  
                linewidth=5, marker="o", markersize=15,  color=colors[cl], label=f"Cluster {cl+1}")
        
    # Draw one axe per variable + add labels
    ax.tick_params(labelsize=24)
    ax.set_rticks([1, 2, 3])
    ax.set_rlabel_position(250)
    ax.set_xticks(angles[:-1], var)
    

    labels = []
    for label, angle in zip(ax.get_xticklabels(), angles):
        x,y = label.get_position()
        lab = ax.text(x,y, ' ', transform=label.get_transform(),
                  ha=label.get_ha(), va=label.get_va())
        lab.set_rotation(90-angle/(2*pi)*360)
        labels.append(lab)
    ax.set_xticklabels([])


    # Styling
    plt.legend(bbox_to_anchor=(1.2, 0.6), fontsize=35)

    return fig




