import sys

import pandas


def movies_choose(genre):
    df = pandas.read_csv("dags/fixtures/movies.csv")
    filter_by_movie_genre = df["Genre"] == genre
    row = df[filter_by_movie_genre].sample().astype(str)
    return ",".join(row.values.flatten().tolist())


if __name__ == "__main__":
    genre = sys.argv[1]
    sys.stdout.write(movies_choose(genre=genre))
