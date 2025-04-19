#set up your environment
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#first gather your data from any browser or anything;
#next label your data as below
reviews = ['This movie was fantastic! A must-watch.',
           'I didn\'t enjoy this movie at all.',
           'Amazing storyline and great acting!',
           'The plot was dull and predictable.',
           'Loved the cinematography! Highly recommended.']

labels = ['positive', 'negative', 'positive', 'negative', 'positive']
#vectorize your text data(Convert your text data into numbers that the 
#computer can understand using CountVectorizer:)
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)
#split your data(Split your data into training and testing sets so the computer can 
#learn from some data and be tested on the rest)
x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)
#train the model(Create a Naive Bayes classifier and train it using the training data)
model = MultinomialNB()
model.fit(x_train, y_train)
#test the model(Use the trained model to predict the vibes of the test data)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print('Accuracy:', accuracy)
#interpret the result(Finally, you can decide if the movie has "Good vibes!"
#based on the accuracy of your model. If the accuracy is above 80%, print "Good vibes!)
if accuracy > 0.8:
  print('Good vibes. Book the ticket!')
else:
  print('Needs more work!')