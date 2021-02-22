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
        on_press: root.add_test()

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
        on_press: root.add_test()

    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'} 

<TestScreenV>:
    name: "testv"
    
    ScrollView:
        do_scroll_x: False
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(1100)
            spacing: "20dp"
            
            MDSeparator:
                height: "1dp"
                
    
            MDCard:
                orientation: "vertical"
                padding: "8dp"
                size_hint: 0.9,1
                pos_hint: {"center_x": .5, "center_y": .5}
        
                OneLineListItem:                          
                    text: "Vyber možnosť, ktorá ťa NAJVIAC vystihuje"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    
                    
                Button:
                    text: "Vymazať poslednú možnosť"
                    background_normal: ""
                    back_color: (1,0,1,1)
                    color: (0,0,0,1)
                    on_press: self.background_color = (0.95,0.26,0.2,0.5)
                    on_release: root.dele_v()
                    size: (1, 1)
                    size_hint: 1, 0.15
                    
                MDSeparator:
                    height: "1dp"
                    
                ScrollView:
                    do_scroll_x: False
                    
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(6500)
        
                        OneLineListItem:
                            text: "1/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                            
                        Button:
                            text: "rád sa delím s inými"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_release:
                                root.plus()
                                root.s_plus()
                        Button:
                            text: "som bezproblemový spoločník"
                            on_press: 
                                root.plus()
                                root.n_plus()
                            text_of_the_option: ("n",)
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                        Button:
                            text: "chcem zvíťaziť"
                            on_press: 
                                root.plus()
                                root.d_plus()
                            text_of_the_option: ("d",)
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                        Button:
                            text: "veľa sa smejem"
                            on_press: 
                                root.plus()
                                root.n_plus()
                            text_of_the_option: ("n",)
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            
                        OneLineListItem:
                            text: "2/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color   
                        Button:
                            text: "Som prístupný novým nápadom"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.plus()
                                root.i_plus()
                            text_of_the_option: "i"
                        Button:
                            text: "Rád robím láskavosti"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:    
                            text: "mám silnú vôľu"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "som bezstarostný a veselý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "3/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "robím, čo odomňa očakávajú"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "robím, čo chcem ja"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button:   
                            text: "priateľským chovaním dosiahnem, čo chcem"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "som úprimný k iným"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "4/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "som u iných obľúbený"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "viem sa dobre ovládať"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:   
                            text: "som kolegiálny a milý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "som nekľudný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "5/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "je ťažké splniť moje očakávania"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "snažím sa prekonať ostatných"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button: 
                            text: "držím sa pravidiel"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "som za každú srandu"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
        
                        OneLineListItem:
                            text: "6/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "rád podstupujem riziká"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "som ohľaduplný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "som pôvabný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "som spokojný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "7/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "som schopný sa nadchnúť"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "som presný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "som vyrovnaný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "rád prevezmem iniciatívu"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "8/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        Button:
                            text: "mám sebaisté vystupovanie"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "som rád stredobodom pozornosti"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button: 
                            text: "mám skolny predpokladať ťažkosti"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "som ľahko ovplyvniteľný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "9/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "dostávam často pochvalu od iných"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "som ochotný pomôcť iným"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "zasadzujem sa za svoje princípy"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "nemám problém poradiť sa"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "10/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        Button:
                            text: "som netrpezlivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "dobre vychádzam s inými"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "vždy chcem každému vyhovieť"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "som temperamentný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
        
                        OneLineListItem:
                            text: "11/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        Button:
                            text: "mám rád kontakt s ľuďmi"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "som človek činu"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button: 
                            text: "mám mäkké srdce"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "mám zmysel pre krásne veci"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "12/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "nevidím všetko tak prísne a presne"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "rád sa zabávam"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button: 
                            text: "nevyhýbam sa hádkam"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "som diplomatický"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                            
                        OneLineListItem:
                            text: "13/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "ľahko sa dokážem rozhodnúť"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "som spontánny, bezprostredný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button:   
                            text: "som mierumilovný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "prejavujem iným dôveru"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "14/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "som zdvorilý a vychádzam iným v ústrety"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "mám rád dobrodružstvá"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button: 
                            text: "s optimizmom hľadím do budúcnosti"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "beriem ohľad na iných"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "15/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        Button:
                            text: "ľahko sa dokážem preniesť do cítenia iných"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "som zdržanlivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:  
                            text: "dokážem iných ľahko presvedčiť"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "mám veľa nápadov"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "16/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        Button:
                            text: "som zhovorčivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "nemám ťažkosti zmieriť sa s niečím"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        Button:  
                            text: "držím sa svojich zvyklostí"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "rád rozhodujem"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "17/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "som váhavý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "považujem za dôležité mať úspech"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button:   
                            text: "milo sa správam k iným"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "dokážem iných ovplyvniť"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
        
                        OneLineListItem:
                            text: "18/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "dokážem iných strhnúť"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "dokážem sa vytrvalo zahryznúť do úlohy"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button: 
                            text: "som zvedavý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "dbám na potreby iných"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "19/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "som spoločenský"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "rád pracujem sám"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button: 
                            text: "som skôr tichý typ človeka"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "len tak ľahko sa nerozčúlim"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "20/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "som disciplinovaný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "som otvorený a spoločenský"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "som veľkorysý a štedrý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "som veľmi priamočiary"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "21/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "som hanblivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "mám odvahu rozhodovať"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "ľahko dokážem nadchnúť iných"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "ľahko sa poddám"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "22/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color 
                        Button:
                            text: "ľahko si dokážem iných omotať kolo prsta"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.i_plus()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "mám sklony neprejaviť svoju mienku"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "najskôr si premyslím, potom poviem"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "poviem rovno, čo si myslím"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "23/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "som srdečný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "nemám rád extrémy"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.s_plus()
                                root.plus()
                            text_of_the_option: "s"
                        Button:  
                            text: "som prístupný novým úlohám"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.k_plus()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "chcem zažiť niečo zaujímavé"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "24/24 "
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                        Button:
                            text: "dokážem presadiť svoju vôľu"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.d_plus()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "som chápavý voči iným"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "preukazujem rešpekt voči iným"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
                            on_press: 
                                root.n_plus()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "som sebaistý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.95,0.26,0.2,1)
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
                    
                Button:
                    text: "Vymazať poslednú možnosť"
                    background_normal: ""
                    back_color: (1,0,1,1)
                    color: (0,0,0,1)
                    on_press: self.background_color = (0.6,0.73,0.35,0.5)
                    on_release: root.dele_m()
                    size: (1, 1)
                    size_hint: 1, 0.15
    
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
                            
                        Button:
                            text: "prieberčivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            text_of_the_option: "s"
                            on_press: 
                                root.plus()
                                root.s()
                        Button:
                            text: "poslušný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button: 
                            text: "náročný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.plus()
                                root.d()
                            text_of_the_option: "d"
                        Button:
                            text: "hravý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.plus()
                                root.n()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "2/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1 
                        Button:
                            text: "spoločenský"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.plus()
                                root.i()
                            text_of_the_option: "i"
                        Button:
                            text: "sebaistý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.plus()
                                root.k()
                            text_of_the_option: "k"
                        Button:
                            text: "trpezlivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.plus()
                                root.n()
                            text_of_the_option: "n"
                        Button:
                            text: "kľudný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.plus()
                                root.s()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "3/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "atraktívny"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "zásadový"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "neústupčivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "milý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "4/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "diplomatický"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "spokojný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "odvážny"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "šikovný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "5/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "nekľudný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "kritický"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "obľúbený"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "priateľský"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
        
                        OneLineListItem:
                            text: "6/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "odvážny"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "podnetný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "poddajný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "hanblivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "7/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "jemný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "presvedčivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:   
                            text: "skromný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "originálny"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "8/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "arogantný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "ústupčivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button: 
                            text: "podmanivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "bojazlivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "9/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "priateľský"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "presný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        Button:  
                            text: "priamy"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "uzatvorený"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "10/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "zdvorilý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "pripravený na riziko"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "optimistický"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "ústretový"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
        
                        OneLineListItem:
                            text: "11/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "träfalý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "ľahko ovplyvniteľný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:  
                            text: "lojálny"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "šarmantný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "12/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "ohľaduplný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "ctižiadostivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button: 
                            text: "veselý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "vyrovnaný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                            
                        OneLineListItem:
                            text: "13/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "odvážny"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "pokojný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "puntičkársky"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "šťastný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "14/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "hašterivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "prispôsobivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "vtipný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "nenútený"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "15/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "učenlivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "snaživý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button: 
                            text: "príjemný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "bezstarostný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "16/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1 
                        Button:
                            text: "rozhodný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "uznávaný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "starostlivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "neistý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "17/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "zhovorčivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "zdržanlivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "tradicionalista"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "sebaistý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
        
                        OneLineListItem:
                            text: "18/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "suverénny"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "chápavý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "tolerantný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "priebojný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "19/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "veľkorysý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "živý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:  
                            text: "poriadkumilovný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "vytrvalý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
        
                        OneLineListItem:
                            text: "20/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "dôverčivý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "povzbudzujúci"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button: 
                            text: "pozitívne mysliaci"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        Button:
                            text: "mierumilovný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "21/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "obozretný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "činorodý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:   
                            text: "strhujúci"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "dobročinný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
        
                        OneLineListItem:
                            text: "22/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1 
                        Button:
                            text: "spontánny"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.i()
                                root.plus()
                            text_of_the_option: "i"
                        Button:
                            text: "ochotný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "silný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "zábavný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "23/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "dobrodružný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "rozhodný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.s()
                                root.plus()
                            text_of_the_option: "s"
                        Button: 
                            text: "sympatický"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.k()
                                root.plus()
                            text_of_the_option: "k"
                        Button:
                            text: "rozumný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
        
                        OneLineListItem:
                            text: "24/24 "
                            theme_text_color: "Custom"
                            text_color: 0.19,0.38,0.17,1
                        Button:
                            text: "komunikatívny"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.d()
                                root.plus()
                            text_of_the_option: "d"
                        Button:
                            text: "kultivovaný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:   
                            text: "silný"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
                            on_press: 
                                root.n()
                                root.plus()
                            text_of_the_option: "n"
                        Button:
                            text: "zhovievavý"
                            background_normal: ""
                            back_color: (1,0,1,1)
                            color: (0,0,0,1)
                            on_press: self.background_color = (0.19,0.38,0.17,0.85)
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


