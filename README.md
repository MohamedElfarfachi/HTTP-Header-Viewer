# HTTP Header Viewer

## Overview
The HTTP Header Viewer is a Python script with a graphical user interface (GUI) that allows users to fetch and view HTTP headers from a specified URL. It leverages the popular `requests` library for making HTTP requests and `tkinter` for creating the GUI.

## Features
- Fetch HTTP headers from a URL.
- Display the status code and headers.
- Supports HTTP and HTTPS URLs.
- User-friendly error handling for invalid URLs.
- Responsive GUI using threading to prevent freezing during requests.

## Prerequisites
- Python 3.x
- The `requests` library (can be installed using `pip install requests`).
- Tkinter (usually included with Python).

## Usage
1. Run the script by executing the Python file.
2. Enter the URL you want to inspect in the provided input field.
3. Click the "Fetch HTTP Data" button.
4. The script will display the status code and HTTP headers in the text area.

## Additional Options (Customization)
- You can customize this script by adding options to specify request headers, HTTP methods, and handling redirects.
- You can also add the ability to display and save the response content (HTML, JSON, etc.) if needed.

## Error Handling
- If an invalid URL is entered (without 'http://' or 'https://'), the script will display an error message.

## License
This script is provided under the MIT License. Feel free to modify and distribute it according to your needs, while adhering to ethical and legal guidelines.

## Disclaimer
This script is intended for educational and ethical purposes only. Please use it responsibly and respect the terms of service of the websites you access.

## Author
Mohamed El Farfachi

## Contact Information
elfarfachi.developer@gmail.com
