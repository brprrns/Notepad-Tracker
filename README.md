# Notepad Tracker

A simple Flask-based web application that allows users to create and edit text files while automatically tracking changes using Git.

## Features

- Simple web-based text editor
- Create and save text files
- Save files to any directory on the machine
- Automatically save changes after the user stops typing
- Automatically create Git commits for file changes
- Logging for important application operations
- Exception handling for file and Git operations
- Unit tests using pytest

## Requirements

- Python 3.12+
- Flask
- Git
- pytest

## Installation

Clone or copy the project and navigate to the project directory.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

On Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask application:

```bash
python app.py
```

Open the following URL in a browser:

```text
http://127.0.0.1:5000
```

## How It Works

1. Enter the path where the note should be saved.
2. Write or edit the note in the text editor.
3. When typing stops for approximately 2 seconds, the application automatically saves the file.
4. The application initializes Git in the file's directory if required.
5. The changed file is added to Git.
6. A Git commit is created for the change.

## Running Tests

Run:

```bash
python -m pytest -v
```

The tests verify the Flask home page, file saving functionality, and validation of missing file paths.

## Example

File path:

```text
C:\Users\brpra\Documents\NotepadTest\notes.txt
```

After writing and stopping for a few seconds, the application saves the file and creates a Git commit.

## Assignment Requirements

The application satisfies the following requirements:

1. Provides a normal text editor.
2. Automatically saves changes after the user stops writing and tracks the changes using Git.
3. Allows files to be created and saved in different directories on the machine.