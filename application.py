import os

def main():
    while(True):

        company_name = input("Enter company name: ")
        write_to_file(company_name)

        # Exits the program if user doesn't want to add another name
        exit_status = input("Exit program?\n")
        if(exit_status == "yes"):
            break

def write_to_file(company_name):

    # creates directory with company to store information
    directory = company_name
    parent_dir = 'jobs/'
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    os.mkdir(path + '/resources')


    file = open('jobs/' + company_name + '/' + company_name + ".txt", 'a')
    file.write('Company Name: ' + company_name + "\n")
    

    # Retrieves date applied
    date = input("Enter date applied: ")
    file.write('Date: ' + date + '\n')

    # What website did you apply through
    website = input("Enter website applied to: ")
    file.write('Website: ' + website + '\n')

    # What email did you use
    email = input("Enter email used: ")
    file.write('Email: ' + email + '\n')

    # Saves password to website if account was created
    profile = input("Was there a profile created: ")
    if profile == "no":
        file.write('No profile created. \n')
        return 0
    else:
        file.write("Profile\n")
        username = input("Enter username: ")
        password = input("Enter password: ")
        file.write('Username: ' + username + '\n')
        file.write('Password: ' + password + '\n')
    
    return 0

if __name__ == '__main__':
    main()