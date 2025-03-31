from collections import defaultdict

def keyword_index(docs):
    # implement this
    d = {}
    for idx, doc in enumerate(docs):
        for word in doc.split():
            if word in d:
                if idx in d[word]:
                    d[word][idx] +=1
                else:
                    d[word][idx] = 1
            else:
                d[word] = {idx: 1}
    return d

# Implementation using defaultDict


def keyword_index_1(docs):
    index = defaultdict(lambda: defaultdict(int))

    for idx, doc in enumerate(docs):
        for word in doc.split():
            index[word][idx] +=1
    for word in index:
        index[word] = dict(index[word])
    return dict(index)



if __name__ == '__main__':
    docs = ["Hello world", "world of python", "python is a snake"]
    print(keyword_index_1(docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}