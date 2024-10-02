age_input=input("Please enter your age:")
age=int(age_input)

if age<18:
    age_statement="you are a Minor"
elif age>=18 and age<65:
    age_statement="you are an Adult"
else:
    age_statement="you are a Senior Citizen"

print("You are", age)
print("Therefor", age_statement)