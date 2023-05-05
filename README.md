# dat500-project
final project for subject dat500 with demo data sets

Folder contains 2 demo data_sets (books_demo3.txt and ratings_demo3.txt), these two data sets are smaller versions of original ones containing first 10 000 lines
In order to run entire pipeline these two data sets needs to be converted to .csv files with use of hadoop. To do so:
- datasets have to be transported to hadoop file system with command "hadoop fs -put books_demo3.txt /" this will place the first data set in the root of hadoop file system
 - next we need to convert the data into .csv with use of hadoop, for this purpose we run command "python3 txt_to_csv.py  --hadoop-streaming-jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar     -r hadoop hdfs:///book_demo3.txt   --output-dir hdfs:///books_demo3" this command will run th etxt_to_csv file in cluster with default path for hadoop, other way is to run it as normal python code without using hadoop, as it is only the demo set it won't take too long
 -now we can run spark_app file, wchich takes the demo files automatically from root of hadoop file system
 - results are presented at the bottom of spark_app code
