import tkinter as tk
import pyshorteners
import pyperclip

root = tk.Tk()
long_url = tk.StringVar()
short_url = tk.StringVar()

# Converts long url into short one
def UrlShortener():
    type_bitly = pyshorteners.Shortener(api_key='9e0f4161d322843e355785bc26f68b392b2212e8')
    url = long_url.get()
    
    if url:
        short_url.set(type_bitly.bitly.short(url))
    else:
        short_url.set("Please enter a valid URL")


# Copy url to clipboard
def UrlCopy():
    url = short_url.get()
    pyperclip.copy(url)


root.title("CodeClause Project 1")
root.geometry("600x400")
root.config(bg="#2C3E50")
root.iconbitmap("url.ico")
# Heading Label
heading_label = tk.Label(root, text="URL Shortener", font=("Arial", 28, "bold"), fg="#ECF0F1", bg="#2C3E50")
heading_label.pack(pady=20)

# Input Entry (Long URL)
textbox1 = tk.Entry(root, textvariable=long_url, justify="center", width=40, font=("Arial", 14), bg="#ECF0F1")
textbox1.pack(pady=20)

# Generate Button
button_generate = tk.Button(root, text="Generate Short URL", command=UrlShortener, font=("Arial", 14), bg="#3498DB", fg="#ECF0F1")
button_generate.pack(pady=20)

# Output Entry (Short URL)
textbox2 = tk.Entry(root, textvariable=short_url, justify="center", width=40, font=("Arial", 14), bg="#ECF0F1", state="readonly")
textbox2.pack(pady=20)

# Copy Button
button_copy = tk.Button(root, text="Click to Copy", justify='center',command=UrlCopy, font=("Arial", 14), bg="#3498DB", fg="#ECF0F1")
button_copy.pack(pady=20)
root.mainloop()
