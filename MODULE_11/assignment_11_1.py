class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self,name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)


    def print_information(self):
        print(f" name of publication: {self.name} name of author : {self.author} , page count: {self.page_count}")



class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)


    def print_information(self):
        print(f"name of publication is : {self.name}")
        print(f"name of chief editor is: {self.chief_editor}")


teos=Magazine("Donald Duck","Aki Hyyppä")
teos1=Book("Compartment No.6", "Rosa Liksom", 192)
teos.print_information()
teos1.print_information()

