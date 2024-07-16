import re

# Input and output file paths
input_file_path = "./localisation/english/countries_l_english.yml"
output_file_path = "./localisation/english/countries_l_english_new.yml"

# Read the content of the input file
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Prepare a dictionary to store the tag definitions
tags = {}

# Regular expression pattern to match the lines
pattern = re.compile(r'(\w+)_neutrality:0 "(.*)"')
pattern_def = re.compile(r'(\w+)_neutrality_DEF:0 "(.*)"')

# Extract neutrality definitions
for line in lines:
    match = pattern.match(line.strip())
    if match:
        tag = match.group(1)
        name = match.group(2)
        if tag not in tags:
            tags[tag] = {'neutrality': name}

    match_def = pattern_def.match(line.strip())
    if match_def:
        tag = match_def.group(1)
        definition = match_def.group(2)
        if tag not in tags:
            tags[tag] = {}
        tags[tag]['neutrality_DEF'] = definition

# Write the new content to the output file
with open(output_file_path, 'w') as file:
    # Write original content
    for line in lines:
        file.write(line)
    
    file.write("\n\n# Additional Ideology Definitions\n\n")
    
    for tag, definitions in tags.items():
        if 'neutrality' in definitions and 'neutrality_DEF' in definitions:
            c_name = definitions['neutrality']
            c_def = definitions['neutrality_DEF']
            
            file.write("\n")  # Write a blank line for spacing
            file.write(f"{tag}_neutrality:0 \"{c_name}\"\n")
            file.write(f"{tag}_neutrality_DEF:0 \"{c_def}\"\n")
            file.write(f"{tag}_democratic:0 \"{c_name}\"\n")
            file.write(f"{tag}_democratic_DEF:0 \"{c_def}\"\n")
            file.write(f"{tag}_communism:0 \"{c_name}\"\n")
            file.write(f"{tag}_communism_DEF:0 \"{c_def}\"\n")
            file.write(f"{tag}_fascism:0 \"{c_name}\"\n")
            file.write(f"{tag}_fascism_DEF:0 \"{c_def}\"\n")
            file.write("\n")  # Write a blank line for spacing
