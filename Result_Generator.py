# This file defines the ReportGenerator class which generates reports based on the movie data.

import math
from result import YearReportResult, GenreReportResult, VotesReportResult


class ReportGenerator:
    def __init__(self, movies):
        self.movies = movies

    
    # 1. Report by Year (-r)
   
    def report_by_year(self, year):
        filtered = [m for m in self.movies if m.start_year == year]

        if not filtered:
            return None

        highest = max(filtered, key=lambda m: m.rating)
        lowest = min(filtered, key=lambda m: m.rating)

        avg_runtime = sum(m.runtime_minutes for m in filtered) / len(filtered)

        return YearReportResult(highest, lowest, avg_runtime)

    
    # 2. Report by Genre (-g)
    
    def report_by_genre(self, genre):
        filtered = [m for m in self.movies if genre in m.genre]

        if not filtered:
            return None

        count = len(filtered)
        avg_rating = sum(m.rating for m in filtered) / count

        return GenreReportResult(count, avg_rating)

   
    # 3. Report by Votes (-v)
    
    def report_by_votes(self, year):
        filtered = [m for m in self.movies if m.start_year == year]

        if not filtered:
            return None

        # Sort by number of votes (descending)
        sorted_movies = sorted(filtered, key=lambda m: m.num_votes, reverse=True)

        top_movies = sorted_movies[:10]

        if not top_movies:
            return None

        max_votes = top_movies[0].num_votes
        step = math.ceil(max_votes / 80)

        return VotesReportResult(top_movies, step)