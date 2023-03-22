class RideManager:
    def __init__(self) -> None:
        # print("Ride Manager is active")
        self.__trip_history=[]
        self.__income =0
        self.__avalable_cars = []
        self.__avalable_bikes = []
        self.__avalable_cngs = []

    def add_a_vehicle(self,vehicle_type,vehicle):
        if vehicle_type == 'car':
            self.__avalable_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__avalable_bikes.append(vehicle)
        else:
            self.__avalable_cngs.append(vehicle)

    def get_available_vehicle_car(self):
        return self.__avalable_cars

    def total_income(self):
        return self.__income

    def trip_history(self):
        return self.__income

    def find_a_vehicle(self,rider,vehicle_type,destination):
        if vehicle_type =='car':
            vehicales = self.__avalable_cars
        elif vehicle_type == 'bike':
            vehicales =self.__avalable_bikes
        else:
            vehicales = self.__avalable_cngs
        if len(vehicales) == 0:
            print("Sorry no cars Available")
            return False
        for vehicle in vehicales:
            # print('Potensial',rider.location,car.driver.location)
            if abs(rider.location-vehicle.driver.location) < 10:
                distance = abs(rider.location - destination)
                fare  =  distance * vehicle.rate
                if rider.balance < fare:
                    print("You have not enough money for this trip ",fare , rider.balance)
                    return False
                if vehicle.status == 'available':
                    vehicle.status=='unavailable'
                    trip_info = f'Match {vehicle_type} for {rider.name} for fare: {fare} with {vehicle.driver.name} started: {rider.location}  To : {destination}'
                    print(trip_info)
                    # print("avaliable car ",len(vehicales))
                    vehicales.remove(vehicle)
                    # print("avaliable car ",len(vehicales))
                    rider.start_trip(fare,trip_info)
                    vehicle.driver.start_a_trip(rider.location, destination,fare*0.8,trip_info)
                    self.__income += fare * 0.2
                    # print(f'match for {rider.name} for fare: {fare} with {car.driver.name} started: {rider.location}  To : {destination}')
                    self.__trip_history.append(trip_info)

                    # rider.balance=rider.balance - fare
                    return True

uber=RideManager()