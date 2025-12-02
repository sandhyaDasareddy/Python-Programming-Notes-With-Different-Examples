'''
# Filtering URLs that start with HTTPS
# -----------------------------------

# List of URLs
lst = [
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "http://mail.google.com/mail/u/0/"
]

# Loop through each URL
for url in lst:

    # Print only the URLs that use secure HTTPS protocol
    if url.startswith("https"):
        print(url)

# List of names
lst1 = ["sandhya", "sagar", "sameera", "sampath", "sheela"]

# Print names starting with "sam"
for name in lst1:
    if name.startswith("sam"):
        print(name)

Output:
------
https://www.google.com/
https://www.facebook.com/
https://www.instagram.com/
sameera
sampath
'''

# ---------------------------------------------------------
# Filtering URLs that end with "com" or "com/"
# ---------------------------------------------------------

lst = [
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.instagram.com",
    "http://mail.google.com/mail/u/0/"
]

# ---- Method 1: Using slicing (manual checking) ----
for url in lst:
    # Check if URL ends with "com" or "com/"
    if url[-3:] == "com" or url[-4:] == "com/":
        print(url)

# ---- Method 2: Using built-in string methods ----
for url in lst:
    # endswith() checks the ending of a string
    if url.endswith("com") or url.endswith("com/"):
        print(url)

# ---- Method 3: Most optimized approach ----
for url in lst:
    # endswith() can take a tuple (multiple endings)
    if url.endswith(("com", "com/")):
        print(url)

'''
Output:
------
https://www.google.com/
https://www.facebook.com/
https://www.instagram.com
'''
