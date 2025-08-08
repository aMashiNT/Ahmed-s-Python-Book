#Function to calculate network subnet size


def subnet_size(mask_bits):
    hosts = 2 ** (32 - mask_bits) - 2
    return hosts

print("Subnet /24 can have", subnet_size(24), "hosts")
print("Subnet /30 can have", subnet_size(30), "hosts")
