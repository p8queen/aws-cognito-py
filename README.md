## Notes

The Users pool have username, email, password for each user. You want send username, passowrd and get Token. 

First:   
Amazon Cognito -> Users pool - > User pool name -> App Integration -> app client Name 
-> show details/Edit -> Authentication flows -> Allow user-password-auth flow for app-based authentication (USER_PASSWORD_AUTH).

Second:   
Write Python Code. 
