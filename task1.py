name = "Karina"
surname = "Pikul"
group = "IT-32"
city = "Kamin-Kashyrskyi"
birth_year = 2009
hobbies = ["music", "reading", "games"]

me = {
    "name": name,
    "surname": surname,
    "group": group,
    "city": city,
    "birth_year": birth_year,
    "hobbies": hobbies
}

for key, value in me.items():
    print(key, "->", value)

print("Keys:", list(me.keys()))
print("Number of pairs:", len(me))

print("Group:", me["group"])
print("Email:", me.get("email", "unknown"))

# me["email"] спричинило б KeyError, бо такого ключа ще немає.

me["email"] = "2024.pikul.karyna@ktbp.net.ua"
me["city"] = "Lutsk"

removed_year = me.pop("birth_year")
print("Removed birth year:", removed_year)

print("Dictionary after changes:")
print(me)

print("Is phone in dictionary?", "phone" in me)