st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 't':
        print(word)

for word in st.split():
    if len(word)%2 == 0:
        print(word+" <-- has an even length!")
        

