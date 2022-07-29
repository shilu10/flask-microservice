import requests

def is_image_accessable(url): 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        }
    if url != "": 
        response = requests.get(url.strip(), headers = headers)
        return True if response.status_code == 200 else False
    return False