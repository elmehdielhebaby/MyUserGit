from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
class Accueil(Screen):
    def username(self):
        return self.ids.username.text
    def password(self):
        return self.ids.password.text
    def signin(self): #comment
        print(self.password()+" "+self.username())
class User(Screen):
    info=0
    math=0
    phy=0
    bio=0
    autr=0
    data_info = [{"isbn": "1", "name": "info1", "categorie": "info","Disponible":"oui"},
                 {"isbn": "2", "name": "info2", "categorie": "info","Disponible":"oui"},
                 {"isbn": "3", "name": "info3", "categorie": "info","Disponible":"oui"}]
    name_info = ["info","Info","informatique","Informatique"]
    def table(self):
        aff_tab=self.ids.afftable
        details = BoxLayout(size_hint_y=None, height=30, pos_hint={"top": 1})
        aff_tab.add_widget(details)
        ISBN = Label(text='ISBN', size_hint_x=.1, color=(0, 0, 0, 1))
        Titre = Label(text='Titre', size_hint_x=.1, color=(0, 0, 0, 1))
        Categorie = Label(text='Categorie', size_hint_x=.1, color=(0, 0, 0, 1))
        Disponible = Label(text='Disponible', size_hint_x=.1, color=(0, 0, 0, 1))
        details.add_widget(ISBN)
        details.add_widget(Titre)
        details.add_widget(Categorie)
        details.add_widget(Disponible)
    def informatique(self,widjet):
            self.info=1
           # self.table()
            aff_lol=self.ids.aff
            for i in range(len(self.data_info)):
                details = BoxLayout(size_hint_y=None, height=30, pos_hint={"top": 1})
                aff_lol.add_widget(details)
                isbn = Label(text=self.data_info[i]["isbn"], size_hint_x=.15, color=(0, 0, 0, 1))
                titre = Label(text=self.data_info[i]["name"], size_hint_x=.4, color=(0, 0, 0, 1))
                Categorie = Label(text=self.data_info[i]["categorie"], size_hint_x=.2, color=(0, 0, 0, 1))
                Disponible = Label(text=self.data_info[i]["Disponible"], size_hint_x=.25, color=(0, 0, 0, 1))
                details.add_widget(isbn)
                details.add_widget(titre)
                details.add_widget(Categorie)
                details.add_widget(Disponible)
    def info_button(self, widjet):
        self.ids.chercher.text = "chercher"
        if widjet.state == "down" and self.info == 0:
            self.informatique(widjet)
    def chercher(self,widjet):
        book=self.ids.book_name.text
        if  book in self.name_info:
            if self.info==0:
                self.info=1
                self.informatique(widjet)
class MyGrid(Screen):
    pass
class WindowManager(ScreenManager):
    pass
kv = Builder.load_file('My.kv')
class Myapp(App):
    def build(self):
        return kv
if __name__=='__main__':
    Myapp().run()



#book_recherch_info=["info","Info","informatique","Informatique"]