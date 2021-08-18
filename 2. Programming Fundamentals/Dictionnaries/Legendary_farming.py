def collect_materials(dictionary_key_materials: dict, junk_materials: dict, mat: str, qty: int):
    if mat == "shards" or mat == "motes" or mat == "fragments":
        dictionary_key_materials[mat] += qty
    else:
        if mat not in junk_materials:
            junk_materials[mat] = qty
        else:
            junk_materials[mat] += qty


key_materials_dict = {'shards': 0, 'fragments': 0, "motes": 0}
junk_materials_dict = {}
item_obtained = ""
while item_obtained == "":
    command = input().split()

    for i in range(0, len(command), 2):
        quantity = int(command[i])
        material = command[i+1].lower()

        collect_materials(key_materials_dict, junk_materials_dict, material, quantity)

        if key_materials_dict['shards'] >= 250:
            item_obtained = "Shadowmourne"
            key_materials_dict["shards"] -= 250
            break
        elif key_materials_dict['motes'] >= 250:
            item_obtained = "Dragonwrath"
            key_materials_dict["motes"] -= 250
            break
        elif key_materials_dict["fragments"] >= 250:
            item_obtained = "Valanyr"
            key_materials_dict["fragments"] -= 250
            break

sorted_dict = dict(sorted(key_materials_dict.items(), key=lambda x: (-x[1], x[0])))
print(f'{item_obtained} obtained!')
for key, value in sorted_dict.items():
    print(f'{key}: {value}')

sorted_dict_junk = dict(sorted(junk_materials_dict.items(), key=lambda x: x[0]))
for key, value in sorted_dict_junk.items():
    print(f'{key}: {value}')

