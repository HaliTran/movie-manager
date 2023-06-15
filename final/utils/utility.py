import requests
import os

API_KEY = os.environ.get('API_KEY')
API_URL = "http://www.omdbapi.com/"

def get_movie_data(query):
        """
        Wrapper to OMDB API call to retrieve information about a movie

        Parameter:
            query: dictionary object containing query parameters
        
        Required key for query dictionary:
            t: String (title of movie)
            i: String (a valid imdb ID)
            
            *Note that although both are listed as required, only provide the title OR imdb ID
        
        Optional key for query dictionary:
            type: String (valid options include -> movie, series, or episode)
            y: String (year of release)
            plot: String (valid options include -> short or full)
            r: String (valid options include -> json or xml)
        
        Returns:
            On successfully fetch of movie, a JSON response object containing information about the movie
            On failure, an error response object with an "error_message" key indicating what the error was
        """
        param = {
            "apikey": API_KEY,
            "t": query["title"],
        }
        error = {}
        try:
            response = requests.get(f"{API_URL}", params=param)
            response.raise_for_status()
            if response.status_code == 200:
                response = response.json()
            else:
                error["error_message"] = f"There was a {response.status_code} error with your request."
                return error
        except (requests.ConnectionError, requests.HTTPError, requests.Timeout, requests.TooManyRedirects) as e:
            error["error_message"] = f"There was a '{str(e)}' error with your request."
            return error
        else:
            return response