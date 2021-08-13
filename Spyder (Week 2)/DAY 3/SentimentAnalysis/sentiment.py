from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = analyzer.polarity_scores(sentence)
    
    print("Overall sentiment dictionary is : ", sentiment_dict)
    
    print("\nsentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

    if sentiment_dict['compound'] >= 0.05:
        overall = 'Positive'
    elif sentiment_dict['compound'] <= -0.05:
        overall = 'Negative'
    else:
        overall = 'Neutral'
        
    print("\nSentence Overall Rated As: ", overall)
 
sentence_list = ['I really like playing video games',
                 'My week has been the same as always',
                 'I did not feel well yesterday']
 
for sentence in sentence_list:
    print('-------------------------------------------')
    print(sentence)
    sentiment_scores(sentence)