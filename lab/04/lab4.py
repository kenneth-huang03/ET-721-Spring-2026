"""
Kenneth Huang
Feb 5, 2026
Lab 4 | Python Dictionary
"""

print("Example 1: Dictionary")
contacts = {
    "Bill": "718-111-2222",
    "Rick": "917-000-1111",
    "Mary": "800-222-3333",
}

print(f"Originnal Dictionary of contacts:\n{contacts}")

contacts["Rick"] = "347-000-1111"

print(f"Updated Dictionary of Contacts:\n{contacts}")

contacts["Peter"] = "888-000-1111"

print(f"Update dictionary with new KV pair:\n{contacts}")

print("Example 2: Looping through a Dictionary")
print("Print Key")
for value in contacts:
    print(value)

print("Print Value")
for value in contacts:
    print(contacts[value])

print("Print Key: Value")
for value in contacts:
    print(f"{value}'s Phone Number is {contacts[value]}")

print("Example 3: `dict`.items(), `dict`.keys(), `dict`.values()")

print(f"`dict`.items() {contacts.items()}")
print(f"`dict`.keys() {contacts.keys()}")
print(f"`dict`.values() {contacts.values()}")

print("Example 4: Checking for a key using `in`")

print(f"Is \"Jen\" a key in the dictionary? {"Jen" in contacts}")
print(f"Is \"Rick\" a key in the dictionary? {"Rick" in contacts}")

print("Example 5: `len()` of a Dictionary")

print(f"The `len()` of the Dictionary is {len(contacts)}")

print("Example 6: Remove a Key Value Pair using `dict`.pop()")

print(f"Current Dictionary of Contacts:\n{contacts}")
contacts.pop("Mary")
print(f"Updated Dictionary of Contacts:\n{contacts}")

print("Example 7: Get a value using `dict`.get()")

print(f"Using get on the Key \"Bill\": {contacts.get("Bill")}")
print(f"Using get on the Key \"Mary\": {contacts.get("Mary")}")

print("Example 8: `dict`.update()")

print(f"Current Dictionary of Contacts:\n{contacts}")
contacts.update({"Annie": "718-888-999"})
print(f"Updated Dictionary of Contacts:\n{contacts}")

