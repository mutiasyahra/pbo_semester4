# main.py
from views.cli import CLI

def main():
    print("Welcome to the Comic Collection & Review Tracker!")
    # Initialize application components here
    # Set up interactive menu and handle user input
    cli = CLI()
    cli.run()

if __name__ == "__main__":
    main()