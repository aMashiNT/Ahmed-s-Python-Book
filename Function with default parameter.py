# Function with default parameter


def ping_device(ip="192.168.1.1"):
    print("Pinging", ip, "...")
    # just simulation, no actual ping
    print("Ping successful!")

ping_device()
ping_device("8.8.8.8")
