def count(value):
    if value % 5 == 0 and value % 3 == 0:
        print('Testing')
        return
    if value % 5 == 0:
        print('Agile')
    elif value % 3 == 0:
        print('Software')
    else:
        print(value)


if __name__ == "__main__":
    value = input('Enter a value: ')
    try:
        count(int(value))
    except ValueError:
        print('Please enter an integer value')
