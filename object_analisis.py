import json
import sys

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Functionn aboundant to find the highest total of objects by type
# Taking an object array with elements are dictionary as input                                               
# Counting the total of stars, galaxies, supernovae, frbs (assumption is fast radio burst - doublecheck)
# Return a string which is the name of the type of the which has the highest count.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def aboundant(objects):
    # asign initiate variables in one line
    sum_stars = sum_galaxies = sum_supernovae = sum_frbs = 0

    for o in objects: # number of for loops is reduced
        if o['type'] == 'star':
            sum_stars += 1
        if o['type'] == 'galaxy':
            sum_galaxies += 1
        if o['type'] == 'supernovae':
            sum_supernovae += 1
        if o['type'] == 'frb':
            sum_frbs += 1
    
    # using build-in function max and reducing logical conditions
    max_count = max(sum_stars,sum_galaxies,sum_stars,sum_supernovae,sum_frbs)
    if max_count == sum_stars:    
        return 'stars'
    if max_count == sum_galaxies:
        return 'galaxies'
    if max_count == sum_supernovae:
        return 'supernovae'
    if max_count == sum_frbs:
        return 'frbs'


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Function farthest to find the object with highest redshift
# Taking an object array with elements are dictionary as input                                               
# Return an object which has the highest redshift
# If many objects have the same highest redshift. It will return the first one to be found.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def farthest(objects):
    # initiate value is the first object is highest to reduce calculation and logical condition
    highest_redshift = None
    for o in objects:
        if (highest_redshift == None) or (o["redshift"] > highest_redshift):
            highest_redshift = o["redshift"]
    for o in objects:
        if o["redshift"] == highest_redshift:
            return o


def main():
    # Some example inputs to test funtions
    input = """
    [
        {
            "type": "star",
            "name": "alpha-centaurus",
            "redshift": 0
        },
        {
            "type": "nebula",
            "name": "crab",
            "redshift": 0
        },
        {
            "type": "galaxy",
            "name": "sombrero",
            "redshift": 0
        }
    ]
    """

    input1 = """
    [
        {
            "type": "frb",
            "name": "crab",
            "redshift": 0
        }
    ]
    """

    input2 = """
    [
        {
            "type": "frb",
            "name": "crab",
            "redshift": 0
        },
        {
            "type": "galaxy",
            "name": "sombrero",
            "redshift": 4
        }
    ]
    """

    input3 = """
    []
    """

    print(aboundant(json.loads(input)))
    print(farthest(json.loads(input)))

    # little examples 
    print(aboundant(json.loads(input1)))
    print(farthest(json.loads(input2)))
    print(aboundant(json.loads(input3)))
    print(farthest(json.loads(input3)))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    main()