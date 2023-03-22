from abc import ABC, abstractmethod
# import time
from time import sleep

class Vehicle(ABC):
    speed={
        'car' :30,
        'bike':50,
        'cng' : 15
    }

    def __init__(self,vehicle_type,license_plate,rate,driver):
        self.vehicle_type=vehicle_type
        self.liense_plate=license_plate
        self.rate = rate
        self.driver = driver
        self.status='available'
        self.speed=self.speed[vehicle_type]

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_finished(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)


    def start_driving(self,start,destination):
        self.status='unavailable'
        print(self.vehicle_type,self.liense_plate,'started')
        distance = abs(start - destination)

        for i  in range(0,distance):
            sleep(0.5)
            print(f'Driving: {self.liense_plate } current postion {i} of {distance}\n')
        self.trip_finished()

    def trip_finished(self):
        self.status='available'
        print(self.vehicle_type,self.liense_plate,'complited Trip')
        # return super().trip_finished()



class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)


    def start_driving(self,start,destination):
        self.status='unavailable'
        print(self.vehicle_type,self.liense_plate,'started')
        distance = abs(start - destination)

        for i  in range(0,distance):
            sleep(0.5)
            print(f'Driving: {self.liense_plate } current postion {i} of {distance}\n')
        self.trip_finished()


    def trip_finished(self):
        self.status='available'
        print(self.vehicle_type,self.liense_plate,'complited Trip')
        # return super().trip_finished()



class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self,start,destination):
        self.status='unavailable'
        print(self.vehicle_type,self.liense_plate,'started')
        distance = abs(start - destination)

        for i  in range(0,distance):
            sleep(0.5)
            print(f'Driving: {self.liense_plate } current postion {i} of {distance}\n')
        self.trip_finished()



    def trip_finished(self):
        self.status='available'
        print(self.vehicle_type,self.liense_plate,'complited Trip')
        # return super().trip_finished()