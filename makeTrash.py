def make_is_even():
    script = ""
    with open("is_even.py", "w") as f:
        
        for c in range(0, 5000):
            script += f"\nelif number == {c}:\n    print(f'Number {{number}} is even')"
        
        script += "\nelse:\n    print(f'Number {number} is not registered')\n"
        
        f.write()
        

# import json

# with open("API.json", "r") as f:
#     data = json.load(f)
    
    
# print(data)
