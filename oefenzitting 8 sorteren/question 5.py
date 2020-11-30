def insert(tree, item):
    correct_level = False
    choices = []
    node = tree
    while not correct_level:
        iterating = True
        i = 0
        while iterating:
            el = node[i]
            if type(el) != list:
                if el == item:
                    return
                elif i == 0:  # als de node geen linker deel heeft
                    if el < item:  # als we naar rechts moeten
                        choices.append(1)
                        if len(node) > 1:  # als er een rechter deel bestaat
                            node = node[i + 1]
                        else:
                            node.append([item])
                            correct_level = True
                    else:
                        choices.append(0)
                        node.insert(0, [item])
                        correct_level = True
                else:
                    if el < item:  # als we naar rechts moeten
                        choices.append(1)
                        if len(node) > 1:  # als er een rechter deel bestaat
                            node = node[i + 1]
                        else:
                            node[i + 1] = [item]
                            correct_level = True
                    else:
                        choices.append(0)
                        node = node[0]
            i = i + 1
            if i >= len(node):
                iterating = False
    return tree


boom = [
    [[1], 2, [3]],
    4,
    [[5], 7, [9]]
]
insert(boom, 0)
print(boom)
