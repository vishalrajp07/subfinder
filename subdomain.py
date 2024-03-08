import os
import requests

def download_file(url, local_filename):
    response = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(response.content)

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

# Get target URL from user input
target_url = input("Enter the target URL (e.g., example.com): ")

# Use the default URL if the user doesn't provide any input
target_url = target_url.strip() or "google.com"

# File URLs
input_file_url = "https://raw.githubusercontent.com/n0kovo/n0kovo_subdomains/main/n0kovo_subdomains_small.txt"
input_file_local = "n0kovo_subdomains_small.txt"
output_file = "discovered_urls.txt"

# Download the input file if it doesn't exist locally
if not os.path.isfile(input_file_local):
    print("Downloading input file...")
    download_file(input_file_url, input_file_local)
    print("Download complete.")

# Process the input file
with open(input_file_local, "r") as wordlist_file, open(output_file, "a") as output:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            discovered_url = "http://" + test_url
            print("[+] Discovered URL -->", discovered_url)

            # Append the discovered URL to the output file
            output.write(discovered_url + "\n")

# Provide instructions to the user
print("Discovered URLs have been saved to:", output_file)
print("You can download them using the following wget command:")
print("wget -i", output_file)
