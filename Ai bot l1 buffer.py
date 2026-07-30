import webbrowser

print("Hello! I am AI Bot. What's your name? : ")
name = input().strip()

print(f"Nice to meet you, {name}!")

print("Which website do you want to open? (example: google, youtube, wikipedia) : ")
site_name = input().strip().lower()

# Build a simple URL: https://www.<name>.com
url = f"https://www.{site_name}.com"

print(f"Opening {url} now...")
webbrowser.open(url)

print(f"It was nice chatting with you {name}. Bye!")