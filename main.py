import kivy
kivy.require('1.11.1')

import datetime
from kivymd.app import MDApp

from helpers import screen_helper
from result import BehaviorModel1, BehaviorModel2, BehaviorModel3, BehaviorModel4

from functools import partial

from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDIconButton,MDRaisedButton, MDFillRoundFlatButton,MDFloatingActionButton, MDRectangleFlatButton, MDFloatingActionButtonSpeedDial, MDFlatButton, MDRoundFlatButton, MDTextButton
from kivymd.uix.list import OneLineAvatarIconListItem,ILeftBodyTouch ,ThreeLineAvatarListItem,MDList, ThreeLineAvatarIconListItem
from kivymd.uix.boxlayout import BoxLayout, MDBoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.card import MDSeparator
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.toast.kivytoast.kivytoast import toast

from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout

class ImageButton(ButtonBehavior,FloatLayout, Image):
    pass

class FirstScreen(Screen):
    start_dialog = None

    def on_enter(self):
        btn = MDRectangleFlatButton(text="Poďme na to", on_release= self.frst_dialog, on_press= self.go )
        self.start_dialog = MDDialog(text="Táto aplikácia ti ponúka test, v ktorom odhalíš svoje prednosti. Na základe nich sa môžeš v budúcnosti zlepšovať. "
                                          "Na hlavnej stránke sa môžeš bližšie oboznámiť s myšlienkou testu. Volíš si okuh, pre ktorý chceš test vypĺňať. "
                                          "Pre pokračovanie k testu klikni na stredné tlačidlo. Na začiatku si pomenuj test, potvrď a môžeš začať. ",
                                     size_hint=[0.8, 0.5], auto_dismiss=True,buttons=[btn])
        self.start_dialog.open()
    def go(self,obj):
        self.manager.current = "home"
    def frst_dialog(self,obj):
        self.start_dialog.dismiss()

