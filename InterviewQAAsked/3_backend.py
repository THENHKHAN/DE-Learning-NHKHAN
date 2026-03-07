
Q-1: In FastApi , Can  two endpoints have the same path if HTTP methods also same ? which method will be executed when we hit that endpoint ?
Short And:   In FastAPI, you cannot have two endpoints with the same path and the same HTTP method. If you try to define two endpoints with the same path and method, FastAPI will raise an error during the application startup, indicating that there is a conflict in the route definitions.
                Or maybe the last defined will override the prevous one.



Q-2: 