import random
import time
from datetime import datetime, timedelta

# List of sample data
users = ['alice', 'bob', 'charlie', 'dave']
actions = ['login', 'logout', 'file_download', 'file_upload', 'access_denied']
ip_addresses = ['192.168.1.{}'.format(i) for i in range(1, 101)]

# Open a file to write the log data
with open('network_traffic.log', 'a') as file:  # Use 'a' to append to the file
    while True:  # Infinite loop for continuous data generation
        timestamp = datetime.now() - timedelta(minutes=random.randint(0, 60))
        user = random.choice(users)
        action = random.choice(actions)
        ip_address = random.choice(ip_addresses)
        size = random.randint(100, 10000) if action in ['file_download', 'file_upload'] else 0

        log_entry = f"{timestamp}, {user}, {action}, {ip_address}, {size}\n"
        file.write(log_entry)
        file.flush()  # Ensure data is written to disk immediately

        # Simulate real-time log generation
        time.sleep(0.01)
