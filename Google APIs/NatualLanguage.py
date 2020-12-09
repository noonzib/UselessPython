# Imports the Google Cloud client library
from google.cloud import language_v1


# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = u"Hello World"
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

print("Text : {}, Sentiment: {}, {}".format(text,sentiment.score, sentiment.magnitude))