# Spam Classifier using NLP 🔍

This project implements a spam classifier using Flask 🌐, a web framework for Python 🐍. The spam classifier is built using machine learning techniques to classify text messages as spam or not spam.

## Overview ℹ️

The spam classifier utilizes a machine learning model trained on a dataset of text messages. It preprocesses the text data by tokenizing, removing punctuation, stopwords, and stemming words. The preprocessed text is then transformed into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency).

The trained machine learning model is deployed as a web application using Flask. Users can input text messages into a form, and the application will classify whether the message is spam or not spam in real-time.

### Text Preprocessing 📝

Text preprocessing is a crucial step in preparing the input data for machine learning. In this project, the `clean_data()` function is responsible for cleaning and preprocessing the text input. Here's what it does:

- **Lowercasing**: Converts the text to lowercase to ensure consistency.
- **Tokenization**: Splits the text into individual words or tokens.
- **Punctuation Removal**: Removes punctuation marks from the text.
- **Stopword Removal**: Filters out common English stopwords using NLTK's stopwords corpus.
- **Stemming**: Reduces words to their base or root form using the Porter stemming algorithm.

### Machine Learning Model 🤖

The heart of the spam classifier is the machine learning model trained to classify text messages as spam or not spam. In this project, a logistic regression model is used for classification. The model is trained on a dataset of labeled text messages and learns to predict whether a given message is spam or not spam based on its features extracted using TF-IDF.

### Pickled Files 📦

The trained machine learning model and TF-IDF vectorizer are serialized and saved as pickled files (`model.pkl` and `vector.pkl`, respectively). These files are loaded into memory when the Flask application starts, allowing the application to make predictions in real-time without retraining the model.

### Contributing 🚀

Contributions to this project are welcome! Whether you have ideas for improvements, new features, or bug fixes, we'd love to hear from you. Here's how you can contribute:

1. Fork the repository to your own GitHub account.
2. Clone the repository to your local machine.
3. Make your changes and enhancements.
4. Commit and push your changes to your fork.
5. Submit a pull request to the main repository, detailing the changes you've made and why they should be included.

I appreciate any contributions that help make this project better for everyone! 🙌

