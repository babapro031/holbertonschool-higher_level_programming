# task_02_requests.py
import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their titles."""
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts.")

def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save them to a CSV file."""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        # Strukturlaşdırılmış data: list of dictionaries
        structured_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # CSV faylına yazmaq
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in structured_posts:
                writer.writerow(post)
    else:
        print("Failed to fetch posts for CSV.")
