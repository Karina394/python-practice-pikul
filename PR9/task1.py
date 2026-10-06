full_name = " pIKUl kariNa OLEksandRivna "

parts = full_name.split()
full_name = " ".join(parts).title()

print("Full name:",full_name)
print("Length:", len(full_name))

surname, name, patronymic = full_name.split()

print("First letter of surname:", surname[0])
print("Last letter of surname:", surname[-1])
print("Surname reversed:", surname[::-1])

name_formatn = f"{surname} {name[0]}. {patronymic[0]}."
initials = f"{surname[0]}{name[0]}{patronymic[0]}"

print("Name formatted:", name_formatn)
print("Initials:", initials)

vowels = "aeiou"
vowel_count = sum(1 for char in full_name.lower() if char in vowels)
print("Number of vowels:", vowel_count)

group = "IT-32"
position = group.find("-")
print("Before hyphen:", group[:position])
print("After hyphen:", group[position + 1:])
print("After hyphen is a number:", group[position + 1:].isdigit())

login = name[0].lower() + "." + surname.lower()
email = login + "@student.edu.ua"
print("Login:", login)
print("Email:", email)