class HomeScreen(Screen):
    choose_dialog= None
    choice = None
    help_dialog= None

    def change1back(self):
        self.ids.btn1.source = "Vztah.png"
    def change2back(self):
        self.ids.btn2.source = "Ciele.png"
    def change3back(self):
        self.ids.btn3.source = "Tim.png"
    def change4back(self):
        self.ids.btn4.source = "Ja.png"

    def change1(self):
        self.ids.bla.text = "Otvor svoje srdce"
        self.ids.btn1.source = "VztahD.png"

    def change2(self):
        self.ids.bla.text = "Využi svoje vlastnosti"
        self.ids.btn2.source = "CieleD.png"

    def change3(self):
        self.ids.bla.text = "Pochop svoj tím"
        self.ids.btn3.source = "TimD.png"

    def change4(self):
        self.ids.bla.text = "Spoznaj sám seba"
        self.ids.btn4.source = "JaD.png"

    def show_ChooseDialog(self):
        self.choose_dialog = MDDialog(title="Test zameraný pre:",text= " - osobné zlepšenie (1) \n - prácu v tíme (2) \n - osobné vzťahy (3)",size_hint=[0.9, 0.5], auto_dismiss=True,
                buttons=[MDRaisedButton(text="1",on_release= self.next_page_me,
                                   on_press= self.close_choose_dialog,),
                        MDRaisedButton(text="2", on_release= self.next_page_team,
                                    on_press= self.close_choose_dialog, ),
                        MDRaisedButton(text="3",on_release= self.next_page_we,
                                    on_press= self.close_choose_dialog,)],)
        self.choose_dialog.open()


    def close_choose_dialog(self, obj):
        self.choose_dialog.dismiss()

    def next_page_me (self,obj):
        self.manager.current = "motivationme"
    def next_page_team (self,obj):
        self.manager.current = "motivationteam"
    def next_page_we (self,obj):
        self.manager.current = "motivationwe"

    def show_HelpDialog(self):
        ok_button = MDRaisedButton(text= "Rozumiem",on_release=self.close_help_dialog)
        self.help_dialog = MDDialog(title="O čo v teste ide?", text="Ak chceme v živote niečo dosiahnuť, potrebujeme vedieť, v čom sme výnimoční. Tento "
                                                                    "test ti ponúka 48 otázok, pre lepšie pochopenie svojich schopností. Pokiaľ budeš "
                                                                    "odpovedať úprimne, umožnia ti vytvoriť prehľad svojej osobnosti. \n\n"
                                                                    "Poznať sám seba je prvý krok k úspechu.\n"
                                                                    "Ak chceš naozaj naplniť svoje túžby a zistiť, čo môžeš v živote dokázať, "
                                                                    "neváhaj začni už dnes! Zadefinuj si osobné ciele a vytrvaj v ich plnení. "
                                                                    "Časom si z nich vytvoríš návyk, ktorý ti pomôže spraviť seba lepším. \n\n"
                                                                    "Tak neváhaj a otvor sa sám sebe.",
                              size_hint=[0.9, None], auto_dismiss=False,
                              buttons=[ok_button])
        self.help_dialog.open()

    def close_help_dialog(self,obj):
        self.help_dialog.dismiss()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == 'flash':
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class MotivationScreenMe(Screen):
    M_dialog = None

    def show_motivation_dialog (self):
        ok_button = MDRaisedButton(text="Poďme na to", on_release=self.close_M_dialog)
        self.M_dialog = MDDialog(title="Naučíš sa: ", text="- Lepšie spoznať svoje správanie a vystupovanie\n"
                                                                 "- Odhaliť svoje osobné prednosti a tendencie\n"
                                                                 "- Využívať svoju energiu tam, kde môžete byť najúspešnejší\n"
                                                                 "- Vytvoriť si prostredie v tíme, ktoré najviac dopomôže k úspechu\n"
                                                                 "- Spoznať oblasti možných konfliktov s inými ľuďmi a zredukovať ich na minimum\n"
                                                                 "- Rozvíjať svoje silné stránky, sebapoznaním\n",
                                    size_hint=[0.8, 0.5], auto_dismiss=False,
                                    buttons=[ok_button])
        self.M_dialog.open()

    def close_M_dialog(self,obj):
        self.M_dialog.dismiss()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == 'flash':
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class MotivationScreenTeam(Screen):
    M_dialog = None

    def show_motivation_dialog (self):
        ok_button = MDRaisedButton(text="Poďme na to", on_release=self.close_M_dialog)
        self.M_dialog = MDDialog(title="Naučíš sa: ", text="- Lepšie spoznať svoje správanie a vystupovanie\n"
                                                                 "- Odhaliť svoje osobné prednosti a tendencie\n"
                                                                 "- Využívať svoju energiu tam, kde môžete byť najúspešnejší\n"
                                                                 "- Vytvoriť si prostredie v tíme, ktoré najviac dopomôže k úspechu\n"
                                                                 "- Spoznať oblasti možných konfliktov s inými ľuďmi a zredukovať ich na minimum\n"
                                                                 "- Rozvíjať svoje silné stránky, sebapoznaním\n",
                                    size_hint=[0.8, 0.5], auto_dismiss=False,
                                    buttons=[ok_button])
        self.M_dialog.open()

    def close_M_dialog(self,obj):
        self.M_dialog.dismiss()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == 'flash':
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class MotivationScreenWe(Screen):
    M_dialog= None

    def show_motivation_dialog (self):
        ok_button = MDRaisedButton(text="Poďme na to", on_release=self.close_M_dialog)
        self.M_dialog = MDDialog(title="Naučíš sa: ", text="- Lepšie spoznať svoje správanie a vystupovanie\n"
                                                                 "- Odhaliť svoje osobné prednosti a tendencie\n"
                                                                 "- Využívať svoju energiu tam, kde môžete byť najúspešnejší\n"
                                                                 "- Vytvoriť si prostredie v tíme, ktoré najviac dopomôže k úspechu\n"
                                                                 "- Spoznať oblasti možných konfliktov s inými ľuďmi a zredukovať ich na minimum\n"
                                                                 "- Rozvíjať svoje silné stránky, sebapoznaním\n",
                                    size_hint=[0.8, 0.5], auto_dismiss=False,
                                    buttons=[ok_button])
        self.M_dialog.open()

    def close_M_dialog(self,obj):
        self.M_dialog.dismiss()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == 'flash':
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class test:

    def __init__(self, testovatel, test_v=[], test_m=[]):
        self.testovatel = testovatel
        self.test_v = test_v
        self.test_m = test_m

    # spocitanie znakov v teste v#
    def pocetvd(self):
        dv = self.test_v.count('d')
        return dv

    def pocetvi(self):
        iv = self.test_v.count('i')
        return iv

    def pocetvs(self):
        sv = self.test_v.count('s')
        return sv

    def pocetvk(self):
        kv = self.test_v.count('k')
        return kv

    def pocetvn(self):
        nv = self.test_v.count('n')
        return nv

    def pocetmd(self):
        dm = self.test_m.count('d')
        return dm

    def pocetmi(self):
        im = self.test_m.count('i')
        return im

    def pocetms(self):
        sm = self.test_m.count('s')
        return sm

    def pocetmk(self):
        km = self.test_m.count('k')
        return km

    def pocetmn(self):
        nm = self.test_m.count('n')
        return nm

    # prepocet spolocneho vysledku testv-testm
    def vyratajd(self):
        return self.pocetvd() - self.pocetmd()

    def vyrataji(self):
        return self.pocetvi() - self.pocetmi()

    def vyratajs(self):
        return self.pocetvs() - self.pocetms()

    def vyratajk(self):
        return self.pocetvk() - self.pocetmk()

    def vyratajn(self):
        return self.pocetvn() - self.pocetmn()

    # ntica testuv#
    def vysledok_v(self):
        return (self.pocetvd(), self.pocetvi(), self.pocetvs(), self.pocetvk(), self.pocetvn())

    # ntica testum#
    def vysledok_m(self):
        return (self.pocetmd(), self.pocetmi(), self.pocetms(), self.pocetmk(), self.pocetmn())

    # ntica vysledna#
    def vysledok_spol(self):
        return (self.vyratajd(), self.vyrataji(), self.vyratajs(), self.vyratajk(), self.vyratajn())

    def priorita(self):
        self.d= self.vyratajd()
        self.i= self.vyrataji()
        self.s= self.vyratajs()
        self.k= self.vyratajk()
        self.ukazovatel = ()

        #d
        if self.d < 1:
            self.d_hodnota = 0
        elif self.d == 1:
            self.d_hodnota = 1
        elif self.d == 2 or self.d == 3:
            self.d_hodnota = 2
        elif self.d == 4:
            self.d_hodnota = 3
        elif self.d == 5:
            self.d_hodnota = 4
        elif self.d == 6:
            self.d_hodnota = 5
        elif self.d == 7:
            self.d_hodnota = 6
        elif self.d == 8:
            self.d_hodnota = 7
        elif self.d == 9:
            self.d_hodnota = 8
        elif self.d == 10:
            self.d_hodnota = 9
        elif self.d == 11 or self.d == 12:
            self.d_hodnota = 10
        elif self.d == 13:
            self.d_hodnota = 11
        elif self.d == 14:
            self.d_hodnota = 12
        elif self.d == 15:
            self.d_hodnota = 13
        elif self.d == 16:
            self.d_hodnota = 14
        elif self.d > 16:
            self.d_hodnota = 15

        # i
        if self.i < 0:
            self.i_hodnota = 0
        elif self.i == 0:
            self.i_hodnota = 1
        elif self.i == 1:
            self.i_hodnota = 3
        elif self.i == 2:
            self.i_hodnota = 4
        elif self.i == 3:
            self.i_hodnota = 5
        elif self.i == 4:
            self.i_hodnota = 7
        elif self.i == 5:
            self.i_hodnota = 8
        elif self.i == 6:
            self.i_hodnota = 9
        elif self.i == 7:
            self.i_hodnota = 11
        elif self.i == 8:
            self.i_hodnota = 12
        elif self.i == 9:
            self.i_hodnota = 13
        elif self.i == 10:
            self.i_hodnota = 14
        elif self.i > 10:
            self.i_hodnota = 15
        # s
        if self.s < -1:
            self.s_hodnota = 0
        elif self.s == -1:
            self.s_hodnota = 1
        elif self.s == 0:
            self.s_hodnota = 3
        elif self.s == 1:
            self.s_hodnota = 4
        elif self.s == 2:
            self.s_hodnota = 5
        elif self.s == 3:
            self.s_hodnota = 6
        elif self.s == 4:
            self.s_hodnota = 7
        elif self.s == 5:
            self.s_hodnota = 8
        elif self.s == 6 or self.s == 7:
            self.s_hodnota = 9
        elif self.s == 8:
            self.s_hodnota = 11
        elif self.s == 9:
            self.s_hodnota = 12
        elif self.s == 10:
            self.s_hodnota = 13
        elif self.s == 11:
            self.s_hodnota = 14
        elif self.s > 11:
            self.s_hodnota = 15

        # k
        if self.k < -2:
            self.k_hodnota = 0
        elif self.k == -2:
            self.k_hodnota = 1
        elif self.k == -1:
            self.k_hodnota = 3
        elif self.k == 0:
            self.k_hodnota = 4
        elif self.k == 1:
            self.k_hodnota = 6
        elif self.k == 2:
            self.k_hodnota = 7
        elif self.k == 3:
            self.k_hodnota = 8
        elif self.k == 4:
            self.k_hodnota = 10
        elif self.k == 5:
            self.k_hodnota = 11
        elif self.k == 6:
            self.k_hodnota = 12
        elif self.k == 7:
            self.k_hodnota = 13
        elif self.k == 8:
            self.k_hodnota = 14
        elif self.k > 8:
            self.k_hodnota = 15

        self.d_dvojica = (self.d_hodnota, self.d)
        self.i_dvojica = (self.i_hodnota, self.i)
        self.s_dvojica = (self.s_hodnota, self.s)
        self.k_dvojica = (self.k_hodnota, self.k)

        print(self.d_dvojica, self.i_dvojica, self.s_dvojica, self.k_dvojica, )

        #pre styri
        if self.d_dvojica[0] > 0 and self.i_dvojica[0] > 0 and self.s_dvojica[0] > 0 and self.k_dvojica[0] > 0:
            self.ukazovatel = "zle"

        #pre tri
        elif self.d_dvojica[0] > 0 and self.i_dvojica[0] > 0 and self.s_dvojica[0] > 0 and self.k_dvojica[0] == 0:
            print("123")
            self.ukazovatel = "123"
        elif self.d_dvojica[0] > 0 and self.i_dvojica[0] > 0 and self.s_dvojica[0] == 0 and self.k_dvojica[0] > 0:
            print("124")
            self.ukazovatel = "124"
        elif self.d_dvojica[0] > 0 and self.i_dvojica[0] == 0 and self.s_dvojica[0] > 0 and self.k_dvojica[0] > 0:
            print("134")
            self.ukazovatel = "134"
        elif self.d_dvojica[0] == 0 and self.i_dvojica[0] > 0 and self.s_dvojica[0] > 0 and self.k_dvojica[0] > 0:
            print("234")
            self.ukazovatel = "234"


        #pre dve rovnaka pozicia
        elif self.d_dvojica[0] == self.i_dvojica[0]  and self.s_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("12")
            self.ukazovatel = "12"
        elif self.d_dvojica[0] == self.s_dvojica[0]  and self.i_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("13")
            self.ukazovatel = "13"
        elif self.d_dvojica[0] == self.k_dvojica[0]  and self.s_dvojica[0] == 0 and self.i_dvojica[0] == 0:
            print("14")
            self.ukazovatel = "14"
        elif self.d_dvojica[0] == 0 and self.i_dvojica[0] == self.s_dvojica[0]  and self.k_dvojica[0] == 0:
            print("23")
            self.ukazovatel = "23"
        elif self.d_dvojica[0] == 0 and self.i_dvojica[0] == self.k_dvojica[0]  and self.s_dvojica[0] == 0:
            print("24")
            self.ukazovatel = "24"
        elif self.d_dvojica[0] == 0 and self.i_dvojica[0] == 0 and self.s_dvojica[0] == self.k_dvojica[0]:
            print("34")
            self.ukazovatel = "34"


        #pre dve rozdielna pozicia
        elif self.d_dvojica[0] > self.i_dvojica[0] != 0 and self.s_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("12")
            self.ukazovatel = "12"
        elif self.d_dvojica[0] > self.s_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("13")
            self.ukazovatel = "13"
        elif self.d_dvojica[0] > self.k_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.s_dvojica[0] == 0:
            print("14")
            self.ukazovatel = "14"

        elif self.i_dvojica[0] > self.d_dvojica[0] != 0 and self.s_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("21")
            self.ukazovatel = "21"
        elif self.i_dvojica[0] > self.s_dvojica[0] != 0 and self.d_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("23")
            self.ukazovatel = "23"
        elif self.i_dvojica[0] > self.k_dvojica[0] != 0 and self.s_dvojica[0] == 0 and self.d_dvojica[0] == 0:
            print("24")
            self.ukazovatel = "24"

        elif self.s_dvojica[0] > self.d_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("31")
            self.ukazovatel = "31"
        elif self.s_dvojica[0] > self.i_dvojica[0] != 0 and self.d_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("32")
            self.ukazovatel = "32"
        elif self.s_dvojica[0] > self.k_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.d_dvojica[0] == 0:
            print("34")
            self.ukazovatel = "34"

        elif self.k_dvojica[0] > self.d_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.s_dvojica[0] == 0:
            print("41")
            self.ukazovatel = "41"
        elif self.k_dvojica[0] > self.i_dvojica[0] != 0 and self.d_dvojica[0] == 0 and self.s_dvojica[0] == 0:
            print("42")
            self.ukazovatel = "42"
        elif self.k_dvojica[0] > self.s_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.d_dvojica[0] == 0:
            print("43")
            self.ukazovatel = "43"

        # pre jedno
        elif self.d_dvojica[0] > 0 and self.i_dvojica[0] == 0 and self.s_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("1")
            self.ukazovatel = "1"
        elif self.d_dvojica[0] == 0 and self.i_dvojica[0] > 0 and self.s_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("2")
            self.ukazovatel = "2"
        elif self.d_dvojica[0] == 0 and self.i_dvojica[0] == 0 and self.s_dvojica[0] > 0 and self.k_dvojica[0] == 0:
            print("3")
            self.ukazovatel = "3"
        elif self.d_dvojica[0] == 0 and self.i_dvojica[0] == 0 and self.s_dvojica[0] == 0 and self.k_dvojica[0] > 0:
            print("4")
            self.ukazovatel = "4"

        else:
            pass

    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        return now.strftime("%d-%m-%Y %H:%M")
        #return str(datetime.datetime.now())

    def zapis_test(self):
        with open("testy.txt", "r") as p:
            load = p.read()
        with open("testy.txt", "w") as p:
            p.write(load)
            p.write("Názov: "+ self.testovatel  + "; Ukazovateľ: " + self.ukazovatel +"; "+ self.get_date()+ "\n")

