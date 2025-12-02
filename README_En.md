**English** | [中文](./README.md)

# GoldenDict Integration for `translate.py`

This guide explains how to integrate the `translate.py` script into GoldenDict, allowing you to automatically translate selected text between Chinese and English based on language detection.

## Script Functionality

The `translate.py` script performs the following actions:
-   **Language Detection**: Automatically detects the language of the input text.
-   **Conditional Translation**:
    -   If the detected language is **Chinese**, it translates the text to **English**.
    -   If the detected language is **not Chinese** (e.g., English, Spanish, etc.), it translates the text to **Chinese**.
-   **GoldenDict Optimized Output**: Produces a clean HTML output specifically designed for GoldenDict's display panel.

## Prerequisites

Before integrating, ensure you have the following:

- install [uv](https://docs.astral.sh/uv/#installation)

## Setup

1.  **Save the script**: Ensure `translate.py` is saved in a permanent location on your system (e.g., `C:\Users\YourUser\Scripts\translate.py` or `/home/youruser/scripts/translate.py`).

2.  **Configure GoldenDict**:
    *   Open GoldenDict.
    *   Go to `Edit -> Dictionaries -> Programs` tab.
    *   Click on `Add program`.
    *   **Type**: Select `Html`.
    *   **Command Line**: This is crucial. Enter the following command, replacing "path/to/translate.py" with the actual, absolute path to your `translate.py` file. `uv` will automatically manage the script's dependencies in a temporary virtual environment.
        ```
        uv run "path/to/translate.py" "$GDSEARCH$"
        ```
        **Example (Windows)**:
        `uv run "C:\Users\YourUser\Scripts\translate.py" "$GDSEARCH$"`
        **Example (Linux/macOS)**:
        `uv run "/home/youruser/scripts/translate.py" "$GDSEARCH$"`
        **Important**: The `$GDSEARCH$` variable is GoldenDict's placeholder for the selected text. Ensure it's enclosed in double quotes if the text might contain spaces.
    *   **Name**: Give it a descriptive name, e.g., "Auto-Translate with uv".
    *   **Icon (Optional)**: You can choose an icon for your program.
    *   Click `OK` to save the program dictionary.

## Usage in GoldenDict

Use it as a normal dictionary.
