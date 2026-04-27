#!/usr/bin/env python3

def find_the_redheads(family):
    redheads_filter = filter(lambda name: family[name] == "red", family.keys())
    return list(redheads_filter)

if __name__ == "__main__":
    dupont_family = {
        "nudee": "mocca",
        "focus": "pink",
        "i-ko": "blond",
        "wawwaw": "red",
        "japan": "red",
        "zeworn": "orange",
        "field": "black",
        "so": "red"   
    }

    print(find_the_redheads(dupont_family))
    