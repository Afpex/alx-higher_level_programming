#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for item in my_list[:x]:
        if count >= x:
            break
        try:
            print("{}".format(item), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
