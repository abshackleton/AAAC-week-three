# write a script that will scan the filenames in the results folder 
# work out the ones that contain a gene symbol
# verify gene symbol using http://rest.genenames.org/fetch/symbol/<gene_symbol)
# use time.sleep(0.25) before calling the API to ensure you don't overload it

# import the libraries we'll need
import time
import os
import requests

# list the files that are in the results folder


current_dir = os.getcwd()
input_dir = current_dir + '\\results'

files = os.listdir(input_dir)

base_url = 'http://rest.genenames.org/fetch/'
query = 'symbol/'

additional_headers = {'Accept': 'application/json'}

filenames = []

for file in files:
    # split the filename into sections
    file_name_tokenized = file.split(" ")

    for token in file_name_tokenized:
        time.sleep(0.25)
        full_url = base_url + query + token
        r = requests.get(url=full_url, headers=additional_headers)
        data = r.json()
        if data['response']['numFound'] > 0:
            filenames.append(file)

print(filenames)