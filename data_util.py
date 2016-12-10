import pickle

def read_data():
	train_set = pickle.load(open("data/Training.dialogues.pkl","rb"))
	test_set = pickle.load(open("data/Test.dialogues.pkl","rb"))
	validation_set = pickle.load(open("data/Validation.dialogues.pkl","rb"))
	dictionary = pickle.load(open("data/Dataset.dict.pkl","rb"))
	print test_set

