# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "googletrans",
# ]
# ///
import asyncio
import sys
from googletrans import Translator

sys.stdout.reconfigure(encoding="utf-8")

async def auto_translate(text):
    translator = Translator()
    
    # Detect the source language
    detection = await translator.detect(text)
    source_lang = detection.lang
    
    # Determine the destination language
    if 'zh' in source_lang:
        dest_lang = 'en'
        dest_lang_name = 'English'
    else:
        dest_lang = 'zh-cn'
        dest_lang_name = 'Chinese'
        
    # Translate the text
    translated_result = await translator.translate(text, dest=dest_lang)
    return translated_result.text, dest_lang_name

async def main():
    if len(sys.argv) < 2:
        return  # Exit silently if no input is provided

    sentence_to_translate = sys.argv[1]
    translated_text, target_language = await auto_translate(sentence_to_translate)

    # Generate HTML output for GoldenDict
    html_output = f"""
<div style="font-family: sans-serif; padding: 5px;">
    <h2 style="color: #333; font-size: 1.2em; margin-bottom: 5px;">Translation ({target_language})</h2>
    <p style="font-size: 1.1em; margin: 0;">{translated_text}</p>
</div>
"""
    print(html_output)

if __name__ == "__main__":
    asyncio.run(main())
