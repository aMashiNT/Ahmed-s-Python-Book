#Function That Returns Something


def get_subnet(ip):
    return ip + "/24"

subnet = get_subnet("10.0.0.1")
print("Subnet is:", subnet)
