import tkinter as tk

# Define the dictionary of movies with their genres
movies = {
    "The Shawshank Redemption": ["Drama"],
    "The Godfather": ["Drama", "Crime"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
    "Forrest Gump": ["Drama", "Romance"],
    "Inception": ["Action", "Adventure", "Sci-Fi"],
    "The Matrix": ["Action", "Sci-Fi"],
    "Goodfellas": ["Crime", "Drama"],
    "The Silence of the Lambs": ["Crime", "Drama", "Thriller"],
    "The Lord of the Rings: The Return of the King": ["Adventure", "Drama", "Fantasy"],
    "3 Idiots": ["Comedy", "Drama"],
    "Andhadhun": ["Crime", "Thriller"],
    "Hera Pheri": ["Comedy"],
    "Dil Chahta Hai": ["Comedy", "Drama"],
    "Golmaal": ["Comedy"],
    "Drishyam": ["Crime", "Thriller"],
    "Hindi Medium": ["Comedy", "Drama"],
    "Barfi!": ["Comedy", "Drama", "Romance"],
    "Kahaani": ["Thriller"],
    "OMG: Oh My God!": ["Comedy", "Drama"],
    "Stree": ["Comedy", "Horror"],
    "The Departed": ["Crime", "Drama", "Thriller"],
    "Interstellar": ["Adventure", "Drama", "Sci-Fi"],
    "Gladiator": ["Action", "Drama"],
    "The Prestige": ["Drama", "Mystery", "Sci-Fi"],
    "The Green Mile": ["Crime", "Drama", "Fantasy"],
    "Fight Club": ["Drama"],
    "The Pursuit of Happyness": ["Biography", "Drama"],
    "The Lion King": ["Animation", "Adventure", "Drama"],
    "The Dark Knight Rises": ["Action", "Thriller"],
    "The Godfather: Part II": ["Crime", "Drama"],
    "Forrest Gump": ["Drama", "Romance"],
    "The Intouchables": ["Biography", "Comedy", "Drama"],
    "The Usual Suspects": ["Crime", "Drama", "Mystery"],
    "The Lion King": ["Animation", "Adventure", "Drama"],
    "Schindler's List": ["Biography", "Drama", "History"],
    "The Lord of the Rings: The Fellowship of the Ring": ["Action", "Adventure", "Drama"],
    "The Lord of the Rings: The Two Towers": ["Action", "Adventure", "Drama"],
    "The Godfather: Part III": ["Crime", "Drama"],
    "The Sixth Sense": ["Drama", "Mystery", "Thriller"],
    "The Matrix Reloaded": ["Action", "Sci-Fi"],
    "The Matrix Revolutions": ["Action", "Sci-Fi"],
    "The Truman Show": ["Comedy", "Drama", "Sci-Fi"],
    "The Big Lebowski": ["Comedy", "Crime", "Sport"],
    "The Shining": ["Drama", "Horror"],
    "The Silence of the Lambs": ["Crime", "Drama", "Thriller"]
}

# Function to recommend movies based on user input
def recommend_movies(genres):
    recommended_movies = {}
    for genre in genres:
        recommended_movies[genre] = []
        for movie, movie_genres in movies.items():
            if genre.lower() in [g.lower() for g in movie_genres]:
                recommended_movies[genre].append(movie)
    return recommended_movies

# Function to handle button click event
def on_submit():
    # Get user input for preferred genres
    user_genres = entry.get().split(",")
    # Remove leading/trailing whitespaces from user input
    user_genres = [genre.strip() for genre in user_genres]
    # Get recommended movies based on user's preferred genres
    recommended_movies = recommend_movies(user_genres)
    result_text = ""
    for genre, movies in recommended_movies.items():
        if movies:
            result_text += f"\n{genre} Movies:\n" + "\n".join(movies) + "\n\n"
    if result_text:
        result.config(text=result_text, justify="left", fg="#333", font=("Arial", 12), padx=10, pady=10)
    else:
        result.config(text="No movies found with the provided genres.", justify="left", fg="#333", font=("Arial", 12), padx=10, pady=10)

# Create the main window
root = tk.Tk()
root.title("Movie Recommendation System")
root.configure(bg="#F5F5F5")

# Create and pack GUI widgets with styling
heading = tk.Label(root, text="Movie Recommendation System", bg="#F5F5F5", fg="#333", font=("Arial", 16, "bold"))
heading.pack(pady=10)

label = tk.Label(root, text="Enter your preferred genres (comma-separated):", bg="#F5F5F5", fg="#333", font=("Arial", 12))
label.pack(pady=5)

entry = tk.Entry(root, bg="#FFF", fg="#333", font=("Arial", 12))
entry.pack(ipadx=50, ipady=5)

submit_button = tk.Button(root, text="Submit", command=on_submit, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
submit_button.pack(pady=10)

result = tk.Label(root, text="", bg="#F5F5F5", fg="#333", font=("Arial", 12, "bold"), justify="left", padx=10, pady=10)
result.pack()

# Categories section
categories_label = tk.Label(root, text="Available Categories:", bg="#F5F5F5", fg="#333", font=("Arial", 12, "bold"))
categories_label.pack(pady=5)

categories_list = tk.Label(root, text="Drama, Crime, Action, Romance, Adventure, Sci-Fi, Thriller, Comedy, Horror, Animation", bg="#F5F5F5", fg="#333", font=("Arial", 12))
categories_list.pack(pady=5)

# Start the GUI event loop
root.mainloop()

