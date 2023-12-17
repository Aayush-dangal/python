

# task
# recursion this function using recursion
# range() recursive
def number_recursive(current, end):
    if current <= end:
        print(current)
        number_recursive(current + 1, end)


number_recursive(1, 5)
