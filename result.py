# This file defines the result classes for the reports.


class YearReportResult:
    def __init__(self, highest, lowest, average_runtime):
        self.highest = highest
        self.lowest = lowest
        self.average_runtime = average_runtime


class GenreReportResult:
    def __init__(self, count, average_rating):
        self.count = count
        self.average_rating = average_rating


class VotesReportResult:
    def __init__(self, top_movies, step):
        self.top_movies = top_movies
        self.step = step