class TestScreenV(Screen):
    eval_dialog = None
    dele_dialog = None
    help_dialog_mm = None
    help_dialog_mv = None
    help_dialog_vm = None
    help_dialog_vv = None
    start_dialog = None

    def on_enter(self):
        btn = MDRectangleFlatButton(text="Rozumiem", on_release=self.frst_dialog)
        self.start_dialog = MDDialog(
            text="Zvoľ si názov, potvrď a môžeš začať s testom ",
            size_hint=[0.8, 0.5], auto_dismiss=True, buttons=[btn])
        self.start_dialog.open()

    def frst_dialog(self, obj):
        self.start_dialog.dismiss()

    def add_test(self):
        if self.ids.nazov_testu.text != "":
            self.testovatel = test(self.ids.nazov_testu.text)
        else:
            self.testovatel = test("Test1")

    def dele_v(self):
        if self.testovatel.test_v != []:
            toast("Vymazaná posledná možnosť z testu NAJVIAC")
            del self.testovatel.test_v[len(self.testovatel.test_v)-1]

    def dele_m(self):
        if self.testovatel.test_m != []:
            del self.testovatel.test_m[len(self.testovatel.test_m)-1]
            toast("Vymazaná posledná možnosť z testu NAJMENEJ")


    def show_HelpDialogMM(self):
        ok_button = MDRaisedButton(text= "Skontroluj si test",on_release=self.close_help_dialogMM)
        self.help_dialog_mm = MDDialog(title="Niečo nieje v poriadku", text="V teste ,, NAJMENEJ ma vystihuje ,, si vynechal niektorú otázku. ",
                              size_hint=[0.9, None], auto_dismiss=False,
                              buttons=[ok_button])
        self.help_dialog_mm.open()

    def show_HelpDialogMV(self):
        ok_button = MDRaisedButton(text= "Skontroluj si test",on_release=self.close_help_dialogMV)
        self.help_dialog_mv = MDDialog(title="Niečo nieje v poriadku", text="V teste ,, NAJMENEJ ma vystihuje ,, zaškrtol viac možností ako je potreba. ",
                              size_hint=[0.9, None], auto_dismiss=False,
                              buttons=[ok_button])
        self.help_dialog_mv.open()

    def show_HelpDialogVM(self):
        ok_button = MDRaisedButton(text= "Skontroluj si test",on_release=self.close_help_dialogVM)
        self.help_dialog_vm = MDDialog(title="Niečo nieje v poriadku", text="V teste ,, NAJVIAC ma vystihuje ,,si vynechal niektorú otázku. ",
                              size_hint=[0.9, None], auto_dismiss=False,
                              buttons=[ok_button])
        self.help_dialog_vm.open()

    def show_HelpDialogVV(self):
        ok_button = MDRaisedButton(text= "Skontroluj si test",on_release=self.close_help_dialogVV)
        self.help_dialog_vv = MDDialog(title="Niečo nieje v poriadku", text="V teste ,, NAJVIAC ma vystihuje ,, si zaškrtol viac možností ako je potreba. ",
                              size_hint=[0.9, None], auto_dismiss=False,
                              buttons=[ok_button])
        self.help_dialog_vv.open()

    def close_help_dialogMM(self,obj):
        self.help_dialog_mm.dismiss()
    def close_help_dialogMV(self,obj):
        self.help_dialog_mv.dismiss()
    def close_help_dialogVV(self,obj):
        self.help_dialog_vv.dismiss()
    def close_help_dialogVM(self,obj):
        self.help_dialog_vm.dismiss()

    def d_plus(self):
        self.testovatel.test_v += ('d',)

    def i_plus(self):
        self.testovatel.test_v += ('i',)

    def s_plus(self):
        self.testovatel.test_v +=('s',)

    def k_plus(self):
        self.testovatel.test_v +=('k',)

    def n_plus(self):
        self.testovatel.test_v +=('n',)

    def d(self):
        self.testovatel.test_m +=('d',)

    def i(self):
        self.testovatel.test_m +=('i',)

    def s(self):
        self.testovatel.test_m +=('s',)

    def k(self):
        self.testovatel.test_m +=('k',)

    def n(self):
        self.testovatel.test_m +=('n',)

    def skontroluj(self):
        if len(self.testovatel.test_v)== 24 and len(self.testovatel.test_m)== 24:
            self.show_ev_dialog()
        elif len(self.testovatel.test_v)< 24:
            self.show_HelpDialogVM()
        elif len(self.testovatel.test_v)> 24:
            self.show_HelpDialogVV()
        elif len(self.testovatel.test_m)< 24:
            self.show_HelpDialogMM()
        elif len(self.testovatel.test_m)> 24:
            self.show_HelpDialogVV()
        else:
            pass



    def show_ev_dialog(self):
        btn2 = MDRaisedButton(text="ULOŽIŤ", on_release=self.close_dialog, on_press= self.evaluate)
        btn1 = MDFlatButton(text="ZRUŠIŤ", on_release= self.close_dialog)
        self.eval_dialog = MDDialog(title="Ukončiť test? ",
                                 size_hint=[0.8, 0.5], auto_dismiss=True,
                                 buttons=[btn1, btn2])
        self.eval_dialog.open()

    def close_dialog(self, obj):
        self.eval_dialog.dismiss()

    def evaluate (self,obj):
        self.testovatel.priorita()
        self.testovatel.zapis_test()
        self.manager.current= "history"
        self.manager.transition.direction = 'left'

