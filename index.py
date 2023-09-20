import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading

class HttpHeaderViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("HTTP Header Viewer")
        
        self.create_widgets()
        
    def fetch_http_data(self):
        url = self.entry_url.get()
        
        if not url.startswith("http://") and not url.startswith("https://"):
            messagebox.showerror("Error", "Invalid URL. Please include 'http://' or 'https://' in the URL.")
            return
        
        self.text_output.delete(1.0, tk.END)
        self.text_output.insert(tk.END, "Fetching data...")

        def fetch_data_thread():
            try:
                response = requests.get(url)
                status_code = response.status_code
                headers = response.headers
                content = response.text
                
                self.text_output.delete(1.0, tk.END)
                self.text_output.insert(tk.END, f"Status Code: {status_code}\n\n")
                
                for header, value in headers.items():
                    self.text_output.insert(tk.END, f"{header}: {value}\n")
                    
                # Optionally, display the response content
                # self.text_output.insert(tk.END, "\nResponse Content:\n")
                # self.text_output.insert(tk.END, content)

            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"Error fetching data: {e}")

        # Create a thread to fetch data
        fetch_thread = threading.Thread(target=fetch_data_thread)
        fetch_thread.start()
    
    def create_widgets(self):
        self.label_url = tk.Label(self.root, text="Enter URL:")
        self.label_url.pack(pady=10)
        
        self.entry_url = tk.Entry(self.root, width=50)
        self.entry_url.pack()
        
        self.button_fetch = tk.Button(self.root, text="Fetch HTTP Data", command=self.fetch_http_data)
        self.button_fetch.pack(pady=10)
        
        self.text_output = scrolledtext.ScrolledText(self.root, height=15, width=80)
        self.text_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = HttpHeaderViewer(root)
    root.mainloop()
