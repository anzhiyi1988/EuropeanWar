unit_data = open("unit.dat", "r", encoding="utf8")
units = unit_data.readlines()

harm_data = open("harm.dat", "r", encoding="utf8")
harms = harm_data.readlines()
harm_relation = {}

for harm in harms:
    harm_infos = harm.split(" ")
    key = harm_infos[0] + harm_infos[1]
    value = harm_infos[2].replace("\n", "")
    harm_relation[key] = value

unit_relations = []
for attacker in units:
    for defender in units:
        attacker_infos = attacker.replace("\n", "").split(" ")
        defender_infos = defender.replace("\n", "").split(" ")
        name = attacker_infos[1] + "-->" + defender_infos[1]
        out = attacker_infos[2] + defender_infos[3]
        get = defender_infos[2] + attacker_infos[3]
        # print(name + ": out-" + harm_relation[out] + ";get-" + harm_relation[get] + ".")
        unit_relation = [attacker_infos[1], defender_infos[1], harm_relation[out], harm_relation[get]]
        unit_relations.append(unit_relation)

print(unit_relations)


def marger(arr, start, mid, end):
    arr1 = arr[start:mid + 1]
    arr2 = arr[mid + 1:end + 1]
    arr1.append(['站位', '站位', '0', '900'])
    arr2.append(['站位', '站位', '0', '900'])
    i = 0
    j = 0
    for k in range(start, end + 1):
        r1 = arr1[i]
        r2 = arr2[j]
        if r1[0] == r2[0] and int(r1[2]) < int(r2[2]):
            arr[k] = r2
            j = j + 1
        elif i >= len(arr1) - 1:
            arr[k] = r2
            j = j + 1
        else:
            arr[k] = r1
            i = i + 1


def sort(arr, start, end):
    if end > start:
        mid = int((end + start) / 2)
        sort(arr, start, mid)
        sort(arr, mid + 1, end)
        marger(arr, start, mid, end)


unit_relations_tmp = unit_relations.copy()
unit_relations_tmp2 = unit_relations.copy()
sort(unit_relations_tmp, 0, len(unit_relations_tmp) - 1)
print(unit_relations_tmp)


def marger2(arr, start, mid, end):
    arr1 = arr[start:mid + 1]
    arr2 = arr[mid + 1:end + 1]
    arr1.append(['站位', '站位', '0', '900'])
    arr2.append(['站位', '站位', '0', '900'])
    i = 0
    j = 0
    for k in range(start, end + 1):
        r1 = arr1[i]
        r2 = arr2[j]
        # if r1[0] == r2[0] and r1[2] == r2[2] and int(r1[3]) > int(r2[3]):
        if r1[0] == r2[0] and int(r1[3]) > int(r2[3]):
            arr[k] = r2
            j = j + 1
        elif i >= len(arr1) - 1:
            arr[k] = r2
            j = j + 1
        else:
            arr[k] = r1
            i = i + 1


def sort2(arr, start, end):
    if end > start:
        mid = int((end + start) / 2)
        sort2(arr, start, mid)
        sort2(arr, mid + 1, end)
        marger2(arr, start, mid, end)


sort2(unit_relations_tmp, 0, len(unit_relations_tmp) - 1)
print(unit_relations_tmp)

unit_relations_new = []
for unit_relation in unit_relations_tmp2:
    out = int(unit_relation[2])
    get = int(unit_relation[3])
    if out - get > 0:
        unit_relations_new.append([unit_relation[0], unit_relation[1], out - get])

print(unit_relations_new)
