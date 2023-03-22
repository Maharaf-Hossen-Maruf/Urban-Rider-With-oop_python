import hashlib
from random import random,randint,choice
from brta import BRTA
from vehicale import Car,Bike,Cng
from ride_manager import uber
import threading

license_authority = BRTA()

class UserAlreadyExists(Exception):
    def __init__(self,email ,*args: object) -> None:
        print(f'user {email} already exists. ')
        super().__init__(*args)


class User:
    def __init__(self,name,email,password) -> None:
        self.name=name
        self.email=email
        pwd_encrycpted=hashlib.md5(password.encode()).hexdigest()
        already_exists = False
        with open('user.txt','r') as file:
            if email in file.read():
                already_exists = True
                # raise UserAlreadyExists(email)
        file.close()

        if already_exists == False:
                with open("user.txt","a") as file:
                    file.write(f"{email} {pwd_encrycpted}\n")
        file.close()

        # print(self.name,'user created')

    @staticmethod
    def log_in(mail,password):
        stored_password =''
        with open("user.txt","r") as file:
            lines=file.readlines() 
            for line in lines:
                if mail in line:
                    stored_password= line.split(" ") [1]

        file.close()       
        hashed_password=hashlib.md5(password.encode()).hexdigest()


        if hashed_password == stored_password:
            print("Valid User")
        else:
            print("InValid User")


class Rider(User):
    def __init__(self, name, email, password,location,balance) -> None:
        self.location=location
        self.balance= balance
        self.__trip_history=[]
        super().__init__(name, email, password)
    
    def set_location(self,location):
        self.location=location

    def get_location(self):
        return self.location

    def request_trip(self,destination):
        pass

    def get_trip_info(self):
        return self.__trip_history

    def start_trip(self,fare,trip_info):
        print(f'A trip started for {self.name}')
        self.balance -= fare
        self.__trip_history.append(trip_info)


class Driver(User):
    def __init__(self, name, email, password,location,license) -> None:
        super().__init__(name, email, password)
        self.location=location
        self.license=license
        self.valid_driver = license_authority.validate_license(email,license)
        self.earnings= 0
        self.__trip_history=[]
        self.vehicale=None

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result ==False:
            # print("you have failed,try Again")
            self.license = None
        else:
            self.license=result
            self.valid_driver=True

    def register_a_vehicale(self,vehicle_type,license_plate,rate):
        if self.valid_driver is True:
            # new_vehicale = None
            if vehicle_type == 'car':
                self.vehicale = Car(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicale)
            elif vehicle_type == 'bike':
                self.vehicale = Bike(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicale)
            else:
                self.vehicale = Cng(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicale)

            
        else:
            pass
            # print("You are not a valid Driver")


    def start_a_trip(self,start,destination,fare,trip_info):
        self.earnings  += fare
        self.location = destination
        #Start Thread
        trip_thread = threading.Thread(target=self.vehicale.start_driving ,args=(start,destination, ))
        # self.vehicale.start_driving(start,destination)
        trip_thread.start()
        self.__trip_history.append(trip_info)





rider1=  Rider('rider1','rider1@gmail.com','rider1',randint(0,30),1000)
rider2=  Rider('rider2','rider2@gmail.com','rider2',randint(0,30),1000)
rider3=  Rider('rider3','rider3@gmail.com','rider3',randint(0,30),1000)
rider4=  Rider('rider4','rider4@gmail.com','rider4',randint(0,30),1000)
rider5=  Rider('rider5','rider5@gmail.com','rider5',randint(0,30),1000)

vehicale_types=['car','bike','cng']

for i in range(1,100):
    driver1=Driver(f'driver{i}',f'driver{i}@gmail.com',f'driver{i}',randint(0,100),randint(1000,9999))
    driver1.take_driving_test()
    driver1.register_a_vehicale(choice(vehicale_types),randint(1000,9999),10)



# print(dir(rider1))

uber.find_a_vehicle(rider1,choice(vehicale_types),randint(1,100))
uber.find_a_vehicle(rider2,choice(vehicale_types),randint(1,100))
uber.find_a_vehicle(rider3,choice(vehicale_types),randint(1,100))
uber.find_a_vehicle(rider4,choice(vehicale_types),randint(1,100))
uber.find_a_vehicle(rider5,choice(vehicale_types),randint(1,100))

print(rider1.get_trip_info())