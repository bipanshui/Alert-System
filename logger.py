from datetime import datetime


def log(message : str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a") as f:
        f.write(f"{timestamp} - {message}")
    