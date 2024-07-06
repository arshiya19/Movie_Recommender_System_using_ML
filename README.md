# Movie_Recommender_System_using_ML

1. Importing Libraries and Datasets
Import Libraries: Necessary libraries like numpy for numerical operations, pandas for data manipulation, and ast for parsing strings to lists/dictionaries are imported. These are essential for handling and transforming the data efficiently.

Load Datasets: The movies and credits datasets are loaded. These datasets contain information about movies and their respective cast/crew, which are crucial for building a recommendation system.

Data Merging
Merge Datasets: The movies and credits datasets are merged based on the title column to combine relevant information from both datasets into a single dataframe. This simplifies the data handling process and ensures all necessary information is in one place.
Data Selection
Select Relevant Columns: Only the essential columns (movie_id, title, overview, genres, keywords, cast, crew) are kept. This reduces the complexity of the dataset and focuses on the attributes necessary for creating recommendations.
Data Cleaning
Handle Missing Values: Rows with missing values are dropped to ensure data completeness and avoid errors during further processing. Missing data can lead to inaccurate recommendations.

Check for Duplicates: Duplicate rows are identified and counted to ensure data uniqueness. Duplicate data can skew the results and lead to repetitive recommendations.

Data Preprocessing
Convert JSON Columns: The JSON-like columns (genres, keywords, cast, crew) are converted into lists of strings to make them more manageable and usable for text processing and vectorization.

Extract Top 5 Cast Members: Only the top 5 cast members are kept to reduce the dimensionality of the data and focus on the most prominent actors, which are likely more relevant for recommendations.

Extract Director: The director is extracted from the crew column to add a significant attribute to the recommendation system. Directors often have a unique style that can influence recommendations.

Convert Overview to List: The overview text is split into a list of words to facilitate text processing and feature extraction. This conversion helps in creating tags for vectorization.

Remove Spaces: Spaces in the genres, keywords, cast, and crew columns are removed to prevent issues when creating tags. This ensures that multi-word attributes are treated as single entities during vectorization.

Create Tags: A new Tags column is created by concatenating the overview, genres, keywords, cast, and crew columns. This column combines all relevant textual information into a single attribute, which is used for creating a text-based similarity measure.

Text Vectorization and Similarity Calculation
Text Vectorization: The Tags text is converted into vectors using CountVectorizer, which transforms text into numerical representations. Stemming is applied to reduce words to their root form, ensuring that similar words are treated the same.

Calculate Cosine Similarity: Cosine similarity between the vectors is computed to measure the similarity between movies based on their tags. This similarity measure is the core of the recommendation algorithm, determining how closely related different movies are.

Recommendation Function
Recommendation Function: A function is defined to recommend movies based on cosine similarity. This function retrieves the most similar movies to a given movie, providing the basis for the recommendation system.
Save Models and Data
Save Data and Models: The processed data and similarity matrix are saved using pickle. This ensures that the data and model can be easily loaded and used in the web application without the need for reprocessing.
Web Application using Streamlit
Streamlit App: An interactive web application is created using Streamlit to allow users to interact with the recommendation system. Users can select a movie and get recommendations, making the system accessible and user-friendly.
This report outlines the key steps and rationale behind building a movie recommendation system, emphasizing data preparation, feature extraction, model building, and creating an interactive user interface. Each step is designed to ensure the system is accurate, efficient, and user-friendly.
