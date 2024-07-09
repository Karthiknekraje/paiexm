class Crossword:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
    
    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()
    
    def can_place_word_horizontally(self, word, row, col):
        if col + len(word) > self.size:
            return False
        return all(self.grid[row][col + i] in (' ', word[i]) for i in range(len(word)))
    
    def can_place_word_vertically(self, word, row, col):
        if row + len(word) > self.size:
            return False
        return all(self.grid[row + i][col] in (' ', word[i]) for i in range(len(word)))
    
    def place_word_horizontally(self, word, row, col):
        for i in range(len(word)):
            self.grid[row][col + i] = word[i]
    
    def place_word_vertically(self, word, row, col):
        for i in range(len(word)):
            self.grid[row + i][col] = word[i]
    
    def add_word(self, word):
        for row in range(self.size):
            for col in range(self.size):
                if self.can_place_word_horizontally(word, row, col):
                    self.place_word_horizontally(word, row, col)
                    return True
                if self.can_place_word_vertically(word, row, col):
                    self.place_word_vertically(word, row, col)
                    return True
        return False

def main():
    size = 10  # Size of the crossword grid
    words = ['python', 'java', 'ruby', 'javascript', 'html', 'css']
    
    crossword = Crossword(size)
    for word in words:
        if not crossword.add_word(word):
            print(f"Couldn't place the word: {word}")
    
    crossword.display()

if __name__ == "__main__":
    main()
