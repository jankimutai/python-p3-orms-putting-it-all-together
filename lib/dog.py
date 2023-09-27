import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    all = []
    def __init__(self,name,breed):
        self.id=id
        self.name = name
        self.breed = breed
    @classmethod
    def create_table(self):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS dogs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT
        )
        """)

    def drop_table():
        CURSOR.execute('''DROP TABLE IF EXISTS dogs''')
    
    def save(self):
        sql = ('''INSERT INTO dogs (name, breed) VALUES (?,?)''')
        CURSOR.execute(sql , (self.name,self.breed))
        CONN.commit()
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM dogs").fetchone()[0]
    @classmethod
    def create(self,name,breed):
        dog = Dog(name,breed)
        dog.save()
        return dog
    @classmethod
    def new_from_db(cls, row):
        dog = cls(row[1], row[2])
        dog.id = row[0]
        return dog
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM dogs"
        all = CURSOR.execute(sql).fetchall()
        cls.all = [cls.new_from_db(row) for row in all]
        return cls.all
    
    @classmethod
    def find_by_name(cls,name):
        sql = """
            SELECT * 
            FROM dogs 
            WHERE name = ? 
            LIMIT 1
        """
        dog= CURSOR.execute(sql, (name,)).fetchone()
        # if dog is None:
        #     return None
        if dog:
            return cls.new_from_db(dog)
        
    @classmethod
    def find_by_id(cls,id):
        sql = """
            SELECT * 
            FROM dogs 
            WHERE id = ? 
            LIMIT 1
        """
        dog = CURSOR.execute(sql, (id,)).fetchone()
        return cls.new_from_db(dog)
    @classmethod
    def find_or_create_by(cls,name,breed):
        sql = """
            SELECT * 
            FROM dogs 
            WHERE name = ? 
            LIMIT 1
        """
        dog = CURSOR.execute(sql, (name,)).fetchone()
        if dog == None:
            dog = Dog(name,breed)
            dog.save()
        return dog
    def update(self):
        sql = '''
            UPDATE dogs 
            SET  name = ?, breed = ?  
            WHERE id = ? '''
        CURSOR.execute(sql, ( self.name,self.breed,self.id))
        #CONN.commit()
        
    
    

    
    
    
        



 

