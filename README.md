# dat500-project
final project for subject dat500

Folder contains 2 demo data_sets (books_demo3.txt and ratings_demo3.txt), these two data sets are smaller versions of original ones containing first 10 000 lines
In order to run entire pipeline these two data sets needs to be converted to .csv files with use of hadoop. To do so:
- datasets have to be transported to hadoop file system with command "hadoop fs -put books_demo3.txt /" this will place the first data set in the root of hadoop file system
 - hadoop
