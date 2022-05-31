
   
"""Top-level package for waterpyk."""

__author__ = """Erica McCormick"""
__email__ = "erica.elmstead@gmail.com"
__version__ = "1.1.1"

import sys
import pkg_resources
import pandas as pd

def load_data(layers):
    """Finds the import data (either all.csv or minimal.csv corresponding to layers input) and loads it.
    
    Args:
        layers (str, optional): the GEE input layers to be extracted. Options if string are 'minimal' or 'all'.
    
    Returns:
        :obj:`df`: dataframe of read csv from layers.
    """
    
    file_path = 'layers_data/' + layers + '.csv'
    stream = pkg_resources.resource_stream(__name__, file_path)
    return pd.read_csv(stream, encoding='latin-1')

def in_colab_shell():
    """Checks if code is being executed within Google Colab to decide on default_saving_dir (default saving directory path).
    Function from geemap by Qiusheng Wu
    
    Returns:
        bool
    """

    if "google.colab" in sys.modules:
        return True
    else:
        return False

if in_colab_shell():
    default_saving_dir = '/content/drive/MyDrive'
else:
    default_saving_dir = 'data/output'