class MyGoalsScreen (Screen):

    def on_enter(self):
        file= open("goals.txt" , "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    def bin(self):
        btn2 = MDRaisedButton(text="VYMAZAŤ", on_release=self.close_dialog, on_press=self.vymaz)
        btn1 = MDFlatButton(text="ZRUŠIŤ", on_release=self.close_dialog)
        self.bin_d = MDDialog(title="Naozaj vymazať testy?",text= "Pri vymazaní sa stratia všetky "
                                                                  "tovje ciele.",
                                    size_hint=[0.8, 0.5], auto_dismiss=True,
                                    buttons=[btn1, btn2])
        self.bin_d.open()

    def close_dialog(self, obj):
        self.bin_d.dismiss()

    def vymaz(self,obj):
        with open("goals.txt", "w") as p:
            p.write("")
        self.on_enter()


    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == 'flash':
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class GoalsScreen(Screen):
    model = ObjectProperty (None)
    ciel1= ObjectProperty(None)
    ciel2 = ObjectProperty(None)
    ciel3 = ObjectProperty(None)
    ciel4 = ObjectProperty(None)
    ciel5 = ObjectProperty(None)
    ciel6 = ObjectProperty(None)
    ciel7 = ObjectProperty(None)
    ciel8 = ObjectProperty(None)
    ciel9 = ObjectProperty(None)
    ciel10 = ObjectProperty(None)
    ciel11 = ObjectProperty(None)

    def add_goals(self):
        if self.ids.model.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Môj model je: "+ self.ids.model.text + "\n")

        if self.ids.ciel1.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Kde a ako môžem využiť svoje prednosti: "+ self.ids.ciel1.text +"\n" )

        if self.ids.ciel2.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Ako sa môžem rozvíjať: "+ self.ids.ciel2.text +"\n" )

        if self.ids.ciel3.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Čo nové som o sebe zistil: "+ self.ids.ciel3.text +"\n" )

        if self.ids.ciel4.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Ako vytvorím pre mňa motivujúce prostredie: "+ self.ids.ciel4.text +"\n" )

        if self.ids.ciel5.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Ako mojími prednosťami pomôžem tímu: " + self.ids.ciel5.text + "\n")

        if self.ids.ciel6.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Ako viem zvíšiť efektivitu a postoj k úlohám: " + self.ids.ciel6.text + "\n")

        if self.ids.ciel7.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Čo by som mal zvážiť pri jednaní s inými: " + self.ids.ciel7.text + "\n")

        if self.ids.ciel8.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Čo je na mne atraktívne: " + self.ids.ciel8.text + "\n")

        if self.ids.ciel9.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Ako viem vytvoriť príjemnejšie prostredie: " + self.ids.ciel9.text + "\n")

        if self.ids.ciel10.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Moje kroky k zdokonalovaniu sú: " + self.ids.ciel10.text + "\n")

        if self.ids.ciel11.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Čo pre to musím urobiť: " + self.ids.ciel11.text + "\n")

    def show_smart(self):
        self.smart_dialog = MDDialog(title="Technika SMART", text="Je jednou z pomôcok pre dobré definovanie cieľa \n"
                                                                "Tvoj cieľ musí byť: \n\n"
                                                                 "S- špecifický, pretože musíme vedieť čo\n"
                                                                 "M- merateľný, aby sme vedeli definovať pokrok\n"
                                                                 "A- akceptovaný, pre istotu, že všetic relevantí vedia a súhlasia\n"
                                                                 "R- realistický, aby bolo jasné, že stojíme nohami na zemi\n"
                                                                 "T- termínovaný, určený do kedy má byť splnený\n"
                                                                 "\n\n"
                                                                 "Mal by zodpovedať tieto otázky:\n\n"
                                                                 "- Čo potrebuje zmenu?\n"
                                                                 "- Aká zmena je potrebná?\n"
                                                                 "- Na koho je zmena zameraná?\n"
                                                                 "- Kde sa zmena uplatní?\n"
                                                                 "- Kedy sa zmena uplatní?\n",
                                   size_hint=[0.8, None], auto_dismiss=True,)
        self.smart_dialog.open()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == 'flash':
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"



class HistoryScreen(Screen):
    custom_sheet = None
    bin_d = None

    def on_enter(self):
        file = open("testy.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel3.text = load_file



    def bin(self):
        btn2 = MDRaisedButton(text="VYMAZAŤ", on_release=self.close_dialog, on_press=self.vymaz)
        btn1 = MDFlatButton(text="ZRUŠIŤ", on_release=self.close_dialog)
        self.bin_d = MDDialog(title="Naozaj vymazať testy?",text= "Pri vymazaní sa stratia všetky "
                                                                  "vyhodnotenia testov.",
                                    size_hint=[0.8, 0.5], auto_dismiss=True,
                                    buttons=[btn1, btn2])
        self.bin_d.open()

    def close_dialog(self, obj):
        self.bin_d.dismiss()

    def vymaz(self,obj):
        with open("testy.txt", "w") as p:
            p.write(" ")
        self.on_enter()

    def show_bottom_sheet(self):
        bs = MDListBottomSheet()
        bs.add_item("Model správania", lambda x: x,icon='account-group-outline')

        for y in 1, 2, 3, 4, 12, 13, 14, 21, 23, 24, 31, 32, 34, 41, 42, 43, 123, 124, 134, 234:
            bs.add_item(f"Ukazovateľ {y} ", partial(self.behavior, y), icon='account-group-outline')
            bs.open()

    def behavior(self, x, instance):
        self.manager.current = str(x)

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == 'flash':
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass

class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        screen = Builder.load_string(screen_helper)
        return screen

MainApp().run()
