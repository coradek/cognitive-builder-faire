import os
import json
from os.path import join, dirname
from dotenv import load_dotenv
from watson_developer_cloud import AlchemyLanguageV1 as AlchemyLanguage

def get_text_sentiment(alchemy_language, text):
  dotenv_path = join(dirname(__file__), '.env')
  load_dotenv(dotenv_path)
  
  result = alchemy_language.sentiment(text=text)
  if result['docSentiment']['type'] == 'neutral':
    return 'netural', 0
  return result['docSentiment']['type'], result['docSentiment']['score']

def main():
  alchemy_api_key = os.environ.get("ALCHEMY_API_KEY")
  alchemy_language = AlchemyLanguage(api_key=alchemy_api_key)

  text = "I hate galvanize"
  
  sentiment, score = get_text_sentiment(alchemy_language, text)
  print(sentiment, score)  

if __name__ == '__main__':
  main()