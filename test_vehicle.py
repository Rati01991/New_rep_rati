import pytest
from vehicle import Vehicle, ElectricVehicle

@pytest.fixture
def vehicle():
    return Vehicle("Maserati", "Granturismo", 2024)

@pytest.fixture
def electric_vehicle():
    return ElectricVehicle("Kia", "EV9", 2024)

def test_vehicle_fuel_up(vehicle):
    assert vehicle.fuel_up == "Gas tank is now full or can move."

def test_vehicle_drive(vehicle):
    assert vehicle.drive == "The Granturismo is now driving."  # Adjusted for Granturismo

def test_electric_vehicle_charge(electric_vehicle):
    assert electric_vehicle.charge == "The vehicle is now charged."

def test_electric_vehicle_fuel_up(electric_vehicle):
    assert electric_vehicle.fuel_up == "This vehicle has no fuel tank!"