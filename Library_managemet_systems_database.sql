create database Library_management_system;
use Library_management_system;
create table if not exists Users (
ID int not null AUTO_INCREMENT,
primary key (ID),
FirstName varchar(30) NOT NULL,
LastName varchar(30) NOT NULL,
DateOfRegistration date NOT NULL,
AmountOfActualPayments float NOT NULL
);
create table if not exists Books (
ID int not null AUTO_INCREMENT,
primary key (ID),
Title varchar(50) NOT NULL,
Author varchar (60) NOT NULL,
YearOfRelease int NOT NULL
);
create table if not exists Borrows (
ID int not null AUTO_INCREMENT,
primary key (ID),
ID_books int not null,
ID_users int not null,
FOREIGN KEY (ID_books) REFERENCES books(ID),
FOREIGN KEY (ID_users) REFERENCES users(ID),
DateOfBorrow date,
DateOfReturn date,
StatusOfBorrow bool
);
create table if not exists Reservation (
ID int not null AUTO_INCREMENT,
primary key (ID),
ID_books int not null,
ID_users int not null,
FOREIGN KEY (ID_books) REFERENCES books(ID),
FOREIGN KEY (ID_users) REFERENCES users(ID),
DateOfReservation date,
EndOfReservation date,
StatusOfReservation bool
);
create table if not exists Payments (
ID int not null AUTO_INCREMENT,
primary key (ID),
ID_users int not null,
FOREIGN KEY (ID_users) REFERENCES users(ID),
AmountOfPayment float,
DateOfPayment date,
StatusOfPayment bool
);






