import requests

def search_itunes(query, media_type="music"):
    """Search iTunes and return results in JSON format.
    
    Args:
        query (str): The search term.
        media_type (str): The type of media to search for (e.g., music, movie, podcast).
    
    Returns:
        dict: The JSON response from the iTunes API.
    """
    base_url = "https://itunes.apple.com/search"
    params = {
        "term": query,
        "media": media_type,
        "limit": 10  # Limit the number of results to 10
    }
    
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Convert the response to JSON
    else:
        response.raise_for_status()  # Raise an exception for HTTP errors
        


# Example usage
#query = "Taylor Swift"
#media_type = "music"
#results = search_itunes(query, media_type)

#print(results)