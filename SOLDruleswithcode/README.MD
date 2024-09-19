Single Responsibility Principle (SRP):- The Tourist class has multiple responsibilities:

Generating a unique ID
Storing tourist information (name, age, gender, birthdate)
Managing cost and places
Managing status
To adhere to SRP, we can break down the Tourist class into smaller classes, each with a single responsibility. For example:

TouristIdGenerator class to generate unique IDs
TouristInfo class to store tourist information
TouristCostManager class to manage cost
TouristPlaceManager class to manage places
TouristStatusManager class to manage status
Open-Closed Principle (OCP):- The TouristSystem class is not open for extension but closed for modification. To adhere to OCP, we can introduce an abstract base class TouristSystem with abstract methods for adding, displaying, updating, and adding places. Then, we can create concrete implementations of this class, such as DefaultTouristSystem or AdvancedTouristSystem, which can be extended or modified without changing the base class.

Liskov Substitution Principle (LSP):- The Tourist class does not have any derived classes, so LSP is not applicable in this case.

Interface Segregation Principle (ISP) :- The TouristSystem class has a large interface with multiple methods. To adhere to ISP, we can break down the interface into smaller, more focused interfaces, such as:

TouristAdder interface for adding tourists
TouristDisplay interface for displaying tourists
TouristUpdater interface for updating tourist information
TouristPlaceAdder interface for adding places

Dependency Inversion Principle (DIP):- The TouristSystem class depends on the Tourist class, which is a low-level module. To adhere to DIP, we can introduce an abstraction layer, such as an interface ITourist, which can be implemented by the Tourist class. Then, the TouristSystem class can depend on the ITourist interface, rather than the concrete Tourist class.