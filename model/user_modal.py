import mysql.connector
import json
class user_modal():
    def __init__(self):
       try:
          self.con = mysql.connector.connect(host="localhost",user="root",password="Bhushan@1234",database="flask_tutorial")
          self.con.autocommit =True
          self.cur = self.con.cursor(dictionary=True)
       except:
           print("some error")
           
    def user_getAll_modal(self):
        self.cur.execute("SELECT * FROM users")
        result =self.cur.fetchall()
        if len(result)>0:
          return json.dumps(result)
        else :
           return "No data found"
        
    def user_addOne_modal(self, data):
            self.cur.execute(f"INSERT INTO users(name, email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
            print(data)
            return "User created successfully..!!!"
    
    def user_update_modal(self, data):
            self.cur.execute(f"UPDATE  users SET name='{data['name']}', email ='{data['email']}',phone = '{data['phone']}',role = '{data['role']}',password= {data['password']} WHERE id = '{data['id']}'")
            if self.cur.rowcount> 0:
             return "User updated successfully..!!!"
            else:
                return "NOthing to change"
            

    
    def user_delete_modal(self, id):
            self.cur.execute(f"DELETE  FROM users   WHERE id = {id}")
            if self.cur.rowcount> 0:
             return "User deleted successfully..!!!"
            else:
                return "Not deleted"     ss   