# Bag-of-words (The order does not matter)

* "I like eggs" => Feature vector = [vec("I") + vec("like") + vec("eggs")] / 3
* Use any classifier: Naive Bayers, Logistic Regression, Random Forest, Extra Trees, Etc..


# Exercise for lator

* RNN
* Embedding layer (word embedding matrix)
* Recurrent unit: Simple unit, GRU, or LSTM
* Dense layer: maps recurrent unit's output to one of the output classes
* Each leaf node is a word
* Once you've set the pretrained embedding, don't update it at all during training

# Bigrams and Language Models
* Language model: a model of the probability of a sequence of words
* p("The quick brown fox jumps over the laze dog.")

## What is a model
* Model si never correct
* Bigram model: p(w_t | w_(t-1))

## What is a bigram
* Bigram: 2 consecrutive words in a sentence

## Trigrams and N-grams
* Tigrams: The quick dream

