import cv2
from PIL import Image, ImageTk
import pytesseract
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tkinter as tk
from tkinter import ttk

import nltk
nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    return text

def preprocess_text(text):
    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    return filtered_words

def generate_abstractive_summary(text, max_words):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=100, min_length=20, length_penalty=2.0, num_beams=4, early_stopping=True)

    summary_text = ' '.join(summary[0]['summary_text'].split()[:max_words])

    return summary_text

def display_summary_and_image(summary, image_path):
    root = tk.Tk()
    root.title("Abstractive Summary and Image Viewer")

    root.configure(bg="#f0f0f0")

    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)

    summary_label = ttk.Label(frame, text="Summary:", font=("Helvetica", 14, "bold"), background="#f0f0f0")
    summary_label.grid(row=0, column=0, sticky=tk.W)

    summary_text = tk.Text(frame, height=10, width=50, wrap=tk.WORD)
    summary_text.insert(tk.END, summary)
    summary_text.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    img = Image.open(image_path)
    img.thumbnail((400, 400))
    img = ImageTk.PhotoImage(img)
    image_label = ttk.Label(frame, image=img, background="#f0f0f0")
    image_label.image = img
    image_label.grid(row=0, column=1, rowspan=2, padx=10)

    close_button = ttk.Button(root, text="Close", command=root.destroy)
    close_button.pack(pady=10)


    root.mainloop()

max_words = int(input("Enter the desired number of words for the summary: "))

image_path = 'C:/Users/ZAID/Downloads/new1.png'
text = extract_text_from_image(image_path)
abstractive_summary = generate_abstractive_summary(text, max_words)
display_summary_and_image(abstractive_summary, image_path)
