My email in recruitment process: thekalkam@gmail.com

--

# Biblioteki użyte w kodzie

W kodzie użyłem tylko i wyłącznie jednej biblioteki nazwanej PyGithub.

Można ją zainstalować na kilka sposobów:

1)
Za pomocą komendy:
pip install PyGithub

2)
Skopiować bezpośrednio z githuba - https://github.com/PyGithub/PyGithub

3)
Jeśli korzystamy ze środowiska PyCharm - nawigować się w zakładkę "Python Packages"(podświetlona ciemnym kolorem na zrzucie ekranu), następnie w wyszukiwarce wpisać "PyGithub", nacisnąć na wynik z nazwą odpowiadającą bibliotece, a następnie zainstalować za pomocą przycisku install (zaznaczony na czerwono).
![image](https://user-images.githubusercontent.com/102754595/165184043-6bacb29a-270e-422b-8aa7-1c92c518c58a.png)

# Generowanie githubowego tokenu potrzebnego do autoryzowanego połączenia z Github API

Jeśli takowego tokenu nie posiadamy (będzie on potrzebny podczas uruchamiania programu), to pod tym linkiem opisane jest jak go wygenerować - https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

# Krótki opis działania programu

Po uprzednim zainstalowaniu biblioteki PyGithub możemy uruchomić kod w naszym Pythonowym środowisku (zwyczajnie klikając przycisk "Run")

Po uruchomieniu programu powinna wyskoczyć prośba o podanie Githubowego tokenu do połączenia się do Github API. Podając token uzyskujemy połączenie autoryzowane, które pozwala na wysyłanie większej ilości requestów - przykładowo bez podawania tokenu byłem w stanie odczytać ~30 repozytoriów, po czym środowisko github zwracało mi błąd. Po wprowadzeniu tokenu jesteśmy w stanie odczytać nawet 4800 repozytoriów (według mojego researchu jest to największa ilość repozytoriów na pojedynczym profilu - profil Microsoft)


![image](https://user-images.githubusercontent.com/102754595/165182702-7a9be9cb-888a-44d4-bb57-796c91efd26d.png)


Po wprowadzeniu tokenu, jeśli był on poprawny, należy wpisać nazwę użytkownika, dla którego chcemy uzyskać dane.
![image](https://user-images.githubusercontent.com/102754595/165183463-e49eaf16-3cad-4691-a793-9371890142db.png)

Po zatwierdzeniu przycisku enter powinno rozpocząć się "wczytywanie" informacji o użytkowniku - przykład dla mojego profilu "MichalKaleta99":

![image](https://user-images.githubusercontent.com/102754595/165183667-06a85a8d-963c-4608-b39f-d27e3d120762.png)

Oczywiście, tak jak widać na zrzucie ekranu oraz jest napisane - wpisując nową nazwę, odczytamy następnego użytkownika. Program kończymy wpisując "/" zamiast nazwy użytkownika.


