class WordDictionary:

    def __init__(self):
        self.bucket = []

    def addWord(self, word: str) -> None:
        self.bucket.append(word)

    def search(self, word: str) -> bool:
        for strr in self.bucket:
            if len(strr) != len(word):
                continue
            matched = True
            for s, w in zip(strr, word):
                if w == '.':
                    continue
                if s!=w and w!='.':
                    matched = False
            if matched == True:
                return True
        return False
