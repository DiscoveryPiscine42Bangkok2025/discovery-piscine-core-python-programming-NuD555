#!/usr/bin/env python3
def main():
  
    try:
        user_input = input("Enter a number less than 25\n")
        number = int(user_input)

        if number > 25:
            print("Error")
        else:
            
            while number <= 25:
                print(f"Inside the loop, my variable is {number}")
                number += 1 
                
    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()