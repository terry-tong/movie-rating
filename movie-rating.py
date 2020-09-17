def rotten_tomatoes(movie_title):
    from urllib.request import urlopen
    import re

    title = list(movie_title.lower().replace(" ", "_"))
    for char in title:
        if char == "&":
            char = "and"
        elif char in "!?,:#'":
            title.remove(char)
    url = "https://www.rottentomatoes.com/m/{}".format(''.join(title))
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    match = re.search(r"(\d{1,3}%)(\n +)(</span>)", html)
    if match:
        print("Tomatometer: {}".format(match.group(1)))


def imdb(movie_title):
    from urllib.request import urlopen
    from urllib.parse import quote
    import re

    url_search = "https://www.imdb.com/search/title/?title={}&title_type=feature".format(quote(movie_title))
    page = urlopen(url_search)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    match = re.search(r"tt\d{7,8}", html)
    if match:
        url = "https://www.imdb.com/title/{}".format(match.group(0))
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        match = re.search(r"(\"ratingValue\": \")(\d{1,2}.\d{1})(\")", html)
        if match:
            print("IMDb rating: {}/10".format(match.group(2)))


movie = input("Please enter the movie title here: ")
rotten_tomatoes(movie)
imdb(movie)
