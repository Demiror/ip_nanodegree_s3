import html_gen
import notes

toy_story = notes.Movie("Toy Story",
                        "The Indian in the Cupboard 2",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = notes.Movie("Avatar",
                     "Pocahontas 2",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=8KAtG68bIUc")


movies = [toy_story, avatar] 
html_gen.open_movies_page(movies)
