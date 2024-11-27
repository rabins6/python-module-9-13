import requests

def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json().get("value")
        print("Here's a Chuck Norris joke for you:")
        print(joke)
    else:
        print("Failed to fetch a joke. Please try again.")

# Run the function
get_random_chuck_norris_joke()