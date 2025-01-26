class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                words = []
                for j in file:
                    for k in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        j = j.replace(k, '')
                    words.extend(j.lower().split())
                    all_words[i] = words
        return all_words

    def find(self, word):
        found = {}
        for i, j in self.get_all_words().items():
            for k in j:
                if word.lower() == k:
                    index = j.index(k) + 1
                    found[i] = index
        return found

    def count(self, word):
        counted = {}
        for i, j in self.get_all_words().items():
            counter = 0
            for k in j:
                if word.lower() == k:
                    counter += 1
                    counted[i] = counter
        return counted

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))