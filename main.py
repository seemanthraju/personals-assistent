from search_query import takeCommand
from search_query import sq



if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if query=="start":
            sq(query)
            break
    
    