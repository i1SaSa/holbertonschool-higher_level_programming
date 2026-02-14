import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post['title'])
    else:
        print("Failed to fetch data")


def fetch_and_save_posts():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        structured_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in data
        ]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_data)

        print("Data saved to posts.csv")
    else:
        print("Failed to fetch data")
