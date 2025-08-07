# 📄 Flask OCR App

A simple Flask web application that performs **Optical Character Recognition (OCR)** on uploaded images using **Tesseract OCR**. It extracts text from images and displays the results in a clean, user-friendly interface.

---

## 🔍 Features

- 📤 Upload image files (`.png`, `.jpg`, `.jpeg`)
- 📄 Extract text using Tesseract OCR
- 📋 View extracted text on a result page
- 🖼️ Image preview with progress bar for large files
- 🌐 Clean and responsive web interface using HTML & CSS

---

## 🚀 Demo

> Want to see a live version? Ask me how to deploy this on **Render**, **Railway**, or **Heroku** (free hosting platforms).

---

## 🧰 Tech Stack

- Python 3.x
- Flask
- HTML, CSS, JS
- Tesseract OCR (`pytesseract`)
- Bootstrap (for design)

---

## 📸 Screenshots

| Home (Upload) | Result (Text Output) |
|---------------|----------------------|
| ![Home](https://via.placeholder.com/300x200.png?text=Upload+Image+Page) | ![Result](https://via.placeholder.com/300x200.png?text=OCR+Result+Page) |

---

## ⚙️ How to Run Locally

1. **Clone this repo**
   ```bash
   git clone https://github.com/Sarthak210805/Flask-ocr-app.git
   cd Flask-ocr-app
   ```

2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Mac/Linux
   ```

3. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 🔧 Requirements

- Python 3.7+
- Tesseract OCR installed
  - [Tesseract for Windows](https://github.com/tesseract-ocr/tesseract)
  - Add the path to `pytesseract.pytesseract.tesseract_cmd` in `app.py` if needed

---

## 📁 Project Structure

```
ocr_ocr/
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── uploads/
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

This project is open-source under the MIT License.
