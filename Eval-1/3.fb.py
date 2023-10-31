

class post:
    def __init__(self,title,des):
        self.title = title
        self.des=des

post1=post("eat","eat n sleeping")


class Inv:
    def __init__(self):
        self.post=[]

    def add_post(self,post):
        self.post.append(post)
    def del_post(self,id):
        self.post=[post for post in self.post if post.id==id]
    