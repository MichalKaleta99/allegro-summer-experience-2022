from github import Github
global g
def create_instance(token):
    global g
    try:
        g = Github(token)
        auth=g.get_user().login
        print("Pomyślnie zalogowano jako: " +str(auth))
    except:
        next_token = input("Podano zły token. Spróbuj ponownie (/ - zamknięcie programu).\n")
        if next_token=='/':
            quit()
        create_instance(next_token)
def check(mylist, lan):
    for sub_list in mylist:
        if lan in sub_list:
            return (mylist.index(sub_list), sub_list.index(lan))
    return False

def read_repos(user_to_read):
    global g
    languages_used = []
    byte_list = []
    sum_of_bytes = 0
    try:
        login = g.get_user(user_to_read).login
        repos = g.get_user(user_to_read).get_repos()
        username = g.get_user(user_to_read).name
        bio = g.get_user(user_to_read).bio
    except:
        print("Błąd komunikacyjny - spróbuj ponownie. Upewnij się, że prawidłowo wpisałeś nazwę użytkownika.")
        decision = input("\nPodaj login nastepnego użytkownika lub jeśli chcesz zakończyć - wpisz '/'\n")
        if decision == '/':
            quit()
        read_repos(decision)
    if username==None:
        username="Użytkownik nie uzupełnił tego pola"
    if bio==None:
        bio="Użytkownik nie uzupełnił tego pola"

    print("Nazwa użytkownika - " + username + "\nLogin - " + login + "\nBio - " + bio)

    if g.get_user(user_to_read).get_repos().totalCount==0:
        print("\nUżytkownik nie posiada repozytoriów")
    else:
        print("\nRepozytoria użytkownika:")

    for count, repo in enumerate(repos, start=1):
        languages=list(repo.get_languages().items())
        print(str(count) + ") " + "Nazwa - " + repo.name)
        if repo.language==None:
            print("brak języka")
        else:
            for l in languages:
                print("Język - " + str(l[0]) + ", liczba bajtów - " + str(l[1]))
                if check(languages_used, l[0])==False:
                    languages_used.append(l[0])
                    byte_list.append(l[1])
                else:
                    position=check(languages_used, l[0])
                    index=position[0]
                    byte_list[index]+=l[1]
    for i in range(0, len(byte_list)):
        sum_of_bytes+=byte_list[i]
    if g.get_user(user_to_read).get_repos().totalCount!=0:
        print("\nZagregowana lista języków programowania użyta we wszystkich ("+str(count)+") repozytoriach użytkownika: ")
    for i in range (0, len(languages_used)):
        bytes_percentage=str(round((byte_list[i]/sum_of_bytes)*100,2))
        if bytes_percentage=="0.0":
            bytes_percentage="<0.01"
        print(str(i+1) + ") " + "Nazwa języka - " + str(languages_used[i]) + ", łączna liczba bajtów - " + str(byte_list[i]) + " (" + bytes_percentage + "%)")
    decision = input("\nPodaj login nastepnego użytkownika lub jeśli chcesz zakończyć - wpisz '/'\n")
    if decision=='/':
        quit()
    else:
        read_repos(decision)
token = input("Podaj token aby zalogować się do GitHub API: \n")
create_instance(token)
user_to_read = input("Podaj login użytkownika, dla którego chcesz odczytać dane (wielkość liter bez znaczenia): \n")
read_repos(user_to_read)