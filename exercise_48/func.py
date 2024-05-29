def by_to_mb(by):
    return round((by / 1048576), 2)





def percentage(list):
    total = sum(list)
    values_in_list = []
    for value in list:
        values_in_list.append(round(((value / total) * 100), 2))
    media = round((sum(list) / len(list)), 2)
    return total, values_in_list, media





