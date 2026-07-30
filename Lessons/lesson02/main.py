my_name = "Taha"
my_age = 24
my_favorite_programming_language = "IDK yet, but i guess it's going to be python"
my_dream_company = "Systems LTD"

print(f"My name is: {my_name}", f"\nMy age is: {my_age}" , "\nMy favorite programming language: " , my_favorite_programming_language, "\nMy dream company is: " , my_dream_company)
# years_until_30 = 30 - my_age
# print("Years until 30: " , years_until_30)
# print("\nData Types:\n", type(my_name), "\n", type(my_age), "\n", type(my_favorite_programming_language), "\n", type(my_dream_company))

def yearsIn30(age):
    return f"Years in 30: {30 - age}"
print(yearsIn30(int(input("Enter your age: "))))

