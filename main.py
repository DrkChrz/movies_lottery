import mysql.connector
import random

db = mysql.connector.connect(
    host="host",
    user="user",
    passwd="passwd",
    database="database"
)

mycursor = db.cursor(buffered=True)


def main():
    get_user_input()


def create_obejrzane_table():
    bla = []
    mycursor.execute("show tables like 'obejrzane'")
    for x in mycursor:
        bla.append(x)
    if not bla:
        mycursor.execute("create table obejrzane(id INT , Tytul VARCHAR(50), Czyje VARCHAR(2))")
    else:
        pass


def get_user_input():
    create_obejrzane_table()
    while True:
        print()
        print("--Menu--")
        print()
        print("1. Dodaj nowy film do bazy.")
        print("2. Losuj film z bazy.")
        print("3. Pokaż obejrzane filmy")

        inp = input()
        if inp == "1":

            new_title, who = input("Podaj tytul i czyj: ").split()
            mycursor.execute("insert into filmy(id, Tytul) values(%s%s)", new_title, who)
            db.commit()

        elif inp == "2":

            tab = []
            mycursor.execute("select Tytul from filmy")
            for x in mycursor:
                tab.append(x)

            random_guess = random.choice(tab)
            print("a")
            print(str(random_guess).rstrip(")").lstrip("(").rstrip(",").lstrip("'").rstrip("'"))
            mycursor.execute("select * from filmy where Tytul= %s", random_guess)
            for x in mycursor:
                print(x)
            print("b")
            new = str(random_guess).rstrip(")").lstrip("(").rstrip(",").lstrip("'").rstrip("'")
            print("c")
            inp2 = input("Czy chcesz obejrzec film i przeniesc go do obejrzanych? y/n?")

            if inp2.lower() == "y":
                mycursor.execute("insert into obejrzane select * from filmy where Tytul =%s", random_guess)
                print()
                print("{} zostal dodany do obejrzanych".format(str(new)))
                print()
                mycursor.execute("delete from filmy where Tytul =%s", random_guess)
                db.commit()
            else:
                continue
        elif inp == "3":
            obejrzane_tab = []
            mycursor.execute("select * from obejrzane")
            for x in mycursor:
                obejrzane_tab.append(x)
            for movie in obejrzane_tab:
                print(movie)

        elif inp == "q":
            break


if __name__ == "__main__":
    main()
