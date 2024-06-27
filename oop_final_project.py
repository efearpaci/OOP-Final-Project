import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image, ImageTk

class Dictionary:
    def __init__(self):
        self.dictionary = {}
        self.load_data()

    def add_word(self, word, meaning):
        self.dictionary[word] = meaning
        with open("dictionary.txt", "a") as f:
            f.write(f"{word} : {meaning}\n")

    def get_meaning(self, word):
        return self.dictionary.get(word, "Word not found in dictionary")

    def list_words(self):
        return ", ".join(self.dictionary.keys())

    def delete_word(self, word):
        if word in self.dictionary:
            del self.dictionary[word]
            self.update_file()
        else:
            return "Word not found in dictionary"

    def load_data(self, file_path="dictionary.txt"):
        try:
            with open(file_path, "r") as f:
                for line in f:
                    parts = line.strip().split(":")
                    if len(parts) == 2:
                        word, meaning = parts
                        self.dictionary[word.strip()] = meaning.strip()
        except FileNotFoundError:
            pass

    def update_file(self, file_path="dictionary.txt"):
        with open(file_path, "w") as f:
            for word, meaning in self.dictionary.items():
                f.write(f"{word} : {meaning}\n")

class DictionaryApp:
    def __init__(self, root):
        self.dictionary = Dictionary()
        self.root = root

        self.word_label = tk.Label(root, text="Enter word:")
        self.word_label.grid(row=0, column=0, sticky="W")
        self.word_entry = tk.Entry(root)
        self.word_entry.grid(row=0, column=1, sticky="EW")

        self.meaning_label = tk.Label(root, text="Enter meaning:")
        self.meaning_label.grid(row=1, column=0, sticky="W")
        self.meaning_entry = tk.Entry(root)
        self.meaning_entry.grid(row=1, column=1, sticky="EW")

        self.add_button = tk.Button(root, text="Add Word", command=self.add_word)
        self.add_button.grid(row=2, column=0, columnspan=2, sticky="EW")

        self.get_button = tk.Button(root, text="Get Meaning", command=self.get_meaning)
        self.get_button.grid(row=3, column=0, columnspan=2, sticky="EW")

        self.list_button = tk.Button(root, text="List Words", command=self.list_words)
        self.list_button.grid(row=4, column=0, columnspan=2, sticky="EW")

        self.delete_button = tk.Button(root, text="Delete Word", command=self.delete_word)
        self.delete_button.grid(row=5, column=0, columnspan=2, sticky="EW")

        self.extra_button = tk.Button(root, text="Extra", command=self.show_image)
        self.extra_button.grid(row=7, column=0, columnspan=2, sticky="EW")

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.grid(row=8, column=0, columnspan=2, sticky="EW")

        root.columnconfigure(1, weight=1)

        for i in range(9):
            root.rowconfigure(i, weight=1)

    def show_image(self):
        image_window = tk.Toplevel(self.root)
        try:
            image = Image.open("/Users/sezinerz/Downloads/breakingbad_meme.jpg")
        except FileNotFoundError:
            mb.showerror("Error", "Image file not found")
            return
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(image_window, image=photo)
        label.image = photo
        label.pack()

    def add_word(self):
        word = self.word_entry.get()
        meaning = self.meaning_entry.get()
        if not word or not meaning:
            mb.showerror("Error", "Word or meaning cannot be empty")
            return
        self.dictionary.add_word(word, meaning)
        mb.showinfo("Success", f"{word} added successfully")

    def get_meaning(self):
        word = self.word_entry.get()
        if not word:
            mb.showerror("Error", "Word cannot be empty")
            return
        meaning = self.dictionary.get_meaning(word)
        mb.showinfo("Meaning", f"Meaning of '{word}': " + meaning)

    def list_words(self):
        words = self.dictionary.list_words()
        if not words:
            mb.showerror("Error", "No words in the dictionary")
            return
        mb.showinfo("Words", words)

    def delete_word(self):
        word = self.word_entry.get()
        if not word:
            mb.showerror("Error", "Word cannot be empty")
            return
        result = self.dictionary.delete_word(word)
        if result is None:
            mb.showinfo("Success", f"{word} deleted successfully")
        else:
            mb.showinfo("Error", result)

def main():
    root = tk.Tk()
    root.title("Dictionary App")
    app = DictionaryApp(root)
    root.mainloop()

main()