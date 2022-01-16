import random

text=[]
with open('toeic_vocabulary.txt','r',encoding='utf-8') as f:
    for r in f:
        if r != '\n':
            text.append(r.replace('\n',''))

while True:
    print(len(text))
    que=random.choice(text)
    text.remove(que)
    eng, *chi=que.split(' ')
    ans=input(eng+'  ')
    print(' '.join(chi)) 