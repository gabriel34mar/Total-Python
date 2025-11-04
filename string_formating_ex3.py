#Tell the user the amount of points earned within the following phrase:
#"You have earned (new_points) points! In total, you have accumulated (total_points) points"
#This time, the amount of points accumulated (total_points) will be equal to the previous_points plus the new_points.

previous_points = 875
new_points = 350
total_points= previous_points+new_points
print(f"You have earned {new_points} points! In total, you have accumulated {total_points} points")