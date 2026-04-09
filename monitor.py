from alerts import send_alert
import requests as request
import time
from config import URLS, CHECK_INTERVAL, TIMEOUT
from logger import log

def check_url(url):
    try:
        start = time.time()
        response = request.get(url, timeout=TIMEOUT)
        response_time = round(time.time() - start, 2)

        if response.status_code == 200:
            msg = f"the {url} is up ({response_time}s)"
            print(msg)
            log(msg)
        else:
            msg = f"the {url} is down ({response_time})"
            print(msg)
            send_alert(msg)    

    except request.exceptions.RequestException:     
        msg = f"the {url} is down"
        print(msg)
        log(msg)
        send_alert(msg)

def main():
    while True:
        for url in URLS:
            check_url(url)

        time.sleep(CHECK_INTERVAL)    

if __name__ == "__main__":
    main()
