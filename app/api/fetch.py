import requests

def fetch():
    """
    Fetches the page content from the Uniben website.
    Returns the content of the page if successful, otherwise raises an exception.
    """
    page = requests.get("https://uniben.edu/")
    if page.status_code != 200:
        print(f'Error {page.status_code}')
        raise requests.exceptions.RequestException(f"Couldn't Fetch Page: Status code {page.status_code}")

    print(f'Page fetched successfully with status code {page.status_code}')
    return page.content
    
    
