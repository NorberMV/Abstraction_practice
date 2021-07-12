
# Model an User with his personal info, and loging attempts

class User:
    def __init__(self, first_name, last_name, username, pk, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.pk = pk
        self.email = email
        self.logging_attempts = 0
        
    def describe_user(self):
        self.firstName = 'First Name'
        self.lastName = 'Last Name' 
        self.Username = 'User Name'
        self.Pk = 'Pk'
        self.Email = 'email'
                    
        self.user_info = {
            self.firstName:self.first_name, 
            self.lastName:self.last_name, 
            self.Username:self.username, 
            self.Pk:self.pk, 
            self.Email:self.email
        }
        
        for k, v in self.user_info.items():
            print('{}: {}'.format(k,v))
            
    def increment_logging_attempts(self):
        self.logging_attempts += 1
        
    def reset_logging_attempts(self):
        self.logging_attempts = 0

if __name__=='__main__':
    my_user = User('Norberto', 'Moreno', 'norberMV', 1, 'jdk.dev@gmail.com')

    my_user.describe_user()

    my_user.logging_attempts

    my_user.reset_logging_attempts()