import sys
import getopt
import hashlib
import random


#get the location of files to use
dictionary_db = input('Dictionary textfile:\t')
dictionary2_db = input('Seed textfile:\t')

#get the number of domains to generate
generate_how_much = input('Enter the amount of domains you would like to generate:\t')
if type(generate_how_much) != int:
    print "\nInvalid input!"
else:
    for x in range(0, generate_how_much) :

        def process_doc(input_doc):
            document_data = open(input_doc)
            document_data = document_data.read()
            document_data = document_data.splitlines()
            return document_data

#data files to generate entropy
        dictionary = process_doc(dictionary_db)
        hashgen_seed = process_doc(dictionary2_db)

        def split_line(input_text):
            random_word = random.choice(input_text)
            return random_word

#this will allow two seeding materials. one will return a word for hashing, the other will return a word
#to append to ensure that the IDS doesn't catch the domain
        dictionary_list = split_line(dictionary)
        hash_list = split_line(hashgen_seed)

        def hash_limit(input_to_hash):
            hash_to_cut = hashlib.sha512(input_to_hash)
            hash_to_cut = hash_to_cut.hexdigest()
            hash_to_cut = hash_to_cut[0:8]
            return hash_to_cut

        hash_list = hash_limit(hash_list)

        tlds = ['com','net','org','ru','cn','tv', 'co.uk']
        tlds = random.choice(tlds)

        generation_choice = [0, 1]
        random_choice = random.choice(generation_choice)
        if random_choice == 0:
            domain = dictionary_list + "-" + hash_list + "." + tlds
            print domain
        else:
            domain = dictionary_list + hash_list + "." + tlds
            print domain
