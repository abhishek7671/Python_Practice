# def fun(*args, **kwargs):
#     print("args:",args)
#     print("**kwargs:",kwargs)

# fun("geeks","for","geeks",first="abhi",middle= "kumar",last="reddy")    


class car():
    def __init__(self,*args):
        self.speed=[0]
        self.color=[1]

audi= car(250,"red")
bmw = car(450,"black")
lam = car(500,"gery")


print(audi.color)