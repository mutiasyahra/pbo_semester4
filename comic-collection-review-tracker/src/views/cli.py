import sys
from controllers.review_controller import ReviewController

class CLI:
    def __init__(self):
        self.review_controller = ReviewController()

    def display_menu(self):
        print("1. Add a Comic")
        print("2. View Comics")
        print("3. Add a Review")
        print("4. View Reviews")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Please select an option: ")

            if choice == '1':
                self.add_comic()
            elif choice == '2':
                self.view_comics()
            elif choice == '3':
                self.add_review()
            elif choice == '4':
                self.view_reviews()
            elif choice == '5':
                print("Exiting the application. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

    def add_comic(self):
        title = input("Enter comic title: ")
        author = input("Enter comic author: ")
        genre = input("Enter comic genre: ")
        rating = input("Enter comic rating: ")
        self.review_controller.add_comic(title, author, genre, rating)
        print("Comic added successfully!")

    def view_comics(self):
        comics = self.review_controller.get_comics()
        if not comics:
            print("No comics found.")
            return
        for comic in comics:
            print(f"Title: {comic['title']}, Author: {comic['author']}, Genre: {comic['genre']}, Rating: {comic['rating']}")

    def add_review(self):
        comics = self.review_controller.get_comics()
        if not comics:
            print("No comics available. Please add a comic first.")
            return
        print("Select a comic to review:")
        for idx, comic in enumerate(comics, 1):
            print(f"{idx}. {comic['title']}")
        try:
            choice = int(input("Enter the number of the comic: "))
            if 1 <= choice <= len(comics):
                comic_title = comics[choice - 1]['title']
                review_text = input("Enter your review: ")
                rating = input("Enter your rating: ")
                self.review_controller.add_review(comic_title, review_text, rating)
                print("Review added successfully!")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")

    def view_reviews(self):
        all_reviews = self.review_controller.reviews
        if not all_reviews:
            print("No reviews found.")
            return
        for comic_title, reviews in all_reviews.items():
            print(f"Comic: {comic_title}")
            for idx, review in enumerate(reviews, 1):
                print(f"  {idx}. Review: {review['review']}, Rating: {review['rating']}")

if __name__ == "__main__":
    cli = CLI()
    cli.run()