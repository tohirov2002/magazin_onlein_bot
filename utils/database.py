import sqlite3

class Database:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def get_categories(self):
        categories = self.cursor.execute("SELECT id,category_name FROM categories;")
        return categories
    def add_category(self,new_cat):
        categories = self.cursor.execute(
            "SELECT id,category_name FROM categories WHERE category_name=?;",
            (new_cat,)
        ).fetchone()
        if not categories:
            try:
                self.cursor.execute(
                    "INSERT INTO categories(category_name) VALUES(?);",
                    (new_cat,)
                )
                self.conn.commit()
                res = {
                    'status': True,
                    'desc': 'Successfully added'
                }
                return res
            except Exception as e:
                res = {
                    'status': False,
                    'desc': 'Something error, please, try again'
                }
                return res
        else:
            res = {
                'status': False,
                'desc': 'exists'
            }
            return res
    def upd_category(self,new_cat,old_cat):
        categories = self.cursor.execute(
            "SELECT id,category_name FROM categories WHERE category_name=?;",
            (new_cat,)
        ).fetchone()
        if not categories:
            try:
                self.cursor.execute(
                    "UPDATE categories SET category_name=? WHERE category_name=?;",
                    (new_cat,old_cat)
                )
                self.conn.commit()
                res = {
                    'status': True,
                    'desc': 'Successfully update'
                }
                return res
            except Exception as e:
                res = {
                    'status': False,
                    'desc': 'Something error, please, try again'
                }
                return res
        else:
            res = {
                'status': False,
                'desc': 'exists'
            }
            return res
    def del_category(self,cat_name):
        try:
            self.cursor.execute(
                "DELETE FROM categories WHERE category_name=?",
                (cat_name,)
            )
            self.conn.commit()
            return True
        except:
            return False

    def edit_category(self,new_name,id):
        try:
            self.cursor.execute(
                "UPDATE categories SET category_name=? WHERE id=?",
                (new_name,id)
            )
            self.conn.commit()
            return True
        except:
            return False

    def add_product(self,name,image,category_name):
        try:
            self.cursor.execute(
                "INSERT INTO products(product_name,product_image,product_category) VALUES(?,?,?);",
                (name,image,category_name)
            )
            self.conn.commit()
            return True
        except:
            return False


    def get_categorie(self,category_name):
        category = self.cursor.execute(
            "SELECT category_name FROM categories WHERE category_name=?;",
            (category_name,)
        )
        if category.fetchone():
            return True
        return False

    def get_products(self,cat_id):
        products = self.cursor.execute(
            "SELECT id,product_name,product_image FROM products WHERE product_category=?;",
            (cat_id,)
        )
        return products


