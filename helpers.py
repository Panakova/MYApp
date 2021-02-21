screen_helper = """
ScreenManager:
    HomeScreen:
    MotivationScreenMe:
    MotivationScreenTeam:
    MotivationScreenWe:
    TestScreenV:
    GoalsScreen:
    MyGoalsScreen:
    HistoryScreen:
    
    BehaviorModel1:
    BehaviorModel2:
    BehaviorModel3:
    BehaviorModel4:
    BehaviorModel12:
    BehaviorModel13:
    BehaviorModel14:
    BehaviorModel21:
    BehaviorModel23:
    BehaviorModel24:
    BehaviorModel31:
    BehaviorModel32:
    BehaviorModel34:
    BehaviorModel41:
    BehaviorModel42:
    BehaviorModel43:
    BehaviorModel123:
    BehaviorModel124:
    BehaviorModel134:
    BehaviorModel234:
    

<HomeScreen>:
    name: "home"

    MDTextButton:
        text: "=> Spoznaj seba <="
        pos_hint: { "center_x" :0.7, "center_y":0.9}
        custom_color: 0.96,0.79,0.09, 1
        on_release: root.show_motivation_dialog()
    Image:
        source: "all.png"
        pos_hint: { "center_x" :0.5, "center_y":0.5}
        size_hint: (1,1)

    MDFloatingActionButton:
        icon: "play-circle-outline"
        size_hint: None, None
        pos_hint: {"center_x" :0.5, "center_y":0.08}
        md_bg_color: app.theme_cls.primary_color
        on_release: root.show_ChooseDialog()

    MDFloatingActionButton:
        icon: "help-circle-outline"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: { "center_x" :0.15, "center_y":0.08}
        on_release: root.show_HelpDialog()

    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}

<ItemConfirm>
    on_release: root.set_icon(check)

    CheckboxLeftWidget:
        id: check
        group: "check"            

<MotivationScreenMe>:
    name: "motivationme"
    nazov_testu: nazov_testu

    MDCard:
        orientation: "vertical"
        pos_hint:{ "center_x" :0.5, "center_y": 0.6} 
        size_hint: 0.8, 0.7
        padding: "8dp"

        MDLabel:
            text: "Osobné zlepšenie"
            height: self.texture_size[1]
            size_hint_y: None
            halign: "left"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color

        MDSeparator:
            height: "1dp"

        MDLabel:
            text: "Pri plnení otázok sa zameraj hlavne na svoje obvyklé správanie v prostredí, kde sa cítiš sám sebou."
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "   "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "Táto aplikácia ti umožní vytovriť prehľad tvojej osobnosti. Tu môžeš analyzovať svoje slabé, primerné a silné stránky. Ak zapracuješ na svojích slabých stránkach, môžeš sa tým zlepšiť"
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "   "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "Pamätaj, neexistuje zlá vlastnosť, - možno si len nenašiel jej vhodné využitie. Keď ju spoznáš, naučáš sa v akých situáciách ju najlepšie použiješ."
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "Tak poďme na to!"
            size_hint_y: None
            height: self.texture_size[1]
            halign: "center"

    MDTextField:
        id: nazov_testu
        hint_text:"Zadaj názov testu"
        helper_text: "napr. Test 1"
        helper_text_mode: "on_focus"
        pos_hint: { "center_x" :0.5, "center_y":0.2}
        size_hint: 0.8,0.1 

    MDFloatingActionButton:
        icon: "play-circle-outline"
        pos_hint: { "center_x" :0.5, "center_y":0.08}
        md_bg_color: app.theme_cls.primary_color
        on_release: 
            root.manager.current = "testv"
            root.manager.transition.direction = 'up'
        on_press: root.add_test()

    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'} 

<MotivationScreenTeam>:
    name: "motivationteam"
    nazov_testu: nazov_testu

    MDCard:
        orientation: "vertical"
        pos_hint:{ "center_x" :0.5, "center_y": 0.6} 
        size_hint: 0.8, 0.7
        padding: "8dp"

        MDLabel:
            text: "Práca v tíme"
            height: self.texture_size[1]
            size_hint_y: None
            halign: "left"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color

        MDSeparator:
            height: "1dp"   
        MDLabel:
            text: "Pri plnení otázok sa zameraj hlavne na obvyklé správanie vo svojom tíme."
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "   "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "V prípade dobre zabehnutého tímu sa členovia nehanbia prejaviť svoje prednosti a nedostatky. Využívajú teda potenciál tímu naplno. Spoluprácou môžu dosiahnúť ľubovolný cieľ v krátkom čase."
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "   "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "Využi čas aby si pomohol vytvoriť svoj tím, v ktorom sa budeš cítiť pohodlne.  "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "   "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: " Pamätaj, neexistuje zlá vlastnosť, - možno si len nenašiel jej vhodné využitie. Keď ju spoznáš, naučáš sa v akých situáciách ju najlepšie použiješ.  "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "Tak poďme na to!"
            size_hint_y: None
            height: self.texture_size[1]
            halign: "center"
            
    MDTextField:
        id: nazov_testu
        hint_text:"Zadaj názov testu"
        helper_text: "napr. Test 1"
        helper_text_mode: "on_focus"
        pos_hint: { "center_x" :0.5, "center_y":0.2}
        size_hint: 0.8,0.1 

    MDFloatingActionButton:
        icon: "play-circle-outline"
        pos_hint: { "center_x" :0.5, "center_y":0.08}
        md_bg_color: app.theme_cls.primary_color
        on_release: 
            root.manager.current = "testv"
            root.manager.transition.direction = 'up'
        on_press: root.test_name()

    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'} 

<MotivationScreenWe>:
    name: "motivationwe"
    nazov_testu: nazov_testu

    MDCard:
        orientation: "vertical"
        pos_hint:{ "center_x" :0.5, "center_y": 0.6} 
        size_hint: 0.8, 0.7
        padding: "8dp"

        MDLabel:
            text: "Pre vzťah"
            height: self.texture_size[1]
            size_hint_y: None
            halign: "left"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color

        MDSeparator:
            height: "1dp"   
        MDLabel:
            text: "Pri plnení otázok sa zameraj na svoje obvyklé správanie voči svojim blížnym"
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "Ľudí v škole neučia, ako dobre vychádzať so svojím partnerom. Kým pochopíme partnerov charakter môže ubehnúť veľa času, ktorý môžeme využiť na príjemné chvíľky. "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "   "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "Byť správny partner neznamená mať ideálne vlastnosti, ale akceptovať druhého takého aký je. "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "   "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: " Pamätaj, neexistuje zlá vlastnosť, - možno si len nenašiel jej vhodné využitie. Keď ju spoznáš, naučáš sa v akých situáciách ju najlepšie použiješ.  "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "   "
            size_hint_y: None
            height: self.texture_size[1]
            halign: "left"
        MDLabel:
            text: "Tak poďme na to!"
            size_hint_y: None
            height: self.texture_size[1]
            halign: "center"
            

    MDTextField:
        id: nazov_testu
        hint_text:"Zadaj názov testu"
        helper_text: "napr. Test 1"
        helper_text_mode: "on_focus"
        pos_hint: { "center_x" :0.5, "center_y":0.2}
        size_hint: 0.8,0.1 

    MDFloatingActionButton:
        icon: "play-circle-outline"
        pos_hint: { "center_x" :0.5, "center_y":0.08}
        md_bg_color: app.theme_cls.primary_color
        on_release: 
            root.manager.current = "testv"
            root.manager.transition.direction = 'up'
        on_press: root.test_name()

    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'} 


<TestConfirm>
    on_release: root.set_icon(checkbox)
    CheckboxLeftWidget:
        id: checkbox

<TestScreenV>:
    name: "testv"
    
    ScrollView:
        do_scroll_x: False
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(1000)
            spacing: "20dp"
            
            MDSeparator:
                height: "1dp"
                
    
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 0.9,1
                pos_hint: {"center_x": .5, "center_y": .6}
        
                OneLineListItem:                          
                    text: "Vyber možnosť, ktorá ťa NAJVIAC vystihuje"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    font_size: (root.width**2 + root.height**2) / 13**4
        
                ScrollView:
                    do_scroll_x: False
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(6530)
        
                        OneLineListItem:
                            text: "1/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                            
                        TestConfirm:
                            text: "rád sa delím s inými"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            text_of_the_option: ("s",)
                            on_press: 
                                root.plus()
                                root.s_plus()
                        TestConfirm:
                            text: "som bezproblemový spoločník"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.plus()
                                root.n_plus()
                            text_of_the_option: ("n",)
                        TestConfirm:    
                            id: testconfirm
                            text: "chcem zvíťaziť"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.plus()
                                root.d_plus()
                            text_of_the_option: ("d",)
                        TestConfirm:
                            text: "veľa sa smejem"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.plus()
                                root.n_plus()
                            text_of_the_option: ("n",)
        
                        OneLineListItem:
                            text: "2/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color   
                        TestConfirm:
                            text: "Som prístupný novým nápadom"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.plus()
                                root.i_plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "Rád robím láskavosti"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "mám silnú vôľu"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "som bezstarostný a veselý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "3/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "robím, čo odomňa očakávajú"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "robím, čo chcem ja"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "priateľským chovaním dosiahnem, čo chcem"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "som úprimný k iným"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "4/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "som u iných obľúbený"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "viem sa dobre ovládať"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "som kolegiálny a milý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "som nekľudný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "5/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "je ťažké splniť moje očakávania"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "snažím sa prekonať ostatných"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "držím sa pravidiel"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "som za každú srandu"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
        
                        OneLineListItem:
                            text: "6/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "rád podstupujem riziká"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "som ohľaduplný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "som pôvabný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "som spokojný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "7/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "som schopný sa nadchnúť"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "som presný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "som vyrovnaný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "rád prevezmem iniciatívu"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "8/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        TestConfirm:
                            text: "mám sebaisté vystupovanie"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "som rád stredobodom pozornosti"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:    
                            text: "mám skolny predpokladať ťažkosti"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "som ľahko ovplyvniteľný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "9/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "dostávam často pochvalu od iných"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "som ochotný pomôcť iným"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:    
                            text: "zasadzujem sa za svoje princípy"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "nemám problém poradiť sa"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "10/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        TestConfirm:
                            text: "som netrpezlivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "dobre vychádzam s inými"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "vždy chcem každému vyhovieť"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "som temperamentný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
        
                        OneLineListItem:
                            text: "11/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        TestConfirm:
                            text: "mám rád kontakt s ľuďmi"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "som človek činu"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "mám mäkké srdce"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "mám zmysel pre krásne veci"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "12/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "nevidím všetko tak prísne a presne"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "rád sa zabávam"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:    
                            text: "nevyhýbam sa hádkam"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "som diplomatický"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                            
                        OneLineListItem:
                            text: "13/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "ľahko sa dokážem rozhodnúť"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "som spontánny, bezprostredný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:    
                            text: "som mierumilovný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "prejavujem iným dôveru"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "14/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "som zdvorilý a vychádzam iným v ústrety"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "mám rád dobrodružstvá"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "s optimizmom hľadím do budúcnosti"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "beriem ohľad na iných"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "15/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        TestConfirm:
                            text: "ľahko sa dokážem preniesť do cítenia iných"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "som zdržanlivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "dokážem iných ľahko presvedčiť"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "mám veľa nápadov"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "16/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        TestConfirm:
                            text: "som zhovorčivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "nemám ťažkosti zmieriť sa s niečím"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:    
                            text: "držím sa svojich zvyklostí"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "rád rozhodujem"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "17/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "som váhavý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "považujem za dôležité mať úspech"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "milo sa správam k iným"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "dokážem iných ovplyvniť"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
        
                        OneLineListItem:
                            text: "18/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "dokážem iných strhnúť"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "dokážem sa vytrvalo zahryznúť do úlohy"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "som zvedavý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "dbám na potreby iných"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "19/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "som spoločenský"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "rád pracujem sám"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "som skôr tichý typ človeka"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "len tak ľahko sa nerozčúlim"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "20/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "som disciplinovaný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "som otvorený a spoločenský"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:    
                            text: "som veľkorysý a štedrý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "som veľmi priamočiary"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "21/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "som hanblivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "mám odvahu rozhodovať"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "ľahko dokážem nadchnúť iných"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "ľahko sa poddám"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "22/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        TestConfirm:
                            text: "ľahko si dokážem iných omotať kolo prsta"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "mám sklony neprejaviť svoju mienku"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:    
                            text: "najskôr si premyslím, potom poviem"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "poviem rovno, čo si myslím"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "23/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "som srdečný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "nemám rád extrémy"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:    
                            text: "som prístupný novým úlohám"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "chcem zažiť niečo zaujímavé"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "24/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        TestConfirm:
                            text: "dokážem presadiť svoju vôľu"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "som chápavý voči iným"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:    
                            text: "preukazujem rešpekt voči iným"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "som sebaistý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
            
            MDProgressBar:
                id: progress
                size_hint_x: 0.8
                size_hint_y: 0.08
                color: app.theme_cls.accent_color
                pos_hint: { "center_x" :0.5, "center_y":0.2}
                            
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 0.9,1
                pos_hint: {"center_x": .5, "center_y": .6} 
                   
                OneLineListItem:                          
                    text: "Vyber možnosť, ktorá ťa NAJMENEJ vystihuje"
                    theme_text_color: "Custom"
                    text_color: 0.19,0.38,0.17,1
                    font_size: (root.width**2 + root.height**2) / 13**4
    
                ScrollView:
                    do_scroll_x: False
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(6530)
        
                        OneLineListItem:
                            text: "1/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                            
                        TestConfirm:
                            text: "prieberčivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            text_of_the_option: "s"
                            on_press: 
                                root.plus()
                                root.s()
                        TestConfirm:
                            text: "poslušný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:    
                            text: "náročný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.plus()
                                root.d()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "hravý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.plus()
                                root.n()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "2/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1 
                        TestConfirm:
                            text: "spoločenský"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.plus()
                                root.i()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "sebaistý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.plus()
                                root.k()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "trpezlivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.plus()
                                root.n()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "kľudný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.plus()
                                root.s()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "3/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "atraktívny"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "zásadový"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "neústupčivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "milý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "4/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "diplomatický"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "spokojný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "odvážny"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "šikovný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "5/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "nekľudný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "kritický"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "obľúbený"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "priateľský"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
        
                        OneLineListItem:
                            text: "6/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "odvážny"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "podnetný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "poddajný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "hanblivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "7/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "jemný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "presvedčivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "skromný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "originálny"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "8/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "arogantný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "ústupčivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:    
                            text: "podmanivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "bojazlivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "9/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "priateľský"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "presný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:    
                            text: "priamy"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "uzatvorený"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "10/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "zdvorilý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "pripravený na riziko"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "optimistický"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "ústretový"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
        
                        OneLineListItem:
                            text: "11/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "träfalý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "ľahko ovplyvniteľný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "lojálny"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "šarmantný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "12/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "ohľaduplný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "ctižiadostivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:    
                            text: "veselý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "vyrovnaný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                            
                        OneLineListItem:
                            text: "13/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "odvážny"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "pokojný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:    
                            text: "puntičkársky"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "šťastný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "14/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "hašterivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "prispôsobivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "vtipný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "nenútený"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "15/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "učenlivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "snaživý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:    
                            text: "príjemný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "bezstarostný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "16/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1 
                        TestConfirm:
                            text: "rozhodný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "uznávaný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:    
                            text: "starostlivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "neistý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "17/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "zhovorčivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "zdržanlivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "tradicionalista"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "sebaistý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
        
                        OneLineListItem:
                            text: "18/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "suverénny"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "chápavý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "tolerantný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "priebojný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "19/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "veľkorysý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "živý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "poriadkumilovný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "vytrvalý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "20/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "dôverčivý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "povzbudzujúci"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:    
                            text: "pozitívne mysliaci"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:
                            text: "mierumilovný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "21/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "obozretný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "činorodý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:    
                            text: "strhujúci"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "dobročinný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "22/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1 
                        TestConfirm:
                            text: "spontánny"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        TestConfirm:
                            text: "ochotný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:    
                            text: "silný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "zábavný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "23/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "dobrodružný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "rozhodný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        TestConfirm:    
                            text: "sympatický"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        TestConfirm:
                            text: "rozumný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "24/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        TestConfirm:
                            text: "komunikatívny"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        TestConfirm:
                            text: "kultivovaný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:    
                            text: "silný"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        TestConfirm:
                            text: "zhovievavý"
                            font_size: (root.width**2 + root.height**2) / 13**4
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"  
            
            MDSeparator:
                height: "1dp"                
                               
    MDFloatingActionButton:
        icon: "check-circle-outline"
        pos_hint: { "center_x" :0.5, "center_y":0.08}
        md_bg_color: app.theme_cls.primary_color
        on_release: 
            root.vyhodnot()
            root.show_example_snackbar()
            

     
        
<GoalsScreen>:
    name: "goals"
    model: model
    ciel1: ciel1
    ciel2: ciel2
    ciel3: ciel3
    ciel4: ciel4
    ciel5: ciel5
    ciel6: ciel6
    ciel7: ciel7
    ciel8: ciel8
    ciel9: ciel9
    ciel10: ciel10
    ciel11: ciel11
    
    
    MDToolbar:
        title: "Definuj si ciele"
        md_bg_color: app.theme_cls.accent_color
        pos_hint: {"top": 1} 
        left_action_items: [["flash", lambda x: None]]     
        
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.7
        pos_hint: {"center_x": .5, "center_y": .53}
        
        ScrollView:
            do_scroll_x: False
            MDList:
                padding: "10dp"
                spacing: "10dp"
                
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.size[1]
                     
                    MDLabel: 
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text: "Ak si ten, kto chce naplniť svoje túžby a zistiť, čo všetko môže v živote dokázať" 
                     
                    MDLabel:
                        halign: "center"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text: "spoznávaj sa => dodržuj svoje ciele => vytvor si z nich návyk => sprav seba lepším"
                            
                    MDSeparator:
                        height: "1dp"   
                                            
                    MDLabel:
                        text: "V dnešnom svete záleží hlavne na tom, čo dokážes. Ak si spávne zadefinuješ ciele, uistíš sa, že ich zlvádneš. "
                        size_hint_y: None
                        height: self.texture_size[1]  
                        halign: "center" 
                        
                    BoxLayout:                      
                        MDLabel:
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                            text: "Pomôž si overenou technikou:"
                         
                        MDRoundFlatButton:
                            text: "SMART" 
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.accent_color
                            on_press: root.show_smart()
                            
                        #MDIconButton:
                        #    icon: 'lightbulb-on-outline'
                        #    theme_text_color: "Custom"
                        #    text_color: app.theme_cls.accent_color
                        #    on_press: root.img()
        
                OneLineIconListItem:
                    #bg_color: 0.6,0.73,0.35,1
                    bg_color: 1,0.76,0.03,0.5
                    text: "Pre mňa"
                    IconLeftSampleWidget:
                        icon: "human-greeting"
                
                MDTextField:
                    id: model
                    multiline: True
                    hint_text: "Aký  model správania mi vyšiel?"
                    color_mode: "accent"
                    helper_text: "Model"
                    helper_text_mode: "on_focus"
                                
                MDTextField:
                    id: ciel1
                    multiline: True
                    hint_text: "Kde a ako môžem využiť svoje prednosti už dnes?"
                    helper_text: "Cieľ č. 1"
                    helper_text_mode: "on_focus"
                    
                MDTextField:
                    id: ciel2
                    multiline: True
                    hint_text: "Ako sa môžem rozvíjať?"
                    helper_text: "Cieľ č. 2"
                    helper_text_mode: "on_focus"
                    
                MDTextField:
                    id: ciel3
                    multiline: True
                    hint_text: "Čo nové som o sebe zistil?"
                    helper_text: "Cieľ č. 3"
                    helper_text_mode: "on_focus"
                
                MDTextField:
                    id: ciel4
                    multiline: True
                    hint_text: "Ako vytvorím pre mňa motivujúce prostredie?"
                    helper_text: "Cieľ č. 4"
                    helper_text_mode: "on_focus"
                
                OneLineIconListItem:
                    bg_color: 1,0.76,0.03,0.5
                    text: "Pre tím"
                    IconLeftSampleWidget:
                        icon: "human-capacity-increase"
                
                MDTextField:
                    id: ciel5
                    multiline: True
                    hint_text: "Ako môžem svojími prednosťami pomocť tímu?"
                    helper_text: "Cieľ č. 5"
                    helper_text_mode: "on_focus"
                    
                MDTextField:
                    id: ciel6
                    multiline: True
                    hint_text: "Ako viem zvíšiť efektivitu v postoji k úlohám?"
                    helper_text: "Cieľ č. 6"
                    helper_text_mode: "on_focus"
                    
                MDTextField:
                    id: ciel7
                    multiline: True
                    hint_text: "Čo by som mal zvážiť pri jednaní s inými?"
                    helper_text: "Cieľ č. 7"
                    helper_text_mode: "on_focus"
                    
                OneLineIconListItem:
                    bg_color: 1,0.76,0.03,0.5
                    text: "Pre vzťahy"
                    IconLeftSampleWidget:
                        icon: "human-male-female"
                
                MDTextField:
                    id: ciel8
                    multiline: True
                    hint_text: "Čo na mne je atraktívne?"
                    helper_text: "Cieľ č. 8"
                    helper_text_mode: "on_focus"
                    
                MDTextField:
                    id: ciel9
                    multiline: True
                    hint_text: "Ako viem vytvoriť príjemnejšie prostredie?"
                    helper_text: "Cieľ č. 9"
                    helper_text_mode: "on_focus"
                    
                OneLineListItem:
                    bg_color: 1,0.76,0.03,0.5
                    text: "Jednoduché to vedieť, potrebné o tom hovoriť, ale najdôležitejšie je KONAŤ"
                    
                    
                MDTextField:
                    id: ciel10
                    multiline: True
                    hint_text: "Ciele, ktoré som si zadefinoval, môžem dosiahnuť týmito krokmi:"
                    helper_text: "Cieľ č. 10"
                    helper_text_mode: "on_focus"
                        
                MDTextField:
                    id: ciel11
                    multiline: True
                    hint_text: "Čo pre to muším urobiť?"
                    helper_text: "Cieľ č. 11"
                    helper_text_mode: "on_focus"  
                
        
    MDFillRoundFlatButton:
        text: "Uložiť"
        size_hint: None, None
        pos_hint: {"center_x" :0.5, "center_y":0.08}
        on_release: 
            root.add_goals()
              
               
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
               
         
<MyGoalsScreen>:
    name: "mygoals"  
    
    MDToolbar:
        title: "Moje ciele"
        md_bg_color: 0.6,0.73,0.35,1
        #md_bg_color: 0.33,0.6,0.46,1
        pos_hint: {"top": 1} 
        right_action_items: [['lightning-bolt', lambda x: None]] 

    MDCard:
        pos_hint:{ "center_x" :0.5, "center_y": 0.5} 
        size_hint: 0.9, 0.7
        orientation: 'vertical'
        padding: "5dp"
        spacing: "5dp"
                    
        MDLabel:
            text: "Pozrime sa na to, čo môžeš ovplyvniť svojími výnimočnými vlastnosťami:"
            pos_hint: { "center_y":0.95}
            halign: "left"
            size_hint: 0.8, 0.1
            height: self.texture_size[1] 
            
        MDSeparator:
            height: "1dp"

        MDLabel:
            id: mylabel
            halign: "left"
            height: self.texture_size[1] 
         
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Upraviť"
        on_press: 
            root.manager.current = "goals"
            root.manager.transition.direction = 'up'
                    
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
       
<HistoryScreen>:
    name: "history"
    
    MDToolbar:
        title: "História testov"
        md_bg_color: 0.6,0.73,0.35,1
        #md_bg_color: 0.33,0.6,0.46,1
        pos_hint: {"top": 1} 
        right_action_items: [['notebook-outline', lambda x: None]] 
    
    ThreeLineAvatarListItem:   
        id:mylabel2 
        ImageLeftWidget:
            source: "all.png"
    
    MDLabel:
        id: mylabel3
        spacing: "10dp"
        halign: "center"
        height: self.texture_size[1]         

    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Typy osobností"
        on_press: root.show_bottom_sheet()
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            


<MainApp@Screen>:        
    MDFloatingActionButtonSpeedDial:
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
"""


