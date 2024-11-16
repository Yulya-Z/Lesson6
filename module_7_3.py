import re
class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                all_words[name] = []
                for line in file:
                    line = line.lower()
                    re.split(r"[,.=!?;:-]:\W", line)
                    line.split()
                    all_words[name].append(line)

        return all_words

    def find(self, word):
        book1 = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                book1[file_name] = words.index(word)
        return book1

    def count(self, word):
        book2 = {}
        all_word = self.get_all_words()
        for file_name, words in all_word.items():
            book2[file_name] = words.count(word)
        return book2

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

