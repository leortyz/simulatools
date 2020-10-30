from pathlib import Path
import requests

def url_retrieve(url, path):
    with open(path, 'wb') as f:
        try:            
            r = requests.get(url, stream=True)
            r.raise_for_status()  # Replace this with better error handling.

            for chunk in r.iter_content(1024):
                f.write(chunk)
        except:
            print("HTTPError: 404 Client Error | Not Found url")