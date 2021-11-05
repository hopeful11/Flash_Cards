import json
import os
class User:
    # user_list = ['osman','murat','mehmet']
    # user_list = {}
    def __init__(self,user_name):
        self.user_name = user_name

    def login(self):
    #login methode
        if not os.path.isfile('user/'+self.user_name+'.json'):
            self.signup()
        # print('asd')
        # else:
        

        # with open('user_list.json','r') as jsFile:
        #     data1 = json.load(jsFile)
        #     # print(data1)
        #     # print(data1['aaa'])
        #     check = False
            
        #     for k in data1:
        #         if k == self.user_name:
        #             check = True
            # if not check:
            #     self.signup()

        # if self.user_name in self.user_list:
        #     print (f'welcome {self.user_name} !')
        # else:
        #     self.signup()
        
    def signup(self):
    #sign up methode

        self.user_info = {
            'username':self.user_name,
            'level':1
            }
        #-----------------------------------
        # creat een json file as username.json    
        # js_user_info = json.dumps(self.user_info) 
        js_file_name = 'user/'+self.user_name+'.json'       
        with open(js_file_name,'w') as jsFile:
            jsFile.write(json.dumps(self.user_info,indent=4))
        #-----------------------------------
        #add username to user_list.json
        js_user_list = 'user_list.json'
        
        # with open(js_user_list,'a') as file:
        #     file.write(json.dumps(self.user_info,indent=4))

        # with open('user_list.json','a') as f:
        #     str = json.dumps(self.user_info,indent=4)
        #     f.write(str)
        

obj = User('admin')
obj.login()