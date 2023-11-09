# Project overview

&emsp; The project represents a book-scraping program, which gathers books along with their info from a website: http://books.toscrape.com.\
&emsp; The program should be able to sort the data extracted from the website.\
&emsp; The program should be able to filter the extracted data, using various measures, such as rating, genre and others. \
&emsp; The final product represents a GSheet file with all information about extracted data based on the user preferences. 

# Project timeline

Week 1:
1. Get understanding of the project, familiarize with the website and with the beautifulSoup library.
2. Make UML diagram (https://drive.google.com/file/d/17DGCTMOtMwlluFlyhUzPAKDcrxuo3XAs/view?usp=sharing).
3. Make a functionality of extracting web data, stored in a JSON format.

Week 2:
1. Make filter functionality of the data.
2. Make sorting functionality of the data.
3. Store the formated data in a JSON format.

Week 3:
1. Represent the data in a GSheet format.
2. Bug fixing the filtering functionality and optimizing the code.

Week 4:
1. Make more optimizations of the code and solve buggs that appear.
2. Refactor the whole project in order to have easily readable logic flow. 
3. Make unit tests on all the methods used within the project.
4. Prepare GUI using the TKinter library.
5. Make project presentation, concluding the work done in the previous weeks.

# Work organization

Week 1: 
1. Everyone gives a brute-force working solution of the problem. This ensures that team members are familiarized with the libraries used for extracting data.
2. Sharing ideas and working together through an optimal solution based on the first 3 given.

Week 2:
1. Tasks are divided equal between the members of the team. 
2. Different functionalities are combined into a working filtering and sorting program.

Week 3:
1. Everyone writes their model of project and presenting the idea to the others.
2. The best ideas are taken into the combined version of the project in order to achieve the most optimal solution from all 3.
3. Everyone in the team tests the project and resolve any buggs that appear.

Week 4:
1. Unit testing is divided equally between the members of the team.
2. Other task are also divided equally: one makes GUI version, others work on the refactoring of the code.
3. All members of the team are testing the program and resolving any bugs that appear. 

# Project logic flow:

The idea of the project is to receive several command line argumens, which are parsed in the Cli class to a dictionary. 
The Scraper class is creating books one by one. After a book is created, it checks if it meets the filter requirements.
If the book passes the filters test, it is added to a list. After the requirements for the number of books is met, the list 
with books is ready to be processed. If sorting requirement is given, the books are sorted based on these requirements, and
then processed to the database (stored in a json format). The program asks the client if he wants to receive a google sheet
table of the books created and if he chooses yes, the database will fill a google sheet file with information about every
book in the database.

# Project structure

books_scraper/\
|--- main.py\
|--- module/\
&emsp; &emsp; modules/libraries of the project\
|--- `__init__.py`\
|--- README.md\
|--- requirements.txt\
|--- .gitignore\
|--- test/\
 &nbsp;  |--- unit_tests/