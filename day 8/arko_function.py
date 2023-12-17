def sum(a,b):
    return a+b

#print calculator using function
def sum(a, b):
    return a + b

def calculator():
    print("Sagwat xa tepai lai calculator world ma")
    while True:
        try:
            num1 = float(input("Poilo number hanuhos: "))
            num2 = float(input("doshro number hanuhos: "))
            result = sum(num1, num2)
            print(f"Tepai sum of {num1} ra {num2} ko yeti vayako xa: {result}")
        except ValueError:
            print("Wrong vayako xa. Krepiya shai number halnu hos.")
        
        user_input = input("Arko calculator use garna chanu hunxa? (yes/no): ").lower()
        if user_input != 'yes':
            print("TATA see you!")
            break

calculator()
