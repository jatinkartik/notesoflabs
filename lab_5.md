# Lab 5
## SQL METHOD
1. SQL Injection - SQL injection UNION attack, retrieving data from other tables 

2. SELECT a,b FROM products WHERE category = "Gift'

3. END GOAL : - retrieve data from users table by using union operator and from credentials login to administrator account 

## Injection method 

 
    The following are basic rules for combining the result sets of two queries by using UNION:

        --> The number and the order of the columns must be the same in all queries.

        --> The data types must be compatible.


    SELECT a,b FROM products WHERE category = 'Gifts' 

 ###
    1. to break the above query we have to use union in the query and attached another query selecting same no of the columns --> to find the no of column used in the query we will start with 1 and increment till the query give a valid output 
## STEP 1 
    by using order by method we will find number of columns in the existing query  and after that we will attend other query to existing query

    query for above method will be like this 

    SELECT a,b FROM products WHERE category = 'Gifts' union SELECT username,password from users --
	



## Result 
    The above method break the sql query and find the no of columns used in the query and data type used by columns and display username and password by appending union query

 ###
    Reason for the result of the above query is it select columns and same no of columns we pass using union method 
    and by using order by method it give different output everytime except the invalid no of columns passed in order method 
	
	union query display username and password by which we can Login to administrator account 

