#!/usr/bin/env python3

def play_with_arrays_v3():
    original = [2, 8, 9, 48, 8, 22, -12, 2]
    
    processed_list = [x + 2 for x in original if x > 5]
    
    result_set = set(processed_list)
    
    print(original)
    print(result_set)

if __name__ == "__main__":
    play_with_arrays_v3()