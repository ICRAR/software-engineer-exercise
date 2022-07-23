import json
import sys

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


def farthest(objects):
    # initiate value is the first object is highest to reduce calculation and logical condition
    highest_redshift = objects[0]["redshift"] 
    for o in objects:
        if o["redshift"] > highest_redshift:
            highest_redshift = o["redshift"]
    for o in objects:
        if o["redshift"] == highest_redshift:
            return o


def main():
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

    print(aboundant(json.loads(input)))
    print(farthest(json.loads(input)))

    # little examples 
    print(aboundant(json.loads(input1)))
    print(farthest(json.loads(input2)))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    main()