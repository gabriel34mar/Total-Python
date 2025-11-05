#Replace in the following sentence:
#"If the implementation is hard to explain, it might be a bad idea."
#the following pairs of words:
#"hard" --> "easy"
#"bad" --> "good"
sentence="If the implementation is hard to explain, it might be a bad idea."
sentence1=sentence.replace("hard","easy")
sentence2=sentence1.replace("bad","good")
print(sentence2)