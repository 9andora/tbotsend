#!/usr/bin/python3

import os
import requests
import sys

# Your Telegram bot token and the chat ID of the group
chat_id = "change this"
bot_token = "change this"

def send_file_to_telegram(file_path, message=""):
    method = "sendDocument"
    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found.")
        return
    # Construct the URL for the Telegram Bot API's method
    url = f"https://api.telegram.org/bot{bot_token}/{method}"

    # Parameters for the chosen method
    data = {"chat_id": chat_id, "caption": message}  # Add the message/caption

    files = {"document": open(file_path, "rb")}

    try:
        # Send the file using a POST request
        response = requests.post(url, data=data, files=files)

        # Check the response status
        if response.status_code == 200:
            print("File sent successfully.")
        else:
            print("Failed to send the file. Status code:", response.status_code)
            print(response.text)
    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: script.py <file_path> [message]")
        sys.exit(1)

    file_path = sys.argv[1]
    message = sys.argv[2] if len(sys.argv) > 2 else ""

    send_file_to_telegram(file_path, message)

