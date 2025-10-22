def get_total(numbers):
    return sum(numbers)

def get_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except: 
            pass
    return num