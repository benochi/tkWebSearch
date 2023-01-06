import tkinter as tk
import requests
from bs4 import BeautifulSoup
import csv

# Create the main window
window = tk.Tk()
window.title("Shipping Manager Scraper")

# Create the input fields
url_label = tk.Label(window, text="Website URL:")
url_label.pack()

url_entry = tk.Entry(window)
url_entry.pack()

file_label = tk.Label(window, text="Save to File:")
file_label.pack()

file_entry = tk.Entry(window)
file_entry.pack()

# Create the "Scrape" button
def scrape():
    # Get the URL and file path from the input fields
    url = url_entry.get()
    file_path = file_entry.get()

    # Send a request to the URL
    response = requests.get(url)

    # Parse the HTML of the website
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the shipping manager information
    shipping_managers = []
    for div in soup.find_all("div", class_="shipping-manager"):
        name = div.find("h3").text
        email = div.find("span", class_="email").text
        shipping_managers.append((name, email))

    # Write the shipping manager information to a CSV file
    with open(file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(shipping_managers)

scrape_button = tk.Button(window, text="Scrape", command=scrape)
scrape_button.pack()

# Run the main loop
window.mainloop()
