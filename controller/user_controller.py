from model.user_modal import user_modal
from flask import request
class UserController:
    def user_get_all_Controller(self):
        return user_modal().user_getAll_modal()

    def user_get_addOne_Controller(self):
        if request.method == 'POST':
            data = request.form
            return user_modal().user_addOne_modal(data) ss
        else:
            return "Invalid request method"
        
    def user_Update_Controller(self):
        data = request.form
        return user_modal().user_update_modal(data)
    
    
    def user_delete_Controller(self,id):
        return user_modal().user_delete_modal(id)

