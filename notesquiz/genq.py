from textblob import TextBlob, Word
from collections import namedtuple
import sys

conjunctions = ['because', 'since', 'as']
def generate(text):
    questions = []
    tb = TextBlob(text)
    for sentence in tb.sentences:
        pos = dict(sentence.tags)
        # print(pos)
        keys = list(pos.keys())
        # print(' '.join(key for key in keys))
        values = list(pos.values())
        # print(' '.join(value for value in values))
        """ Questions for 3rd person singular present verbs """
        if 'VBZ' in values:
            idx = values.index('VBZ')
            if values[0] != 'NNP':
                keys[0] = keys[0].lower()
            else:
                obj = ' '.join(key for key in keys[idx:])
                question = f"Who {obj}?" # Who does obj?
                questions.append(question)  
            subject = ' '.join(key for key in keys[:idx])
            if values[idx+1] == 'VBG':
                question = f"What {keys[idx]} {subject} {keys[idx+1]}?" # What is he doing?
            elif values[idx+1] == 'VBN':
                question = f"What {keys[idx]} {subject} {keys[idx+1]}?" # What has he done?
            else:
                if keys[idx] == 'is':
                    if values[idx+1] == 'JJ':
                        question = f"How {keys[idx]} {subject}?" # How is subject?
                    else:
                        question = f"What {keys[idx]} {subject}?" # What is noun?
                else:
                    question = f"What does {subject} {keys[idx].lemmatize('v')}?" # What does he do?
            questions.append(question)
            
        """ Questions for non-3rd person singular present verbs """
        if 'VBP' in values:
            idx = values.index('VBP')
            if values[0] != 'NNP':
                keys[0] = keys[0].lower()
            else:
                obj = ' '.join(key for key in keys[idx:])
                question = f"Who {obj}?" # Who does obj?
                questions.append(question)  
            subject = ' '.join(key for key in keys[:idx])
            if values[idx+1] == 'VBG':
                question = f"What {keys[idx]} {subject} {keys[idx+1]}?" # What are they doing?
            elif values[idx+1] == 'VBN':
                question = f"What {keys[idx]} {subject} {keys[idx+1]}?" # What have they done?
            else:
                if keys[idx] == 'are':
                    if values[idx+1] == 'JJ':
                        question = f"How {keys[idx]} {subject}?" # How are subject?
                    else:
                        question = f"What {keys[idx]} {subject}?" # What are noun?
                else:
                    question = f"What do {subject} {keys[idx]}?" # What do they do?
            questions.append(question)

        """ Questions for past verbs """
        if 'VBD' in values:
            idx = values.index('VBD')
            if values[0] != 'NNP':
                keys[0] = keys[0].lower()
            else:
                obj = ' '.join(key for key in keys[idx:])
                question = f"Who {obj}?" # Who does obj?
                questions.append(question)  
            subject = ' '.join(key for key in keys[:idx])
            if keys[idx] == 'was' or keys[idx] == 'were':
                if values[idx+1] == 'JJ':
                    question = f"How {keys[idx]} {subject}?" # How was/were subject?
                elif values[idx+1] == 'VBG':
                    question = f"What {keys[idx]} {subject} {keys[idx+1]}?" # What was/were they/he doing?
                else:
                    question = f"What {keys[idx]} {subject}?" # What was/were noun?
            else:
                question = f"What did {subject} {keys[idx].lemmatize('v')}?" # What did they/he do?
            questions.append(question)

        """ Questions for modal verbs"""
        if ['MD', 'VB'] in [values[i:i+2] for i in range(len(values) - 1)]:
            idx = values.index('MD')
            if values[0] != 'NNP':
                keys[0] = keys[0].lower()
            else:
                obj = ' '.join(key for key in keys[idx:])
                question = f"Who {obj}?" # Who does obj?
                questions.append(question)  
            subject = ' '.join(key for key in keys[:idx])
            question = f"What {keys[idx]} {subject} {keys[idx+1]}?" # What will they/he do?
            questions.append(question)     

        """ Why questions """
        for conj in conjunctions:
            if conj in keys:
                idx = keys.index(conj)
                phrase = ' '.join(key for key in keys[:idx])
                question = f"Why {phrase}?"
                questions.append(question)   
        else:
            # print('no question')
            question = 'No question'

    return questions

if __name__ == "__main__":
    with open("test.txt") as f:
        text = f.read()
        print(generate(text))
