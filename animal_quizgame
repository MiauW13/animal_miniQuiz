import sqlite3
from unittest import result
import data
from player import Player

# write your code here
print("Hello, Wellcome to My Animal Quiz..:)")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()
print("Let's Play!!!")

one = input("What is Your Name? ")

print("Ok, Lets strat our guessing animal picture...")
quiz = input ("type 'next' to start! ")
if quiz != "next":
    quit()

score = 0

quiz_1 = input(r"""
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
what is the name of this animal? """) 
if quiz_1 == "camel":
    print('**** Yeay, It is Correct **** ')
    score += 20
else :
    print("sorry, it is not Correct")

quiz2 = input("type 'next' to continue: ")
if quiz != "next":
    quit()

quiz_2 = input(r"""

                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
           /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
          /  .'             /  (       .'  /     Ww._     `.  `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
what is the name of this animal? """) 
if quiz_2 == "lion":
    print('**** Yeay, It is Correct **** ')
    score += 20
else :
    print("sorry, it is not Correct")

quiz3 = input("type 'next' to continue: ")
if quiz != "next":
    quit()

quiz_3 = input(r"""

   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
what is the name of this animal? """)
if quiz_3 == "deer":
    print('**** Yeay, It is Correct **** ')
    score += 20
else :
    print("sorry, it is not Correct")

quiz4 = input("type 'next' to continue: ")
if quiz != "next":
    quit()

quiz_4 = input(r"""


                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
what is the name of this animal? """)
if quiz_4 == "swan":
    print('**** Yeay, It is Correct **** ')
    score += 20
else :
    print("sorry, it is not Correct")

quiz5 = input("type 'next' to continue: ")
if quiz != "next":
    quit()
quiz_5 = input(r"""

_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
what is the name of this animal? """)
if quiz_5 == "bat":
    print('**** Yeay, It is Correct **** ')
    score += 20
else :
    print("sorry, it is not Correct")

quiz6 = input("type 'next' to continue: ")
if quiz != "next":
    quit()

quiz_6 = input(r"""
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
what is the name of this animal? """)
if quiz_6 == "rabbit":
    print('**** Yeay, It is Correct **** ')
    score += 20
else :
    print("sorry, it is not Correct")

player1 = Player(one, score)
data.insert_plyr(player1)



print("Thanks for playing, " + one + " get score " + str(score) +" points.")

print("---TABLE SCORE---")

results = data.get_table_score()
for result in results: 
    print(str(result[0]) + "  " + str(result[1]))


