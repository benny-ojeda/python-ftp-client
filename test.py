a = 'cd'
if len(a.split()) == 2 and a.split(' ', 1)[0] == 'cd':
        # second_word=a.split(' ', 1)[1]
        # print(second_word)
        print(len(a))
else:
    #len(a.split()) == 2 and a.split(' ', 1)[0] == 'cd':
    print("missing arg")