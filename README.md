# Kahoot Cheater

This repository contains a Python script that automates the process of using Kahoot and ChatGPT to assist in answering quiz questions. The script utilizes `undetected_chromedriver` to bypass bot detection.

![Untitled video - Made with Clipchamp (3)](https://github.com/user-attachments/assets/36635c85-1c3d-4ae5-8575-779fb2fad66e)

## Features

- Opens a Kahoot quiz and a ChatGPT window.
- Uses `Tkinter` to create a GUI with a "Cheat" button.
- Automatically copies the displayed question from Kahoot to ChatGPT.
- User selects the answer provided by ChatGPT.

## Requirements

To run the script, ensure you have Python 3.9.18 installed along with the required packages specified in `requirements.txt`. 

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd kahoot-cheating-assistant

   ```

2. **Set up a Python environment (optional but recommended):**

   You can use `venv` to create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the main script:**

   ```bash
   python main.py
   ```

2. **Login to Kahoot:**
   - Enter your credentials and select the quiz you want to join.

3. **Start the quiz:**
   - When the multiple-choice question is displayed, click the "Cheat" button in the Tkinter window.

4. **Get the answer:**
   - The question will be copied to ChatGPT, and you will need to choose the answer provided by ChatGPT.

## Code Overview

### main.py

This is the main script that handles:

- Launching the Kahoot and ChatGPT windows using `undetected_chromedriver`.
- Creating a Tkinter window with a button labeled "Cheat".
- Managing the process of copying the question to ChatGPT and retrieving the answer.

### Example `requirements.txt`

```plaintext
undetected-chromedriver
selenium
tkinter
requests
```

## Disclaimer

This tool is intended for educational purposes only. Using automated scripts in online quizzes may violate terms of service. Please ensure you are using this responsibly and ethically. 
