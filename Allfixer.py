import os
 
# assign directory
directory = './history/states'
amount = 3000
# iterate over files in 
# that directory
for filename in os.scandir(directory):
    if filename.is_file() and amount != 0:
        amount -= 1
        file = open(filename, "r")
        content = file.read()
        if not "history" in content:
            content_split = content.split("\n")
            if content_split[-1] == "}":
                content_split[-1] = "\thistory={"
                content_split.append("\t\tadd_core_of = ABC")
            elif content_split[-2] == "}":
                content_split[-2] = "\thistory={"
                content_split[-1] = ("\t\tadd_core_of = ABC")
            content_split.append("\t\towner = ABC")
            content_split.append("\t}")
            content_split.append("}")
            print(content, content_split)
            print("\n\n")
            file.close()
            file = open(filename, "w")
            file.write("")
            file.close()
            file = open(filename, "a")
            for x in content_split:
                file.write(f"{x}\n")
            file.close()