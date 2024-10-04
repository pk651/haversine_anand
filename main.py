from First_git.get_coord import get_coordinates
from First_git.compute_distance import compute_distance


if __name__ == '__main__':
    first = input("what is your first address")
    second = input("what is your second address")

    first_cord = get_coordinates(first)
    second_cord = get_coordinates(second)


    distance = compute_distance(26 rue docteur graffier, 71 avenue des Martyrs CS 20156, 38042 GRENOBLE Cedex 9 - France)

    print(f" the distance between {first} and {second} is {distance}")
