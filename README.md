# DOS HomeWork part 1

Students : Amr Eshtiwi 11840180 , Ahmed Abdallah Al-Qerem 11819195

## Description

The homework for building a DOS using 3 web servers built using `flask`

- frontEnd
- catalog
- order
  everyone of these server is resposible for specific opreation
  the opration that we offered is :
- /sreach -> to show all books in database.
- /search/<category> -> to show all books that have same category.
- /info/< item_number> -> to show information for specific book.
- /purchase/< item_number > -> to purchase specific book from e-shop (through order server).

## frontEnd sever

is resposible for showing the end data to end user by send requset for required server

- if the operation was a search or get information then the requset will send to catalog server
- if the operation was a purchase a book then the requset will send to order server

## catalog server

if it have a requset it will handle it by get the data from the CSV file

## order server

if it have a requset it will send another requset to catalog server to check if the book is exist in the book store or not.
if exist it check it the quntity is larger than 0 to complete the purchase opration.
if the quntity is larger than 0 it send another requset to catalog server to update the quntity on the database.

## How to run this homework

first you need to install:

- flask
- pandas
- requset
  then you need to put every sever on diffrent computer and get their IPs to edit the IP for catalog server in the frontEnd sever and order server , then get the IP for order server to edit the IP for order server in frontEnd server.

then write on the command line `flask run`

## Possible improvement

we can use Doker for easy to implement
we can use GUI can accessed it using fronEnd server

## OUTPUT

/sreach
![image](https://user-images.githubusercontent.com/54311405/180568104-4c353b6c-690a-4966-b1dc-a0671b305934.png)
  
/search/<category>
![image](https://user-images.githubusercontent.com/54311405/180568175-ce879d31-0203-4271-9fb8-4c5f5b97463c.png)

/info/< item_number>
![image](https://user-images.githubusercontent.com/54311405/180568227-b3f5a627-848c-4bc5-8607-85ec152317b2.png)



