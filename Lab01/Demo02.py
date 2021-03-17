def main():
    a = 20
    print("The value of a is" , a)

    b = int(input("Enter an integer number : "))
    print("b =", b)

    c = float(input("Enter a float number : "))
    print("c =", c)

    d = b + c
    print("d = " + str(b) + " + " +  str(c) + " = ", d)

    t = "Evan"
    print(f'My name is {t}')


if __name__ == '__main__':
    main()