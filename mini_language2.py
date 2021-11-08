neptune = "Neptune"
n_dist = 4_498_252_900 / 1_000_000
print(f"|{neptune:^15}|\n|{n_dist:~^15,.1f}|")

"""
Type  – f defines that the value should be displayed using fixed-point notation
Precision – .1 indicates that a single decimal place should be used
Grouping – , denotes that a comma should be used as the thousand separator
Width – 15 is set as the minimum number of characters
Align – ^ defines that the value should be centered
Fill – ~ indicates that a tilde should occupy any unused space
"""
