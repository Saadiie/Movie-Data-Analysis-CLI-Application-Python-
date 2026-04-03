# This file defines the Movie class to represent movie data.


class Movie:
    def __init__(
        self,
        title_type,
        original_title,
        start_year,
        runtime_minutes,
        genre,
        rating,
        num_votes
    ):
        self.title_type = title_type
        self.original_title = original_title

        self.start_year = self.safe_int(start_year)
        self.runtime_minutes = self.safe_int(runtime_minutes, 0)
        self.rating = self.safe_float(rating)
        self.num_votes = self.safe_int(num_votes, 0)

        self.genre = genre.split(",") if genre else []

    def safe_int(self, value, default=None):
        try:
            return int(value)
        except:
            return default

    def safe_float(self, value, default=0.0):
        try:
            return float(value)
        except:
            return default

    def __str__(self):
        return (
            f"{self.original_title} ({self.start_year}) | "
            f"{','.join(self.genre)} | Rating: {self.rating} | Votes: {self.num_votes}"
        )