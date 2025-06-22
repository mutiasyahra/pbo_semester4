import tkinter as tk
from tkinter import messagebox

BG_COLOR = "#fff0f6"      # Soft pink background
BTN_COLOR = "#e0bbff"     # Pastel purple button
BTN_TEXT = "#fff"         # White text
LABEL_COLOR = "#a259c6"   # Deep purple for label
ENTRY_BG = "#fbeaff"      # Light purple for entry
BTN_ACTIVE = "#cdb4f6"    # Button active color

FONT_TITLE = ("Century Gothic", 20, "bold")
FONT_LABEL = ("Century Gothic", 12)
FONT_BTN = ("Century Gothic", 12, "bold")
FONT_ENTRY = ("Century Gothic", 12)
FONT_REVIEW = ("Century Gothic", 11)

class ComicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Comic Collection & Review Tracker")
        self.root.configure(bg=BG_COLOR)
        self.comics = []
        self.reviews = {}
        self.create_menu()

    def create_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Comic Collection & Review Tracker", font=FONT_TITLE, bg=BG_COLOR, fg=LABEL_COLOR).pack(pady=(24, 18))
        tk.Button(self.root, text="Add a Comic", width=28, font=FONT_BTN, command=self.add_comic, bg=BTN_COLOR, fg=BTN_TEXT, bd=0, activebackground=BTN_ACTIVE, cursor="hand2", relief="flat").pack(pady=7)
        tk.Button(self.root, text="View Comics", width=28, font=FONT_BTN, command=self.view_comics, bg=BTN_COLOR, fg=BTN_TEXT, bd=0, activebackground=BTN_ACTIVE, cursor="hand2", relief="flat").pack(pady=7)
        tk.Button(self.root, text="Add a Review", width=28, font=FONT_BTN, command=self.add_review, bg=BTN_COLOR, fg=BTN_TEXT, bd=0, activebackground=BTN_ACTIVE, cursor="hand2", relief="flat").pack(pady=7)
        tk.Button(self.root, text="View Reviews", width=28, font=FONT_BTN, command=self.view_reviews, bg=BTN_COLOR, fg=BTN_TEXT, bd=0, activebackground=BTN_ACTIVE, cursor="hand2", relief="flat").pack(pady=7)
        tk.Button(self.root, text="Exit", width=28, font=FONT_BTN, command=self.root.quit, bg="#ffb4b4", fg=LABEL_COLOR, bd=0, activebackground="#ff6f91", cursor="hand2", relief="flat").pack(pady=(20, 18))

    def add_comic(self):
        form = tk.Toplevel(self.root)
        form.title("Add Comic")
        form.configure(bg=BG_COLOR)
        form.resizable(False, False)

        tk.Label(form, text="Title:", bg=BG_COLOR, fg=LABEL_COLOR, font=FONT_LABEL).grid(row=0, column=0, sticky="e", padx=12, pady=8)
        title_entry = tk.Entry(form, font=FONT_ENTRY, bg=ENTRY_BG, relief="groove", bd=2)
        title_entry.grid(row=0, column=1, padx=12, pady=8)

        tk.Label(form, text="Author:", bg=BG_COLOR, fg=LABEL_COLOR, font=FONT_LABEL).grid(row=1, column=0, sticky="e", padx=12, pady=8)
        author_entry = tk.Entry(form, font=FONT_ENTRY, bg=ENTRY_BG, relief="groove", bd=2)
        author_entry.grid(row=1, column=1, padx=12, pady=8)

        tk.Label(form, text="Genre:", bg=BG_COLOR, fg=LABEL_COLOR, font=FONT_LABEL).grid(row=2, column=0, sticky="e", padx=12, pady=8)
        genre_entry = tk.Entry(form, font=FONT_ENTRY, bg=ENTRY_BG, relief="groove", bd=2)
        genre_entry.grid(row=2, column=1, padx=12, pady=8)

        def submit():
            title = title_entry.get().strip()
            author = author_entry.get().strip()
            genre = genre_entry.get().strip()
            if not title or not author or not genre:
                messagebox.showerror("Error", "All fields are required.")
                return
            for comic in self.comics:
                if comic['title'].lower() == title.lower():
                    messagebox.showerror("Error", "Comic with this title already exists.")
                    return
            self.comics.append({'title': title, 'author': author, 'genre': genre})
            messagebox.showinfo("Success", f"Comic '{title}' added!")
            form.destroy()

        tk.Button(form, text="Submit", command=submit, bg=BTN_COLOR, fg=BTN_TEXT, font=FONT_BTN, bd=0, activebackground=BTN_ACTIVE, cursor="hand2", relief="flat").grid(row=3, column=0, columnspan=2, pady=16)

    def view_comics(self):
        win = tk.Toplevel(self.root)
        win.title("View Comics")
        win.configure(bg=BG_COLOR)
        win.resizable(False, False)
        if not self.comics:
            tk.Label(win, text="No comics found.", bg=BG_COLOR, fg=LABEL_COLOR, font=FONT_LABEL).pack(padx=24, pady=24)
            return
        for comic in self.comics:
            text = f"Title: {comic['title']}\nAuthor: {comic['author']}\nGenre: {comic['genre']}"
            frame = tk.Frame(win, bg="#fbeaff", bd=2, relief="ridge")
            frame.pack(fill="x", padx=18, pady=8)
            tk.Label(frame, text=text, anchor="w", justify="left", bg="#fbeaff", fg=LABEL_COLOR, font=FONT_LABEL).pack(fill="x", padx=10, pady=6)

    def add_review(self):
        if not self.comics:
            messagebox.showinfo("Info", "No comics available. Please add a comic first.")
            return
        win = tk.Toplevel(self.root)
        win.title("Add Review")
        win.configure(bg=BG_COLOR)
        win.resizable(False, False)

        tk.Label(win, text="Select Comic:", bg=BG_COLOR, fg=LABEL_COLOR, font=FONT_LABEL).grid(row=0, column=0, sticky="e", padx=12, pady=8)
        comic_titles = [comic['title'] for comic in self.comics]
        selected = tk.StringVar(value=comic_titles[0])
        tk.OptionMenu(win, selected, *comic_titles).grid(row=0, column=1, padx=12, pady=8)

        tk.Label(win, text="Review:", bg=BG_COLOR, fg=LABEL_COLOR, font=FONT_LABEL).grid(row=1, column=0, sticky="e", padx=12, pady=8)
        review_entry = tk.Entry(win, width=40, font=FONT_ENTRY, bg=ENTRY_BG, relief="groove", bd=2)
        review_entry.grid(row=1, column=1, padx=12, pady=8)

        tk.Label(win, text="Rating (1-5):", bg=BG_COLOR, fg=LABEL_COLOR, font=FONT_LABEL).grid(row=2, column=0, sticky="e", padx=12, pady=8)
        rating_entry = tk.Entry(win, font=FONT_ENTRY, bg=ENTRY_BG, relief="groove", bd=2)
        rating_entry.grid(row=2, column=1, padx=12, pady=8)

        def submit():
            title = selected.get()
            review = review_entry.get().strip()
            rating = rating_entry.get().strip()
            if not review or not rating:
                messagebox.showerror("Error", "All fields are required.")
                return
            if not rating.isdigit() or not (1 <= int(rating) <= 5):
                messagebox.showerror("Error", "Rating must be a number between 1 and 5.")
                return
            if title not in self.reviews:
                self.reviews[title] = []
            self.reviews[title].append({'review': review, 'rating': rating})
            messagebox.showinfo("Success", "Review added!")
            win.destroy()

        tk.Button(win, text="Submit", command=submit, bg=BTN_COLOR, fg=BTN_TEXT, font=FONT_BTN, bd=0, activebackground=BTN_ACTIVE, cursor="hand2", relief="flat").grid(row=3, column=0, columnspan=2, pady=16)

    def view_reviews(self):
        win = tk.Toplevel(self.root)
        win.title("View Reviews")
        win.configure(bg=BG_COLOR)
        win.resizable(False, False)
        if not self.reviews:
            tk.Label(win, text="No reviews found.", bg=BG_COLOR, fg=LABEL_COLOR, font=FONT_LABEL).pack(padx=24, pady=24)
            return
        for comic_title, reviews in self.reviews.items():
            tk.Label(win, text=f"Comic: {comic_title}", font=FONT_LABEL, bg=BG_COLOR, fg=LABEL_COLOR).pack(anchor="w", padx=18, pady=(12,2))
            for idx, review in enumerate(reviews, 1):
                text = f"  {idx}. Review: {review['review']}\n      Rating: {review['rating']}"
                frame = tk.Frame(win, bg="#fbeaff", bd=1, relief="ridge")
                frame.pack(fill="x", padx=28, pady=4)
                tk.Label(frame, text=text, anchor="w", justify="left", bg="#fbeaff", fg=LABEL_COLOR, font=FONT_REVIEW).pack(fill="x", padx=10, pady=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = ComicApp(root)
    root.mainloop()