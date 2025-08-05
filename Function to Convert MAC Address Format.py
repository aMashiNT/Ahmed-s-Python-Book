
#Function to Convert MAC Address Format

def format_mac(mac):
    return mac.upper().replace(":", "-")

print(format_mac("aa:bb:cc:dd:ee:ff"))
