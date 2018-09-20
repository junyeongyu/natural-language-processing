# natural-language-processing

Semantic slot filling: CFG
 - Context-free grammar and parsing
 - Traning corpus (ORIG, DEST, DATE): ex) show me flights from Boston...
 - Probabilistic graphical model
  -> Conditional Random Field (CRF)

Semantic slot filling: LSTM
 - Big training corpus
 - No feature generation
 - Defining the model
 - Training ..

Linguistic knowledge in NLP
NLP Pyramid
- Pragmatics
- Semantics
- Syntax
- Morphology

Libraries and tools
 - NLTK
 - Stanford parser
 - spaCy
 ...

Linguistic knowledge
 - ideas and evaluation
 - WordNet, BabelNet, etc..
 
Linguistic knowledge + Deep learning
 - Task: Question answering /reasoing
 - Linigusitic links: co-reference (red), hypernyms (green)
 - Method: DAG-LSTM
 
Syntax: constituency tree
Sentiment analysis

Bag of words (BOW)
 - Le's count occurences of a particluar token in our text
 - Motivation: we are looking for marker words like "exceelt" or "disappointed"
 - for each token we will have a feature colume, this is called **text vectorization**
 - but problem is it is losing order and couters are not normalized

Let's preserve some ordering (n-grams): problem is too many features
 - ex) a hu..
 
So, remove some n-grams based on occurence frequencies
 - *High grequecny n-grams* : call as *stop-words* -> so need to be removed
 - *low frequency n-grams* : typo, can be overfit -> so need to be removed
 - *Medium frequency n-grams*: those are good n-grams

TF-IDF (Term Frequency Inverse Document Frequency)
 - tf(t,d) - frequency for term (or n-gram) t in document d
 - wighting sceme: binary, ...
 - idf(t, D) = log (N/[formular])
 - tfidf(t,d,D0 = tf(t,d) * idf(t,D)
 - a high weeight in TF-IDF is reached by a high term frequency and a low document frenqucy of the erm in the hole colelciton of documents
