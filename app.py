import tkinter as tk
from tkinter import filedialog, messagebox
import re
from PyPDF2 import PdfReader


def extract_text(path: str) -> str:
    """Extract text from a .txt or .pdf file."""
    if path.lower().endswith('.pdf'):
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    else:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()


def parse_info(text: str) -> dict:
    """Parse important fields from the text."""
    fields = ['Project Name', 'Budget', 'Start Date', 'End Date', 'Client']
    results = {}
    for line in text.splitlines():
        for field in fields:
            if field.lower() in line.lower():
                # Extract part after colon if present
                if ':' in line:
                    results[field] = line.split(':', 1)[1].strip()
                else:
                    results[field] = line.strip()
    return results


def open_file():
    path = filedialog.askopenfilename(
        title='Select Submission File',
        filetypes=[('Text Files', '*.txt'), ('PDF Files', '*.pdf'), ('All Files', '*.*')]
    )
    if not path:
        return
    try:
        text = extract_text(path)
        info = parse_info(text)
        output.delete('1.0', tk.END)
        if info:
            for k, v in info.items():
                output.insert(tk.END, f"{k}: {v}\n")
        else:
            output.insert(tk.END, 'No relevant information found.')
    except Exception as e:
        messagebox.showerror('Error', str(e))


root = tk.Tk()
root.title('Construction Submission Extractor')
root.geometry('600x400')

select_btn = tk.Button(root, text='Select Submission File', command=open_file)
select_btn.pack(pady=10)

output = tk.Text(root, wrap=tk.WORD)
output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
