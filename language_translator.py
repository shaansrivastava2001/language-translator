from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



url_lt = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/389816eb-3af3-4e07-9617-6c7ae679f367'
apikey_lt = 'e6a04_edLPSpQ4pWS8-Pl9aeGKfizPiLp4IMyCNPlP3M'

version_lt = '2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)



language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)

print(language_translator)



from pandas import json_normalize

x = json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")
for i in range(len(x['language'])):
    if x['name'][i]=='Hindi':
        print(x['language'][i],x['name'][i],i)
        
    if x['language'][i]=='en':
        print(x['language'][i],x['name'][i],i)        



english_text = input("Enter the sentence to convert to Hindi:")
translation_hindi = language_translator.translate(text=english_text, model_id='en-hi')


translation = translation_hindi.get_result()
print("Translation dictionary: ",translation)

#accessing the translation result from the dictionary
translation_hin = translation['translations'][0]['translation']
print("Original sentence in English: ",english_text)
print("Sentence tranlsated to hindi: ",translation_hin)