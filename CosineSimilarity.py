from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def CosineSimilarityFunction(str1, str2):
    """
    Compute the cosine similarity between two strings.

    Parameters:
    str1 (str): First string.
    str2 (str): Second string.

    Returns:
    float: Cosine similarity between the two strings.
    """
    # Initialize the TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the strings into TF-IDF vectors
    tfidf_matrix = vectorizer.fit_transform([str1, str2])

    # Compute the cosine similarity between the two vectors
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return similarity_matrix[0][0]


# Example usage
string1 = "I love programming in Python"
string2 = "Python programming is fun"
similarity = CosineSimilarityFunction(string1, string2)
#print(f"Cosine similarity: {similarity}")