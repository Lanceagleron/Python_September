from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models import award_model

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
    def create(cls, data):
        query = "INSERT INTO dogs (name, breed, color, age) VALUES (%(name)s, %(breed)s, %(color)s, %(age)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dogs;"
        result = connectToMySQL(DATABASE).query_db(query)
        # print(result)
        all_dogs = []
        for row_from_db in result:
            dog_instance = cls(row_from_db) #instantiates dog object from row in db
            all_dogs.append(dog_instance) #add instance to list of instances
        return all_dogs#returns list of dog instances

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dogs WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) > 0:
            dog_instance = cls(results[0])
            return dog_instance
        return False

    @classmethod
    def get_one_with_awards(cls,data):
        query = "SELECT * FROM dogs LEFT JOIN awards ON dogs.id = awards.dog_id WHERE dogs.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if len(results) > 0:
            dog_instance = cls(results[0])
            award_list = []
            for row_from_db in results:
                award_data = {
                    'id' : row_from_db['awards.id'],
                    'title' : row_from_db['title'],
                    'created_at' : row_from_db['awards.created_at'],
                    'updated_at' : row_from_db['awards.updated_at'],
                    'dog_id' : row_from_db['dog_id']
                }
                award_instance = award_model.Award(award_data)
                award_list.append(award_instance)
            dog_instance.award_list = award_list
            return dog_instance
        return False

    @classmethod
    def update(cls,data):
        query = "UPDATE dogs SET name = %(name)s, breed = %(breed)s, color = %(color)s, age = %(age)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dogs WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)


    @staticmethod
    def validator(data):
        is_valid = True
        if len(data['name']) <= 0:
            print("name is not valid")
            flash("name is not valid")
        is_valid = False

    
        if len(data['breed']) <= 0:
            print("breed is not valid")
            flash("breed is not valid")
        is_valid = False

    
        if len(data['color']) <= 0:
            print("color is not valid")
            flash("color is not valid")
        is_valid = False

    
        if len(data['age']) <= 0:
            print("age is not valid")
            flash("age is not valid")
        is_valid = False
        return is_valid
















