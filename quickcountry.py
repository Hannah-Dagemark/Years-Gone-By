print("name:")
c_name = input()
print("tag:")
c_tag = input()
print("def:")
c_def = input()
print("adj:")
c_adj = input()
print("colour: (r g b)")
c_colour = input()
x = 0
c_states = []
while x != 1:
    print("state:")
    inp = input()
    if inp != "end" and inp != "":
        c_states.append(inp)
    elif inp == "end":
        x = 1
print(c_states)

def common():
    count_colour_content = f"\n\n{c_tag} = {"{"}\n\tcolor = rgb {"{"} {c_colour} {"}"}\n\tcolor_ui = rgb {"{"} {c_colour} {"}"}\n{"}"}"
    file = open("./common/countries/colors.txt", "a")
    file.write(count_colour_content)
    file.close()
    file = open(f"./common/countries/{c_name}.txt", "w")
    file.write(f"#{c_name}\n\ngraphical_culture = western_european_gfx\ngraphical_culture_2d = western_european_2d\n\ncolor = {"{"} {c_colour} {"}"}")
    file.close()
    file = open("./common/country_tags/01_countries.txt", "a")
    file.write(f"\n{c_tag} = \"countries/{c_name}.txt\"")
    file.close()

def hist():
    count_hist_file = f"{c_tag.upper()} - {c_name}.txt"
    file = open("./history/countries/BTN - Bretagne.txt", "r")
    count_hist_content = file.read()
    file.close()
    file = open(f"./history/countries/{count_hist_file}", "w")
    file.write(count_hist_content)
    file.close()

def states():
    for state in c_states:
        file = open(f"./history/states/{state}-State_{state}.txt", "r")
        content = file.read()
        if "ABC" in content:
            content = content.replace("ABC", f"{c_tag}")
            file.close()
            file = open(f"./history/states/{state}-State_{state}.txt", "w")
            file.write(content)
        file.close()

def localisation():
    file = open("./localisation/english/countries_l_english.yml", "a")
    file.write(f"\n\n {c_tag}_neutrality:0 \"{c_name}\"\n {c_tag}_neutrality_DEF:0 \"{c_def}\"")
    file.write(f"\n {c_tag}_democratic:0 \"{c_name}\"\n {c_tag}_democratic_DEF:0 \"{c_def}\"")
    file.write(f"\n {c_tag}_communism:0 \"{c_name}\"\n {c_tag}_communism_DEF:0 \"{c_def}\"")
    file.write(f"\n {c_tag}_fascism:0 \"{c_name}\"\n {c_tag}_fascism_DEF:0 \"{c_def}\"")
    file.write(f"\n {c_tag}_fascism_ADJ:0 \"{c_adj}\"\n {c_tag}_democratic_ADJ:0 \"{c_adj}\"\n {c_tag}_neutrality_ADJ:0 \"{c_adj}\"\n {c_tag}_communism_ADJ:0 \"{c_adj}\"")
    file.close
        
common()
hist()
states()
localisation()