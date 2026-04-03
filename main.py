# This is the main entry point for the Movie Report CLI application. 
# It handles command-line arguments,reads the movie data, and generates reports based on user input.

import argparse
import os
from Movie_Parser import MovieParser
from Result_Generator import ReportGenerator


def main():
    year_result = None
    votes_result = None
    genre_result = None
    parser = argparse.ArgumentParser(description="Movie Report CLI")

    parser.add_argument("-r", "--year", type=int, help="Report by year")
    parser.add_argument("-g", "--genre", type=str, help="Report by genre")
    parser.add_argument("-v", "--votes", type=int, help="Report by votes (year)")
    parser.add_argument("-f", "--file", type=str, help="Path to Movies CSV file")

    args = parser.parse_args()

    # File path 
    file_path = args.file or os.getenv("MOVIE_FILE") or "Movies.csv"

    if not file_path:
        print("Error: Please provide file path via --file or MOVIE_FILE.")
        return

    movie_parser = MovieParser(file_path)
    movies = movie_parser.parse()

    report_generator = ReportGenerator(movies)

    if args.year:
        year_result = report_generator.report_by_year(args.year)
        if year_result:
           print("\n=== Year Report ===\n")
           print(f"Highest rating: {year_result.highest.rating} - {year_result.highest.original_title}")
           print(f"Lowest rating: {year_result.lowest.rating} - {year_result.lowest.original_title}")
           print(f"Average mean minutes: {year_result.average_runtime:.1f}")
        else:
           print("No movies found for this year.")

    if args.genre:
        genre_result = report_generator.report_by_genre(args.genre)
        if genre_result:
            print("\n=== Genre Report ===\n")
            print(f"Movies found: {genre_result.count}")
            print(f"Average mean rating: {genre_result.average_rating:.1f}")
        else:
            print("No movies found for this genre.")

    if args.votes:
        votes_result = report_generator.report_by_votes(args.votes)

        if votes_result:
            print("\n=== Votes Report ===\n")

            for movie in votes_result.top_movies:
              likes = round(movie.num_votes / votes_result.step)
              emojis = "😀" * likes
              print(f"{movie.original_title} {emojis} {movie.num_votes}")
        else:
            print("No movies found for this votes filter.")
 

    if not (args.year or args.genre or args.votes):
        parser.error("Provide at least one option: -r, -g, or -v")


if __name__ == "__main__":
    main()