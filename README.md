# timestamp_generator

When writing the scripts for the project, I assumed that we will run both orb slam and dso. Hence, only `create_timestamps_orb.py` creates the timestamp based on input frequency. The other two scripts will extract the timestamps from `rgb.txt`. Examples on how to run the scripts can be found below. 

For `create_timestamps_orb.py`
```
 python create_timestamps_orb.py 10 ~/16-833-Project-Datasets/eow_easy_P002/P002/image_left
```

For `create_timestamps_dso.py`
```
python create_timestamps_dso.py ~/16-833-Project-Datasets/eow_easy_P002/P002/
```

For `timestamp_copier_gt.py`
```
python timestamp_copier.py -t ~/16-833-Project-Datasets/eow_easy_P002/P002/
```


