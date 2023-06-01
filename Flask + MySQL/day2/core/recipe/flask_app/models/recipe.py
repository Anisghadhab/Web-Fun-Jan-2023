from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
import re
from flask_app.models import user
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



class Recipe:
    # CONSTRUCTOR -
    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.date = data ['date']
        self.under = data["under"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.poster = user.User.get_by_id({'id':self.user_id}).first_name

    # CREATE A USER
    @classmethod
    def create_recipe(cls, data):
        
        query = """
                    INSERT INTO recipes (user_id, name, description, instruction, date, under)
                    VALUES	(%(user_id)s, %(name)s, %(description)s, %(instruction)s, %(date)s, %(under)s);
                """
        
        result =  connectToMySQL(DB).query_db(query, data)
        # print(result,'-'*33)
        return result
    # GET USER BY ID
    
    @classmethod
    def update(cls, data):
        
        
        query = """
        UPDATE recipes SET name = %(name)s, description = %(description)s, instruction= %(instruction)s , date = %(date)s, under= %(under)s
        WHERE id = %(id)s;
        """""
        
        result =  connectToMySQL(DB).query_db(query, data)
        print(result,'-'*33)
        return result
    
    
    @classmethod
    def delete (cls,data):
        query = """
        DELETE FROM recipes WHERE id = %(id)s;

        """
        result = connectToMySQL(DB).query_db(query, data)
        return result
    @classmethod
    def get_recipe_with_user():
        query ="""
        SELECT * FROM recipes
        JOIN users
        ON recipes.user_id = users.id
        WHERE 
        """
    
    
    @classmethod
    def get_all_with_users(cls):
        query ="""
                SELECT * FROM recipes
                JOIN users 
                ON recipes.user_id = users.id
            """
        results = connectToMySQL(DB).query_db(query)
        # print(results,"--------------------")
        list_of_recipes = []
        for row in results:
            this_recipe = cls(row)
            
            recipe_user = {
                **row,
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
                "id": row["users.id"]
            }
            
            this_recipe.user = user.User(recipe_user)
            list_of_recipes.append(this_recipe)
        return list_of_recipes
    @classmethod
    def get_recipe_by_id(cls, data):
        query = """
                    SELECT *
                    FROM recipes
                    WHERE id = %(id)s;
                """
                
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:
            return []
        return cls(results[0])
    # VALIDATION
    
    # @classmethod
    # def get_by_email(cls, data):
    #     query = """
    #                 SELECT *
    #                 FROM users
    #                 WHERE email = %(email)s;
    #             """
                
    #     results = connectToMySQL(DB).query_db(query, data)
    #     if len(results) < 1:
    #         return []
    #     return cls(results[0])
    
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name'])< 2:
            flash("Name must be at least 3")
            is_valid = False
        if len(data['description'])< 10:
            flash("Description too short")
            is_valid = False
        if len(data['instruction'])< 10:
            flash("Instructions too short")
            is_valid = False
        if data["date"] == "":
            flash("Date is required")
            is_valid = False
        return is_valid
    