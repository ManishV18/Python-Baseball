import os
import glob
import pandas as pd

games_files = glob.glob(os.apth.join(os.getcwd(),'games','*.EVE'))
games_files.sort()
