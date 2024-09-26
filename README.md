# Text Extraction and Abstractive Summarization from Images

## Overview
This Python script extracts text from an image using **OCR (Optical Character Recognition)** and generates an abstractive summary of the extracted text. The script also provides a GUI to display the summary alongside the image.

### Key Features:
- **Text Extraction**: Utilizes `pytesseract` to extract text from images.
- **Text Preprocessing**: Tokenizes and removes stopwords from the extracted text.
- **Abstractive Summarization**: Uses Hugging Face’s `transformers` library to generate an abstractive summary of the text.
- **GUI**: Displays the image and the summary using a Tkinter-based interface.

## Requirements
To run this script, you need to have the following dependencies installed:

```bash
pip install opencv-python-headless Pillow pytesseract transformers nltk tkinter
```

Additionally, you need to have the **Tesseract OCR** engine installed on your system. You can download it from: https://github.com/tesseract-ocr/tesseract

Ensure to set up the path to the Tesseract executable in your environment. For example:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repo-directory
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Download NLTK data for tokenization and stopwords:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## Usage

1. **Extract and summarize text**:
   - Update the `image_path` variable in the script to point to the image file you want to process.
   - Run the script:
     ```bash
     python your_script.py
     ```
   - Enter the desired number of words for the summary when prompted.

2. **GUI Display**: 
   After processing, a window will display the extracted summary alongside the image.


### 1. `extract_text_from_image(image_path)`
- **Description**: Extracts text from the image at the given path using Tesseract OCR.
- **Input**: Path to the image.
- **Output**: Extracted text as a string.

### 2. `preprocess_text(text)`
- **Description**: Tokenizes and removes stopwords from the extracted text.
- **Input**: Text string.
- **Output**: List of filtered words.

### 3. `generate_abstractive_summary(text, max_words)`
- **Description**: Generates an abstractive summary of the input text using a transformer-based model.
- **Input**: Text string and maximum word count for the summary.
- **Output**: A summarized text string.

### 4. `display_summary_and_image(summary, image_path)`
- **Description**: Displays the summary and the image using a Tkinter GUI.
- **Input**: Summary text and path to the image.
