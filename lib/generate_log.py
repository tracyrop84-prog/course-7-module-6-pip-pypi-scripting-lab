
from datetime import datetime
import os
import requests


def generate_log(data):
    """Create a timestamped log file from a list of entries."""

    # Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # Generate filename using today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write log entries to the file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Print confirmation message
    print(f"Log written to {filename}")

    # Return filename
    return filename


def fetch_data():
    """Fetch a post from the JSONPlaceholder API."""

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return {}


def save_api_data(data):
    """Save API data to a text file."""

    filename = "api_result.txt"

    with open(filename, "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

    print(f"API data written to {filename}")

    return filename


def main():
    """Run the automation tool."""

    # Create a sample log
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(log_data)

    # Fetch data from the API
    post = fetch_data()

    if post:
        print("Fetched Post Title:", post.get("title", "No title found"))

        # Save API result to a file
        save_api_data(post)
    else:
        print("Failed to fetch API data")


if __name__ == "__main__":
    main()
