#Function with Two Parameters

def ping_device(device, status):
    if status == "online":
        print("Pinging", device, "... Success!")
    else:
        print("Pinging", device, "... Failed!")

ping_device("Router1", "online")
ping_device("Switch1", "offline")
