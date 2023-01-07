test_dict = {
    "aaa": "123",
    "bbb": "456",
}

print(
    test_dict["aaa"]
)

print(test_dict.get("aaa"))
print(test_dict.get("ccc"))
print(test_dict.get("ccc", "789"))
