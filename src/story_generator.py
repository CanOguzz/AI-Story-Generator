import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_user_input():
    print("Welcome to the story generator!")
    print("Please enter the theme of your story: ")

    return input("> ")

def generate_story(theme):

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt= f"""
    "Write a creative short story about {theme}. The story should:
    - Be approximately two paragraphs long
    - Have a clear beginning, middle, and end
    - Include vivid descriptions and engaging characters
    - Be suitable for all ages
    - Have a satisfying conclusion
    
    Focus on making the story engaging and memorable while keeping it concise."""

    response = model.generate_content(prompt)

    return response.text

def main():

    theme = get_user_input()

    story = generate_story(theme)

    print("\nHere's your story:")
    print(story)

if __name__ == "__main__":
    main()
