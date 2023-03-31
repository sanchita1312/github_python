def get_flames_result(name1, name2):
    
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    
    set1 = set(name1)
    set2 = set(name2)

    
    common_chars = set1.intersection(set2)
    set1 = set1 - common_chars
    set2 = set2 - common_chars

    
    count = len(set1) + len(set2)

    
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(flames) > 1:
        index = count % len(flames) - 1
        if index >= 0:
            flames = flames[index+1:] + flames[:index]
        else:
            flames = flames[:len(flames)-1]
    
    return flames[0]


name1 = "Suhana"
name2 = "Aryan"
result = get_flames_result(name1, name2)
print(f"{name1} and {name2} are {result}")
