# Lab 3
## SQL METHOD
1. SQL Injection - Product category filter  | SQL Injection union attack, SQL injection UNION attack, finding a column containing text 

2. SELECT a,b FROM products WHERE category = "Gift'

3. END GOAL : - find the no of columns used by the query in lab

## Injection method 

 
    The following are basic rules for combining the result sets of two queries by using UNION:

        --> The number and the order of the columns must be the same in all queries.

        --> The data types must be compatible.


    SELECT a,b FROM products WHERE category = 'Gifts' 

 ###
    1. to break the above query we have to use union in the query and attached another query selecting same no of the columns --> to find the no of column used in the query we will start with 1 and increment till the query give a valid output 
## Way 1 
    by using order by method

    query for above method will be like this 

    SELECT a,b FROM products WHERE category = 'Gifts' union SELECT 1,"532ac5",1 --


## Way 2 
    by appending the query using UNION operator

    query for above method will be like this 

    SELECT a,b FROM products WHERE category = 'Gifts' UNION SELECT NULL, NULL 

    increment NULL count till the webapp return 200 response code 

    change the element data type to integer value or any other data type if it give internal error that mean particulat column not support that  
## Result 
    The above method break the sql query and find the no of columns used in the query and data type used by columns

 ###
    Reason for the result of the above query is it select columns and same no of columns we pass using union method 
    and by using order by method it give different output everytime except the invalid no of columns passed in order method 

