import requests

def get_vaccine_data():
    url = "https://data.cdc.gov/resource/rh2h-3yt2.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error if status is 4xx/5xx
        return response.json()       # Returns the parsed JSON data
    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred:", e)
    except requests.exceptions.ConnectionError:
        print("Connection error. Check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
    return None
