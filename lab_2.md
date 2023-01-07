# lab 2 
## SQL METHOD
1. SQL Injection - login as administrator account

2. SELECT * FROM users where user = administrator and password = password

3. END GOAL - login with admin account without password 
    SELECT * FROM users where user = administrator and password = password

 ###
    1. to break above query we just to insert '-- in the username field after administrator 

    2. SELECT * FROM users where user = administrator' --
    3. to above SQL character break the query and -- comment the rest of the query so it will not check for password in the table


## Result 

    The above method break SQL Query and login as admin account 

###
    Reason for the result of the above query is sql character in the parameter field comment out the query and not checking for password so the actual query at server side look like below query

    select * from users where user = administrator 

## Code for exploit 
    '''python
