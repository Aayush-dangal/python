f=open("test.txt")
print(f.readlines()[0])
f.close()


# Task try except
try:
    with open("test.txt", "r") as f:
        lines = f.readlines()
        first_line = lines[5]
        print(first_line)
except FileNotFoundError:
    print("The file was not found.")
except IndexError:
    print("Yo file ma yeha vanda besi xoina.")
except Exception as e:
    print(f"An error occurred: {e}")




# from time import sleep
# f=open("test.txt")
# for i in range(10):
#     f.write("/Add my name")

# import function 
# from function import sum as s
# from arko_function import sum
# sleep(10)
# print(s(1,2))


# import os

# os.remove("test.txt")



# Task
# user input which File
# and creat the file
# file content should be there
# which file should be delete by user input
# and delete the file


# import os

# def create_file(file_name, content):
#     with open(file_name, 'A') as file:
#         file.write(content)

# def delete_file(file_name):
#     try:
#         os.remove(file_name)
#         print(f"The file {file_name} has been deleted.")
#     except FileNotFoundError:
#         print(f"The file {file_name} was not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def main():
#     file_name = input("Enter the name of the file to create: ")
#     file_content = input("Enter the content of the file: ")

#     create_file(file_name, file_content)
#     print(f" {file_name} vana file khuleyako xa tepaila denu vayako content ma:\n{file_content}")

#     delete_file_name = input("Enter the name of the file to delete: ")

#     delete_file(delete_file_name)
#     print(f" {delete_file_name} vana file hatayako vayko xa Dhanabhad:")

# if __name__ == "__main__":
#     main()
