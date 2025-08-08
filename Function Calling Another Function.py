


def get_device_name(ip):
    return f"Device at {ip}"

def show_device_info(ip):
    name = get_device_name(ip)
    print(f"Connected: {name}")

show_device_info("192.168.0.10")
