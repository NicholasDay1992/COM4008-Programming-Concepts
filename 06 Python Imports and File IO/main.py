from total import get_total, get_int

def main():
    print("hello world")
    numbers = [1,2,3,4,5,6,7,8]
    numbers.append(get_int("supply a number:"))
    total = get_total(numbers)
    print(total)
    
main()