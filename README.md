# AI Story Generator

A Python project that generates creative stories using Google's Gemini AI.

## Features

- Generates creative stories based on user-provided themes
- Uses Google's Gemini AI for natural language generation
- Simple command-line interface
- Customizable story prompts

## Setup

1. Clone this repository
2. Install required packages:
   ```bash
   pip install python-dotenv google-generativeai
   ```

3. Create a `.env` file in the project root directory with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
   Get your API key from: https://makersuite.google.com/app/apikey

## Usage

1. Run the story generator:
   ```bash
   python src/story_generator.py
   ```

2. Enter a theme when prompted (e.g., "a magical forest", "a space adventure")

3. The program will generate and display a creative story based on your theme

## Project Structure

```
project/
├── src/
│   └── story_generator.py    # Main story generation script
├── .env                      # API key configuration
└── README.md                # This file
```

## Requirements

- Python 3.8+
- google-generativeai
- python-dotenv

## Note

This project uses Google's Gemini AI API, which has free tier limitations:
- 60 requests per minute
- 1M characters per month
- 100 images per month

## Future Improvements

- Save generated stories to files
- Add different story genres
- Customize story length
- Add character customization
- Create a GUI interface 