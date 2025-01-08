# define named constants
GRAVITATIONAL_CONSTANT = 9.8

# falling_distance takes-in seconds parameter, performs a calcultation to get the distance
# and returns a value (distance)
def falling_distance(time_in_seconds):
    return 0.5 * GRAVITATIONAL_CONSTANT * time_in_seconds **2