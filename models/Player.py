class Player:

    """ this class define the players details -
     name and age, and has a methods that calculated his/hers score in the game"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
#  how do i init an ID for each user?

    def user_score(self):
        pass  # should calculate the user score to later place him in the score table

# - the instance from this class should be written to the db table: 'players'
