
#Function to Convert MAC Address Format

def format_mac(mac):
    return mac.upper().replace(":", "-")

print(format_mac("a1:b1:c1:d1:e1:f1"))
