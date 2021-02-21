from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog


class BehaviorModel1(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu vo vedení,uspokojiť svoju rozhodnosť a individualitu. Pracuje dobre ak sa okolie neustále mení.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Kariéra, výzva, konkurencia, nezávislosť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Určovať chod udalostí a mať svoj osud vo vlastných rukách.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Hovorí energicky, má jasnú logiku a precízne vyberá slová. Suverénne pracuje s vyhláseniami odborníkov a vie dobre vizualizovať. Vyžaduje rozhodné zapojenie sa účastníkov, dokáže iných veľmi dobre presvedčiť o materiálnych veciach a taktiež dobre o nemateriálnych veciach.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Neohrozený vedúci pracovník, ktorý svojmu tímu dokáže aj v ťažkých situáciách udať správny smer. Odmeňuje verných spolupracovníkov, buduje si rad verných, ktorí ho počúvajú.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Využíva informácie na uplatnenie moci. Robí ťažkosti akonáhle nie je stredobodom pozornosti. Nechce sa začleniť do tímu. Stráca záujem akonáhle nemá novú výzvu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Veci vybaví rýchle, otvorene vyjadruje svoj názor k stanoveným cieľom. Na dosiahnutie cieľov využíva všetky prostriedky. Určí si jedného nepriateľa alebo prekážku, ktorú je nutné zdolať. Dosahuje vrcholné osobné výkony.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Konfrontáciou, reaguje pritom netrpezlivo a nervózne, málo sa zaujíma o to ako ho berú iní a či je obľúbený. Chce dosiahnuť, aby sa iní vzdali svojich cieľov.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Je produktívnejší, nátlak pokladá za nástroj na zavedenie opatrení",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Akceptuje len zmysluplné zmeny, často z vecných dôvodov zastáva názory druhej strany aj keď k nej nepatrí. Očakáva nariadenia, ktoré má plniť. Odmieta ako nadriadeného prijať slabú osobnosť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-byť vizionárom, priekopníkom a hľadať nové možnosti a cesty\n"
                                                                                "- rozlišovať dôležité od menej dôležitého\n"
                                                                                "- ukázať rozhľad, napr. pri plánovaní alebo v predvídaní následkov konania",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Prejavovať viac pochopenia a porozumenia voči iným, počúvať čo iní hovoria a neprerušovať ich,výhrady iných využívať ako šance dokázať opak; nevytvárať bojové napätie len preto aby ste presvedčili iných, zapojiť iných do práce radšej ako ochotných spolupracovníkov a nie ako podriadených partnerov, viac spolupracovať s ľuďmi, ktorí lepšie dokážu spolupracovať v tíme (Modely 23,32,234)",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel2(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po akceptovaní, spolupatričnosti a spokojnosti. Pracuje dohre keď nie je pod kontrolou a keď sa nemusí zaoberať maličkosťami.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Kontakt so svetom, uznanie, postavenie, prestíž a mnohorakosť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Zaoberať sa rozličnými aktivitami.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Dokáže druhých zbaviť zaujatosti, prejavuje záujem, vyžaruje šarm a sebave¬domie. Veľa a rád hovorí, vtipkuje, veľa sľubuje. Bagatelizuje ťažkosti. Iných dokáže len ťažko presvedčiť o materiálnych veciach, o nemateriálnych celkom dobre.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Dokáže odstrániť napätie tým. že berie ohľad na to. že jeho tím potrebuje zábavu, akitivity a sociálnu kreativitu. Je pripravený deliť sa o vedenie tímu s inými.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Venuje rutinným úlohám málo pozornosti, zjednodušuje riešenia, nesprávne od¬haduje schopnosti druhých, má často ťažkosti správne odhadnúť potrebný čas na splnenie úloh",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Využíva jestvujúce prostriedky. Myslí si. že nové situácie vyžadujú aj nové me¬tódy. Priťahujú ho také úlohy, ktoré vyžadujú pozitívny prístup a ľudskosť. Chce vždy vytvořit priateľskú, veselú atmosféru a nezaujíma sa o eficieneiu..",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Vyhýba sa im. Myslí si. že konflikty ubližujú ľuďom. Vyžaduje harmóniu, chce aby ho všetci akceptovali a mali radi.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Obnovuje svoje vplyvné kontakty, používa svoj humor a šarm aby sa ubránil kritike.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Stavia mosty tým. že dokáže zabránit napätiu, dokáže sa spoľahnúť na silnú ve¬dúcu osobnosť. Tak zostanú všetci členovia tímu produktívni a disciplinovaní.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-získavať si iných pomocou oduševnených prednášok, iných podporovať a radiť im\n"
                                                                                "-jednať spontánne na základe vnútorného presvedčenia \n"
                                                                                "-dozvedieť sa od iných ich tajné problémy, obavy a pomôcť im.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Koncentrovať sa na úlohu; dodržiavať dohodnuté termíny: hovoriť rozhodne a priamo; byť objektívny pri rozhodovaní: vedieť si poradiť s námietkami; spolupracovať s jednotlivcami, ktorí majú schopnosti v rozvíjaní organizovaného prístupu (Modely 4. 43. 134).",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel3(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Nepokladá osobné schopnosti za dôležité a podceňuje ich. Skrýva svoje osobné nádeje a ambície, čaká čo sa udeje namiesto aby niečo aktívne zmenil.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po spolupráci, spokojnosti a zdržanlivosti. Pracuje dobre, keď má dostatok času na na to. aby postupoval systematicky.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Priateľstvo, istota, plnenie povinností, uznanie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Dosiahnuť úspech pomocou špecializácie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Kľudným a úprimným spôsobom zapája angažovaných a skromných ľudí. prosí iných o pomoc aby bol dosiahnutý úspech pri predstavení výhod produktu alebo nápadu. Dokáže iných relatívne dobre presvedčiť o materiálnych veciach, o ne-materiálnych skôr ťažko.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Je vedúcim, ktorý vychádza iným v ústrety. Umožní tímu vyriešiť ťažkosti keď sa niekoľko kandidátov uchádza o vedúcu pozíciu. Dokáže dobre presmerovať ľudi. ktorí len neochotne spolupracujú.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Má odborné znalosti v jednej oblasti, pri riešení problémov využíva zdravý rozum, krok za krokom sa učí nové metódy. Má ťažkosti odolať nadmernej zod¬povednosti.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Uzatvára kompromisy, aby sa našlo pre obe stránky vyhovujúce riešenie alebo stredná cesta medzi dvoma extrémami.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Ochotne preberá zodpovednosť a hľadá najlepšie trvalé riešenie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Identifikuje sa s tými kolegami, ktorí si želajú prísny štýl vedenia. Pracuje efek¬tívne ako špecialista, dokáže dobre stanovovať priority..",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-je cieľavedomý, napr. v presnom odoslaní termínovaných podkladov \n"
                                                                                "-Prijíma nariadenia a pokyny, bez váhania ich plní a akceptuje\n"
                                                                                "-ovláda obsluhu zariadení a prístrojov",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Aj pod nátlakom nestratiť kontrolu; okamžite pokarhať tých. ktorí sú nezodpovední; stanoviť smernice na dosiahnutie úloh; jednať prezieravo, radšej sa sám chopiť iniciatívy než vyčkávať a reagovať na ľudí alebo udalosti: spolupracovať s jednotlivcami, ktorí majú schopnosti vniesť do práce rôznorodosť (Modely 12.24. 124). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel4(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po odbornosti, svedomitosti a sebadisciplíne. Pracuje dobre keď môže postupovať podľa jasne stanovených a Strukturovaných línií.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Etický a morálny kódex, vedomosti, precízna práca a uznanie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Vniesť poriadok do chaosu",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Stavia na reťazi argumentov, aby presvedčil iných. Dokáže si získať ich dôveru svojimi uváženými, presnými a zdržanlivými prejavmi. Neprejavuje city. Do¬káže druhých veľmi dobre presvedčiť o materiálnych veciach, o nemateriálnych relatívne dobre. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Je vedúcim technickým pracovníkom, ktorý pomáha tímu pri riešení odborných problémov. Česť a rituály sú preňho dôležité, dbá na dodržiavanie formálnosti v správaní.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Je precitlivelý voči kritike, doslova striehne na dodržiavanie pravidiel a predpisov, je nadmeru starostlivý. Má nedostatok spontánnosti na to, aby dokázal rýchlo zmeniť svoje plány. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Svoje ciele dosahuje vážnym, kľudným a rozhodným spôsobom. Vytvára odbor¬né postupy a vyvíja sa minimálne v jednej časti svojej odbornosti ako odborník. Uprednostňuje úlohy, ktoré si vyžadujú analytické a kritické schopnosti pri riešení problémov",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Vyhýba sa im. Snaží sa nemiešať do problémov, ktoré môžu spôsobiť konflikt. Myslí si. že nemá zmysel pokúšať sa riešiť konflikty.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Stane sa ešte opatrnejším a svedomitejším.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Pred každým rozhodnutím starostlivo zvažuje možné následky. Svojimi kritickými úvahami a zbieraním informácií pomáha všetkým. Dokáže dobre analyzovať. viac sa venuje riešeniu úloh a nezaoberá sa vzťahmi osôb v tíme.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-účtovníctvo, všetko čo súvisí s číslami, napr. pokladňa a štatistiky \n"
                                                                                "-vytváranie plánov a návrhov, napr. plán stavby\n"
                                                                                "-zaraďovanie objektov do kategórií, napr. knihy ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Nadviazať kontakt s novými ľuďmi; vyvinúť schopnosť lepšie znášať konflikty: urýchliť rozhodovanie sa; spoznať, že nie všetky problémy sú komplikované: nacvičovať si rýchlejšie rozhodovanie v menej dôležitých oblastiach: spolupracovať s jednotlivcami, ktorí majú dobré schopnosti nadväzovať kontakty s inými (Modely 2. 24, 123). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel12(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po rozhodnosti, individualite a plnení úloh. Pracuje dobre keď si môže získať prestíž a autoritu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Výzva, súťaženie, získanie moci a prestíž. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Kreatívne myšlienky zmysluplne zužitkovať na dosiahnutie cieľa.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Vzbudzuje ich zvedavosť, sľubuje im zaujímavé úlohy, zhovára sa s inými aby odhalil ich želania. Dokáže iných dobre presvedčiť o materiálnych ako aj o ne-materiálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Vedie svoj tím ako dirigent a plní tým potrebu tímu po jednote, bez váhania udeľuje úlohy, zaprisaháva členov tímu na jednu spoločnú úlohu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Menej obľúbené úlohy prideľuje iným, nemá trpezlivosť voči pomalejším a dlhšie uvažujúcim kolegom. Často nedokáže delegovať úlohy a vnucuje iným svoje názory.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Sústreďuje sa na to. čo má pre neho a jeho okolie najväčší význam a prináša im najväčšie výhody. Má rád konkurenciu a mimoriadne úlohy. Rád vopred plánuje, zabezpečuje opatrenia. Detaily prenecháva na iných. Pracuje presne, keď má vopred stanovený termín.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Dúfa, že spoluprácou s ostatnými vyrieši konflikty. Pomáha vyriešiť situácie, ktoré vznikli na základe negatívneho a nesprávneho prístupu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Pokým je to možné, dovolí druhým aby mu pomohli. Sám podstupuje riziká a zmätie tým dokonca aj protivníkov.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Vyhľadáva si úlohu zástupcu vedúceho tímu. ktorý vedúceho podporuje. Súčasne ovplyvňuje jeho rozhodnutia, kolíše pri svojich rozhodnutiach medzi náklonnosťou k úlohe a k človeku.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-motivovať druhých aby konali\n"
                                                                                "-byť plný fantázie a pomôcť tak iným vidieť veci z iného hľadiska\n"
                                                                                "-rýchlo sa rozhodovať, napr. ihneď zlepšiť jestvujúci proces",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Dbať viac na dodržiavanie termínov; vyhýbať sa útokom na iných, keď sú títo pod nátlakom; dať za pravdu tým. ktorí majú pravdu po odbornej stránke; nemanipulovat' iných; spolupracovať s jednotlivcami, ktorí majú schopnosti sledovať okolie a vytvoriť predvídateľné prostredie (Modely I4. 34. 134). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel13(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po nezávislosti, odvahe a praktickosti. Pracuje dobre keď môže sledovať plnenie úlohy po koncepčnej stránke od jej začiatku až po ukončenie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Dobrodružstvo, výhra, vedomosti, psychická vyrovnanosť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Zvažovať, spoznať rozdiely a stanoviť zmysluplné aktivity.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= " Energicky argumentuje, aby si druhých získal pre svoj postup práce. Rýchlo reaguje na pripomienky, vie bez problémov odpovedať na otázky využívajúc pritom fakty a dokumentáciu. Je vážny a priamy. Dokáže iných relatívne dobre presvedčiť o materiálnych aj nemateriálnych veciach.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Cieľavedomý vedúci tímu. ktorý tímu jasne dáva najavo, že je potrebné tvrdo pracovať. Pri nezhodách okamžite rozhoduje.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Zanedbáva malé rituály, ktoré by druhých ukľudnili. Ak ho naháňajú termíny, je často nemilý a netaktný. Považuje za ťažké delegovať úlohy.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Vyvíja systematické plány vrátane opatrení pre prípad výskytu prekážok. Má úspech svojim rýchlym konaním a to aj bez toho. aby musel prísne kontrolovať. Je rozhodný a agresívny. Pomáha pri zlepšovaní kvality.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Konfrontáciou, provokatérom robí ťažkosti. Odmieta sa vzdať osobných cieľov. Znervózňuje tým druhých a vyvoláva tak nepokoj.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Tvrdohlavosťou, často si volí nesprávny čas na výmenu názorov.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Využíva osobné skúsenosti viac ako svoje vedomosti zo školy, preberá úlohy ktoré sú pre druhých ťažké. Pracuje najlepšie, keď nie je rušený a kontrolovaný prísnym a kritickým vedúcim.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-Usmerňovať druhých a sprevádzať ich pri plnení úloh\n"
                                                                                "-Preverovať a posudzovať, či sú výkony druhých v danej oblasti dostatočné\n"
                                                                                "-Podporovať postup pri práci. napr. povzbudzovaním k rozhodnutiam ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Jasnejšie konať: stanoviť časový limit na rozriešenie konfliktu a dosiahnutie zhody: byť otvorený iným názorom: podporovať nové nápady iných a vyjadriť im aj uznanie; byť ochotný zmeniť tempo alebo vyjsť iným v ústrety: spolupracovať s jednotlivcami, ktorí sú prispôsobivejší a taktnější (Modely 21. 23, 32). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel14(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po výkone, individualite a ústraní. Pracuje dobre keď má dostatok času na overenie správnosti svojich myšlienok a konania.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Intelektuálna a fyzická výzva, kreativita, uznanie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Vynájsť a implementovat' nové myšlienky.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Využíva moc faktov a je nadšený ak nápad alebo výrobok zodpovedá jeho vysokým nárokom. Uznanie dosahuje svojím dobre organizovaným a priamym postupom. Dokáže druhých nadmieru dobre presvedčiť o materiálnych veciach a taktiež dobre o nemateriálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Je inovatívnym vedúcim pracovníkom, pomáha tímu vyvíjať nové teórie. Je takmer vždy formálny, je vzorom pre iných, preberá priveľa zodpovednosti.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Sústreďuje sa len na jedinú úlohu, čím často trpia ostatné oblasti práce. Často si robí starosti, ktoré sú niekedy neopodstatnené. Je nadmieru opatrný a potrebuje pomoc aby dokázal ukončiť projekt.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Rieši radšej úlohy ako medziľudské problémy. Sústreďuje sa na komplexitu jednej otázky, pracuje dlho a udáva tempo práce, ktoré je pre druhých často veľmi namáhavé.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Spoluprácou, pričom tlačí druhých najprv do defenzívy a skrýva tým svoju vlastnú neistotu. Potom pomenuje všetky starosti a problémy, ktoré vidí.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Je dobre pripravený na všetky eventuality, sám sa zaväzuje ešte viac pracovať.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Uvažuje o jestvujúcich postupoch a metódach, rieši problémy a žiada o povo¬lenie nanovo preveriť a testovať výsledky. Rád preberá úlohy vo výskume a rád hľadá odborné informácie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-byť kreatívnym, napr. vyvinúť nový pracovný postup\n"
                                                                                "-systematizovať a zaviesť poriadok napr. poukladať náradie a nástroje do také¬ho poradia, v ktorom budú použité \n"
                                                                                "-diagnostikovať, napr. nájsť koreň problému",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Dopriať si uvoľnenie od napätia z pracovného úsilia: byť objektívny a starost¬livý: pri vyjadrovaní kritiky voči iným brať do úvahy ich pocity; prejaviť iným uznanie za vynaložené úsilie; spolupracovať s jednotlivcami, ktorí majú lepšie schopnosti v nadväzovaní sociálnych kontaktov a lepšie vedia zvládať napätie (Modely 12. 21.23). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel21(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po sebarealizácii, spolupatričnosti a mimoriadnych výkonoch. Pracuje dobre keď má možnosť byť v kontakte s rozmanitými ľuďmi.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Výzva, súťaženie, medziľudské kontakty, uznanie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Očakávať úspešné výsledky.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Vnáša čerstvý vietor do práce, vyzdvihuje do popredia šance, dokáže sa svojím prejavom prispôsobiť osobnosti poslucháča. Je priateľský a milý. Rád pracuje blízko ostatných a odstraňuje tak bariéry. Dokáže druhých veľmi dobre presvedčiť o materiálnych aj nemateriálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Je demokratickou vedúcou osobnosťou, ktorá spľňa predstavy tímu o zaujímavých zážitkoch. Správa sa férovo k druhým, stavia mosty medzi nepriateľmi.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Nemá rád stereotypné činnosti, vyhýba sa jednostrannej práci. Nedokáže ukončiť zle zvolené projekty. Nadmieru sa nadchýna.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Teší sa možnostiam prejaviť svoj talent. Dokáže nájsť správne slová na predstavenie svojich plánov, svojím emocionálnym prejavom budí emócie aj u iných. Svoje nadšenie dokáže podmurovať praktickými schopnosťami. Malé práce prenechá na iných, vie dobre povzbudzovať pri dosahovaní cieľov..",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Spoluprácou, na kritiku odpovedá vtipom a humorom. Je pripravený zohľadniť želania druhých.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Trpezlivosťou, menuje problémy a plánuje to čo je potrebné na ich odstránenie",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Rád sa venuje ťažkým úlohám. Dáva veci do pohybu, vyjadruje sa k ťažkým otázkam, ktorým sa iní vyhýbajú alebo sa ich obávajú. I lovorím aj v mene slabších členov tímu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-využívať svoje znalosti, napr. v presvedčovaní druhých \n"
                                                                                "-vytvoriť dobré vzťahy, napr. v komunikácii so zákazníkmi\n"
                                                                                "-viesť druhých, napr. pomôcť tímu odhaliť skryté možnosti ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Spomaliť tempo: vyhýbať sa vyčerpaniu: úprimne pochváliť druhých; dať iným čas vyjadriť ich pochybnosti, obavy a námietky: vyhýbať sa preceňovaniu: vedieť kedy je načase ukončiť presviedčanie iných; spolupracovať s jednotlivcami, ktorí majú schopnosti v organizovaní a systematickom plánovaní (Modely 13. 14. 34). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel23(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu v akceptovaní, lojalite a dôvere. Pracuje dobre ak je spolupráca s inými priateľská a informatívna.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Priateľstvo, nezávislosť, istota, plnenie povinností.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Podporovať iných a umožniť im tak. aby dokázali pomôcť sami sebe.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Hľadá spoločné záujmy, ktoré ho spájajú s priateľmi a kolegami. Rád sa pozerá priamo do očí, má príjemný výraz tváre a priateľské uvoľnené správanie. Tvorí osobné kontakty k druhým, vie druhých pomerne dobre presvedčiť o materiálnych veciach a veľmi dobre o nemateriálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Veľmi ľudský vedúci pracovník, ktorý podporuje svoj tím vyjadrením uznania a odmenami pre jednotlivých pracovníkov. Dáva len nepriame nariadenia.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Pokúša sa vyhnúť problematickým témam, pri jednáních sa rýchlo poddáva, padne mu ťažko protirečiť kolegom a priateľom, kritiku jeho práce považuje za kritiku jeho osoby.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Udržuje priateľstvá a rozširuje harmóniu. Dokáže určiť ciele a požiadavky, ktoré sú potrebné na splnenie danej úlohy. Úlohy si plní v spolupráci s inými, po dlhšej fáze spolupráce pracuje rád aj sám.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Uzatvára kompromisy, pričom ale nestráca z očí svoje ciele. Vyhýba sa pria¬mym útokom voči iným.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Núti sám seba sledovať detail až do konca a hľadá pritom podporu druhých.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Odstraňuje prekážky, je sprostredovateľom medzi kolegami, od samého začiatku práce sa stará o harmonickú spoluprácu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "- robiť kompromisy, napr. riešenie potrieb druhých\n"
                                                                                "-Viesť druhých, napr. tréningom a poradenstvom \n"
                                                                                "- využívať jestvujúce prostriedky",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Úlohy načas dotiahnuť do konca: sledovať pritom kľúčové detaily; byť priamy a rozhodný pri riešení medziľudských konfliktov: stať sa energickejším, spolupracovať s jednotlivcami, ktorí majú dobrú schopnosť rozvíjať znalosti na základe faktov (Modely 14. 34,41).  ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"



class BehaviorModel24(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po sebarealizácii, individualite a nezvyčajných výkonoch. Pracuje dobre keď má možnosť uplatnit svoj talent a schopnosti.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Súťaženie, kreativita, uznanie, moc a vedenie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Plánovať nepredvídané udalosti.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Predstavuje užitočnosť daného výrobku alebo nápadu, svojimi inšpirujúcimi slovami dodáva odvahu aj iným. Dokáže načrtnúť cesty, ktoré vedú k úspechu. Voči iným prejavuje otvorenosť, záujem a dôveru. Dokáže druhých veľmi dobre predvedčiť o materiálnych ako aj o nemateriálnych veciach ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Je mnohostranným vedúcim pracovníkom, ktorý podporuje svoj tím pri kreatívnych ako aj technických ťažkostiach. Pri výbere dôležitých zamestnancov rozhoduje rozumne.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Niekedy stavia na mocenské hry, pričom odmieta popustiť. Zanedbáva rutinné činnosti. Využíva taktiku vyčkávania keď nemá dosť informácií. Niekedy má ostrý jazyk.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Využíva svoju schopnosť sledovať okolie, posudzovať a plánovať. Aj keď už má i	chuť dačo začať, najskôr si pozorne vypočuje čo si o tom myslia druhí. Delí sa ochválu aj kritiku s inými.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Spoluprácou, pri ktorej dokáže predvídať kroky protivníka. Zostáva kľudný, stačia mu jestvujúce prostriedky na dosiahnutie cieľa.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Stane sa konkurentom, využíva svoju duševnú flexibilitu a šikovnosť, zavádza nové metódy a zvyšuje tak efektivitu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Snaží sa priblížiť k centru moci. Radí vedúcemu a členom tímu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "- Konštrukcia a vývoj. napr. vytvorenie pracovných postupov\n"
                                                                                "-Diagnóza problémov a hľadanie koreňa problému\n"
                                                                                "-Predaj, reklama, jednania, presviedčanie a ovplyvňovanie iných o výrobku alebo projekte",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Dodržať sľuby; plniť záväzky: prejaviť ohľaduplnosť pri jednaní s inými: vyhýbať sa odďaľujúcim taktikám; akceptovať realistické kontroly: prívetivo akceptovať aj nepriaznivé úsudky; spolupracovať s jednotlivcami, ktorí venujú viac pozornosti špecifickým detailom (Modely 3. 13. 234). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel31(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po naplnení, vysokej odbornosti a úspe-choch na vysokej úrovni. Pracuje dobre keď je obklopený kolegami, ktorí ho rešpektujú a s ktorými ho spájajú spoločné ciele.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Uznanie, objasnenie nejasností, plnenie povinností, kontrola.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Dožadovať sa výsledkov, ktoré je možné vyhodnotiť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Namiesto citov používa rozum. Vytiahne na svetlo niekoľko faktov, ktorými nie je možné otriasť a od tých. ktorí s ním nesúhlasia žiada aby uviedli pádne dôvody svojho nesúhlasu. Dokáže druhých pomerne dobre presvedčiť o materiálnych ako aj nemateriálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Je pragmatickou vedúcou osobnosťou, pomáha tímu pracovať ako skupina a nie jednotlivo. Pri sociálne zameraných úlohách potrebuje pomoc.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Len ťažko dokáže dôverovať emocionálne založeným ľuďom.Má vždy odstup voči iným a niekedy robí neistý dojem. Odmieta sa učiť nové pokým za to nie je patrične odmenený.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Plánuje a vykonáva úlohy, komunikuje priamo a jasne, problém rieši nezávisle. Má sklony k jednoduchým riešeniam. Vyslovuje chválu za dobrú prácu a karhá za slabé výkony.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Spoluprácou. Dokáže rozoznať dobrý úmysel, aj keď tento nebol uskutočnený. Pri riešení úloh prijme pomoc od dnihých.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Ešte viac sa ovláda. Stará sa osobne aj o najmenšie detaily.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Preveruje správnosť názorov druhých, pôsobí uzmierujúco a stará sa o to. aby bol všetkým jasný cieľ a účel danej úlohy.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-sústredenie sa na určité úlohy. napr. stanovenie priorít. \n"
                                                                                "-výskum, zhromažďovanie informácií, napr. nájsť najlepšieho dodávateľa tovaru.\n"
                                                                                "-opravovať alebo zostaviť. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= " Prejaviť flexibilitu a ochotu premyslieť si stratégie; obrazne vyjadriť svoje myšlienky; vyhýbať sa hlbokým a nesprávne orientovaným negatívnym pocitom; spolupracovať s jednotlivcami, ktorí majú schopnosti dobrej a taktnej komunikácie s inými (Modely 2I. 123. I24).",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel32(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po spolupatričnosti, lojalite a sebaobetovaní. Pracuje dobre keď dostane jasne definované úlohy.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Priateľstvo, plnenie povinností, stabilita a uznanie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Zabezpečiť rovnosť príležitostí a spravodlivosť pre každého.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Získa si ich dôveru jasnou komunikáciou a zdravým rozumom dosiahne príjemnú atmosféru. Chváli rozumný prístup u iných, vyhýba sa agresívnym metódam. Dokáže druhých veľmi dobre presvedčiť o materiálnych veciach a pomerne dobre o nemateriálnych veciach.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Je vedúcim, ktorý tímu poskytuje oporu. Stojí pri svojich ľuďoch pri technických projektoch a dáva pokyny, ak bol vyzvaný radiť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Vyhýba sa dôležitým konfrontáciám. Pracuje až do vyčerpania pre druhých. Má sklony podriadiť sa silným osobnostiam. Pod nátlakom sa stane nerozhodným a vyhýbavým.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Používa overené postupy. Prejavuje záujem o technické projekty, pri ktorých má dočinenia s ľuďmi. Svoje výsledky dosiahne trpezlivosťou a prispôsobivosťou voči ľuďom s rozdielnymi vlastnosťami a rozdielnym spôsobom práce.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Vychádza druhým v ústrety. Na nepríjemné otázky odpovedá dôkladne. Pokúša sa ukľudniť emócie u druhých a zachovať dobré vzťahy.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Prevezme viac zodpovednosti. Obracia sa na vyššie postavených alebo na odborníkov. aby overili správnosť jeho rozhodnutia.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Prevezme aj tie úlohy, ktoré by iní odmietli. Ak je to potrebné, prejavuje nezávislosť. Dokáže prekvapiť svojou otvorenosťou a úprimnosťou.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "- ponúknuť pomoc. napr. pri odbúravaní stresu u druhých\n"
                                                                                "-starať sa o určité úlohy. napr. o dôkladné vedenie účtovníctva \n"
                                                                                "- prejaviť chválu a uznanie, napr. za prínos jednotlivca k riešeniu úlohy",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Mať odvahu pustiť sa do niečoho nového; zaviesť flexibilitu do pracovnej rutiny; vyskúšať nové a odlišné pracovné úlohy; požiadať iných o podponi pri detailoch; stať sa neústupnějším a okamžite, dôsledne jednať; spolupracovať s jednotlivcami, ktorí radi podstupujú riziko a majú kreatívne nápady (Modely I. 12, 13).  ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel34(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text="Príležitosťami uspokojiť vlastnú potrebu po spolupatričnosti, naplnení a predvídateľnoxti. Pracuje dobre keď má detailný popis práce.",
                                 size_hint=[0.8, None], auto_dismiss=True, )

        self.m_dialog.open()

    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text="Uznanie, vedomosti, istota, stabilita.",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.oc_dialog.open()

    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text="Stanoviť a dodržiavať premyslené a stále tempo.",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.zz_dialog.open()

    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text="Svojou stálosťou a spoľahlivosťou. Vyzdvihuje dosiahnuté úspechy, vysoko oceňuje užitočnosť a plnenie povinností. Používa dobre strukturované prezentácie, často pri prejavoch používa svoj manuskript.Dokáže druhých dobre presvedčiť o materiálnych veciach, o nemateriálnych veciach pomerne dobre. ",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.apd_dialog.open()

    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text="Je analytickou vedúcou osobnosťou, ktorá podporuje svoj tím pri hľadaní faktov a posudkov. Je bezhranične lojálny voči svojim ľuďom.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.avt_dialog.open()

    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text="Niekedy býva pesimistický. Má sklony priskoro posudzovať iných podľa ich správania a vystupovania. Niekedy je nepríjemný k ľuďom, ktorí nezdieľajú jeho názor",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.mss_dialog.open()

    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text="Má technické vedomosti. Vypracuje si svoj pevný pracovný postup a pri práci udržiava stále tempo. Bez. sťažovania sa prevezme aj nepríjemné úlohy. Má sklony až priveľmi sa spoliehať na overených ľuďí. výrobky alebo nápady.",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.ru_dialog.open()

    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text="Uzatvára premyslené kompromisy. Pritom využíva svoje skúsenosti a nájde riešenie. ktoré je prijateľné pre všetkých.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.ark_dialog.open()

    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text="Spolieha sa na vlastný úsudok. Uzatvorí sa do seba a svoje plány tají až do správnej chvíle.",
                                    size_hint=[0.8, None], auto_dismiss=True, )

        self.arpn_dialog.open()

    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text="Podieľa sa na spoločných úlohách, využíva svoj zdravý úsudok, praktické skúsenosti a cenovo výhodné metódy. Má záujem o dobrý konečný výsledok.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.act_dialog.open()

    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text="-premyslieť problém, napr. zvážiť dôsledky rozličných rozhodnutí  \n"
                                                                              "-plány a pokyny cieľavedome dodržať, napr. dodržať termíny \n"
                                                                              "-obsluhovať prístroje a nástroje ",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.nu_dialog.open()

    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text="Vyjadrovať svoje obavy otvorene a priamo; vyrovnať sa s kritikou bez přecitlivělosti; prejaviť väčšiu vnímavosť k zmenám; otvorenejšie čeliť prekážkam; nevyhýbať sa diskusiám; vyhýbať sa tajnostkárstvu pri plánovaní: spolupracovať s jednotlivcami, ktorí lepšie vedia vyjadriť svoju mienku (Modely 12,21,32).  ",
                                 size_hint=[0.8, None], auto_dismiss=True, )

        self.s_dialog.open()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel41(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text="Príležitosťami uspokojiť vlastnú potrebu po významných výkonoch, práci osamote v ústraní a disciplíne. Pracuje dobre keď má možnosť preveriť užitočnosť svojho nápadu.",
                                 size_hint=[0.8, None], auto_dismiss=True, )

        self.m_dialog.open()

    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text="Kreativita, precízna práca, uznanie, stabilita",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.oc_dialog.open()

    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text="Vyvíjanie praktických nápadov a metód.",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.zz_dialog.open()

    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text="Znižuje pocit neistoty a plní svoje sľuby. Druhých dokáže presvedčiť predložením jasných podkladov. Na ich poznámky reaguje kľudne. Druhých dokáže relatívne dobre presvedčiť o materiálnych aj nemateriálnych veciach. ",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.apd_dialog.open()

    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text="Vynaliezavý vedúci tímu. Pomáha tímu vidieť veci v inom svetle. Povzbudzuje a dodáva odvahu vyskúšať nové možnosti.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.avt_dialog.open()

    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text="Je nadmieru vážny a zdržanlivý. Potrebuje priveľa času na dôležité rozhodnutia. Navonok poskytuje viac informácií ako by bolo potrebné.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.mss_dialog.open()

    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text="Získavanie aktuálnych informácií považuje za veľmi dôležité. Každý nápad preveruje aby zistil, či je užitočný. Opakovane preveruje svoje pôvodné názor)', dôkladné plánovanie mu dáva nádej na dobrý výsledok. Len zriedka sa stane, že zle zaháji svoju prácu. Nezvykne brzdiť chod vecí a nemíňa svoju energiu na zbytočnosti.",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.ru_dialog.open()

    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text="Pomocou spolupráce. Dokáže problém rozložiť na kúsky a analyzovať ho. Nespráva sa pritom impulzívne a dokáže sa vzdať svojho názoru v prospech druhého.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.ark_dialog.open()

    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text="Starostlivo sa pripravuje na úlohy. Vyvíja také riešenia, ktoré zabránia vzniku ďalších ťažkostí.",
                                    size_hint=[0.8, None], auto_dismiss=True, )

        self.arpn_dialog.open()

    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text="Skúša všetky možné cesty aby našiel najlepšie riešenia, zlepšuje kvalitu aj keď tým môže ublížiť druhým. Dodáva iným odvahu, aby ho hodnotili.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.act_dialog.open()

    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text="-používať to. čo iní vyvinuli a stavať na tom \n"
                                                                              "-konštruovať, napr. modely alebo konečný výrobok\n"
                                                                              "-vynájsť napr. pojmy, procesy, výrobky, nápady ",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.nu_dialog.open()

    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text="Prejaviť vlastné emócie; hlavne optimizmus; usmievať sa; naučiť sa vyrovnať s možným odmietnutím; získať si aspoň jednu dôveryhodnú osobu ako svojho hovorcu; dodávať iným odvahu vysloviť aj pochybnosti a očakávať reakciu; mať otvorenú myseľ; dať ľuďom druhú šancu; je lepšie rozdielne nározy prediskutovať ako sa utiahnuť do ústrania; spolupracovať s jednotlivcami, ktorí pôsobia závažnejšie. (Modely 3. 23. 234).  ",
                                 size_hint=[0.8, None], auto_dismiss=True, )

        self.s_dialog.open()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel42(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text="Príležitosťami uspokojiť potrebu po mimoriadnych výsledkoch, korektnosti a nových poznatkoch. Pracuje dobre keď má možnosť tvoriť niečo hodnotné a kvalitné.",
                                 size_hint=[0.8, None], auto_dismiss=True, )

        self.m_dialog.open()

    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text="Súťaženie sa. odhaľovanie nového, dosiahnutie uznania, etický a morálny kódex.",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.oc_dialog.open()

    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text="Preskúšať a testovať použiteľnosť nápadov.",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.zz_dialog.open()

    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text="Priamočiarou komunikáciou. Fakty dokáže veľmi dobre vysvetliť a vtipne podať. Je pripravený diskutovať o komentároch, ktoré boli vyjadrené a rád poradí iným. Dokáže druhých veľmi dobre presvedčiť o materiálnych a celkom dobre o nemateriálnych veciach. ",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.apd_dialog.open()

    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text="Starostlivý vedúci pracovník, ktorý je oporou svojho tímu. Trvá na tom. aby boli predpisy a pravidlá vždy dodržiavané.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.avt_dialog.open()

    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text="Niekedy je prehnane kritický. V pokročilých fázach projektu prejavuje netrpezlivosť, strach a obavy keď je potrebne uskutočniť rozhodnutie.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.mss_dialog.open()

    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text="Zvažuje dôležitosť jednotlivých úloh. rozhoduje o tom že čo je najdôležitejšie a kladie vysoké ciele. Nadväzuje správne kontakty, je realistický, svoj zájujem o prácu obohacuje svojou mnohostrannosťou a dokáže žonglovať s viacerými projektmi súčasne.",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.ru_dialog.open()

    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text="Je pripravený na kompromisy, povzbudzuje ostatných aby boli konštrukívni a vždy sa správa korektne. Pokúša sa vždy nájsť spoločného menovateľa..",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.ark_dialog.open()

    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text="Stane sa konkurentom, ochraňuje vlastné záujmy, je zaťatý a nepríjemný.",
                                    size_hint=[0.8, None], auto_dismiss=True, )

        self.arpn_dialog.open()

    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text="Dobrovoľne sa hlási na výkon takých úloh. ktoré sú spojené s nárokom na dokonalosť myšlienky alebo produktu. Iní ho obdivujú pretože aj počas stresových situácií zachováva kľud a dodržuje svoje sľuby..",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.act_dialog.open()

    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text="-riešenie problémov, napr. odstránenie prekážok, ktoré obmedzujú produktivitu  \n"
                                                                              "-porovnávanie, zisťovanie rozdielov a podobností, napr. v ponukách a v opisoch výrobkov\n"
                                                                              ,
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.nu_dialog.open()

    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text="Byť menej tvrdý pri oceňovaní iných; akceptovať ľudí takých akí sú; umožniť im robiť svoje vlastné rozhodnutia: načúvať aj múdrosti iných; dotiahnuť detaily, ktoré sú súčasťou úlohy dôsledne do konca; stanoviť realistické termíny dokončenia; naučiť sa lepšej rozhodnosti čo sa týka malých aspektov úloh : ľahko sa vyrovnať s námietkami; vyhýbať sa obviňovaniam: spolupracovať s jednotlivcami, ktorí sú trpezlivejší a dôkladnejší (Modely 3.4. 43).  ",
                                 size_hint=[0.8, None], auto_dismiss=True, )

        self.s_dialog.open()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel43(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text="Príležitosťami uspokojiť vlastnú potrebu po využiží odborných znalostí, poznatkoch a usporiadanosti. Pracuje dobre keď je pracovné prostredie jasne definované a priateľské.",
                                 size_hint=[0.8, None], auto_dismiss=True, )

        self.m_dialog.open()

    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text="Vedomosti, precíznosť, stálosť a uznanie.",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.oc_dialog.open()

    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text="Zvládať úlohy pomocou praktických zručností.",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.zz_dialog.open()

    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text="Svojím priateľským a zodpovedným prístupom. Menuje všetky pre a proti daného nápadu alebo produktu. Voči slabo informovaným protivníkom vie zvoliť len správny tón. Dokáže druhých pomerne dobre presvedčiť o materiálnych ako aj nemateriálnych veciach. ",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.apd_dialog.open()

    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text="Tradičný vedúci pracovník, ktorý sa snaží dosiahnuť v tíme pocit spolupatričnosti.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.avt_dialog.open()

    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text="Niekedy je nadmieru opatrný. Má väčší záujem o údaje a čísla ako o ľudí. Spolieha sa na zabehané postupy alebo na svojho nadriadeného.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.mss_dialog.open()

    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text="Rozvíja overené kontakty a zdroje, posudzuje či sú použité pracovné postupy dostatočné. Chce zvýšiť kvalitu, dbá na vysoký štandard a trvá na trestoch pre tých. ktorí prinášajú slabé výsledky.",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.ru_dialog.open()

    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text="Nerieši ich. Rozmýšľa o nich len sám a dovolí tým. aby sa rozšírili negatívne pocity u ľudí a aby sa o problémoch navonok nehovorilo.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.ark_dialog.open()

    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text="Vedenie prenechá na iných. On pracuje naďalej ako zvyčajne.",
                                    size_hint=[0.8, None], auto_dismiss=True, )

        self.arpn_dialog.open()

    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text="Vykoná pridelené úlohy, ak má pochybnosti o správnosti postupu, prejedná to s odborníkmi. Uprednostňuje stálosť pred nekontrolovaným postupom.",
                                   size_hint=[0.8, None], auto_dismiss=True, )

        self.act_dialog.open()

    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text="-darovať iným pozornosť, napr. doslovné vysvetlenie danej úlohy  \n"
                                                                              "-počítať a kalkulovať, napr. vytvoriť rozpočet na jedno obdobie\n"
                                                                              "-dokumentovať a dokladovat', napr. dôkazy pre nejakú prácu ",
                                  size_hint=[0.8, None], auto_dismiss=True, )

        self.nu_dialog.open()

    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text="Preukázať srdečnosť a pochopenie pre iných; pozície a úlohy jasne a zreteľne slovne komunikovať: vyvinúť toleranciu pre konflikty: využívať taktnú a diplomatickú komunikáciu aj v prípade útoku: klásť iným otázky a tým ich povzbudiť k účasti na riešení; spolupracovať s jednotlivcami, ktorí lepšie dokážu zjednocovať ľudí (Modely 2.42. 234).  ",
                                 size_hint=[0.8, None], auto_dismiss=True, )

        self.s_dialog.open()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel123(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po výkone, sebarealizácii a spolupatričnosti. Pracuje dobre keď musí plávať proti prúdu a keď má možnosť získať výhody.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Ľudia, ich vedenie, mnohostrannosť, znalosti, konkurencia.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Excelovať v rozvoji nových možností.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Pri konfrontáciách je v prevahe. Dokáže byť v pravej chvíli veselý, šarmantný alebo zadumaný. Rýchlo odpovedá na otázky. Dokáže drahých veľmi dobre presvedčiť o materiálnych ako aj o nemateriálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Spolucítiaci vedúci pracovník. Snaží sa zužitkovať a pozdvihnúť talenty všetkých jednotlivcov v lime. Tým sa znižuje celková nespokojnosť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Ak predpokladá nerovnosť názorov, rozhoduje len váhavo. Pri nových projektoch má sklony k prehnanej sebakritike. Nápady nenasleduje s vždy rovnakým nasadením.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Pri práci a technických znalostiach chce vynikať. Starostlivo formuluje pláno¬vané program a postupy, umožňuje nezvyčajne vysoké tempo práce a dokáže dodržať realistické termíny.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Rieši ich spoluprácou. Zhovára sa s kolegami o iných riešeniach a pokiaľ majú dobré úmysly, zisťuje ich motívy. Napriek rozdielnym názorom sa pokúša nájsť zhodu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Je naďalej presvedčený o svojom, zaťatý a tvrdohlavý.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Dodržuje realistické termíny odovzdávky a pracuje veľmi samostatne. Hľadá si úlohy, ktoré vyžadujú široký rozhľad a vedomosti o celom procese alebo projekte.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "- rýchlo zhodnotiť ľudí alebo situácie a vytvoriť si tak celkový obraz \n"
                                                                                "-viesť drahých, napr. pri predstavení novej myšlienky\n"
                                                                                "-udeľovať pochvaly a uznania ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Iniciovať diskusiu na rozriešenie nejasných situácií; naučiť sa akceptovať tých. ktorí sú viac tradicionalisti a konvenčné typy v praxi: reagovať bez. predsudkov na otázky týkajúce sa výkonov iných; učiť sa ako lepšie ohodnotiť úsilie iných: spolupracovať s jednotlivcami, ktorí lepšie dokážu preveriť otázky týkajúce sa presnosti (Modely 14, 31.41).  ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class BehaviorModel124(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po prejavení schopností, individualizme a spolupatričnosti. Pracuje dobre keď má možnosť vypracovať a použiť rôzne prostriedky k dosiahnutiu cieľa.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Výzva, kreativita, rozhodovanie, mnohostrannosť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Dosiahnuť priame výsledky.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Zhromaždené informácie využíva priamo a efektívne. Pripravuje lak poslucháčov na logické a užitočné rozhodnutie. Na oživenie svojho prejavu používa humor a vtipné anekdoty. Dokáže druhých veľmi dobre presvedčiť o materiálnych ako aj o nemateriálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Sprostredkujúci vedúci pracovník. Pomáha v time nájsť pochopenie pre odôvod¬nené rozdiely v názoroch a pokúša sa to posúdiť z rozličných uhlov pohľadu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Neznáša banálne povinnosti a stereotypné činnosti. Ak si druhí nevykonajú svoje drobné práce dostatočne, nedokáže dodržať termíny. Vydáva dlhé vyhlásenia, ktoré drahí často považujú za arogantné a bezcitné.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Úlohy preberá bez predsudkov a snaží sa nájsť lepšie metódy. Je pripravený nahradiť staré a zlé metódy a začať odznova. Hľadá si nové úlohy, skúsenosti prinášajú úspechy.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Kompromismi. Vychádza iným v ústrety, dokáže sa vzdať časti svojich osobných cieľov pre celkový výsledok a nabáda k tomu aj ostatných..",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Je uvoľnený a sebavedomý. Pri malých úlohách žiada o pomoc drahých.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Učí sa novému, v tíme preberá rozličné úlohy a pomáha oživiť zastaralé veci. Najvhodnejšie úlohy/funkcie",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-prejavť svoju kreativitu pri navrhovaní nových symbolov alebo obrázkov. napr. nové slogany, logá. nadpisy článkov a pod \n"
                                                                                "-svoje vedomosti uplatniť na ľuďoch, napr. vytvoriť motivujúce prostredie\n"
                                                                                "-vymyslieť nové veci. napr. názvy, tvary, produkty a pod ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Byť spravodlivý pri jednaní aj s tými. ktorí zanedbávajú svoju zodpovednosť; lepšie hospodáriť s časom na zabezpečenie dôkladného zvládania aj menších úloh; rešpektovať skúsených špecialistov; zjednotiť odlišných ľudí: spolupracovať s jednotlivcami, ktorí dokážu úlohy dôsledne dotiahnuť do konca (Modely 31.34,41).  ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel134(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po individualite, naplnenia poznatkoch. Pracuje dobre keď je odmenený za svoje nezvyčajné úsilia.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Výzva, etický a morálny kódex, kreativita, precízna práca.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Kombinovať analýzu s intuíciou.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Využíva odborné znalosti. Ukáže jasné ciele, predpokladá otázky a odpovie na ne ešte skôr ako mu boli položené. Dokáže vyvrátiť pripomienky. Dokáže druhých veľmi dobre presvedčiť o materiálnych veciach ale vie len slabo presvedčiť o nemateriálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Skutočnosťami riadený vedúci pracovník. Svojmu tímu dodáva slušné informácie a racionálne podnety k práci.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Má slony považovať svoj čas za hodnotnejší ako čas druhých. Ak iní nespľňajú požiadavky, mlčí.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Hľadá si úlohy, ktoré ho nadchnú, napr. nájde nový spôsob a koncept ako môže spolupráca firiem lepšie fungovať. Teórie uplatňuje v praxi, nikdy nezovšcobecňuje a myslí len špecificky. Pri nových projektoch rýchlo napreduje.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Konfrontáciou. Pokúša sa zvíťaziť nad protivníkom nielen aby dominoval ale hlavne preto, aby ukázal váhu svojich argumentov.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Najskôr prešetruje a premýšla. než dačo vykoná. Je schopný riešiť komplexné problémy.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Chce vedieť ako veci fungujú a súvisia. Hľadá to podstatné pod povrchom, objasňuje a usporiadava údaje.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-analyzovať, klasifikovať \n"
                                                                                "-testovať, objasňovať, napr. pri zisťovaní najlepšej metódy\n"
                                                                                "-preskúšať, použiť, testovať a školiť o tom druhých ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Komunikovať taktne: byť trpezlivejší s rutinnými detailami. keď je projekt už rozbehnutý; počúvať: zvážiť myšlienky a skúsenosti iných; zohľadniť aj nápady a skúsenosti iných a oceniť ich úsilia: vedieť zaobchádzať s vlastným pocitom nadradenosti: spolupracovať s jednotlivcami, ktorí majú lepšie komunikačné schopnosti a ktorí vyvíjajú priamočiarejšie metódy (Modely I3. 24, 42).  ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel234(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po naplnení, spolupatričnosti a dôvere. Pracuje dobre keď sa a s ním zaobchádza s úprimnosťou a sympatiou.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Vedomosti, stálosť, uznanie, plnenie povinností.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Vytvoriť atmosféru spolupráce.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Zavádza atmosféru pohody. Rozvíja trvalé dobré vzťahy s ostatnými, zisťuje aké záujmy majú jeho poslucháči a pripravuje si tak materiály na konverzáciu s nimi. Vie bezprostredne lichotiť, dokáže druhých pomerne dobre presvedčiť o materiálnych aj nemateriálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Pracovitý vedúci pracovník, ktorý je svojou cieľavedomosťou a kvalitnou prácou vzorom celému tímu. Rád sa učí novému.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Nerád odpontje silným osobnostiam. Len váhavo dokáže delegovať dôležité úlohy. Má sklony ochraňovať svojich dobrých priateľov.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Preberá rád tie činnosti, ktoré iných zaťažujú. Teší sa ak bol vybratý na základe svojich znalostí a schopností. Používa systematické postupy pre dosiahnutie systematickej práce a svoje úlohy si plní načas.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Je pripravený na kompromisy. Dodáva druhým odvahu vyjadriť sa pozitívne a negatívne, pracuje na budovaní dôvery, navrhuje strednú cestu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Robí si nadmerné starosti ohľadne budúcnosti, je otvorený iným možnostiam.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Vytvára pre seba a pre iných pohodlný ale produktívny štýl práce. Opatrným prístupom zabraňuje vzniku chýb a škôd.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-organizovať, napr. plánovať úlohy \n"
                                                                                "-spoznať potreby iných, napr. pri nákupe kancelárskych potrieb \n"
                                                                                "-učiť, školiť a trénovať male skupiny ľudí ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Postaviť sa ZOČÍ voči oponentovi keď je to nevyhnut né: uznať spoľahnutie sa na iných, ktorí poskytujú technické a špecifické detaily: vyhľadávať kontakty aj mimo okruhu svojich priateľov; podeliť sa s negatívnymi pocitmi; spolupracovať s jednotlivcami, ktorí dokážu otvorenejšie vyjadrovať nespokojnosť (Modely l. I2. I24).  ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"



KV = '''

<BehaviorModel1>:
    name: "1"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 1"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: BOJOVNÍK"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Využíva príležitosti: vychutnáva si zložité situácie, stanoví si priority, dáva nariadenia: robí ľudí zodpovedných za ich konania, meria výsledky,odmeny a tresty: odmieta pomalú a opatrnú cestu spolupráce, uprednostňuje súťaživé úlohy a výzvy,reaguje rýchlo a rozhodne "
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel2>:
    name: "2"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 2"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: ZABÁVAČ"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Súperí o pozornosť; chce byť stredobodom pozornosti; delí sa s inými o rady, materiály a úspech; nadväzuje okamžité kontakty s ľuďmi prostredníctvom emocionality a schopnosti presviedčať; povzbudzuje iných, aby vyjadrili svoj názor; nepoučuje iných ; vyhýba sa prístupu ,,oko za oko,,; spolieha sa na podporu iných"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel3>:
    name: "3"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 3"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: STABILIZÁTOR"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Určí si stále tempo a drží sa ho; prejavuje trpez¬livosť; dodržiava záväzky; očakáva a prejavuje lojalitu; venuje pozornosť dôležitým detailom; určuje a bráni si vlastné presvedčenia a hodnoty; dokáže sa nadchnúť pre prírodu a krásne okolie "
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel4>:
    name: "4"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 4"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: PERFEKCIONISTA"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Má sklon súperiť radšej s vecami, než s ľuďmi; snaží sa robiť radosť iným a vychádzať im v ústrety; usiluje sa radšej nadchnúť niekoho pre spoluprácu než ho k tomu nútiť, robí kompromisy keď je to nevyhnutné; dokáže sa podriadiť uznávanej autorite; verí, že tvrdá práca a spravodlivosť sa vyplácajú a vyhľadáva zodpovednosti, ktoré si vyžadujú samostatnú prácu a koncentráciu"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel12>:
    name: "12"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 12"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: VÍŤAZNÝ BEŽEC"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Radšej sa oddelí od skupiny, než by bol jedným z mnohých; dosahuje úspech ako pohonný motor so silným vplyvom; nabáda iných k práci; pracuje voľne a nezávisle; udáva rýchle tempo; dokáže pracovať aj bez pokynov"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel13>:
    name: "13"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 13"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: PRIEKOPNÍK"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Premieňa frustráciu na prostriedok k vyriešeniu problémov; vyvíja jedinečnú kombináciu rozhodnosti a podrobnej, dôslednej práce; dokáže veľmi presvedčivo prezentovať svoju mienku; dokáže si vynútiť konania; odhodlane sa bráni proti opozícii a rýchlo odhalí slabé argumenty"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel14>:
    name: "14"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 14"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: VYNÁLEZCA"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Vyberá si praktický prístup; kladie otázky namiesto aby si vynucoval analýzy; nachádza odpovede, ktoré vychádzajú z logického myslenia a skúsenosti; vykonáva rozsiahlu prípravu na úlohy; je iniciátorom a pracuje na vývoji; udržuje si odstup od všetkých okrem najbližších dôverných spolupracovníkov; je spokojný ak môže sám pracovať na projekte; nedovolí iným aby ho obmedzovali"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}

<BehaviorModel21>:
    name: "21"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 21"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: PRESVEDČOVATEĽ"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Využíva motiváciu iných; upútava pozornosť iných prostredníctvom svojich pozitívnych názorov a vhodne vyberanými slovami; má často podporu iných; snaží sa zopakovať dosiahnuté úspechy; stáva sa podráždeným, keď sa práca stáva rutinou; chce dobre vyzerať a cítiť sa dobre; nemá rád neprehľadné situácie "
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}

<BehaviorModel23>:
    name: "23"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 23"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: SÚLADCA "
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Nadväzuje kontakty s ľuďmi, aby vyvinul jedinečné a priateľské prostredie: buduje mosty medzi jednotlivcami a pracovnými tímami: prebúdza sympatie v iných; občas je až príliš chápavý a nečiní ľudí zodpovedných za svoje chyby v konaní; delí sa ostatnými a tým ich zapája do práce a hľadania riešení"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel24>:
    name: "24"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 24"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: STRATÉG"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Napĺňa potreby iných; predvída a pripraví sa na ťažkosti; je vynaliezavý; improvizuje a posúva veci vpred; poskytuje presvedčivé dôvody pre zmeny v smere; kriticky hodnotí udalosti a ľudí; je otvorený novým a neobvyklým nápadom "
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel31>:
    name: "31"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 31"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: ŠPECIALISTA"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Kritický poslucháč; skúma slabé stránky druhej strany; je horlivý, dôkladný a všímavý; kombinuje fakty s cieľom vývoja nových metód; vyslúži si rešpekt skôr činmi, než slovami; rád zbiera poznatky a vyvíja si špecializáciu v niektorom odbore"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}

<BehaviorModel32>:
    name: "32"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 32"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: PODPORCA"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Nastolí atmosféru dobrej vôle; pozorne si vypočuje iných; dodáva ľuďom to. čo naozaj potrebujú a to aj za tú cenu, že to preňho znamená dodatočné úsilie; zostáva otvorený novým nápadom a postupom; berie vážne názory iných; dokáže organizovať; kontroluje dôležité detaily; je úprimný, priateľský a prejavujúci ocenenie "
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}

<BehaviorModel34>:
    name: "34"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 34"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: STRÁŽCA"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Všeobecný opis správania Vyslúži si rešpekt; dosahuje úspech vďaka húževnatosti; zhromažďuje údaje na to aby si vytvoril úsudok; vyhľadáva istotu a chce sa presvedčiť o správnosti nápadov; často veci spochybňuje, vypytuje sa, robí kompromisy a dosahuje zhodu; rád sa delí so zodpovednosťou s inými a prenecháva iným aj konečné rozhodnu tia; skôr než niečo sľúbi si to naplánuje"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel41>:
    name: "41"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 41"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: EXPERIMENTÁTOR"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Zvažuje všetky stránky problému; má ťažkosti učiniť správne rozhodnutie; robí rozhodnutia založené na opakovanom testovaní a praxi; objasňuje problémy a zjednodušuje procesy; volí si uvážené pracovné tempo, má dôkladné vyjadrovanie a podáva podrobné vysvetlenia; je starostlivý a nápomocný ale emócie prejavuje len veľmi dôverným priateľom "
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
            
<BehaviorModel42>:
    name: "42"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 42"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: ZNALEC"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Je priateľský, taktný a príjemný, využívajúci akceptovateľné a predvídateľné správanie; má tendencie hovoriť v ,,mal by som,, a ,,nemal by som,, , viac o sebe samom než voči iným; rozvíja analytické a systematické prístupy: očakáva odmeny ako zvýšenie platu a iné výhody za svoju dobrú prácu; dokáže predpovedať výsledok reťazca udalostí"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}

<BehaviorModel43>:
    name: "43"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 43"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: KRITICKÝ MYSLITEĽ"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Verí, že dokáže predchádzať problémom; využíva obranné stratégie na vyhnutie sa ťažkostiam: vypočuje si všetky aspekty problému; je racionálny a rozumný: má silný zmysel pre rozlišovanie toho čo je správne a nesprávne; snaží sa posunúť ľudí ku kompromisom; hovorí premyslene; venuje pozornosť detailom; potom, čo má poruke fakty, vezme na seba kalkulovatcľné riziká"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}

<BehaviorModel123>:
    name: "123"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 123"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: SPRÁVCA"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Komunikuje dobre so širokou škálou ľudí; prejavuje ochotu počúvať, pýtať sa. vyjednávať a robiť kompromisy: je stimulovaný novými nápadmi. odvahou a priateľskou rivalitou; je samostatný; využíva emócie aj fakty na podporu vlastných presvedčení"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel124>:
    name: "124"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 124"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: SPROSTREDKOVAŤEĽ"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Obráti prehrané situácie vo víťazné; je fascinovaný novými technikami a metódami; testuje a vyberá si najlepšie nápady, implementuje ich do súčasného systému na zdokonalenie kvality výsledkov; je plný tvorivosti, vynaliezavý a svedomitý; poskytuje praktické a merateľné metódy na zhodnotenie pracovného úsilia,"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}

<BehaviorModel134>:
    name: "134"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 134"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: DIZAJNÉR"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Vnáša vieryhodnosf do neusporiadaných situácií: dosahuje úspechy pri riešení komplexných problémov; buduje databázy a rozvíja nové procesy; dodržiava pravidlá a nariadenia; preberá nepríjemné a ťažké úlohy iných na svoje plecia; neobľubuje povinné spoločenské rozhovory o všeobecných témach, často pracuje sám "
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel234>:
    name: "234"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 234 "
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: PRAKTIK"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Vyvíja harmonické priateľské vzťahy; považuje tradície a rituály za užitočné pri upevňovaní vzťahov: podporuje iných pri plánovaní a organizovaní: je dobre informovaný a priateľský; analyzuje problémy a odhaľuje rozporuplnosti; vyjadruje svoje úsudky a odsudzuje iných keď je sklamaný alebo znechutený udalosťami alebo ľuďmi: vysokú hodnotu pripisuje odbornosti v špecializovaných oblastiach "
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            

'''
Builder.load_string(KV)