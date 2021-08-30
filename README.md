# language-translator
The project is made using IBM Watson Cloud studio.
It requires an API key and unique URL to get the language translator.
And then to get the language codes for different languages we use JSON_Normalize from Pandas.
Using these codes we pass them into model_id attribute of translate method. 
For eg: translation_hindi = language_translator.translate(text=english_text, model_id='en-hi') for English to Hindi conversion.
Then, we use get_result() method to get the result of translation.
Lastly, to get the translated data/sentence we use translation['translations'][0]['translation'] to access the converted sentence.
