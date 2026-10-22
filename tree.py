def make_node(value):
    return {"value": value, "left": None, "right": None}


def build():

    
    root = make_node(50)
    root["left"] = make_node(30)
    root["right"] = make_node(70)
    root["left"]["left"] = make_node(20)
    root["left"]["right"] = make_node(40)
    root["right"]["left"] = make_node(60)
    root["right"]["right"] = make_node(80)
    return root
root = build()
print(root)

def leftmost_valued_node(node):
    current = node
    while current["left"] is not None:
        current = current["left"]
    else:
        return current["value"]

print(leftmost_valued_node(root))

def rightmost_valued_node(node):
    current = node
    while current["right"] is not None:
        current = current["right"]
    else:
        return current["value"]

print(rightmost_valued_node(root))
