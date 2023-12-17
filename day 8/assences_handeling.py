def divider():
        num1=int(input("enter the number:"))
        num2=int(input("enter the number:1"))
        if num1 ==5:
            raise Exception("input number cannot be 5")
        print(num1/num2)
while True:
    try:
        divider()
    except ZeroDivisionError:
        print("cannnot divide any number by 0")
        
    except Exception as e:
        print("somethingwant",e)