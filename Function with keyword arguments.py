#Function with keyword arguments (**kwargs)


def display_info(**info):
    for key, value in info.items():
        print(key, ":", value)

display_info(name="Ahmed", age=25, city="Dhaka")
