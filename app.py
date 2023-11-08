from flask import Flask
from controller.user_controller import UserController
from controller.product_controller import ProductController

app = Flask(__name__)

user_controller = UserController()
product_controller = ProductController()

@app.route('/user/getAll',methods=["GET"])ss
def getAllUSer():
    return user_controller.user_get_all_Controller()

@app.route('/user/add',methods=["POST"])
def addOne():
    return user_controller.user_get_addOne_Controller()

@app.route('/user/update',methods=["PUT"])
def updateOne():
    return user_controller.user_Update_Controller()


@app.route('/user/delete/<id>',methods=["DELETE"])
def deleteOne(id):
    return user_controller.user_delete_Controller(id)
if __name__ == '__main__':
    app.run(debug=True)
