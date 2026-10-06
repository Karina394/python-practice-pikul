about = "My name is Karina and I have two cats named Lucy and Asya"
name = "Karina"

print("Word count:", len(about.split()))
print("Longest word:", max(about.split(), key=len))
print("Reverse order:", " ".join(about.split()[::-1]))

print("Letter a count:", about.lower().count("a"))

print("Capitalized words:", " ".join(word.capitalize() for word in about.split()))
print("Underscores:", about.replace(" ", "_"))

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print("Name palindrome:", is_palindrome(name))
print("Phrase palindrome:", is_palindrome("Never odd or even"))

alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypted = ""
for char in name.lower():
    position = alphabet.find(char)
    new_position = (position + 24) % 26
    encrypted += alphabet[new_position]
print("Encrypted name:", encrypted)

decrypted = ""
for char in encrypted:
    position = alphabet.find(char)
    new_position = (position - 24) % 26
    decrypted += alphabet[new_position]
print("Decrypted name:", decrypted)