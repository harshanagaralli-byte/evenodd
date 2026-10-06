def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    n = int(input("Enter a number: "))

    print("The number is: ", even_odd(n))