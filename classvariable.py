# # class Demo:
    
# #     class_var = 'shared variable'

# # print(Demo.class_var)
# # print(Demo.__dict__)
# # class Demo:
# #     class_var = 'shared variable'

# # d1 = Demo()

# # d2 = Demo()
# # Demo.class_var = 'shared variable11'

# # print(Demo.class_var)
# # print(d1.class_var)
# # print(d2.class_var)

# # print('contents of d1:', d1.__dict__)
# # class Duck:
# #     counter = 0
# #     species = 'duck'

# #     def __init__(self, height, weight, sex):
# #         self.height = height
# #         self.weight = weight
# #         self.sex = sex
# #         Duck.counter +=1

# #     def walk(self):
# #         pass

# #     def quack(self):
# #         print('quacks')

# # class Chicken:
# #     species = 'chicken'

# #     def walk(self):
# #         pass

# #     def cluck(self):
# #         print('clucks')

# # duckling = Duck(height=10, weight=3.4, sex="male")
# # drake = Duck(height=25, weight=3.7, sex="male")
# # hen = Duck(height=20, weight=3.4, sex="female")

# # chicken = Chicken()

# # print('So many ducks were born:', Duck.counter)

# # for poultry in duckling, drake, hen, chicken:
# #     print(poultry.species, end=' ')
# #     if poultry.species == 'duck':
# #         poultry.quack()
# #     elif poultry.species == 'chicken':
# #         poultry.cluck()
# # #==========================================================#
# # class Phone:
# #     counter = 0

# #     def __init__(self, number):
# #         self.number = number
# #         Phone.counter += 1

# #     def call(self, number):
# #         message = 'Calling {} using own number {}'.format(number, self.number)
# #         return message


# # class FixedPhone(Phone):
# #     last_SN = 0

# #     def __init__(self, number):
# #         super().__init__(number)
# #         FixedPhone.last_SN += 1
# #         self.SN = 'FP-{}'.format(FixedPhone.last_SN)


# # class MobilePhone(Phone):
# #     last_SN = 0

# #     def __init__(self, number):
# #         super().__init__(number)
# #         MobilePhone.last_SN += 1
# #         self.SN = 'MP-{}'.format(MobilePhone.last_SN)


# # print('Total number of phone devices created:', Phone.counter)
# # print('Creating 2 devices')
# # fphone = FixedPhone('555-2368')
# # mphone = MobilePhone('01632-960004')

# # print('Total number of phone devices created:', Phone.counter)
# # print('Total number of mobile phones created:', MobilePhone.last_SN)

# # print(fphone.call('01632-960004'))
# # print('Fixed phone received "{}" serial number'.format(fphone.SN))
# # print('Mobile phone received "{}" serial number'.format(mphone.SN))
# # #==========================================================#

# # a=1
# # b=-1

# # b = -b

# # print(a)
# # print(b)
# # class A:
# #     def __init__(self) -> None:
# #         self.obj="AAA"

# # a=A()
# # print(a.__repr__())
# # print(repr(a))	


# # class A:
# #     def info(self):
# #         print('Class A')

# # class B(A):
# #     def info(self):
# #         print('Class B')

# # class C(A):
# #     def info(self):
# #         print('Class C')

# # class D(B, C):
# #     pass

# # a=A
# # b=B
# # c=C
# # d=D
# # print(B.mro())
# # B().info()
# # print(D.mro())
# # D().info()


# class Device:
#     def turn_on(self):
#         print('The device was turned on')

# class Radio(Device):
#     pass

# class PortableRadio(Device):
#     def turn_on(self):
#         print('PortableRadio type object was turned on')

# class TvSet(Device):
#     def turn_on(self):
#         print('TvSet type object was turned on')

# device = Device()
# radio = Radio()
# portableRadio = PortableRadio()
# tvset = TvSet()

# radio.turn_on()
# # for element in (device, radio, portableRadio, tvset):
# #     element.turn_on()

#############################
#decorators
# def simple_decorator(function):
#     print('We are about to call "{}"'.format(function.__name__))
#     return function


# @simple_decorator
# def simple_hello():
#     print("Hello from simple function!")


# simple_hello()

# def warehouse_decorator(material):
#     def wrapper(our_function):
#         def internal_wrapper(*args):
#             print('Wrapping items from {} with {}'.format(our_function.__name__, material))
#             our_function(*args)
#             print()
#         return internal_wrapper
#     return wrapper
# def warehouse_decorator(our_function):
#     def wrapper(our_function):
#         def internal_wrapper(a):
#             print("we are calling ",our_function.__name__)
#             print("with args ",a)
#             print('Wrapping items from {}'.format(our_function.__name__))
#             our_function(a)
#             print()
#         return internal_wrapper
#     return wrapper


# @warehouse_decorator('KRAFTFT')
# def pack_books(a):
#     print("We'll pack books:", a)

# pack_books('Alice in Wonderland')

# # @warehouse_decorator('foil')
# # def pack_toys(*args):
# #     print("We'll pack toys:", args)


# # @warehouse_decorator('cardboard')
# # def pack_fruits(*args):
# #     print("We'll pack fruits:", args)


# #pack_books('Alice in Wonderland', 'Winnie the Pooh')
# #pack_toys('doll', 'car')
# #pack_fruits('plum', 'pear')



class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter +=1

    @classmethod
    def get_internal(cls):
        return '# of objects created: {}'.format(cls.__internal_counter)

print(Example.get_internal())

example1 = Example(10)
print(Example.get_internal())

example2 = Example(99)
print(Example.get_internal())

