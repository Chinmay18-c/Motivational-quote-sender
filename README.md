# Motivational Quote Emailer

Automatically sends a motivational quote via email on weekdays.

## Features
- Sends an email with a random motivational quote.
- Only sends on weekdays (Monday to Thursday).
- Uses Gmail SMTP for email delivery.

## Folder Structure

```
motivational_emailer/
├── quotes.txt             # List of motivational quotes
├── motivational_emailer.py # Main Python script
├── password.env           # NOT pushed to GitHub (contains email credentials)
├── requirements.txt       # Required Python packages
└── README.md
```

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Gmail credentials and recipient email:
   ```
   MY_EMAIL=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   TO_EMAIL=recipient_email@example.com
   ```
   **Note:** Use a Gmail App Password, not your regular password.

4. Add motivational quotes to `quotes.txt`, one quote per line.

5. Run the script:
   ```bash
   python motivational_emailer.py
   ```

## Security
- **Do NOT push `password.env` or `.env`** to GitHub.
- Add sensitive files to `.gitignore`:
  ```
  password.env
  .env
  __pycache__/
  *.pyc
  ```

## Example quotes in `quotes.txt`

```
Believe in yourself and all that you are.
The only way to do great work is to love what you do.
Don’t watch the clock; do what it does. Keep going.
Success is not final, failure is not fatal: It is the courage to continue that counts.
```

## Notes
- Make sure the recipient email is valid.
- The script only sends emails on weekdays (Monday to Thursday).
- Never commit real passwords to GitHub.
