from langdetect import detect

def identify_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Unknown"
    
text = "This is a sample text to identify its language."

language = identify_language(text)
print(f"The language of the text is: {language}")