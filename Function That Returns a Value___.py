#Function That Returns a Value


def calculate_network_speed(data_size_mb, time_seconds):
    speed = data_size_mb / time_seconds
    return speed

result = calculate_network_speed(500, 50)
print(f"Network speed is {result} MB/s")
