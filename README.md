# Guess-my-animal
A simple CLI-based animal guessing game that uses Google Gemini to randomly select an animal. The player asks questions to figure out which animal was chosen.

## Features
- The animal is not hardcoded; it is automatically selected using Gemini.
- Players can ask any type of question about the animal.
- The program handles exits gracefully.
- A 10-question limit keeps the game challenging.

## How the App Works
1. Run the program.
2. Start asking questions to guess the animal.
3. Three outcomes are possible:
    - Correct Guess – If you guess the animal correctly, the program ends and displays your score.
    - Normal Question – The program answers your question to help you narrow down the animal.
    - Question Limit Reached – After 10 questions, the program ends and reveals the correct animal.

## How to Run the Program
1. Make sure **Python** is installed.
2. Install all required modules using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
3. Open `Main.py` and add your Google Gemini API key where indicated.
    You can get an API key from the Google Gemini website.
4. Run the program
    ```bash
    python Main.py
    ```
    
## File Structure
```bash
project/
│── Main.py
│── README.md
│── requirements.txt
```

## Technologies Used
- Python
- Google Gemini API (`google-genai`)

## Notes
- Be careful with Gemini API usage, as excessive requests may consume your API tokens.
- If an error occurs, check whether your API key is valid and has remaining quota.

## Author
Muhammad Awais Tariq

---
If you like this project, consider giving it a star on GitHub!
