##################################################
# Comlete your code here
##################################################

# numbers = list(map(int, input().split()))

def main():
    numbers = input().split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    print(numbers)

    ######################################################
    # Use this variable for the result
    ######################################################
    main.evenlist = []
    ######################################################

    # Code your program here

    print(main.evenlist)


if __name__ == '__main__':
    main()
