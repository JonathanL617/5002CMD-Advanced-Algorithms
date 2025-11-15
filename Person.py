class Person:
    def __init__(self, user_id, name, gender, age, biography, privacy="public"):
        self.__user_id = user_id
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__biography = biography
        self.__privacy = privacy #public or private

    #getter
    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def get_biography(self):
        return self.__biography

    def get_privacy(self):
        return self.__privacy

    #setter
    def set_name(self,name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_age(self, age):
        self.__age = age

    def set_biography(self, biography):
        self.__biography = biography

    def set_privacy(self, privacy):
        self.__privacy = privacy

    #print
    def display_profile(self, respect_privacy=False):
        print(f'User Profile - @{self.__user_id}')
        print("=" * 50)
        print(f'Name: {self.__name}')

        if respect_privacy and self.__privacy == "private":
            print(f'Privacy: {self.__privacy}')
            print("This account is private. Account details are hidden")

        else:
            print(f'Gender: {self.__gender}')
            print(f'Age: {self.__age}')
            print(f'Biography: {self.__biography}')
            print(f'Privacy: {self.__privacy}')

        print("=" * 50)