# This file defines the Movie class and the MovieParser class to read movie data from a CSV file.
import os
import csv
from movie import Movie


class MovieParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        movies = []
        skipped_count = 0

        def safe_int(value):
            if value in (None, "", "\\N"):
                return None
            return int(value)

        def safe_float(value):
            if value in (None, "", "\\N"):
                return None
            return float(value)

        with open(self.file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    movie = Movie(
                        title_type=row.get('titleType'),
                        original_title=row.get('originalTitle'),
                        start_year=safe_int(row.get('startYear')),
                        runtime_minutes=safe_int(row.get('runtimeMinutes')),
                        genre=row.get('genres'),
                        rating=safe_float(row.get('rating')),
                        num_votes=safe_int(row.get('numVotes'))
                    )

                    if not movie.original_title or movie.start_year is None:
                        skipped_count += 1
                        continue

                    movies.append(movie)

                except Exception:
                    skipped_count += 1
                    continue

        if skipped_count > 0:
            print(f"Skipped {skipped_count} invalid rows.")

        return movies