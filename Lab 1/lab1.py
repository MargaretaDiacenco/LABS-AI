import random

#tourists database

tourist1 = [0, 'two', 'eight', 'human', 'combined', 'arachnimorph']
tourist2 = [0, 'two', 'four', 'animal', 'oval', 'cowl']
tourist3 = [0, 'one', 'cipher', 'none', 'sphere', 'floating_eyeball']
tourist4 = [0, 'two', 'four', 'human', 'oval', 'gifany']
tourist5 = [0, 'zero', 'twelve', 'animal', 'combined', 'multibear']
tourist6 = [0, 'two', 'four', 'none', 'oval', 'time_baby']
tourist7 = [0, 'zero', 'two', 'human', 'hexagon', 'hectorgon']
alien = [0, 'zero', 'two', 'animal', 'combined', 'loonie']

attributes = ['sum', 'nr_of_eyes', 'nr_of_limbs', 'hair_type', 'body_shape']
list_of_creatures = [tourist1, tourist2, tourist3, tourist4, tourist5, tourist6, tourist7, alien]
inputs = []

#the system

def initial_question(i):
    print("What is their " + attributes[i] + "?")

def record_input():
    global list_of_creatures
    global creature_input
    creature_input = input() #user input
    inputs.append(creature_input)
    copy_list_of_creatures = list_of_creatures.copy()
    new_list = []
    possible_creatures = []

    result = creature_input
    for i in range(len(list_of_creatures)):
        for j in range(len(attributes)):
            if result == copy_list_of_creatures[i][j]:
                new_list.append(list_of_creatures[i])
                possible_creatures.append(list_of_creatures[i][-1]) #append to the to the last item of the list

    if len(possible_creatures) > 1:
        print("INTERMEDIATE RESULTS: I narrowed my data down to the following creatures: " + creature_input + " " + attributes[rn])
        print(possible_creatures)
    list_of_creatures = new_list
    counter()

#adds creatures to the list, if the initial attribut is ambiguous
def counter():
    for j in range(len(list_of_creatures)):
        for i in range(len(attributes)):
            if list_of_creatures[j][i] == creature_input:
                list_of_creatures[j][0] += 1

def max_sum():
    # create a dictionary of sums and creatures
    all_sums = []
    all_creatures = []

    for i in range(len(list_of_creatures)):
        all_sums.append(list_of_creatures[i][0])

    for i in range(len(list_of_creatures)):
        all_creatures.append(list_of_creatures[i][-1])

    zip_iterator = zip(all_creatures, all_sums)
    sum_dic = dict(zip_iterator)

    max_sum = [key for key in sum_dic if sum_dic[key] == max(sum_dic.values())]
    max_creature = max(sum_dic, key=sum_dic.get) #creature that fits the most

    if len(max_sum) == 1:
        print("FINAL RESULT: I think you encountered a " + max_creature + ", because you entered:")
        print(inputs)
    elif len(max_sum) == 2:
        print('It sounds like it could be either ' + max_sum[0] + ' or ' + max_sum[1])
    elif len(max_sum) >= 3:
        print('I am confused. Your info is either not enough or your creature is from a different planet')

def q_a(i):
    initial_question(i)
    record_input()

#asks until is sure
#the order of the questions is proportional to the attribute's sum
def interrogation():
    for i in range(1, len(attributes)):
        q_a(i)
    max_sum()

def if_same(i):
    lst = [item[i] for item in list_of_creatures]
    return all(x == lst[0] for x in lst)

def expert_reply():
    questions = [1, 2, 3, 4]
    global rn

    while len(list_of_creatures) > 1:
        rn = random.choice(questions)
        # narrow down the set of possible aliens every iteration by excluding fruitless questions
        if not if_same(rn):
            q_a(rn)
    max_sum()

expert_reply()   