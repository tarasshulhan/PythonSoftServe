import random, copy

#open text file
def open_file(file_name):
    with open(file_name, 'r') as infile:
        file = [line.strip() for line in infile][:192]
        return file

#divide list into smaller lists of lenght n
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

#create all possible outcomes for given target
def create_possibilities(start_list):
    possiblilities = []
    for i in start_list[1:]:
        temp_list = ["", "", "", ""]
        temp_list[0] = i
        temp_list[1] = start_list[0]
        possiblilities.append(temp_list)
        temp_list = ["", "", "", ""]
        temp_list[0] = i
        temp_list[-1] = start_list[0]
        possiblilities.append(temp_list)
    return possiblilities

#create all outcomes for all targets
def all_possible_outcomes(start_list):
    all_possibilities = []
    for i in start_list:
        all_possibilities.append(create_possibilities(i))
    return all_possibilities


def randomize_person(main_list, personal_counter, master_counter):
    personal_list =[]
    loop_count = 0
    while True:
        choice = random.randint(0, len(main_list[0]) - 1)
        if personal_counter[choice] != 0 and master_counter[loop_count][choice] != 0:
            personal_list.append(main_list[loop_count][choice])
            personal_counter[choice] -= 1
            master_counter[loop_count][choice] -= 1
            loop_count += 1
        else:
            continue
        if loop_count == len(main_list):
            break
    print("personal count:", personal_counter)
    return personal_list



#open the example words
word_file = open_file("words.txt")

#cut up the list into a list of smaller lists
word_matrix = list(chunks(word_file, 5))

#create main counter matrix
Col=((len(word_matrix[0]))-1)*2
Row=len(word_matrix)
count_matrix = [[1]*Col for _ in range(Row)]

print(count_matrix)
print(len(count_matrix))
print(len(count_matrix[0]))
print("\n\n")

#create all possible outcomes for the experiment
possibilities_matrix = all_possible_outcomes(word_matrix)
#print(possibilities_matrix)
#print(len(possibilities_matrix))
#print(len(possibilities_matrix[0]))

#create a balanced experiment for one person
person = randomize_person(possibilities_matrix, [3 for _ in range(Col)], count_matrix)
person_2 = randomize_person(possibilities_matrix, [3 for _ in range(Col)], count_matrix)
person_3 = randomize_person(possibilities_matrix, [3 for _ in range(Col)], count_matrix)
person_4 = randomize_person(possibilities_matrix, [3 for _ in range(Col)], count_matrix)

#shuffle around the results
#shuffled = copy.deepcopy(person)
#random.shuffle(shuffled)

print("\n\n")
print(person)
print("\n\n")
print(person_2)
print("\n\n")
print(person_3)
print("\n\n")
print(person_4)
print("\n\n")
print(count_matrix)
print("zero count:")
print(sum(x.count(0) for x in count_matrix))
#print(shuffled)
print("\n\n")




"""
def randomize(main_list, counter):
    needed_items = len(main_list)+1
    word_list = [""]
    while len(word_list) < needed_items:

        # temporary list to store target and random prime
        temp_list = ["", "", "", ""]

        # pick random target list from main list
        random_target = random.randint(0, len(main_list) - 1)
        # pick random prime for the target
        random_prime_int = random.randint(1, 3)
        random_target_prime = main_list[random_target][random_prime_int]
        # pick random spacing amount
        random_spacing = random.choice([1, 3])

        count_pos = 0
        if random_spacing == 1:
            count_pos = random_prime_int - 1
        else:
            count_pos = random_prime_int + 2

        if(counter[random_target][count_pos]) <= 3:
                # pick random prime and put into first index of temp list
                temp_list[0] = random_target_prime
                # put target either rigth after prime or two spaces away
                temp_list[random_spacing] = main_list[random_target][0]

                # remove unnecesary trailing space
                if temp_list[-1] == '':
                    temp_list.pop(-1)

                # overlap if two double space lists are next to each other
                '''    
                if word_list[-1] != "" and temp_list[-1] != "":
                   word_list[-2] = temp_list[0]
                   temp_list = temp_list[2:]
                '''
                # add the values from the temp list to the random word list
                word_list.append(temp_list)

                # remove current index from the main list
                main_list.pop(random_target)
                counter[random_target][count_pos] += 1
        else:
            continue


    return word_list


for i in range(10):
    temp_matrix = copy.deepcopy(word_matrix)
    experiment_dict[i] = randomize(temp_matrix, count_matrix)
    del temp_matrix

print(word_matrix)
print(len(word_matrix))
print("\n\n")
print(count_matrix)
print(len(count_matrix))
print("\n\n")
print(experiment_dict)
"""
