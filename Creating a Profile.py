#Creating a Profile

def creating_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()} : {value}")
    

creating_profile(name="Ahmed", age=29, city="Chittagong")  
