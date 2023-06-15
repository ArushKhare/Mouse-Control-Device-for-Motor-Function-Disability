from next_word_prediction import GPT2

gpt = GPT2()

def word_generate(phrase, num_of_suggestions):
    return gpt.predict_next(phrase, num_of_suggestions)

#print(word_generate("Hi, how", 10))