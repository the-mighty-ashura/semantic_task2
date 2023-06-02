import spacy

nlp = spacy.load('en_core_web_md')

def find_most_similar_movie(description):
    # Read the movies.txt file
    with open('movies.txt', 'r') as file:
        movies = file.readlines()

    max_similarity = -1
    most_similar_movie = None

    # Iterate over the movies and calculate similarity
    for movie in movies:
        movie_title, movie_description = movie.strip().split(':')
        similarity = nlp(description).similarity(nlp(movie_description))
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_movie = movie_title

    return most_similar_movie

# Example usage
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
recommended_movie = find_most_similar_movie(description)
print("Recommended Movie:", recommended_movie)
