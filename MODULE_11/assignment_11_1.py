class Publication:
    def __init__(self, name):
        self.name = name


class Book:
    def __init__(self, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)


    def print_information(self):



class Magazine:
    def __init__(self, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)


    def print_information(self):
