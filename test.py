def get_user_menu_choice(self):
    users_choice = str(input("Do you want to play or show results ? (p or s)"))
    if users_choice == 'p':
        print('Lets play !')
    elif users_choice == 's':
        print('Here are your results !')
    else:
        users_choice = str(input("It must be 'p' or 's' "))
        self.get_user_menu_choice()