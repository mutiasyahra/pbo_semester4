class ReviewController:
    def __init__(self):
        self.reviews = {}
        self.comics = []
    
    def add_comic(self, title, author, genre, rating):
        comic = {
            'title': title,
            'author': author,
            'genre': genre,
            'rating': rating
        }
        self.comics.append(comic)

    def get_comics(self):
        return self.comics

    def add_review(self, comic_title, review_text, rating):
        if comic_title not in self.reviews:
            self.reviews[comic_title] = []
        self.reviews[comic_title].append({'review': review_text, 'rating': rating})

    def edit_review(self, comic_title, review_index, new_review_text, new_rating):
        if comic_title in self.reviews and 0 <= review_index < len(self.reviews[comic_title]):
            self.reviews[comic_title][review_index] = {'review': new_review_text, 'rating': new_rating}

    def delete_review(self, comic_title, review_index):
        if comic_title in self.reviews and 0 <= review_index < len(self.reviews[comic_title]):
            del self.reviews[comic_title][review_index]

    def get_reviews(self, comic_title):
        return self.reviews.get(comic_title, [])