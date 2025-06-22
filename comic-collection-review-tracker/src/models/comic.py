class Comic:
    def __init__(self, title, author, genre, rating):
        self.title = title
        self.author = author
        self.genre = genre
        self.rating = rating

    def update_details(self, title=None, author=None, genre=None, rating=None):
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if genre is not None:
            self.genre = genre
        if rating is not None:
            self.rating = rating

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Rating: {self.rating}"