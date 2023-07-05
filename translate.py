import requests

def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    # API endpoint URL
    url = "https://sunbird-ai-api-5bq6okiwgq-ew.a.run.app"
    
    # access token
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJJbnRlcm5zaGlwcyIsImV4cCI6NDg0MTQ4NzEyMn0.-j3rdudJ9pXEm3-456LLiDPun5SwIm5sw-RoNvgDwfk"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # Data payload for the translation request
    data = {
        "text": text,
        "source_language": source_lang.capitalize(),
        "target_language": target_lang.capitalize()
    }
    
    # Send the POST request to the translation endpoint
    response = requests.post(f"{url}/tasks/translate", headers=headers, json=data)
    
    # Process the response
    if response.status_code == 200:
        response_data = response.json()
        translated_text = response_data.get("text")
        # Check if the translated text exists
        if translated_text:
            return translated_text
        else:
            print("Translation response error:", response_data)
    else:
        print("Translation request failed. Error:", response.text)

    return "Translation failed"

def main():
    """
    Prompt the user to choose the source language.
    If the source language is English, prompt the user to choose the target language.
    If the source language is not English, set the target language to English by default.
    """
    source_language = input("Please choose the source language (English, Luganda, Runyankole, Ateso, Lugbara, or Acholi): ")

    if source_language.lower() == "english":
        target_language = input("Please choose the target language (Luganda, Runyankole, Ateso, Lugbara, or Acholi): ")
    else:
        target_language = "english"

    # Ask the user for the text to be translated
    text = input("Enter the text to translate from the source language chosen: ")

    # Call the translate_text function to perform the translation
    translated_text = translate_text(text, source_language.lower(), target_language.lower())
    
    print("Translated Text: ", translated_text)


if __name__ == "__main__":
    main()
