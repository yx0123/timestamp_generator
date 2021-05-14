import os
import argparse
import numpy as np
import pandas as pd

"""Creates times.txt file which associates a timestamp with each image file using timestamps from rgb.txt. For use with DSO. 
"""

if __name__ == "__main__":
    # E.g. In the current directory, run: python timestamp_copier.py -t rgb.txt -o pose_left.txt -f ground_truth.txt
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=str, help = 'path/to/file_with_timestamp.txt')
    #parser.add_argument('-o', '--original_poses_txt', type=str, help = 'path/to/original_poses_file.txt')
    #parser.add_argument('-f', '--output_txt', type=str, help = 'path/to/output_file.txt')
    args = parser.parse_args()
    path = args.folder+"/rgb.txt"
    print(path)

    with open(args.folder+"/rgb.txt") as f:
        with open(args.folder+"/times.txt", "w+") as f1:
            id = 0
            for line in f:
                timestamp = line.split()[0]
                #f1.write(str(id).zfill(6) + " " + titmestamp.split(".")[0]+timestamp.split(".")[1]+"\n" )
                f1.write(str(id).zfill(6) + " " + timestamp +"\n" )
                id = id+1
 
    f.close
    f1.close
    
    #print(f"Extracted timestamp (1st col.) from {args.timestamp_txt} and data from {args.original_poses_txt}. Saved to {args.folder}")

