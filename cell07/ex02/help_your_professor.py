#!/usr/bin/env python3

def average(class_scores):
    scores = class_scores.values()

    if len(class_scores) == 0:
        return 0
    
    total = sum(int(s) for s in scores)
    count = len(class_scores)
    
    return total / count

if __name__ == "__main__":
    class_3B = {
        "nudee": "17",
        "nuea": "19",
        "korkai": "15",
        "ner": "14",
        "taro": "20"
    }
    
    class_3C = {
        "justin": "20",
        "sze": "14",
        "sabrina": "16",
        "billie": "15"
    }

    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")