#------------------------------------------------------#
#         NFT Rarity Tool - Made by Jax and Anton      #
#             https://twitter.com/SolanaJax            #
#                      MIT license                     #
#                        v0.0.1                        #
#                 Discord Tag Jax#3333                 #
#------------------------------------------------------#

# Donations are not necessary but always welcomed 3NEVEHsNgzgCGgdzNpxZrH8ws1eJaUV9AAbjDag9xxCq

# Modules
import os
import json

metadata_path = r'metadata'
metadata_count = 0

file_count = 0

trait_types = []
traits = []

# Get the name of the NFT collection
with open(r'%s\%s.json' % (metadata_path, metadata_count)) as data_file:
    data = json.load(data_file)
    name_length = len(data['name'])
    collection_name = data['name'][:- 3]
    print(f'Finding The Rarity Of: "{collection_name}"')

# find the total number if metadata files
for path in os.listdir(metadata_path):
    if os.path.isfile(os.path.join(metadata_path, path)):
        metadata_count += 1
print('Metadata File Count:', metadata_count)

# Loop through all metadata files to find all types of attributes in the NFT collection
while file_count < metadata_count:
    with open(r'%s\%s.json' % (metadata_path, file_count)) as data_file:
        data = json.load(data_file)

        print(f"Finding Rarity For: {str(file_count)}.json")

        for trait_fields in data["attributes"]:
            if trait_types == []:
                print("List is empty")
                trait_types.append(trait_fields['trait_type'])

            elif trait_fields['trait_type'] == trait_types:
                print('duplicate')

            else:
                trait_types.append(trait_fields['trait_type'])

    file_count += 1
print(trait_types)
print(traits)
