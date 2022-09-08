from mysqlconnection import connectToMySQL
DATABASE = 'dogs_db'

class Dog:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.breed = data['breed']
        self.color = data['color']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dogs;"
        result = connectToMySQL(DATABASE).query_db(query)
        # print(result)
        all_dogs = []
        for row_from_db in result:
            dog_instance = cls(row_from_db) #instantiates dog object from row in db
            all_dogs.append(dog_instance) #add instance to list of instances
        return all_dogs