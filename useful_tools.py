import random

feet_in_mile = 5280
meters_in_km = 1000
beatles = ['Lennon', 'McCartney', 'Harrison', 'Starr']


def get_file_ext(filename):
    return filename[filename.index(".")+1:]


def roll_dice(num):
    no_of_faces = num
    return random.randint(1, no_of_faces)
