import sqlite3

# audio elements
try:
       import vlc
       # audio elements - effect
       info    = vlc.MediaPlayer("Components\\Audio\\Effects\\info.mp3")
       info2   = vlc.MediaPlayer("Components\\Audio\\Effects\\info2.mp3")
       good    = vlc.MediaPlayer("Components\\Audio\\Effects\\good.mp3")
       good2   = vlc.MediaPlayer("Components\\Audio\\Effects\\good2.mp3")
       good3   = vlc.MediaPlayer("Components\\Audio\\Effects\\good3.mp3")
       bad     = vlc.MediaPlayer("Components\\Audio\\Effects\\bad.mp3")
       alarm   = vlc.MediaPlayer("Components\\Audio\\Effects\\alarm.mp3")
       loading = vlc.MediaPlayer("Components\\Audio\\Effects\\loading.mp3")
       effect1 = vlc.MediaPlayer("Components\\Audio\\Effects\\effect1.mp3")
       effect2 = vlc.MediaPlayer("Components\\Audio\\Effects\\effect2.mp3")

#defining Alpha Protocol World Map Function
def APMap():
    print(clear)
    print("\n"*2)
    #PART I : CONTINENTS
    c1 = 0 #North America
    c2 = 0 #South America
    c3 = 0 #Antarctica
    c4 = 0 #Europe
    c5 = 0 #Africa
    c6 = 0 #Asia
    c7 = 0 #Australia
    db = sqlite3.connect("Components\\Data\\APDB")
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM subjectsGREEN;""")
    for i in cursor.fetchall():
        if   "NORTH AMERICA," in str(i[15]).upper():
            c1 += 1
        elif "SOUTH AMERICA," in str(i[15]).upper():
            c2 += 1
        elif "ANTARCTICA,"    in str(i[15]).upper():
            c3 += 1
        elif "EUROPE,"        in str(i[15]).upper():
            c4 += 1
        elif "AFRICA,"        in str(i[15]).upper():
            c5 += 1
        elif "ASIA,"          in str(i[15]).upper():
            c6 += 1
        elif "AUSTRALIA,"     in str(i[15]).upper():
            c7 += 1
    cursor.execute("""SELECT * FROM subjectsRED;""")
    for i in cursor.fetchall():
        if   "NORTH AMERICA," in str(i[15]).upper():
            c1 += 1
        elif "SOUTH AMERICA," in str(i[15]).upper():
            c2 += 1
        elif "ANTARCTICA,"    in str(i[15]).upper():
            c3 += 1
        elif "EUROPE,"        in str(i[15]).upper():
            c4 += 1
        elif "AFRICA,"        in str(i[15]).upper():
            c5 += 1
        elif "ASIA,"          in str(i[15]).upper():
            c6 += 1
        elif "AUSTRALIA,"     in str(i[15]).upper():
            c7 += 1
    c1, c2, c3, c4, c5, c6, c7 = str(c1), str(c2), str(c3), str(c4), str(c5), str(c6), str(c7)
    pic = Fore.LIGHTBLACK_EX+"""          
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWX0KKkxkkONWWWWWNXOkd:'';ldxKWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0Kk:,:,...  'clo:,,;:,'.    ....;oxolo0XXXXXXXXXXXXXXXWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKx0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNNXNXWX0Kl..lc'.. .,;;oc.                  ..ck0NXXXXXXXXXX0oxxoooldKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNx:;oO0KWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXN0lkWKooOdxOl:o:. .:OKxc.                    .;OWXXXXXXXXXXXX0oo,.;clKXXXXXXXXXXXXXXXXXXXXWXXXXXXXXXXXN0OkccOWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKdloOk;c00dcx0x::c,..,xWXNOo;,;.                  .dWXXXXXXXXXXXXXXXKkXXKWXXXXXXXXXXXXXXXNOxxkONXXXXXXXWXKOxdxc..;;;dXXXXXXXXXXXKxxONNKXWXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXklcoOxlccoOo;xxlo:;c;c0XXXXXWNWWXc                 ,OWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo;cd0NWNKNXXXN0x;.        ..;x00XWWKKNXXKdoxKXOKWXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXK: ..,:coock0:'dold:,,.,:cOWXXXXXXX0'      """+Fore.LIGHTGREEN_EX+c3+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""      .'lXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWo.oNXXXWo.lO00o,.          .......;;..oXXKKKxcoxxkXWXWXXXXXXXXXXNKNXXXXXXXXXX
                      XXXXXXXXWXOxdxkO0KXXWXXXNXKKKxdOx,     :0xol:OXl..... .;lOWXXXXXo'           .',dNXXXWKXXXXXXXXXXXXWNNNkocclkXWXXXXXWN0lx0K00O, ':,...                      .......     '::;:kKOO00xxkxxKXXXXXXXXXX
                      XXXXXXKxc'.    .....;cdd;...,,;lc,,::,;d0dl:.,xkc;dko:.  cXWXXXKo'        .'.'cOWXXXXXWWXXXXXXXXXXXXxlc.    ..:oON0k0kdoo:,..',..cc..                                        ..  ..   .':okXWXXXXXX
                      XXXXWKo,.                         .';..,,...  .;,cKKkk; .;,oNXXNc      ..'dXXNKkdxxxXXXXXXXXXXXXXXKc.   ..    ';cd:.'.          .,.                                                      .,,;cxNXXX
                      XXXXNd,'.                                    ';;oXWOo:. .:o0WXXWk.    c0XNWXXXXo,..cKXXXXXXXXXXNko,   .:l.    ,c,.                                                                       :OOdlkWXXX
                      XXXWKo,.                                   ,dK0kKWKooxdc:dXXXXXXWo.  :XXXXXXXXXWNKXWXXXXXXXXXKo,.    ;Ol                                                                      .''..    .:o0WXWXXXXX
                      XXXWx.    .'.;c;..                       .dNXXXXXWd   ;0NKNXXXXXXN0olKXXXXXXXXXXXXXXXXXXXWNWX0'      'O0:..                                                             ...''.cXKo,;odd0XXXXXXXXXXX
                      XXXXWOl'..dkkNXWXOl,.                    .dKNXXXXX:   .;:.cXXXXXXXXXXXXXXXXXXXXXXXXXXXWKol0XXWOccc;. cX0c.                                                            .dKXKXNKXNo..oNXXXXXXXXXXXXXX
                      XXWKkdddkkKXXXXXXXXNx.                    ..;oOXW0,       .oXXXXXXXXXXXXXXXXXXXXXXXXXWKx:.:XXXXk:cxdlkO:                                                             .dNWWWXXXXX:  :XXXXXXXXXXXXXXX
                      XXNkdkXWXXXXXXXXXXXXWx.                       .oNc          ,kWXXXXXXXXXXXXXXXXXXXXXXO,,o; :KKd;...,..                                                                .'cokNXXXXO,;0WXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXWo.                       ':.     ....''oWXXXXXXXXXXXXXXXXXXXXXXXOKkc,,;'                                            """+Fore.LIGHTGREEN_EX+c6+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                             .lckWXXXWXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXX0:.                             ..oKKd'.dWXXXXXXXXXXXXXXXXXXXXXXXWXd,.    """+Fore.LIGHTGREEN_EX+c4+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""               ..      .                                               .kKKWXXXXXXXXXXXXXXXXXXXXXX
  """+Style.RESET_ALL+Style.BRIGHT+"""    XXXXXXXXXXX     """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXX:           """+Fore.LIGHTGREEN_EX+c1+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""                   .:dKX0kOWXXXXXXXXXXXXXXXXXXXXXXXWWX:        '.       ,l,;l'    ,do'   .lc                                       .dWKkKWXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""XXXXXXXXXXX    """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""   X           X    """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXWd.                            .lkkOXWXXXXXXXXXXXXXXXXXXXXXXXXXXNd;:c. .:lol:,;l:.    ;0Kxx0kc.  cKx,.  .,'                                    .;lOWWk;lXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X          X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXX:                           .cOWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK,    ,kNXXkkOkcco, 'c;,'..'::.   cKO,                                   .;,...oNXXXXkcOXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXNo.                         ;KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK:...,kK0Okxx0NOkXKld0l...        'kk'                                   .clkk,;0WWNO;.kXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXc.                       'OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNd,;;'..    cNWWXXWNNNK0kd'       ..                                     .lNXk;dKxc::dXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  XXXXXXXXXXXXXXX   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXNk'                   .;xKWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKc.          .:okXk:cx0K0Oo.                                               .kXWNKdxKWXXXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""XXXXXXXXXXXXX  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXWd;,.        .,,':lc.,0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXc.               ..   .....       ';.                                       :XXXXWWXXXXXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXNd:;.      ;0WNXWXXx'xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXo.                         .;;.     .;ll:,.....                              .dNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXXWxcl'    '0XXXXXXN0okXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNl                             cd.      .:;':xKKOd'           ..            ..:xx0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXXXWXXO'   .OXXXdxXX00kdkXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'                             .dx.         .kWXXXKo:.      .l00c.      .::d0KNWXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   """+Style.RESET_ALL+Style.BRIGHT+"""X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWOc.  ,ll' cNXXXKloxoo0KNXXXXXXXXXXXXXXXXXXXXXXXXXXK,                              .dk,      .:OWXXXXXXK,    .cOWXXNl..    ;xkXXXXWOl0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXkoll'  ,lkNXWNWWWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXWk.                               .ll..',cxXWXXXXXXXXWx.  :0WXXXXXXOc     .xWXXXWd,dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOx, cNXXXNOxONXWWWXXXXXXXXXXXXXXXXXXXXXXXX0,                    """+Fore.LIGHTGREEN_EX+c5+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""            ':xOkkXXXXXXXXXXXXWd. dXXXXXXXXWk.,c.  lWXXXW0kdxNXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKc:dxkx;.  ':;,lXXXXXXXXXXXXXXXXXXXXXXXXXK:                                 ....:XXXXXXXXXXXXXNo;lOWXXXXXXXWxckkldXXXXW0OKxcoXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKkxl.         'oxONXXXXXXXXXXXXXXXXXXXXXNx,  ...,cc.                         ;KXXXXXXXXXXXXXXWNkxNXXXXXW00K:.lXXXXXNd:xXKxdXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWk.             ,kWXXXXXXXXXXXXXXXXXXXXXXxkKKXNXWKx:..                   .c0XXXXXXXXXXXXXXXXXXXXXXXXXW0xo:.,OWN0d, .dXNXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNd.               ,OKXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXWd..                 .c0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO,.lKXd.   ,oodO0k0XWXKXNXXXXXWNWXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO.                ...':odONXXXXXXXXXXXXXXXXXXXXXXXXWkc'                ,OWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0:.;OXd;,;xl.cKNXKXNd,',cokNXNkONXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO.                       .,kWXXXXXXXXXXXXXXXXXXXXXXXXXK;              .xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNkllodxkKN0xkXXXWWWXO;   .:OO0XXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.                        cNXXXXXXXXXXXXXXXXXXXXXXXXXWd.              oWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN0kdoxKXK0KNWXXWWXWOo:okccOWXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.                     .lXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'              ;XXXW0KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWNWWKo:lkWNddNWKKWXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.        """+Fore.LIGHTGREEN_EX+c2+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""           cNXXXXXXXXXXXXXXXXXXXXXXXXXXXXc               ,KN0l.lWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXd;:'   cKX:.dNXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKd;.                 oWXXXXXXXXXXXXXXXXXXXXXXXXXXX0'             'o0Nd. 'OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNx'        .,. '0WXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:                ,KXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.           ;KXXNl .oWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNOo:,.              ,xNXXXXXXW0KXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWl             .:l0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWl           cNXXK; ;0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXc.                   .oNXXXXXXNNXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN:            cXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.         cXWXXWKkXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;           """+Fore.LIGHTGREEN_EX+c7+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""         .kXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'           '0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo.       cXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWo                     '0XXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.          ;0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:    .,xNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.   .,;cl:.         .dNXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXk.       .,lKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0loxkONXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWkclodONXXXW0d:.     ,OWXXXXXXXXXW00XXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo        ;0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXo'..,oKXXXXXXXXXXXWd;dNX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNc     .cOXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxdKXXXXXXXXXXXW0xc:OWX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.   .oXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXocKXXXXXXXXWXkl:xXNXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'  .cXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWXXXXXXXXXK:'dXWXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO.  .dWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKKWXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0,  ,0XXNKXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0:.cKWXKk0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN0do0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL
    effect1.stop()
    effect1.play()
    print(pic)
    input("")
    #PART II : COUNTRIES
    t155, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, hh, t17, t18, t19, jj, t21, AD, ww, nn, ss, mm, t27, rr, uu, pp, qq, AA, zz, t34, tt, AE, ii, yy, AF, t40, t41, AC, vv, oo, AB, xx, t47, AL, AJ, WW, AK, AG, t53, AI, AH, t56, t57, t58, t59, t60, ll, t62, kk, t64, t65, t66, t67, t68, t69, t70, t71, t72, t73, t74, t75, t76, t77, t78, t79, t80, t81, t82, t83, t84, t85, t86, LL, KK, JJ, II, HH, t92, t93, t94, t95, t96, t97, t98, t99, t100, t101, t102, t103, t104, t105, t106, t107, t108, GG, t110, t111, FF, DD, EE, CC, BB, AX, t118, t119, t120, t121, t122, t123, t124, t125, t126, t127, t128, t129, t130, t131, t132, t133, t134, t135, t136, XX, YY, t139, t140, SS, RR, QQ, PP, OO, t146, t147, t148, MM, t150, t151, TT, t153, VV, UU, ZZ, aa, bb, cc, NN, t161, t162, t163, t164, t165, t166, t167, t168, gg, t170, t171, t172, t173, t174, t175, t176, t177, t178, t179, t180, dd, t182, ff, t184, ee, t186, t187, t188, t189   =   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    cursor.execute("""SELECT * FROM subjectsGREEN;""")
    for i in cursor.fetchall():
        if   ", CANADA," in str(i[15]).upper():
            t1 += 1
        elif ", USA," in str(i[15]).upper():
            t2 += 1
        elif ", MEXICO," in str(i[15]).upper():
            t3 += 1
        elif ", ARGENTINIA," in str(i[15]).upper():
            t4 += 1
        elif ", BOLIVIA," in str(i[15]).upper():
            t5 += 1
        elif ", BRASIL," in str(i[15]).upper():
            t6 += 1
        elif ", CHILE," in str(i[15]).upper():
            t7 += 1
        elif ", ECUADOR," in str(i[15]).upper():
            t8 += 1
        elif ", GUYANA," in str(i[15]).upper():
            t9 += 1
        elif ", COLUMBIA," in str(i[15]).upper():
            t10 += 1
        elif ", PARAGUAY," in str(i[15]).upper():
            t11 += 1
        elif ", PERU," in str(i[15]).upper():
            t12 += 1
        elif ", SURINAME," in str(i[15]).upper():
            t13 += 1
        elif ", URUGUAY," in str(i[15]).upper():
            t14 += 1
        elif ", VENEZUELA," in str(i[15]).upper():
            t15 += 1
        elif ", PORTUGAL," in str(i[15]).upper():
            t16 += 1
        elif ", GERMANY," in str(i[15]).upper():
            hh += 1
        elif ", FRANCE," in str(i[15]).upper():
            t17 += 1
        elif ", ITALY," in str(i[15]).upper():
            t18 += 1
        elif ", SPAIN," in str(i[15]).upper():
            t19 += 1
        elif ", UNITED KINGDOM," in str(i[15]).upper():
            jj += 1
        elif ", SWITZERLAND," in str(i[15]).upper():
            t21 += 1
        elif ", GREECE," in str(i[15]).upper():
            AD += 1
        elif ", CROATIA," in str(i[15]).upper():
            ww += 1
        elif ", NETHERLANDS," in str(i[15]).upper():
            nn += 1
        elif ", POLAND," in str(i[15]).upper():
            ss += 1
        elif ", BELGIUM," in str(i[15]).upper():
            mm += 1
        elif ", ICELAND," in str(i[15]).upper():
            t27 += 1
        elif ", SWEDEN," in str(i[15]).upper():
            rr += 1
        elif ", AUSTRIA," in str(i[15]).upper():
            uu += 1
        elif ", DENMARK," in str(i[15]).upper():
            pp += 1
        elif ", NORWAY," in str(i[15]).upper():
            qq += 1
        elif ", SERBIA," in str(i[15]).upper():
            AX += 1
        elif ", UKRAINE," in str(i[15]).upper():
            zz += 1
        elif ", MALTA," in str(i[15]).upper():
            t34 += 1
        elif ", CZECH REPUBLIC," in str(i[15]).upper():
            tt += 1
        elif ", ROMANIA," in str(i[15]).upper():
            AE += 1
        elif ", IRELAND," in str(i[15]).upper():
            ii += 1
        elif ", HUNGARY," in str(i[15]).upper():
            yy += 1
        elif ", BULGARIA," in str(i[15]).upper():
            AF += 1
        elif ", FINLAND," in str(i[15]).upper():
            t40 += 1
        elif ", CYPRUS," in str(i[15]).upper():
            t41 += 1
        elif ", ALBANIA," in str(i[15]).upper():
            AC += 1
        elif ", SLOVENIA," in str(i[15]).upper():
            vv += 1
        elif ", LUXEMBURG," in str(i[15]).upper():
            oo += 1
        elif ", MONTENEGRO," in str(i[15]).upper():
            AB += 1
        elif ", SLOVAKIA," in str(i[15]).upper():
            xx += 1
        elif ", MONACO," in str(i[15]).upper():
            t47 += 1
        elif ", LITHUANIA," in str(i[15]).upper():
            AL += 1
        elif ", ESTONIA," in str(i[15]).upper():
            AJ += 1
        elif ", BOSNIA & HERZEGOVINA," in str(i[15]).upper():
            WW += 1
        elif ", LATVIA," in str(i[15]).upper():
            AK += 1
        elif ", MACEDONIA," in str(i[15]).upper():
            AG += 1
        elif ", VATICAN CITY," in str(i[15]).upper():
            t53 += 1
        elif ", BELARUS," in str(i[15]).upper():
            AI += 1
        elif ", MOLDOVA," in str(i[15]).upper():
            AH += 1
        elif ", GIBRALTAR," in str(i[15]).upper():
            t56 += 1
        elif ", LICHTENSTEIN," in str(i[15]).upper():
            t57 += 1
        elif ", ANDORRA," in str(i[15]).upper():
            t58 += 1
        elif ", FAROE ISLANDS," in str(i[15]).upper():
            t59 += 1
        elif ", SAN MARINO," in str(i[15]).upper():
            t60 += 1
        elif ", ISLE OF MAN," in str(i[15]).upper():
            ll += 1
        elif ", JERSEY," in str(i[15]).upper():
            t62 += 1
        elif ", NORTHERN IRELAND," in str(i[15]).upper():
            kk += 1
        elif ", GUERNSEY," in str(i[15]).upper():
            t64 += 1
        elif ", ALAND ISLANDS," in str(i[15]).upper():
            t65 += 1
        elif ", AUSTRALIA," in str(i[15]).upper():
            t66 += 1
        elif ", FIJI," in str(i[15]).upper():
            t67 += 1
        elif ", KIRIBATI," in str(i[15]).upper():
            t68 += 1
        elif ", MARSHALL ISLANDS," in str(i[15]).upper():
            t69 += 1
        elif ", MICRONESIA," in str(i[15]).upper():
            t70 += 1
        elif ", NAURU," in str(i[15]).upper():
            t71 += 1
        elif ", NEW ZEALAND," in str(i[15]).upper():
            t72 += 1
        elif ", PALAU," in str(i[15]).upper():
            t73 += 1
        elif ", PAPUA NEW GUINEA," in str(i[15]).upper():
            t74 += 1
        elif ", SAMOA," in str(i[15]).upper():
            t75 += 1
        elif ", SOLOMON ISLANDS," in str(i[15]).upper():
            t76 += 1
        elif ", TONGA," in str(i[15]).upper():
            t77 += 1
        elif ", TUVALU," in str(i[15]).upper():
            t78 += 1
        elif ", VANUATU," in str(i[15]).upper():
            t79 += 1
        elif ", EGYPT," in str(i[15]).upper():
            t80 += 1
        elif ", LYBIA," in str(i[15]).upper():
            t81 += 1
        elif ", TUNISIA," in str(i[15]).upper():
            t82 += 1
        elif ", ALGERIA," in str(i[15]).upper():
            t83 += 1
        elif ", MOROCCO," in str(i[15]).upper():
            t84 += 1
        elif ", WESTERN SAHARA," in str(i[15]).upper():
            t85 += 1
        elif ", MAURITANIA," in str(i[15]).upper():
            t86 += 1
        elif ", SENEGAL," in str(i[15]).upper():
            LL += 1
        elif ", THE GAMBIA," in str(i[15]).upper():
            KK += 1
        elif ", GUINEA-BISSAU," in str(i[15]).upper():
            JJ += 1
        elif ", GUINEA," in str(i[15]).upper():
            II += 1
        elif ", SIERRA LEONE," in str(i[15]).upper():
            HH += 1
        elif ", ERITREA," in str(i[15]).upper():
            t92 += 1
        elif ", ETHIOPIA," in str(i[15]).upper():
            t93 += 1
        elif ", SOMALIA," in str(i[15]).upper():
            t94 += 1
        elif ", SOMALILAND," in str(i[15]).upper():
            t95 += 1
        elif ", DRC" in str(i[15]).upper():
            t96 += 1
        elif ", EQUATORIAL GUINEA," in str(i[15]).upper():
            t97 += 1
        elif ", RWANDA," in str(i[15]).upper():
            t98 += 1
        elif ", BURUNDI," in str(i[15]).upper():
            t99 += 1
        elif ", ANGOLA," in str(i[15]).upper():
            t100 += 1
        elif ", MALAWI," in str(i[15]).upper():
            t101 += 1
        elif ", MOZAMBIQUE," in str(i[15]).upper():
            t102 += 1
        elif ", NAMIBIA," in str(i[15]).upper():
            t103 += 1
        elif ", SOUTH AFRICA," in str(i[15]).upper():
            t104 += 1
        elif ", LESOTHO," in str(i[15]).upper():
            t105 += 1
        elif ", COMOROS," in str(i[15]).upper():
            t106 += 1
        elif ", MAURITIUS," in str(i[15]).upper():
            t107 += 1
        elif ", SAO TOME & PRINCIPE," in str(i[15]).upper():
            t108 += 1
        elif ", LIBERIA," in str(i[15]).upper():
            GG += 1
        elif ", MALI," in str(i[15]).upper():
            t110 += 1
        elif ", UGANDA," in str(i[15]).upper():
            t111 += 1
        elif ", IVORY COAST," in str(i[15]).upper():
            FF += 1
        elif ", BURKINA FASO," in str(i[15]).upper():
            DD += 1
        elif ", GHANA," in str(i[15]).upper():
            EE += 1
        elif ", TOGO," in str(i[15]).upper():
            CC += 1
        elif ", BENIN," in str(i[15]).upper():
            BB += 1
        elif ", NIGERIA," in str(i[15]).upper():
            AA += 1
        elif ", NIGER," in str(i[15]).upper():
            t118 += 1
        elif ", CHAD," in str(i[15]).upper():
            t119 += 1
        elif ", SUDAN," in str(i[15]).upper():
            t120 += 1
        elif ", SOUTH SUDAN," in str(i[15]).upper():
            t121 += 1
        elif ", DJIBOUTI," in str(i[15]).upper():
            t122 += 1
        elif ", KENYA," in str(i[15]).upper():
            t123 += 1
        elif ", CAR," in str(i[15]).upper():
            t124 += 1
        elif ", RC," in str(i[15]).upper():
            t125 += 1
        elif ", GABON," in str(i[15]).upper():
            t126 += 1
        elif ", CAMEROON," in str(i[15]).upper():
            t127 += 1
        elif ", TANZANIA," in str(i[15]).upper():
            t128 += 1
        elif ", ZAMBIA," in str(i[15]).upper():
            t129 += 1
        elif ", ZIMBABWE," in str(i[15]).upper():
            t130 += 1
        elif ", MADAGASCAR," in str(i[15]).upper():
            t131 += 1
        elif ", BOTSWANA," in str(i[15]).upper():
            t132 += 1
        elif ", SWAZILAND," in str(i[15]).upper():
            t133 += 1
        elif ", CAPE VERDE," in str(i[15]).upper():
            t134 += 1
        elif ", MAYOTTE," in str(i[15]).upper():
            t135 += 1
        elif ", REUNION," in str(i[15]).upper():
            t136 += 1
        elif ", PAKISTAN," in str(i[15]).upper():
            XX += 1
        elif ", AFGHANISTAN," in str(i[15]).upper():
            YY += 1
        elif ", IRAN," in str(i[15]).upper():
            t139 += 1
        elif ", TURKEY," in str(i[15]).upper():
            t140 += 1
        elif ", IRAQ," in str(i[15]).upper():
            SS += 1
        elif ", SYRIA," in str(i[15]).upper():
            RR += 1
        elif ", LEBANON," in str(i[15]).upper():
            QQ += 1
        elif ", JORDAN," in str(i[15]).upper():
            PP += 1
        elif ", ISRAEL," in str(i[15]).upper():
            OO += 1
        elif ", PALESTINE," in str(i[15]).upper():
            t146 += 1
        elif ", SAUDI ARABIA," in str(i[15]).upper():
            t147 += 1
        elif ", YEMEN," in str(i[15]).upper():
            t148 += 1
        elif ", QATAR," in str(i[15]).upper():
            MM += 1
        elif ", UAE," in str(i[15]).upper():
            t150 += 1
        elif ", OMAN," in str(i[15]).upper():
            t151 += 1
        elif ", KUWAIT," in str(i[15]).upper():
            TT += 1
        elif ", GEORGIA," in str(i[15]).upper():
            t153 += 1
        elif ", ARMENIA," in str(i[15]).upper():
            VV += 1
        elif ", AZERBAIJAN," in str(i[15]).upper():
            UU += 1
        elif ", KAZAKHSTAN," in str(i[15]).upper():
            t155 += 1
        elif ", TURKMENISTAN," in str(i[15]).upper():
            ZZ += 1
        elif ", UZBEKISTAN," in str(i[15]).upper():
            aa += 1
        elif ", TAJIKISTAN," in str(i[15]).upper():
            bb += 1
        elif ", KYRGYZSTAN," in str(i[15]).upper():
            cc += 1
        elif ", BAHRAIN," in str(i[15]).upper():
            NN += 1
        elif ", CHRISTMAS ISLAND," in str(i[15]).upper():
            t161 += 1
        elif ", RUSSIA," in str(i[15]).upper():
            t162 += 1
        elif ", JAPAN," in str(i[15]).upper():
            t163 += 1
        elif ", INDIA," in str(i[15]).upper():
            t164 += 1
        elif ", CHINA," in str(i[15]).upper():
            t165 += 1
        elif ", INDONESIA," in str(i[15]).upper():
            t166 += 1
        elif ", VIETNAM," in str(i[15]).upper():
            t167 += 1
        elif ", SINGAPORE," in str(i[15]).upper():
            t168 += 1
        elif ", THAILAND," in str(i[15]).upper():
            gg += 1
        elif ", PHILLIPPINES," in str(i[15]).upper():
            t170 += 1
        elif ", NORTH KOREA," in str(i[15]).upper():
            t171 += 1
        elif ", SOUTH KOREA," in str(i[15]).upper():
            t172 += 1
        elif ", MALAYSIA," in str(i[15]).upper():
            t173 += 1
        elif ", HONG KONG," in str(i[15]).upper():
            t174 += 1
        elif ", MYANMAR," in str(i[15]).upper():
            t175 += 1
        elif ", SRI LANKA," in str(i[15]).upper():
            t176 += 1
        elif ", CAMBODIA," in str(i[15]).upper():
            t177 += 1
        elif ", BANGLADESH," in str(i[15]).upper():
            t178 += 1
        elif ", TAIWAN," in str(i[15]).upper():
            t179 += 1
        elif ", MALDIVES," in str(i[15]).upper():
            t180 += 1
        elif ", NEPAL," in str(i[15]).upper():
            dd += 1
        elif ", MACAU," in str(i[15]).upper():
            t182 += 1
        elif ", LAOS," in str(i[15]).upper():
            ff += 1
        elif ", MONGOLIA," in str(i[15]).upper():
            t184 += 1
        elif ", BHUTAN," in str(i[15]).upper():
            ee += 1
        elif ", BRUNEI," in str(i[15]).upper():
            t186 += 1
        elif ", TIMOR-LESTE," in str(i[15]).upper():
            t187 += 1
        elif ", COCOS," in str(i[15]).upper():
            t188 += 1
    cursor.execute("""SELECT * FROM subjectsRED;""")
    for i in cursor.fetchall():
        if   ", CANADA," in str(i[15]).upper():
            t1 += 1
        elif ", USA," in str(i[15]).upper():
            t2 += 1
        elif ", MEXICO," in str(i[15]).upper():
            t3 += 1
        elif ", ARGENTINIA," in str(i[15]).upper():
            t4 += 1
        elif ", BOLIVIA," in str(i[15]).upper():
            t5 += 1
        elif ", BRASIL," in str(i[15]).upper():
            t6 += 1
        elif ", CHILE," in str(i[15]).upper():
            t7 += 1
        elif ", ECUADOR," in str(i[15]).upper():
            t8 += 1
        elif ", GUYANA," in str(i[15]).upper():
            t9 += 1
        elif ", COLUMBIA," in str(i[15]).upper():
            t10 += 1
        elif ", PARAGUAY," in str(i[15]).upper():
            t11 += 1
        elif ", PERU," in str(i[15]).upper():
            t12 += 1
        elif ", SURINAME," in str(i[15]).upper():
            t13 += 1
        elif ", URUGUAY," in str(i[15]).upper():
            t14 += 1
        elif ", VENEZUELA," in str(i[15]).upper():
            t15 += 1
        elif ", PORTUGAL," in str(i[15]).upper():
            t16 += 1
        elif ", GERMANY," in str(i[15]).upper():
            hh += 1
        elif ", FRANCE," in str(i[15]).upper():
            t17 += 1
        elif ", ITALY," in str(i[15]).upper():
            t18 += 1
        elif ", SPAIN," in str(i[15]).upper():
            t19 += 1
        elif ", UNITED KINGDOM," in str(i[15]).upper():
            jj += 1
        elif ", SWITZERLAND," in str(i[15]).upper():
            t21 += 1
        elif ", GREECE," in str(i[15]).upper():
            AD += 1
        elif ", CROATIA," in str(i[15]).upper():
            ww += 1
        elif ", NETHERLANDS," in str(i[15]).upper():
            nn += 1
        elif ", POLAND," in str(i[15]).upper():
            ss += 1
        elif ", BELGIUM," in str(i[15]).upper():
            mm += 1
        elif ", ICELAND," in str(i[15]).upper():
            t27 += 1
        elif ", SWEDEN," in str(i[15]).upper():
            rr += 1
        elif ", AUSTRIA," in str(i[15]).upper():
            uu += 1
        elif ", DENMARK," in str(i[15]).upper():
            pp += 1
        elif ", NORWAY," in str(i[15]).upper():
            qq += 1
        elif ", SERBIA," in str(i[15]).upper():
            AX += 1
        elif ", UKRAINE," in str(i[15]).upper():
            zz += 1
        elif ", MALTA," in str(i[15]).upper():
            t34 += 1
        elif ", CZECH REPUBLIC," in str(i[15]).upper():
            tt += 1
        elif ", ROMANIA," in str(i[15]).upper():
            AE += 1
        elif ", IRELAND," in str(i[15]).upper():
            ii += 1
        elif ", HUNGARY," in str(i[15]).upper():
            yy += 1
        elif ", BULGARIA," in str(i[15]).upper():
            AF += 1
        elif ", FINLAND," in str(i[15]).upper():
            t40 += 1
        elif ", CYPRUS," in str(i[15]).upper():
            t41 += 1
        elif ", ALBANIA," in str(i[15]).upper():
            AC += 1
        elif ", SLOVENIA," in str(i[15]).upper():
            vv += 1
        elif ", LUXEMBURG," in str(i[15]).upper():
            oo += 1
        elif ", MONTENEGRO," in str(i[15]).upper():
            AB += 1
        elif ", SLOVAKIA," in str(i[15]).upper():
            xx += 1
        elif ", MONACO," in str(i[15]).upper():
            t47 += 1
        elif ", LITHUANIA," in str(i[15]).upper():
            AL += 1
        elif ", ESTONIA," in str(i[15]).upper():
            AJ += 1
        elif ", BOSNIA & HERZEGOVINA," in str(i[15]).upper():
            WW += 1
        elif ", LATVIA," in str(i[15]).upper():
            AK += 1
        elif ", MACEDONIA," in str(i[15]).upper():
            AG += 1
        elif ", VATICAN CITY," in str(i[15]).upper():
            t53 += 1
        elif ", BELARUS," in str(i[15]).upper():
            AI += 1
        elif ", MOLDOVA," in str(i[15]).upper():
            AH += 1
        elif ", GIBRALTAR," in str(i[15]).upper():
            t56 += 1
        elif ", LICHTENSTEIN," in str(i[15]).upper():
            t57 += 1
        elif ", ANDORRA," in str(i[15]).upper():
            t58 += 1
        elif ", FAROE ISLANDS," in str(i[15]).upper():
            t59 += 1
        elif ", SAN MARINO," in str(i[15]).upper():
            t60 += 1
        elif ", ISLE OF MAN," in str(i[15]).upper():
            ll += 1
        elif ", JERSEY," in str(i[15]).upper():
            t62 += 1
        elif ", NORTHERN IRELAND," in str(i[15]).upper():
            kk += 1
        elif ", GUERNSEY," in str(i[15]).upper():
            t64 += 1
        elif ", ALAND ISLANDS," in str(i[15]).upper():
            t65 += 1
        elif ", AUSTRALIA," in str(i[15]).upper():
            t66 += 1
        elif ", FIJI," in str(i[15]).upper():
            t67 += 1
        elif ", KIRIBATI," in str(i[15]).upper():
            t68 += 1
        elif ", MARSHALL ISLANDS," in str(i[15]).upper():
            t69 += 1
        elif ", MICRONESIA," in str(i[15]).upper():
            t70 += 1
        elif ", NAURU," in str(i[15]).upper():
            t71 += 1
        elif ", NEW ZEALAND," in str(i[15]).upper():
            t72 += 1
        elif ", PALAU," in str(i[15]).upper():
            t73 += 1
        elif ", PAPUA NEW GUINEA," in str(i[15]).upper():
            t74 += 1
        elif ", SAMOA," in str(i[15]).upper():
            t75 += 1
        elif ", SOLOMON ISLANDS," in str(i[15]).upper():
            t76 += 1
        elif ", TONGA," in str(i[15]).upper():
            t77 += 1
        elif ", TUVALU," in str(i[15]).upper():
            t78 += 1
        elif ", VANUATU," in str(i[15]).upper():
            t79 += 1
        elif ", EGYPT," in str(i[15]).upper():
            t80 += 1
        elif ", LYBIA," in str(i[15]).upper():
            t81 += 1
        elif ", TUNISIA," in str(i[15]).upper():
            t82 += 1
        elif ", ALGERIA," in str(i[15]).upper():
            t83 += 1
        elif ", MOROCCO," in str(i[15]).upper():
            t84 += 1
        elif ", WESTERN SAHARA," in str(i[15]).upper():
            t85 += 1
        elif ", MAURITANIA," in str(i[15]).upper():
            t86 += 1
        elif ", SENEGAL," in str(i[15]).upper():
            LL += 1
        elif ", THE GAMBIA," in str(i[15]).upper():
            KK += 1
        elif ", GUINEA-BISSAU," in str(i[15]).upper():
            JJ += 1
        elif ", GUINEA," in str(i[15]).upper():
            II += 1
        elif ", SIERRA LEONE," in str(i[15]).upper():
            HH += 1
        elif ", ERITREA," in str(i[15]).upper():
            t92 += 1
        elif ", ETHIOPIA," in str(i[15]).upper():
            t93 += 1
        elif ", SOMALIA," in str(i[15]).upper():
            t94 += 1
        elif ", SOMALILAND," in str(i[15]).upper():
            t95 += 1
        elif ", DRC" in str(i[15]).upper():
            t96 += 1
        elif ", EQUATORIAL GUINEA," in str(i[15]).upper():
            t97 += 1
        elif ", RWANDA," in str(i[15]).upper():
            t98 += 1
        elif ", BURUNDI," in str(i[15]).upper():
            t99 += 1
        elif ", ANGOLA," in str(i[15]).upper():
            t100 += 1
        elif ", MALAWI," in str(i[15]).upper():
            t101 += 1
        elif ", MOZAMBIQUE," in str(i[15]).upper():
            t102 += 1
        elif ", NAMIBIA," in str(i[15]).upper():
            t103 += 1
        elif ", SOUTH AFRICA," in str(i[15]).upper():
            t104 += 1
        elif ", LESOTHO," in str(i[15]).upper():
            t105 += 1
        elif ", COMOROS," in str(i[15]).upper():
            t106 += 1
        elif ", MAURITIUS," in str(i[15]).upper():
            t107 += 1
        elif ", SAO TOME & PRINCIPE," in str(i[15]).upper():
            t108 += 1
        elif ", LIBERIA," in str(i[15]).upper():
            GG += 1
        elif ", MALI," in str(i[15]).upper():
            t110 += 1
        elif ", UGANDA," in str(i[15]).upper():
            t111 += 1
        elif ", IVORY COAST," in str(i[15]).upper():
            FF += 1
        elif ", BURKINA FASO," in str(i[15]).upper():
            DD += 1
        elif ", GHANA," in str(i[15]).upper():
            EE += 1
        elif ", TOGO," in str(i[15]).upper():
            CC += 1
        elif ", BENIN," in str(i[15]).upper():
            BB += 1
        elif ", NIGERIA," in str(i[15]).upper():
            AA += 1
        elif ", NIGER," in str(i[15]).upper():
            t118 += 1
        elif ", CHAD," in str(i[15]).upper():
            t119 += 1
        elif ", SUDAN," in str(i[15]).upper():
            t120 += 1
        elif ", SOUTH SUDAN," in str(i[15]).upper():
            t121 += 1
        elif ", DJIBOUTI," in str(i[15]).upper():
            t122 += 1
        elif ", KENYA," in str(i[15]).upper():
            t123 += 1
        elif ", CAR," in str(i[15]).upper():
            t124 += 1
        elif ", RC," in str(i[15]).upper():
            t125 += 1
        elif ", GABON," in str(i[15]).upper():
            t126 += 1
        elif ", CAMEROON," in str(i[15]).upper():
            t127 += 1
        elif ", TANZANIA," in str(i[15]).upper():
            t128 += 1
        elif ", ZAMBIA," in str(i[15]).upper():
            t129 += 1
        elif ", ZIMBABWE," in str(i[15]).upper():
            t130 += 1
        elif ", MADAGASCAR," in str(i[15]).upper():
            t131 += 1
        elif ", BOTSWANA," in str(i[15]).upper():
            t132 += 1
        elif ", SWAZILAND," in str(i[15]).upper():
            t133 += 1
        elif ", CAPE VERDE," in str(i[15]).upper():
            t134 += 1
        elif ", MAYOTTE," in str(i[15]).upper():
            t135 += 1
        elif ", REUNION," in str(i[15]).upper():
            t136 += 1
        elif ", PAKISTAN," in str(i[15]).upper():
            XX += 1
        elif ", AFGHANISTAN," in str(i[15]).upper():
            YY += 1
        elif ", IRAN," in str(i[15]).upper():
            t139 += 1
        elif ", TURKEY," in str(i[15]).upper():
            t140 += 1
        elif ", IRAQ," in str(i[15]).upper():
            SS += 1
        elif ", SYRIA," in str(i[15]).upper():
            RR += 1
        elif ", LEBANON," in str(i[15]).upper():
            QQ += 1
        elif ", JORDAN," in str(i[15]).upper():
            PP += 1
        elif ", ISRAEL," in str(i[15]).upper():
            OO += 1
        elif ", PALESTINE," in str(i[15]).upper():
            t146 += 1
        elif ", SAUDI ARABIA," in str(i[15]).upper():
            t147 += 1
        elif ", YEMEN," in str(i[15]).upper():
            t148 += 1
        elif ", QATAR," in str(i[15]).upper():
            MM += 1
        elif ", UAE," in str(i[15]).upper():
            t150 += 1
        elif ", OMAN," in str(i[15]).upper():
            t151 += 1
        elif ", KUWAIT," in str(i[15]).upper():
            TT += 1
        elif ", GEORGIA," in str(i[15]).upper():
            t153 += 1
        elif ", ARMENIA," in str(i[15]).upper():
            VV += 1
        elif ", AZERBAIJAN," in str(i[15]).upper():
            UU += 1
        elif ", KAZAKHSTAN," in str(i[15]).upper():
            t155 += 1
        elif ", TURKMENISTAN," in str(i[15]).upper():
            ZZ += 1
        elif ", UZBEKISTAN," in str(i[15]).upper():
            aa += 1
        elif ", TAJIKISTAN," in str(i[15]).upper():
            bb += 1
        elif ", KYRGYZSTAN," in str(i[15]).upper():
            cc += 1
        elif ", BAHRAIN," in str(i[15]).upper():
            NN += 1
        elif ", CHRISTMAS ISLAND," in str(i[15]).upper():
            t161 += 1
        elif ", RUSSIA," in str(i[15]).upper():
            t162 += 1
        elif ", JAPAN," in str(i[15]).upper():
            t163 += 1
        elif ", INDIA," in str(i[15]).upper():
            t164 += 1
        elif ", CHINA," in str(i[15]).upper():
            t165 += 1
        elif ", INDONESIA," in str(i[15]).upper():
            t166 += 1
        elif ", VIETNAM," in str(i[15]).upper():
            t167 += 1
        elif ", SINGAPORE," in str(i[15]).upper():
            t168 += 1
        elif ", THAILAND," in str(i[15]).upper():
            gg += 1
        elif ", PHILLIPPINES," in str(i[15]).upper():
            t170 += 1
        elif ", NORTH KOREA," in str(i[15]).upper():
            t171 += 1
        elif ", SOUTH KOREA," in str(i[15]).upper():
            t172 += 1
        elif ", MALAYSIA," in str(i[15]).upper():
            t173 += 1
        elif ", HONG KONG," in str(i[15]).upper():
            t174 += 1
        elif ", MYANMAR," in str(i[15]).upper():
            t175 += 1
        elif ", SRI LANKA," in str(i[15]).upper():
            t176 += 1
        elif ", CAMBODIA," in str(i[15]).upper():
            t177 += 1
        elif ", BANGLADESH," in str(i[15]).upper():
            t178 += 1
        elif ", TAIWAN," in str(i[15]).upper():
            t179 += 1
        elif ", MALDIVES," in str(i[15]).upper():
            t180 += 1
        elif ", NEPAL," in str(i[15]).upper():
            dd += 1
        elif ", MACAU," in str(i[15]).upper():
            t182 += 1
        elif ", LAOS," in str(i[15]).upper():
            ff += 1
        elif ", MONGOLIA," in str(i[15]).upper():
            t184 += 1
        elif ", BHUTAN," in str(i[15]).upper():
            ee += 1
        elif ", BRUNEI," in str(i[15]).upper():
            t186 += 1
        elif ", TIMOR-LESTE," in str(i[15]).upper():
            t187 += 1
        elif ", COCOS," in str(i[15]).upper():
            t188 += 1
    ###########
    if t1 == 0:
        t1 = "  "
    elif t1 != 0 and t1 < 10:
        t1 = Fore.LIGHTGREEN_EX + str(t1) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t1 >= 10:
        t1 = Fore.LIGHTGREEN_EX + str(t1) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t2 == 0:
        t2 = "  "
    elif t2 != 0 and t2 < 10:
        t2 = Fore.LIGHTGREEN_EX + str(t2) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t2 >= 10:
        t2 = Fore.LIGHTGREEN_EX + str(t2) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t3 == 0:
        t3 = "  "
    elif t3 != 0 and t3 < 10:
        t3 = Fore.LIGHTGREEN_EX + str(t3) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t3 >= 10:
        t3 = Fore.LIGHTGREEN_EX + str(t3) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t4 == 0:
        t4 = "  "
    elif t4 != 0 and t4 < 10:
        t4 = Fore.LIGHTGREEN_EX + str(t4) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t4 >= 10:
        t4 = Fore.LIGHTGREEN_EX + str(t4) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t5 == 0:
        t5 = "  "
    elif t5 != 0 and t5 < 10:
        t5 = Fore.LIGHTGREEN_EX + str(t5) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t5 >= 10:
        t5 = Fore.LIGHTGREEN_EX + str(t5) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t6 == 0:
        t6 = "  "
    elif t6 != 0 and t6 < 10:
        t6 = Fore.LIGHTGREEN_EX + str(t6) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t6 >= 10:
        t6 = Fore.LIGHTGREEN_EX + str(t6) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t7 == 0:
        t7 = "  "
    elif t7 != 0 and t7 < 10:
        t7 = Fore.LIGHTGREEN_EX + str(t7) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t7 >= 10:
        t7 = Fore.LIGHTGREEN_EX + str(t7) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t8 == 0:
        t8 = "  "
    elif t8 != 0 and t8 < 10:
        t8 = Fore.LIGHTGREEN_EX + str(t8) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t8 >= 10:
        t8 = Fore.LIGHTGREEN_EX + str(t8) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t9 == 0:
        t9 = "  "
    elif t9 != 0 and t9 < 10:
        t9 = Fore.LIGHTGREEN_EX + str(t9) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t9 >= 10:
        t9 = Fore.LIGHTGREEN_EX + str(t9) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t10 == 0:
        t10 = "   "
    elif t10 != 0 and t10 < 10:
        t10 = Fore.LIGHTGREEN_EX + str(t10) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t10 >= 10:
        t10 = Fore.LIGHTGREEN_EX + str(t10) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t11 == 0:
        t11 = "   "
    elif t11 != 0 and t11 < 10:
        t11 = Fore.LIGHTGREEN_EX + str(t11) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t11 >= 10:
        t11 = Fore.LIGHTGREEN_EX + str(t11) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t12 == 0:
        t12 = "   "
    elif t12 != 0 and t12 < 10:
        t12 = Fore.LIGHTGREEN_EX + str(t12) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t12 >= 10:
        t12 = Fore.LIGHTGREEN_EX + str(t12) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t13 == 0:
        t13 = "   "
    elif t13 != 0 and t13 < 10:
        t13 = Fore.LIGHTGREEN_EX + str(t13) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t13 >= 10:
        t13 = Fore.LIGHTGREEN_EX + str(t13) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t14 == 0:
        t14 = "   "
    elif t14 != 0 and t14 < 10:
        t14 = Fore.LIGHTGREEN_EX + str(t14) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t14 >= 10:
        t14 = Fore.LIGHTGREEN_EX + str(t14) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t15 == 0:
        t15 = "   "
    elif t15 != 0 and t15 < 10:
        t15 = Fore.LIGHTGREEN_EX + str(t15) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t15 >= 10:
        t15 = Fore.LIGHTGREEN_EX + str(t15) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t16 == 0:
        t16 = "   "
    elif t16 != 0 and t16 < 10:
        t16 = Fore.LIGHTGREEN_EX + str(t16) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t16 >= 10:
        t16 = Fore.LIGHTGREEN_EX + str(t16) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if hh == 0:
        hh = "  "
    elif hh != 0 and hh < 10:
        hh = Fore.LIGHTGREEN_EX + str(hh) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif hh >= 10:
        hh = Fore.LIGHTGREEN_EX + str(hh) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t17 == 0:
        t17 = "  "
    elif t17 != 0 and t17 < 10:
        t17 = Fore.LIGHTGREEN_EX + str(t17) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t17 >= 10:
        t17 = Fore.LIGHTGREEN_EX + str(t17) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t18 == 0:
        t18 = "  "
    elif t18 != 0 and t18 < 10:
        t18 = Fore.LIGHTGREEN_EX + str(t18) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t18 >= 10:
        t18 = Fore.LIGHTGREEN_EX + str(t18) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t19 == 0:
        t19 = "  "
    elif t19 != 0 and t19 < 10:
        t19 = Fore.LIGHTGREEN_EX + str(t19) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t19 >= 10:
        t19 = Fore.LIGHTGREEN_EX + str(t19) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if jj == 0:
        jj = "  "
    elif jj != 0 and jj < 10:
        jj = Fore.LIGHTGREEN_EX + str(jj) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif jj >= 10:
        jj = Fore.LIGHTGREEN_EX + str(jj) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t21 == 0:
        t21 = "  "
    elif t21 != 0 and t21 < 10:
        t21 = Fore.LIGHTGREEN_EX + str(t21) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t21 >= 10:
        t21 = Fore.LIGHTGREEN_EX + str(t21) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AD == 0:
        AD = "  "
    elif AD != 0 and AD < 10:
        AD = Fore.LIGHTGREEN_EX + str(AD) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AD >= 10:
        AD = Fore.LIGHTGREEN_EX + str(AD) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if ww == 0:
        ww = "  "
    elif ww != 0 and ww < 10:
        ww = Fore.LIGHTGREEN_EX + str(ww) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif ww >= 10:
        ww = Fore.LIGHTGREEN_EX + str(ww) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if nn == 0:
        nn = "  "
    elif nn != 0 and nn < 10:
        nn = Fore.LIGHTGREEN_EX + str(nn) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif nn >= 10:
        nn = Fore.LIGHTGREEN_EX + str(nn) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if ss == 0:
        ss = "  "
    elif ss != 0 and ss < 10:
        ss = Fore.LIGHTGREEN_EX + str(ss) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif ss >= 10:
        ss = Fore.LIGHTGREEN_EX + str(ss) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if mm == 0:
        mm = "  "
    elif mm != 0 and mm < 10:
        mm = Fore.LIGHTGREEN_EX + str(mm) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif mm >= 10:
        mm = Fore.LIGHTGREEN_EX + str(mm) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t27 == 0:
        t27 = "   "
    elif t27 != 0 and t27 < 10:
        t27 = Fore.LIGHTGREEN_EX + str(t27) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t27 >= 10:
        t27 = Fore.LIGHTGREEN_EX + str(t27) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if rr == 0:
        rr = "  "
    elif rr != 0 and rr < 10:
        rr = Fore.LIGHTGREEN_EX + str(rr) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif rr >= 10:
        rr = Fore.LIGHTGREEN_EX + str(rr) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if uu == 0:
        uu = "  "
    elif uu != 0 and uu < 10:
        uu = Fore.LIGHTGREEN_EX + str(uu) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif uu >= 10:
        uu = Fore.LIGHTGREEN_EX + str(uu) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if pp == 0:
        pp = "  "
    elif pp != 0 and pp < 10:
        pp = Fore.LIGHTGREEN_EX + str(pp) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif pp >= 10:
        pp = Fore.LIGHTGREEN_EX + str(pp) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if qq == 0:
        qq = "  "
    elif qq != 0 and qq < 10:
        qq = Fore.LIGHTGREEN_EX + str(qq) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif qq >= 10:
        qq = Fore.LIGHTGREEN_EX + str(qq) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AA == 0:
        AA = "  "
    elif AA != 0 and AA < 10:
        AA = Fore.LIGHTGREEN_EX + str(AA) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AA >= 10:
        AA = Fore.LIGHTGREEN_EX + str(AA) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if zz == 0:
        zz = "  "
    elif zz != 0 and zz < 10:
        zz = Fore.LIGHTGREEN_EX + str(zz) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif zz >= 10:
        zz = Fore.LIGHTGREEN_EX + str(zz) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t34 == 0:
        t34 = "   "
    elif t34 != 0 and t34 < 10:
        t34 = Fore.LIGHTGREEN_EX + str(t34) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t34 >= 10:
        t34 = Fore.LIGHTGREEN_EX + str(t34) + " "   + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if tt == 0:
        tt = "  "
    elif tt != 0 and tt < 10:
        tt = Fore.LIGHTGREEN_EX + str(tt) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif tt >= 10:
        tt = Fore.LIGHTGREEN_EX + str(tt) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AE == 0:
        AE = "  "
    elif AE != 0 and AE < 10:
        AE = Fore.LIGHTGREEN_EX + str(AE) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AE >= 10:
        AE = Fore.LIGHTGREEN_EX + str(AE) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if ii == 0:
        ii = "  "
    elif ii != 0 and ii < 10:
        ii = Fore.LIGHTGREEN_EX + str(ii) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif ii >= 10:
        ii = Fore.LIGHTGREEN_EX + str(ii) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if yy == 0:
        yy = "  "
    elif yy != 0 and yy < 10:
        yy = Fore.LIGHTGREEN_EX + str(yy) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif yy >= 10:
        yy = Fore.LIGHTGREEN_EX + str(yy) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AF == 0:
        AF = "  "
    elif AF != 0 and AF < 10:
        AF = Fore.LIGHTGREEN_EX + str(AF) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AF >= 10:
        AF = Fore.LIGHTGREEN_EX + str(AF) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t40 == 0:
        t40 = "   "
    elif t40 != 0 and t40 < 10:
        t40 = Fore.LIGHTGREEN_EX + str(t40) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t40 >= 10:
        t40 = Fore.LIGHTGREEN_EX + str(t40) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t41 == 0:
        t41 = "   "
    elif t41 != 0 and t41 < 10:
        t41 = Fore.LIGHTGREEN_EX + str(t41) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t41 >= 10:
        t41 = Fore.LIGHTGREEN_EX + str(t41) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AC == 0:
        AC = "  "
    elif AC != 0 and AC < 10:
        AC = Fore.LIGHTGREEN_EX + str(AC) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AC >= 10:
        AC = Fore.LIGHTGREEN_EX + str(AC) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if vv == 0:
        vv = "  "
    elif vv != 0 and vv < 10:
        vv = Fore.LIGHTGREEN_EX + str(vv) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif vv >= 10:
        vv = Fore.LIGHTGREEN_EX + str(vv) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if oo == 0:
        oo = "  "
    elif oo != 0 and oo < 10:
        oo = Fore.LIGHTGREEN_EX + str(oo) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif oo >= 10:
        oo = Fore.LIGHTGREEN_EX + str(oo) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AB == 0:
        AB = "  "
    elif AB != 0 and AB < 10:
        AB = Fore.LIGHTGREEN_EX + str(AB) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AB >= 10:
        AB = Fore.LIGHTGREEN_EX + str(AB) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if xx == 0:
        xx = "  "
    elif xx != 0 and xx < 10:
        xx = Fore.LIGHTGREEN_EX + str(xx) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif xx >= 10:
        xx = Fore.LIGHTGREEN_EX + str(xx) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t47 == 0:
        t47 = "   "
    elif t47 != 0 and t47 < 10:
        t47 = Fore.LIGHTGREEN_EX + str(t47) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t47 >= 10:
        t47 = Fore.LIGHTGREEN_EX + str(t47) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AL == 0:
        AL = "  "
    elif AL != 0 and AL < 10:
        AL = Fore.LIGHTGREEN_EX + str(AL) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AL >= 10:
        AL = Fore.LIGHTGREEN_EX + str(AL) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AJ == 0:
        AJ = "  "
    elif AJ != 0 and AJ < 10:
        AJ = Fore.LIGHTGREEN_EX + str(AJ) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AJ >= 10:
        AJ = Fore.LIGHTGREEN_EX + str(AJ) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if WW == 0:
        WW = "  "
    elif WW != 0 and WW < 10:
        WW = Fore.LIGHTGREEN_EX + str(WW) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif WW >= 10:
        WW = Fore.LIGHTGREEN_EX + str(WW) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AK == 0:
        AK = "  "
    elif AK != 0 and AK < 10:
        AK = Fore.LIGHTGREEN_EX + str(AK) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AK >= 10:
        AK = Fore.LIGHTGREEN_EX + str(AK) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AG == 0:
        AG = "  "
    elif AG != 0 and AG < 10:
        AG = Fore.LIGHTGREEN_EX + str(AG) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AG >= 10:
        AG = Fore.LIGHTGREEN_EX + str(AG) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t53 == 0:
        t53 = "   "
    elif t53 != 0 and t53 < 10:
        t53 = Fore.LIGHTGREEN_EX + str(t53) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t53 >= 10:
        t53 = Fore.LIGHTGREEN_EX + str(t53) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AI == 0:
        AI = "  "
    elif AI != 0 and AI < 10:
        AI = Fore.LIGHTGREEN_EX + str(AI) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AI >= 10:
        AI = Fore.LIGHTGREEN_EX + str(AI) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AH == 0:
        AH = "  "
    elif AH != 0 and AH < 10:
        AH = Fore.LIGHTGREEN_EX + str(AH) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AH >= 10:
        AH = Fore.LIGHTGREEN_EX + str(AH) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t56 == 0:
        t56 = "   "
    elif t56 != 0 and t56 < 10:
        t56 = Fore.LIGHTGREEN_EX + str(t56) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t56 >= 10:
        t56 = Fore.LIGHTGREEN_EX + str(t56) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t57 == 0:
        t57 = "   "
    elif t57 != 0 and t57 < 10:
        t57 = Fore.LIGHTGREEN_EX + str(t57) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t57 >= 10:
        t57 = Fore.LIGHTGREEN_EX + str(t57) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t58 == 0:
        t58 = "   "
    elif t58 != 0 and t58 < 10:
        t58 = Fore.LIGHTGREEN_EX + str(t58) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t58 >= 10:
        t58 = Fore.LIGHTGREEN_EX + str(t58) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t59 == 0:
        t59 = "   "
    elif t59 != 0 and t59 < 10:
        t59 = Fore.LIGHTGREEN_EX + str(t59) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t59 >= 10:
        t59 = Fore.LIGHTGREEN_EX + str(t59) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t60 == 0:
        t60 = "   "
    elif t60 != 0 and t60 < 10:
        t60 = Fore.LIGHTGREEN_EX + str(t60) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t60 >= 10:
        t60 = Fore.LIGHTGREEN_EX + str(t60) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if ll == 0:
        ll = "  "
    elif ll != 0 and ll < 10:
        ll = Fore.LIGHTGREEN_EX + str(ll) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif ll >= 10:
        ll = Fore.LIGHTGREEN_EX + str(ll) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t62 == 0:
        t62 = "   "
    elif t62 != 0 and t62 < 10:
        t62 = Fore.LIGHTGREEN_EX + str(t62) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t62 >= 10:
        t62 = Fore.LIGHTGREEN_EX + str(t62) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if kk == 0:
        kk = "  "
    elif kk != 0 and kk < 10:
        kk = Fore.LIGHTGREEN_EX + str(kk) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif kk >= 10:
        kk = Fore.LIGHTGREEN_EX + str(kk) + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t64 == 0:
        t64 = "   "
    elif t64 != 0 and t64 < 10:
        t64 = Fore.LIGHTGREEN_EX + str(t64) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t64 >= 10:
        t64 = Fore.LIGHTGREEN_EX + str(t64) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t65 == 0:
        t65 = "   "
    elif t65 != 0 and t65 < 10:
        t65 = Fore.LIGHTGREEN_EX + str(t65) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t65 >= 10:
        t65 = Fore.LIGHTGREEN_EX + str(t65) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t66 == 0:
        t66 = "   "
    elif t66 != 0 and t66 < 10:
        t66 = Fore.LIGHTGREEN_EX + str(t66) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t66 >= 10:
        t66 = Fore.LIGHTGREEN_EX + str(t66) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t67 == 0:
        t67 = "   "
    elif t67 != 0 and t67 < 10:
        t67 = Fore.LIGHTGREEN_EX + str(t67) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t67 >= 10:
        t67 = Fore.LIGHTGREEN_EX + str(t67) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t68 == 0:
        t68 = "   "
    elif t68 != 0 and t68 < 10:
        t68 = Fore.LIGHTGREEN_EX + str(t68) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t68 >= 10:
        t68 = Fore.LIGHTGREEN_EX + str(t68) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t69 == 0:
        t69 = "   "
    elif t69 != 0 and t69 < 10:
        t69 = Fore.LIGHTGREEN_EX + str(t69) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t69 >= 10:
        t69 = Fore.LIGHTGREEN_EX + str(t69) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t70 == 0:
        t70 = "   "
    elif t70 != 0 and t70 < 10:
        t70 = Fore.LIGHTGREEN_EX + str(t70) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t70 >= 10:
        t70 = Fore.LIGHTGREEN_EX + str(t70) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t71 == 0:
        t71 = "   "
    elif t71 != 0 and t71 < 10:
        t71 = Fore.LIGHTGREEN_EX + str(t71) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t71 >= 10:
        t71 = Fore.LIGHTGREEN_EX + str(t71) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t72 == 0:
        t72 = "   "
    elif t72 != 0 and t72 < 10:
        t72 = Fore.LIGHTGREEN_EX + str(t72) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t72 >= 10:
        t72 = Fore.LIGHTGREEN_EX + str(t72) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t73 == 0:
        t73 = "   "
    elif t73 != 0 and t73 < 10:
        t73 = Fore.LIGHTGREEN_EX + str(t73) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t73 >= 10:
        t73 = Fore.LIGHTGREEN_EX + str(t73) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t74 == 0:
        t74 = "   "
    elif t74 != 0 and t74 < 10:
        t74 = Fore.LIGHTGREEN_EX + str(t74) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t74 >= 10:
        t74 = Fore.LIGHTGREEN_EX + str(t74) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t75 == 0:
        t75 = "   "
    elif t75 != 0 and t75 < 10:
        t75 = Fore.LIGHTGREEN_EX + str(t75) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t75 >= 10:
        t75 = Fore.LIGHTGREEN_EX + str(t75) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t76 == 0:
        t76 = "   "
    elif t76 != 0 and t76 < 10:
        t76 = Fore.LIGHTGREEN_EX + str(t76) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t76 >= 10:
        t76 = Fore.LIGHTGREEN_EX + str(t76) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t77 == 0:
        t77 = "   "
    elif t77 != 0 and t77 < 10:
        t77 = Fore.LIGHTGREEN_EX + str(t77) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t77 >= 10:
        t77 = Fore.LIGHTGREEN_EX + str(t77) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t78 == 0:
        t78 = "   "
    elif t78 != 0 and t78 < 10:
        t78 = Fore.LIGHTGREEN_EX + str(t78) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t78 >= 10:
        t78 = Fore.LIGHTGREEN_EX + str(t78) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t79 == 0:
        t79 = "   "
    elif t79 != 0 and t79 < 10:
        t79 = Fore.LIGHTGREEN_EX + str(t79) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t79 >= 10:
        t79 = Fore.LIGHTGREEN_EX + str(t79) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t80 == 0:
        t80 = "   "
    elif t80 != 0 and t80 < 10:
        t80 = Fore.LIGHTGREEN_EX + str(t80) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t80 >= 10:
        t80 = Fore.LIGHTGREEN_EX + str(t80) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t81 == 0:
        t81 = "   "
    elif t81 != 0 and t81 < 10:
        t81 = Fore.LIGHTGREEN_EX + str(t81) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t81 >= 10:
        t81 = Fore.LIGHTGREEN_EX + str(t81) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t82 == 0:
        t82 = "   "
    elif t82 != 0 and t82 < 10:
        t82 = Fore.LIGHTGREEN_EX + str(t82) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t82 >= 10:
        t82 = Fore.LIGHTGREEN_EX + str(t82) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t83 == 0:
        t83 = "   "
    elif t83 != 0 and t83 < 10:
        t83 = Fore.LIGHTGREEN_EX + str(t83) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t83 >= 10:
        t83 = Fore.LIGHTGREEN_EX + str(t83) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t84 == 0:
        t84 = "   "
    elif t84 != 0 and t84 < 10:
        t84 = Fore.LIGHTGREEN_EX + str(t84) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t84 >= 10:
        t84 = Fore.LIGHTGREEN_EX + str(t84) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t85 == 0:
        t85 = "   "
    elif t85 != 0 and t85 < 10:
        t85 = Fore.LIGHTGREEN_EX + str(t85) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t85 >= 10:
        t85 = Fore.LIGHTGREEN_EX + str(t85) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t86 == 0:
        t86 = "   "
    elif t86 != 0 and t86 < 10:
        t86 = Fore.LIGHTGREEN_EX + str(t86) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t86 >= 10:
        t86 = Fore.LIGHTGREEN_EX + str(t86) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if LL == 0:
        LL = "  "
    elif LL != 0 and LL < 10:
        LL = Fore.LIGHTGREEN_EX + str(LL) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif LL >= 10:
        LL = Fore.LIGHTGREEN_EX + str(LL) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if KK == 0:
        KK = "  "
    elif KK != 0 and KK < 10:
        KK = Fore.LIGHTGREEN_EX + str(KK) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif KK >= 10:
        KK = Fore.LIGHTGREEN_EX + str(KK) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if JJ == 0:
        JJ = "  "
    elif JJ != 0 and JJ < 10:
        JJ = Fore.LIGHTGREEN_EX + str(JJ) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif JJ >= 10:
        JJ = Fore.LIGHTGREEN_EX + str(JJ) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if II == 0:
        II = "  "
    elif II != 0 and II < 10:
        II = Fore.LIGHTGREEN_EX + str(II) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif II >= 10:
        II = Fore.LIGHTGREEN_EX + str(II) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if HH == 0:
        HH = "  "
    elif HH != 0 and HH < 10:
        HH = Fore.LIGHTGREEN_EX + str(HH) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif HH >= 10:
        HH = Fore.LIGHTGREEN_EX + str(HH) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t92 == 0:
        t92 = "   "
    elif t92 != 0 and t92 < 10:
        t92 = Fore.LIGHTGREEN_EX + str(t92) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t92 >= 10:
        t92 = Fore.LIGHTGREEN_EX + str(t92) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t93 == 0:
        t93 = "   "
    elif t93 != 0 and t93 < 10:
        t93 = Fore.LIGHTGREEN_EX + str(t93) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t93 >= 10:
        t93 = Fore.LIGHTGREEN_EX + str(t93) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t94 == 0:
        t94 = "   "
    elif t94 != 0 and t94 < 10:
        t94 = Fore.LIGHTGREEN_EX + str(t94) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t94 >= 10:
        t94 = Fore.LIGHTGREEN_EX + str(t94) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t95 == 0:
        t95 = "   "
    elif t95 != 0 and t95 < 10:
        t95 = Fore.LIGHTGREEN_EX + str(t95) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t95 >= 10:
        t95 = Fore.LIGHTGREEN_EX + str(t95) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t96 == 0:
        t96 = "   "
    elif t96 != 0 and t96 < 10:
        t96 = Fore.LIGHTGREEN_EX + str(t96) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t96 >= 10:
        t96 = Fore.LIGHTGREEN_EX + str(t96) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t97 == 0:
        t97 = "   "
    elif t97 != 0 and t97 < 10:
        t97 = Fore.LIGHTGREEN_EX + str(t97) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t97 >= 10:
        t97 = Fore.LIGHTGREEN_EX + str(t97) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t98 == 0:
        t98 = "   "
    elif t98 != 0 and t98 < 10:
        t98 = Fore.LIGHTGREEN_EX + str(t98) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t98 >= 10:
        t98 = Fore.LIGHTGREEN_EX + str(t98) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t99 == 0:
        t99 = "   "
    elif t99 != 0 and t99 < 10:
        t99 = Fore.LIGHTGREEN_EX + str(t99) + "  " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t99 >= 10:
        t99 = Fore.LIGHTGREEN_EX + str(t99) + " "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t100 == 0:
        t100 = "    "
    elif t100 != 0 and t100 < 10:
        t100 = Fore.LIGHTGREEN_EX + str(t100) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t100 >= 10:
        t100 = Fore.LIGHTGREEN_EX + str(t100) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t101 == 0:
        t101 = "    "
    elif t101 != 0 and t101 < 10:
        t101 = Fore.LIGHTGREEN_EX + str(t101) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t101 >= 10:
        t101 = Fore.LIGHTGREEN_EX + str(t101) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t102 == 0:
        t102 = "    "
    elif t102 != 0 and t102 < 10:
        t102 = Fore.LIGHTGREEN_EX + str(t102) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t102 >= 10:
        t102 = Fore.LIGHTGREEN_EX + str(t102) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t103 == 0:
        t103 = "    "
    elif t103 != 0 and t103 < 10:
        t103 = Fore.LIGHTGREEN_EX + str(t103) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t103 >= 10:
        t103 = Fore.LIGHTGREEN_EX + str(t103) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t104 == 0:
        t104 = "    "
    elif t104 != 0 and t104 < 10:
        t104 = Fore.LIGHTGREEN_EX + str(t104) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t104 >= 10:
        t104 = Fore.LIGHTGREEN_EX + str(t104) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t105 == 0:
        t105 = "    "
    elif t105 != 0 and t105 < 10:
        t105 = Fore.LIGHTGREEN_EX + str(t105) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t105 >= 10:
        t105 = Fore.LIGHTGREEN_EX + str(t105) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t106 == 0:
        t106 = "    "
    elif t106 != 0 and t106 < 10:
        t106 = Fore.LIGHTGREEN_EX + str(t106) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t106 >= 10:
        t106 = Fore.LIGHTGREEN_EX + str(t106) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t107 == 0:
        t107 = "    "
    elif t107 != 0 and t107 < 10:
        t107 = Fore.LIGHTGREEN_EX + str(t107) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t107 >= 10:
        t107 = Fore.LIGHTGREEN_EX + str(t107) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t108 == 0:
        t108 = "    "
    elif t108 != 0 and t108 < 10:
        t108 = Fore.LIGHTGREEN_EX + str(t108) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t108 >= 10:
        t108 = Fore.LIGHTGREEN_EX + str(t108) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if GG == 0:
        GG = "  "
    elif GG != 0 and GG < 10:
        GG = Fore.LIGHTGREEN_EX + str(GG) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif GG >= 10:
        GG = Fore.LIGHTGREEN_EX + str(GG) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t110 == 0:
        t110 = "    "
    elif t110 != 0 and t110 < 10:
        t110 = Fore.LIGHTGREEN_EX + str(t110) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t110 >= 10:
        t110 = Fore.LIGHTGREEN_EX + str(t110) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t111 == 0:
        t111 = "    "
    elif t111 != 0 and t111 < 10:
        t111 = Fore.LIGHTGREEN_EX + str(t111) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t111 >= 10:
        t111 = Fore.LIGHTGREEN_EX + str(t111) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if FF == 0:
        FF = "  "
    elif FF != 0 and FF < 10:
        FF = Fore.LIGHTGREEN_EX + str(FF) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif FF >= 10:
        FF = Fore.LIGHTGREEN_EX + str(FF) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if DD == 0:
        DD = "  "
    elif DD != 0 and DD < 10:
        DD = Fore.LIGHTGREEN_EX + str(DD) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif DD >= 10:
        DD = Fore.LIGHTGREEN_EX + str(DD) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if EE == 0:
        EE = "  "
    elif EE != 0 and EE < 10:
        EE = Fore.LIGHTGREEN_EX + str(EE) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif EE >= 10:
        EE = Fore.LIGHTGREEN_EX + str(EE) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if CC == 0:
        CC = "  "
    elif CC != 0 and CC < 10:
        CC = Fore.LIGHTGREEN_EX + str(CC) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif CC >= 10:
        CC = Fore.LIGHTGREEN_EX + str(CC) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if BB == 0:
        BB = "  "
    elif BB != 0 and BB < 10:
        BB = Fore.LIGHTGREEN_EX + str(BB) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif BB >= 10:
        BB = Fore.LIGHTGREEN_EX + str(BB) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if AX == 0:
        AX = "  "
    elif AX != 0 and AX < 10:
        AX = Fore.LIGHTGREEN_EX + str(AX) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif AX >= 10:
        AX = Fore.LIGHTGREEN_EX + str(AX) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t118 == 0:
        t118 = "    "
    elif t118 != 0 and t118 < 10:
        t118 = Fore.LIGHTGREEN_EX + str(t118) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t118 >= 10:
        t118 = Fore.LIGHTGREEN_EX + str(t118) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t119 == 0:
        t119 = "    "
    elif t119 != 0 and t119 < 10:
        t119 = Fore.LIGHTGREEN_EX + str(t119) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t119 >= 10:
        t119 = Fore.LIGHTGREEN_EX + str(t119) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t120 == 0:
        t120 = "    "
    elif t120 != 0 and t120 < 10:
        t120 = Fore.LIGHTGREEN_EX + str(t120) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t120 >= 10:
        t120 = Fore.LIGHTGREEN_EX + str(t120) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t121 == 0:
        t121 = "    "
    elif t121 != 0 and t121 < 10:
        t121 = Fore.LIGHTGREEN_EX + str(t121) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t121 >= 10:
        t121 = Fore.LIGHTGREEN_EX + str(t121) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t122 == 0:
        t122 = "    "
    elif t122 != 0 and t122 < 10:
        t122 = Fore.LIGHTGREEN_EX + str(t122) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t122 >= 10:
        t122 = Fore.LIGHTGREEN_EX + str(t122) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t123 == 0:
        t123 = "    "
    elif t123 != 0 and t123 < 10:
        t123 = Fore.LIGHTGREEN_EX + str(t123) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t123 >= 10:
        t123 = Fore.LIGHTGREEN_EX + str(t123) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t124 == 0:
        t124 = "    "
    elif t124 != 0 and t124 < 10:
        t124 = Fore.LIGHTGREEN_EX + str(t124) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t124 >= 10:
        t124 = Fore.LIGHTGREEN_EX + str(t124) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t125 == 0:
        t125 = "    "
    elif t125 != 0 and t125 < 10:
        t125 = Fore.LIGHTGREEN_EX + str(t125) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t125 >= 10:
        t125 = Fore.LIGHTGREEN_EX + str(t125) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t126 == 0:
        t126 = "    "
    elif t126 != 0 and t126 < 10:
        t126 = Fore.LIGHTGREEN_EX + str(t126) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t126 >= 10:
        t126 = Fore.LIGHTGREEN_EX + str(t126) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t127 == 0:
        t127 = "    "
    elif t127 != 0 and t127 < 10:
        t127 = Fore.LIGHTGREEN_EX + str(t127) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t127 >= 10:
        t127 = Fore.LIGHTGREEN_EX + str(t127) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t128 == 0:
        t128 = "    "
    elif t128 != 0 and t128 < 10:
        t128 = Fore.LIGHTGREEN_EX + str(t128) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t128 >= 10:
        t128 = Fore.LIGHTGREEN_EX + str(t128) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t129 == 0:
        t129 = "    "
    elif t129 != 0 and t129 < 10:
        t129 = Fore.LIGHTGREEN_EX + str(t129) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t129 >= 10:
        t129 = Fore.LIGHTGREEN_EX + str(t129) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t130 == 0:
        t130 = "    "
    elif t130 != 0 and t130 < 10:
        t130 = Fore.LIGHTGREEN_EX + str(t130) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t130 >= 10:
        t130 = Fore.LIGHTGREEN_EX + str(t130) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t131 == 0:
        t131 = "    "
    elif t131 != 0 and t131 < 10:
        t131 = Fore.LIGHTGREEN_EX + str(t131) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t131 >= 10:
        t131 = Fore.LIGHTGREEN_EX + str(t131) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t132 == 0:
        t132 = "    "
    elif t132 != 0 and t132 < 10:
        t132 = Fore.LIGHTGREEN_EX + str(t132) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t132 >= 10:
        t132 = Fore.LIGHTGREEN_EX + str(t132) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t133 == 0:
        t133 = "    "
    elif t133 != 0 and t133 < 10:
        t133 = Fore.LIGHTGREEN_EX + str(t133) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t133 >= 10:
        t133 = Fore.LIGHTGREEN_EX + str(t133) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t134 == 0:
        t134 = "    "
    elif t134 != 0 and t134 < 10:
        t134 = Fore.LIGHTGREEN_EX + str(t134) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t134 >= 10:
        t134 = Fore.LIGHTGREEN_EX + str(t134) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t135 == 0:
        t135 = "    "
    elif t135 != 0 and t135 < 10:
        t135 = Fore.LIGHTGREEN_EX + str(t135) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t135 >= 10:
        t135 = Fore.LIGHTGREEN_EX + str(t135) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t136 == 0:
        t136 = "    "
    elif t136 != 0 and t136 < 10:
        t136 = Fore.LIGHTGREEN_EX + str(t136) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t136 >= 10:
        t136 = Fore.LIGHTGREEN_EX + str(t136) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if XX == 0:
        XX = "  "
    elif XX != 0 and XX < 10:
        XX = Fore.LIGHTGREEN_EX + str(XX) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif XX >= 10:
        XX = Fore.LIGHTGREEN_EX + str(XX) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if YY == 0:
        YY = "  "
    elif YY != 0 and YY < 10:
        YY = Fore.LIGHTGREEN_EX + str(YY) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif YY >= 10:
        YY = Fore.LIGHTGREEN_EX + str(YY) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t139 == 0:
        t139 = "    "
    elif t139 != 0 and t139 < 10:
        t139 = Fore.LIGHTGREEN_EX + str(t139) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t139 >= 10:
        t139 = Fore.LIGHTGREEN_EX + str(t139) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t140 == 0:
        t140 = "    "
    elif t140 != 0 and t140 < 10:
        t140 = Fore.LIGHTGREEN_EX + str(t140) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t140 >= 10:
        t140 = Fore.LIGHTGREEN_EX + str(t140) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if SS == 0:
        SS = "  "
    elif SS != 0 and SS < 10:
        SS = Fore.LIGHTGREEN_EX + str(SS) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif SS >= 10:
        SS = Fore.LIGHTGREEN_EX + str(SS) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if RR == 0:
        RR = "  "
    elif RR != 0 and RR < 10:
        RR = Fore.LIGHTGREEN_EX + str(RR) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif RR >= 10:
        RR = Fore.LIGHTGREEN_EX + str(RR) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if QQ == 0:
        QQ = "  "
    elif QQ != 0 and QQ < 10:
        QQ = Fore.LIGHTGREEN_EX + str(QQ) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif QQ >= 10:
        QQ = Fore.LIGHTGREEN_EX + str(QQ) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if PP == 0:
        PP = "  "
    elif PP != 0 and PP < 10:
        PP = Fore.LIGHTGREEN_EX + str(PP) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif PP >= 10:
        PP = Fore.LIGHTGREEN_EX + str(PP) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if OO == 0:
        OO = "  "
    elif OO != 0 and OO < 10:
        OO = Fore.LIGHTGREEN_EX + str(OO) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif OO >= 10:
        OO = Fore.LIGHTGREEN_EX + str(OO) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t146 == 0:
        t146 = "    "
    elif t146 != 0 and t146 < 10:
        t146 = Fore.LIGHTGREEN_EX + str(t146) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t146 >= 10:
        t146 = Fore.LIGHTGREEN_EX + str(t146) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t147 == 0:
        t147 = "    "
    elif t147 != 0 and t147 < 10:
        t147 = Fore.LIGHTGREEN_EX + str(t147) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t147 >= 10:
        t147 = Fore.LIGHTGREEN_EX + str(t147) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t148 == 0:
        t148 = "    "
    elif t148 != 0 and t148 < 10:
        t148 = Fore.LIGHTGREEN_EX + str(t148) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t148 >= 10:
        t148 = Fore.LIGHTGREEN_EX + str(t148) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if MM == 0:
        MM = "  "
    elif MM != 0 and MM < 10:
        MM = Fore.LIGHTGREEN_EX + str(MM) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif MM >= 10:
        MM = Fore.LIGHTGREEN_EX + str(MM) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t150 == 0:
        t150 = "    "
    elif t150 != 0 and t150 < 10:
        t150 = Fore.LIGHTGREEN_EX + str(t150) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t150 >= 10:
        t150 = Fore.LIGHTGREEN_EX + str(t150) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if TT == 0:
        TT = "  "
    elif TT != 0 and TT < 10:
        TT = Fore.LIGHTGREEN_EX + str(TT) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif TT >= 10:
        TT = Fore.LIGHTGREEN_EX + str(TT) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t151 == 0:
        t151 = "    "
    elif t151 != 0 and t151 < 10:
        t151 = Fore.LIGHTGREEN_EX + str(t151) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t151 >= 10:
        t151 = Fore.LIGHTGREEN_EX + str(t151) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t153 == 0:
        t153 = "    "
    elif t153 != 0 and t153 < 10:
        t153 = Fore.LIGHTGREEN_EX + str(t153) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t153 >= 10:
        t153 = Fore.LIGHTGREEN_EX + str(t153) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if VV == 0:
        VV = "  "
    elif VV != 0 and VV < 10:
        VV = Fore.LIGHTGREEN_EX + str(VV) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif VV >= 10:
        VV = Fore.LIGHTGREEN_EX + str(VV) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if UU == 0:
        UU = "  "
    elif UU != 0 and UU < 10:
        UU = Fore.LIGHTGREEN_EX + str(UU) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif UU >= 10:
        UU = Fore.LIGHTGREEN_EX + str(UU) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t155 == 0:
        t155 = "    "
    elif t155 != 0 and t155 < 10:
        t155 = Fore.LIGHTGREEN_EX + str(t155) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t155 >= 10:
        t155 = Fore.LIGHTGREEN_EX + str(t155) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if ZZ == 0:
        ZZ = "  "
    elif ZZ != 0 and ZZ < 10:
        ZZ = Fore.LIGHTGREEN_EX + str(ZZ) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif ZZ >= 10:
        ZZ = Fore.LIGHTGREEN_EX + str(ZZ) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if aa == 0:
        aa = "  "
    elif aa != 0 and aa < 10:
        aa = Fore.LIGHTGREEN_EX + str(aa) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif aa >= 10:
        aa = Fore.LIGHTGREEN_EX + str(aa) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if bb == 0:
        bb = "  "
    elif bb != 0 and bb < 10:
        bb = Fore.LIGHTGREEN_EX + str(bb) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif bb >= 10:
        bb = Fore.LIGHTGREEN_EX + str(bb) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if cc == 0:
        cc = "  "
    elif cc != 0 and cc < 10:
        cc = Fore.LIGHTGREEN_EX + str(cc) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif cc >= 10:
        cc = Fore.LIGHTGREEN_EX + str(cc) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if NN == 0:
        NN = "  "
    elif NN != 0 and NN < 10:
        NN = Fore.LIGHTGREEN_EX + str(NN) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif NN >= 10:
        NN = Fore.LIGHTGREEN_EX + str(NN) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t161 == 0:
        t161 = "    "
    elif t161 != 0 and t161 < 10:
        t161 = Fore.LIGHTGREEN_EX + str(t161) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t161 >= 10:
        t161 = Fore.LIGHTGREEN_EX + str(t161) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t162 == 0:
        t162 = "    "
    elif t162 != 0 and t162 < 10:
        t162 = Fore.LIGHTGREEN_EX + str(t162) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t162 >= 10:
        t162 = Fore.LIGHTGREEN_EX + str(t162) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t163 == 0:
        t163 = "    "
    elif t163 != 0 and t163 < 10:
        t163 = Fore.LIGHTGREEN_EX + str(t163) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t163 >= 10:
        t163 = Fore.LIGHTGREEN_EX + str(t163) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t164 == 0:
        t164 = "    "
    elif t164 != 0 and t164 < 10:
        t164 = Fore.LIGHTGREEN_EX + str(t164) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t164 >= 10:
        t164 = Fore.LIGHTGREEN_EX + str(t164) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t165 == 0:
        t165 = "    "
    elif t165 != 0 and t165 < 10:
        t165 = Fore.LIGHTGREEN_EX + str(t165) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t165 >= 10:
        t165 = Fore.LIGHTGREEN_EX + str(t165) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t166 == 0:
        t166 = "    "
    elif t166 != 0 and t166 < 10:
        t166 = Fore.LIGHTGREEN_EX + str(t166) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t166 >= 10:
        t166 = Fore.LIGHTGREEN_EX + str(t166) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t167 == 0:
        t167 = "    "
    elif t167 != 0 and t167 < 10:
        t167 = Fore.LIGHTGREEN_EX + str(t167) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t167 >= 10:
        t167 = Fore.LIGHTGREEN_EX + str(t167) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t168 == 0:
        t168 = "    "
    elif t168 != 0 and t168 < 10:
        t168 = Fore.LIGHTGREEN_EX + str(t168) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t168 >= 10:
        t168 = Fore.LIGHTGREEN_EX + str(t168) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if gg == 0:
        gg = "  "
    elif gg != 0 and gg < 10:
        gg = Fore.LIGHTGREEN_EX + str(gg) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif gg >= 10:
        gg = Fore.LIGHTGREEN_EX + str(gg) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t170 == 0:
        t170 = "    "
    elif t170 != 0 and t170 < 10:
        t170 = Fore.LIGHTGREEN_EX + str(t170) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t170 >= 10:
        t170 = Fore.LIGHTGREEN_EX + str(t170) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t171 == 0:
        t171 = "    "
    elif t171 != 0 and t171 < 10:
        t171 = Fore.LIGHTGREEN_EX + str(t171) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t171 >= 10:
        t171 = Fore.LIGHTGREEN_EX + str(t171) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t172 == 0:
        t172 = "    "
    elif t172 != 0 and t172 < 10:
        t172 = Fore.LIGHTGREEN_EX + str(t172) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t172 >= 10:
        t172 = Fore.LIGHTGREEN_EX + str(t172) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t173 == 0:
        t173 = "    "
    elif t173 != 0 and t173 < 10:
        t173 = Fore.LIGHTGREEN_EX + str(t173) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t173 >= 10:
        t173 = Fore.LIGHTGREEN_EX + str(t173) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t174 == 0:
        t174 = "    "
    elif t174 != 0 and t174 < 10:
        t174 = Fore.LIGHTGREEN_EX + str(t174) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t174 >= 10:
        t174 = Fore.LIGHTGREEN_EX + str(t174) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t175 == 0:
        t175 = "    "
    elif t175 != 0 and t175 < 10:
        t175 = Fore.LIGHTGREEN_EX + str(t175) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t175 >= 10:
        t175 = Fore.LIGHTGREEN_EX + str(t175) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t176 == 0:
        t176 = "    "
    elif t176 != 0 and t176 < 10:
        t176 = Fore.LIGHTGREEN_EX + str(t176) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t176 >= 10:
        t176 = Fore.LIGHTGREEN_EX + str(t176) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t177 == 0:
        t177 = "    "
    elif t177 != 0 and t177 < 10:
        t177 = Fore.LIGHTGREEN_EX + str(t177) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t177 >= 10:
        t177 = Fore.LIGHTGREEN_EX + str(t177) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t178 == 0:
        t178 = "    "
    elif t178 != 0 and t178 < 10:
        t178 = Fore.LIGHTGREEN_EX + str(t178) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t178 >= 10:
        t178 = Fore.LIGHTGREEN_EX + str(t178) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t179 == 0:
        t179 = "    "
    elif t179 != 0 and t179 < 10:
        t179 = Fore.LIGHTGREEN_EX + str(t179) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t179 >= 10:
        t179 = Fore.LIGHTGREEN_EX + str(t179) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t180 == 0:
        t180 = "    "
    elif t180 != 0 and t180 < 10:
        t180 = Fore.LIGHTGREEN_EX + str(t180) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t180 >= 10:
        t180 = Fore.LIGHTGREEN_EX + str(t180) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if dd == 0:
        dd = "  "
    elif dd != 0 and dd < 10:
        dd = Fore.LIGHTGREEN_EX + str(dd) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif dd >= 10:
        dd = Fore.LIGHTGREEN_EX + str(dd) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if ff == 0:
        ff = "  "
    elif ff != 0 and ff < 10:
        ff = Fore.LIGHTGREEN_EX + str(ff) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif ff >= 10:
        ff = Fore.LIGHTGREEN_EX + str(ff) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if ee == 0:
        ee = "  "
    elif ee != 0 and ee < 10:
        ee = Fore.LIGHTGREEN_EX + str(ee) + " " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif ee >= 10:
        ee = Fore.LIGHTGREEN_EX + str(ee) +  Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t182 == 0:
        t182 = "    "
    elif t182 != 0 and t182 < 10:
        t182 = Fore.LIGHTGREEN_EX + str(t182) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t182 >= 10:
        t182 = Fore.LIGHTGREEN_EX + str(t182) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t184 == 0:
        t184 = "    "
    elif t184 != 0 and t184 < 10:
        t184 = Fore.LIGHTGREEN_EX + str(t184) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t184 >= 10:
        t184 = Fore.LIGHTGREEN_EX + str(t184) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t186 == 0:
        t186 = "    "
    elif t186 != 0 and t186 < 10:
        t186 = Fore.LIGHTGREEN_EX + str(t186) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t186 >= 10:
        t186 = Fore.LIGHTGREEN_EX + str(t186) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t187 == 0:
        t187 = "    "
    elif t187 != 0 and t187 < 10:
        t187 = Fore.LIGHTGREEN_EX + str(t187) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t187 >= 10:
        t187 = Fore.LIGHTGREEN_EX + str(t187) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if t188 == 0:
        t188 = "    "
    elif t188 != 0 and t188 < 10:
        t188 = Fore.LIGHTGREEN_EX + str(t188) + "   " + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    elif t188 >= 10:
        t188 = Fore.LIGHTGREEN_EX + str(t188) + "  "  + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    if "0" in c7:
        c7 = "  "
    else:
        c7 = Fore.LIGHTGREEN_EX + c7 + Style.RESET_ALL + Fore.LIGHTBLACK_EX
    pic = Fore.LIGHTBLACK_EX+"""          
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWX0KKkxkkONWWWWWNXOkd:'';ldxKWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0Kk:,:,...  'clo:,,;:,'.    ....;oxolo0XXXXXXXXXXXXXXXWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKx0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNNXNXWX0Kl..lc'.. .,;;oc.                  ..ck0NXXXXXXXXXX0oxxoooldKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNx:;oO0KWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXN0lkWKooOdxOl:o:. .:OKxc.                    .;OWXXXXXXXXXXXX0oo,.;clKXXXXXXXXXXXXXXXXXXXXWXXXXXXXXXXXN0OkccOWWWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKdloOk;c00dcx0x::c,..,xWXNOo;,;.                  .dWXXXXXXXXXXXXXXXKkXXKWXXXXXXXXXXXXXXXNOxxkONXXXXXXXWXKOxdxc..;;;dXXXXXXXXXXXKxxONNKXWXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXklcoOxlccoOo;xxlo:;c;c0XXXXXWNWWXc                 ,OWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo;cd0NWNKNXXXN0x;.        ..;x00XWWKKNXXKdoxKXOKWXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXK: ..,:coock0:'dold:,,.,:cOWXXXXXXX0'             .'lXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWo.oNXXXWo.lO00o,.          .......;;..oXXKKKxcoxxkXWXWXXXXXXXXXXNKNXXXXXXXXXX
                      XXXXXXXXWXOxdxkO0KXXWXXXNXKKKxdOx,     :0xol:OXl..... .;lOWXXXXXo'           .',dNXXXWKXXXXXXXXXXXXWNNNkocclkXWXXXXXWN0lx0K00O, ':,...                      .......     '::;:kKOO00xxkxxKXXXXXXXXXX
                      XXXXXXKxc'.    .....;cdd;...,,;lc,,::,;d0dl:.,xkc;dko:.  cXWXXXKo'        .'.'cOWXXXXXWWXXXXXXXXXXXXxlc.    ..:oON0k0kdoo:,..',..cc..                                        ..  ..   .':okXWXXXXXX
                      XXXXWKo,.                         .';..,,...  .;,cKKkk; .;,oNXXNc      ..'dXXNKkdxxxXXXXXXXXXXXXXXKc.   ..    ';cd:.'.          .,.                                                      .,,;cxNXXX
                      XXXXNd,'.                                    ';;oXWOo:. .:o0WXXWk.    c0XNWXXXXo"""+t27+"""cKXXXXXXXXXXNko,   .:l.    ,c,.                                                                       :OOdlkWXXX
                      XXXWKo,.                                   ,dK0kKWKooxdc:dXXXXXXWo.  :XXXXXXXXXWNKXWXXXXXXXXXKo,.    ;Ol  """+t40+"""                                                                 .''..    .:o0WXWXXXXX
                      XXXWx.    .'.;c;..            """+t1+"""         .dNXXXXXWd   ;0NKNXXXXXXN0olKXXXXXXXXXXXXXXXXXXXWNWX0'"""+qq+"""   """+rr+""" 'O0:..                        """+t162+"""                               ...''.cXKo,;odd0XXXXXXXXXXX
                      XXXXWOl'..dkkNXWXOl,.                    .dKNXXXXX:   .;:.cXXXXXXXXXXXXXXXXXXXXXXXXXXXWKol0XXWOccc;. cX0c"""+AJ+"""                                                           .dKXKXNKXNo..oNXXXXXXXXXXXXXX
                      XXWKkdddkkKXXXXXXXXNx.                    ..;oOXW0,       .oXXXXXXXXXXXXXXXXXXXXXXXXXWkx"""+ll+""":XXXXk:cxdlkO:"""+AK+"""                                                           .dNWWWXXXXX:  :XXXXXXXXXXXXXXX
                      XXNkdkXWXXXXXXXXXXXXWx.                       .oNc          ,kWXXXXXXXXXXXXXXXXXXXXXXO"""+ii+""".;"""+jj+"""XXd;"""+pp+""".,.. """+AL+"""  """+AI+"""                                                         .'cokNXXXXO,;0WXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXWo.                       ':.     ....''oWXXXXXXXXXXXXXXXXXXXXXXXOKkc,,;'"""+nn+"""    """+ss+"""        """+zz+"""                   """+t155+"""                                 .lckWXXXWXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXX0:.                             ..oKKd'.dWXXXXXXXXXXXXXXXXXXXXXXXWXd,. """+mm+oo+""" """+hh+""" """+tt+""" """+xx+"""  """+AH+"""  ..      .                                               .kKKWXXXXXXXXXXXXXXXXXXXXXX
  """+Style.RESET_ALL+Style.BRIGHT+"""    XXXXXXXXXXX     """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXX:                               .:dKX0kOWXXXXXXXXXXXXXXXXXXXXXXXWWX: """+t17+"""     """+t21+uu+""" """+yy+AE+""" ,l,;l'    ,do'   .lc                                      .dWKkKWXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   XXXXXXXXXXX    """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""   X           X    """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXWd.         """+t2+"""                 .lkkOXWXXXXXXXXXXXXXXXXXXXXXXXXXXNd;:c. .:lol:."""+vv+ww+WW+AX+AF+"""0Kxx0kc.  cKx,.  .,'                                   .;lOWWk; XXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X          X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXX:                           .cOWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK,  """+t19+""",kNXXkk..xco,"""+AB+"""c;,'..'::."""+t153+"""KO,    """+aa+"""                             .;,  """+t171+"""XXXk  XXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXNo.                         ;KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXK: """+t16+""",kK0Okxx0x."""+t18+"."+AC+"""."""+AD+""" """+t140+"""  """+UU+VV+"""k'  """+ZZ+"""       """+cc+"""                      .clkk  0WWNO;"""+t163+"""XXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXc.                       'OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNd,;;'....."""+t82+"""WWXX  N K0kd' """+RR+SS+"""  ..          """+bb+"""              """+t165+"""       .lNXk"""+t172+"""c   XXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X           X  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  XXXXXXXXXXXXXXX   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXNk'                   .;xKWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKc."""+t84+"""       .:okXk:cx0K0Oo."""+QQ+"""      """+t139+"""  """+YY+"""                               .kXWNKdxKWXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   XXXXXXXXXXXXX  """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXWd;,.        .,,':lc.,0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXc.                   """+t80+"""   """+OO+PP+"""  """+TT+""";.         """+XX+"""       """+dd+" "+ee+"""                :XXXXWWXXXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXNd:;.  """+t3+"""  ;0WNXWXXx'xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXo.       """+t83+"""      """+t81+"""       ;;.     .;ll:,.....             """+t178+"""             .dNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXXWxcl'    '0XXXXXXN0okXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNl"""+t85+"""                          cd. """+t147+NN+MM+"""':xKKOd'    """+t164+"""   .."""+t175+ff+"""      ..:xx0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
  """+Style.RESET_ALL+Style.BRIGHT+"""  X             X   """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""XXXXXXXXXXXXXXXXXXXXXXXXXXXWXXO'   .OXXXdxXX00kdkXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'   """+t86+"""                       .dx.       """+t150+"""WXXXKo:.      .l00c.      .::d0KNWXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""+Style.RESET_ALL+Style.BRIGHT+"""   X              """+Style.RESET_ALL+Fore.LIGHTBLACK_EX+"""
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWOc.  ,ll' cNXXXKloxoo0KNXXXXXXXXXXXXXXXXXXXXXXXXXXK,        """+t110+t118+t119+"""  """+t120+"""    .dk,      """+t151+"""XXXXXXK,    .cOWXXNl.."""+gg+"""  ;xkXXXXWOl0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXkoll'  ,lkNXWNWWWWWWWXXXXXXXXXXXXXXXXXXXXXXXXXWk."""+KK+LL+"""                          """+t92+"""l.."""+t148+"""XWXXXXXXXXWx.  :0WXXXXXXOc    """+t176+"""XXXWd,dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXOx, cNXXXNOxONXWWWXXXXXXXXXXXXXXXXXXXXXXXX0,"""+JJ+"""    """+DD+"""          """+t124+t121+"""      """+t122+"""OkkXXXXXXXXXXXXXXXXXXXXXXXXXWk.,"""+t177+"""lWXXXW0k"""+t170+"""XXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKc:dxkx;.  ':;,lXXXXXXXXXXXXXXXXXXXXXXXXXK:"""+II+HH+FF+EE+CC+BB+""" """+AA+"""                  ....:XXXXXXXXXXXXXXXXXXXXXXXXXXWxckkldXXXXW0OKxcoXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKkxl."""+t10+"""   """+t15+"""'oxONXXXXXXXXXXXXXXXXXXXXXNx,"""+GG+"""...,"""+cc+""".   """+t127+"""            """+t93+""" """+t95+"""KXXXXXXXXXXXXXXXXXXXXXXXXW00K:"""+t173+"""XXXNd:xXKxdXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWk.       """+t9+""" """+t13+""",kWXXXXXXXXXXXXXXXXXXXXXXxkKKXNXWKx:.."""+t97+t125+t111+""" """+t123+"""   .c0XXXXXXXXXXXXXXXXXXXXXXXXXW0xo:.,OWN0d, .dXNXNXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNd.               ,OKXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXWd.."""+t126+t96+t98+"""      """+t94+"""0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO,"""+t168+"""d.   ,oodO0k0XWXKXNXXXXXWNWXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO."""+t8+"""              ...':odONXXXXXXXXXXXXXXXXXXXXXXXXWkc'       """+t99+"""  """+t128+""",OWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0:.;OXd;,;xl.cKNXKXNd,',cokNXNkONXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO.                       .,kWXXXXXXXXXXXXXXXXXXXXXXXXXK;              .xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNkllodxkKN0x"""+t166+"""WWWXO; """+t74+""":OO0XXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx. """+t12+"""        """+t6+"""          cNXXXXXXXXXXXXXXXXXXXXXXXXXWd."""+t100+t129+t101+"""  oWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN0kdoxKXK0KNWXXWWXWOo:okccOWXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.                     .lXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'             """+t102+"""XW0KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWWNWWKo:lkWNddNWKKWXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.    """+t5+"""              cNXXXXXXXXXXXXXXXXXXXXXXXXXXXXc        """+t130+"""   ,KN0l.lWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWXd;:'   cKX:.dNXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKd;.                 oWXXXXXXXXXXXXXXXXXXXXXXXXXXX0'"""+t103+""" """+t132+"""    'o0Nd. 'OXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNx'        .,. '0WXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:    """+t11+"""         ,KXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.           ;KXXNl"""+t131+"""XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWNOo:,.              ,xNXXXXXXW0KXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWl             .:l0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWl           cNXXK; ;0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXc.         """+c7+"""        .oNXXXXXXNNXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN:"""+t7+"""          cXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.         cXWXXWKkXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;                     .kXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'           '0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo."""+t104+"""   cXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWo                     '0XXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.        """+t14+""" XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX:    .,xNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWx.   .,;cl:.         .dNXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXk.  """+t4+"""   .,lKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0loxkONXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWkclodONXXXW0d:.     ,OWXXXXXXXXXW00XXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNo        ;0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXo'..,oKXXXXXXXXXXXWd;dNX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNc     .cOXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxdKXXXXXXXXXXXW0xc:OWX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx.   .oXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXocKXXXXXXXXWXk"""+t72+"""XNXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'  .cXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWWXXXXXXXXXK:'dXWXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO.  .dWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXWKKWXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0,  ,0XXNKXWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXW0:.cKWXKk0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN0do0WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""
    print(clear)
    print("\n"*2)
    effect1.stop()
    effect1.play()
    print(pic)
    input("")
