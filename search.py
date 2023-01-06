import tkinter as tk
import requests

# Create the main window
window = tk.Tk()
window.title("HTML Viewer")

# Create the input field
url_entry = tk.Entry(window)
url_entry.pack()

# Create the "Get HTML" button
def get_html():
    # Get the URL from the input field
    url = url_entry.get()

    # Send a request to the URL
    response = requests.get(url)

    # Get the HTML data from the response
    html = response.text

    # Display the HTML data
    html_label = tk.Label(window, text=html)
    html_label.pack()

get_html_button = tk.Button(window, text="Get HTML", command=get_html)
get_html_button.pack()

# Run the main loop
window.mainloop()
