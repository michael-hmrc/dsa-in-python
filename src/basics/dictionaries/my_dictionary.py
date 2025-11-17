
def exists(d: dict, key) -> None:
    if key in d:
        print("found")
    else:
        print("not found")
        
def exists(d: dict, key) -> bool:
    return key in d        


if __name__ == "__main__":
    
    user_dictionary = {
        "name": "Alice",
        "age": 25,
        "delete_me": "kill me"
    }
    
    print(user_dictionary["name"])
    print(user_dictionary.get("missing", 0))   # Adds a default if key does not exist, 0 (default)

    # print(user["missing"])     # key does not exist so this will crash    
    del user_dictionary["delete_me"]
    print(user_dictionary.pop("does_not_exist", None))