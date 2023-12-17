# def person(**details):
#     print(details)
# person(name='ram',age=12)


# home work
# add more attribute and print in proper string
def person(**details):
    if 'name' in details and 'age' in details and 'occupation' in details:
        result = f"My name is {details['name']} and I am {details['age']} years old."
        
        if 'location' in details:
            result += f" I live in {details['location']}."

        if 'occupation' in details:
            result += f" I work as a {details['occupation']}."

        print(details)
    else:
        print("Please provide both 'name' and 'age' attributes.")


person(name='Aayush', age=22, location='Kathmandu', occupation='Student')
