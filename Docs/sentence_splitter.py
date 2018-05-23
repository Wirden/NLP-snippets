from nltk.tokenize import word_tokenize, sent_tokenize

def split_into_sentences(text):

	sentences = sent_tokenize(text)
	return sentences