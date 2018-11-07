import random

#open text file
def open_file(file_name):
    with open(file_name, 'r') as infile:
        file = [line.strip() for line in infile][:120]
        return file

#divide list into smaller lists of lenght n
def chunks(list, n):
    # For item i in a range that is a length of list,
    for i in range(0, len(list), n):
        # Create an index range for list of n items:
        yield list[i:i+n]

#create all possible outcomes for given target
def create_possibilities(start_list, main_dict):
    for i in start_list[1:]:
        temp_list = ["", "", "", ""]
        temp_list[0] = i
        temp_list[1] = start_list[0]
        main_dict.setdefault(start_list.index(i), []).append(temp_list)
        temp_list = ["", "", "", ""]
        temp_list[0] = i
        temp_list[3] = start_list[0]
        main_dict.setdefault(start_list.index(i)+4, []).append(temp_list)


#create all outcomes for all targets
def all_possible_outcomes(start_list, main_dict):
    for i in start_list:
        create_possibilities(i, main_dict)

#create experiment for one person
def randomize_person(main_dict, personal_counter):
    personal_list =[]
    loop_count = 0
    while True:
        choice = random.randint(1, 8)
        if personal_counter[choice - 1] != 0:
            random.shuffle(main_dict[choice])
            personal_list.append(main_dict[choice].pop())
            personal_counter[choice - 1] -= 1
            loop_count += 1
        else:
            continue
        if loop_count >= 24:
            break
    print("personal count:", personal_counter)
    return personal_list



#open the example words
word_file = open_file("words.txt")

#cut up the list into a list of smaller lists
word_matrix = list(chunks(word_file, 5))

#size of personal counter
counter_len = ((len(word_matrix[0]))-1)*2
#create a dictionary and add all possible outcomes with their conditions as keys
possibilities_dictionary = {}
all_possible_outcomes(word_matrix, possibilities_dictionary)

print("All possible values:")
print(possibilities_dictionary)
print("\n\n")
print("Number of possibilities per condition:")
print(len(possibilities_dictionary[1]))
print("\n\n")

#create a balanced experiment
person = randomize_person(possibilities_dictionary, [3 for _ in range(counter_len)])
person_2 = randomize_person(possibilities_dictionary, [3 for _ in range(counter_len)])
person_3 = randomize_person(possibilities_dictionary, [3 for _ in range(counter_len)])
person_4 = randomize_person(possibilities_dictionary, [3 for _ in range(counter_len)])
person_5 = randomize_person(possibilities_dictionary, [3 for _ in range(counter_len)])
person_6 = randomize_person(possibilities_dictionary, [3 for _ in range(counter_len)])
person_7 = randomize_person(possibilities_dictionary, [3 for _ in range(counter_len)])
person_8 = randomize_person(possibilities_dictionary, [3 for _ in range(counter_len)])

print("\n\n")
print("Experiment for each person: ")
print("\n\n")
print(person)
print("\n\n")
print(person_2)
print("\n\n")
print(person_3)
print("\n\n")
print(person_4)
print("\n\n")
print(person_5)
print("\n\n")
print(person_6)
print("\n\n")
print(person_7)
print("\n\n")
print(person_8)
print("\n\n")
print("Remaining possible values: ")
print(possibilities_dictionary)
print("Number of possibilities per condition:")
print(len(possibilities_dictionary[1]))



