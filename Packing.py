#Packing


def packer(*args, **kwargs):
    print("args:", args)       # tuple of values
    print("kwargs:", kwargs)   # dict of key=value

packer(1, 2, 3, name="Ahmed", age=25)
