from telethon.sync import TelegramClient
import os
import csv

# Your Telegram API Credentials
api_id = ENTER API ID
api_hash = "ENTER API HASH"
channel_username = "ENTER CHANNEL NAME"  # Replace with actual channel username
output_file = "/XXX/XXX/XXX/XXX/XXXX.csv"

# Initialize Telegram Client
client = TelegramClient("session_name", api_id, api_hash)

def scrape_messages():
    """Scrapes text-based messages and saves them to CSV with views and message IDs."""
    with client:
        print("Logged into Telegram successfully!")

        # Test with a smaller limit for debugging
        limit = 150000  # Start with smaller number of messages
        print(f"Fetching up to {limit} messages from {channel_username}...")

        messages = client.get_messages(channel_username, limit=limit)
        print(f" {len(messages)} messages fetched.")

        # Check if messages are empty
        if not messages:
            print("No messages found.")
            return

        # Initialize overall views counter and message counter
        total_views = 0
        message_counter = 1

        # Create CSV File
        with open(output_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Message ID", "Date", "Sender ID", "Message", "Views"])  # CSV Header

            for message in messages:
                if message.text:  # Only process text-based messages
                    # Assign message ID
                    if message.id:
                        message_id = f"MSG-{message.id:05d}"
                    else:
                        message_id = f"MSG-{message_counter:05d}"
                        message_counter += 1

                    # Extract the views count for each message
                    views = message.views if message.views else 0

                    # Add views to the total views count
                    total_views += views

                    # Write the message details along with views to the CSV
                    writer.writerow([message_id, message.date, message.sender_id, message.text, views])

        print(f"Messages saved to {output_file}")
        print(f"Total Views for the channel: {total_views}")

# Run Scraper
if __name__ == "__main__":
    print("Starting scraper...")
    scrape_messages()
