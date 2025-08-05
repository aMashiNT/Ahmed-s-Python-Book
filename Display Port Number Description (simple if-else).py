# Display Port Number Description (simple if-else)

def port_description(port):
    if port == 80:
        return "HTTP - Web Traffic"
    elif port == 443:
        return "HTTPS - Secure Web Traffic"
    elif port == 22:
        return "SSH - Secure Shell"
    elif port == 21:
        return "FTP - File Transfer Protocol"
    else:
        return "Unknown or custom port"

# Test
print(port_description(22))  # SSH - Secure Shell
print(port_description(8080))  # Unknown or custom port
