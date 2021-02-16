import random

#tourists database

tourist1 = [0, 2, 8, 'human', 'combined', 'arachnimorph']
tourist2 = [0, 2, 4, 'animal', 'oval', 'cowl']
tourist3 = [0, 1, 0, 'none', 'sphere', 'floating_eyeball']
tourist4 = [0, 2, 4, 'human', 'oval', 'gifany']
tourist5 = [0, 16, 12, 'animal', 'combined', 'multibear']
tourist6 = [0, 2, 4, 'none', 'oval', 'time_baby']
tourist7 = [0, 0, 2, 'human', 'hexagon', 'hectorgon']
alien = [0, 0, 2, 'animal', 'combined', 'loonie']

attributes = ['sum', 'nr_of_eyes', 'nr_of_limbs', 'hair_type', 'body_shape']
list_of_creatures = [tourist1, tourist2, tourist3, tourist4, tourist5, tourist6, tourist7, alien]

inputs = []

#the system

def initial_question(i):
    print("What is their" + attributes[i] + "?")

def record_input():
    global list_of_creatures
    global creature_input
    creature_input = input()
    inputs.append(creature_input)
    copy_list_of_creatures = list_of_creatures.copy()
    new_list = []
    possible_creatures = []

    result = creature_input
    for i in range(len(list_of_creatures)):
        for j in range(len(attributes)):
            if result == copy_list_of_creatures[i][j]:
                new_list.append(list_of_creatures[i])
                possible_creatures.append(list_of_creatures[i][-1]) #append to the back of the list, to the last item

    if len(possible_creatures) > 1:
        print("INTERMEDIATE RESULTS: I narrowed my data down to the following creatures: " + creature_input + " " + attributes[rn])
        print(possible_creatures)
        list_of_creatures = new_list
        counter()

def counter():
    for j in range(len(list_of_creatures)):
        for i in range(len(attributes)):
            if list_of_creatures[j][i] == creature_input:
                list_of_creatures[j][0] += 1

def max_score():
    # create a dictionary of scores and aliens
    all_scores = []
    all_creatures = []

    for i in range(len(list_of_creatures)):
        all_scores.append(list_of_creatures[i][0])

    for i in range(len(list_of_creatures)):
        all_creatures.append(list_of_creatures[i][-1])

    