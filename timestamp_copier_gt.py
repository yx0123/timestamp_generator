import os
import argparse
import numpy as np
import pandas as pd

"""copy timestamps from rgb.txt to ground truth pose file to match TUM dataset format.
"""

if __name__ == "__main__":
    # E.g. In the current directory, run: python timestamp_copier.py -t rgb.txt -o pose_left.txt -f ground_truth.txt
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--folder', type=str, help = 'path/to/file_with_timestamp.txt')
    #parser.add_argument('-o', '--original_poses_txt', type=str, help = 'path/to/original_poses_file.txt')
    #parser.add_argument('-f', '--output_txt', type=str, help = 'path/to/output_file.txt')
    args = parser.parse_args()

    dataRGB = pd.read_csv(args.folder+"/rgb.txt", skiprows = 3, delimiter = ' ', header = None).iloc[:, 0]
    first_col_RGB = dataRGB.to_numpy().reshape(-1, 1)
    poses = np.loadtxt(args.folder+"/pose_left.txt")
    assert first_col_RGB.shape[0] == poses.shape[0], "Number of rows not the same!"

    groundtruth = np.hstack((first_col_RGB, poses))
    np.savetxt(args.folder+"/ground_truth.txt", groundtruth)
    
    #print(f"Extracted timestamp (1st col.) from {args.timestamp_txt} and data from {args.original_poses_txt}. Saved to {args.folder}")

