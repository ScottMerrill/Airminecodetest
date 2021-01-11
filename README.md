# Great Circle Distance

This is a python script that calculates the air distance (great circle distance) between all pairs of places


## Installation

Make sure you have python3 installed on you machine


## Usage 
You can run the program using either the .csv file: "places.csv"
```bash
python Great_Circle_Distance.py
```

or 
using a single command-line argument (integer) to generate n random locations
```bash
python Great_Circle_Distance.py 10
```


## Example
Here is an example of what you can expect when running this script

```bash
python Great_Circle_Distance.py 5

Random Loc 0              Random Loc 2              912.00153
Random Loc 1              Random Loc 3              7235.43186
Random Loc 0              Random Loc 3              7723.51252
Random Loc 2              Random Loc 3              8576.6573
Random Loc 2              Random Loc 4              9814.1384
Random Loc 0              Random Loc 4              10653.68089
Random Loc 1              Random Loc 4              14430.48543
Random Loc 0              Random Loc 1              14886.97606
Random Loc 1              Random Loc 2              15647.5496
Random Loc 3              Random Loc 4              18364.1941
Average distance: 10824.462769 km. Closest pair: Random Loc 0 – Random Loc 2 912.00153 km.
```

The output should be:

A list of every pair combination of places, sorted by ascending distance. 

Followed by the Average distance and Closest pair.


## Author
Scott Merrill
