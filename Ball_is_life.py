import os
import time


#width of the display
WIDTH = 79

#the message we wish to appear
message = "ball  is  life  vlog_18".upper()

printedMessage = [ "","","","","","","","","","","","","","","","","","","","","","","" ]

characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],
                       
               "B" : [ "$$$$$",
                       "$   $",
                       "$   $",
                       "$$$$$",
                       "$   $",
                       "$   $",
                       "$$$$$",
                       "     " ],
                       
               "A" : [ "$$$$$",
                       "$   $",
                       "$   $",
                       "$$$$$",
                       "$   $",
                       "$   $",
                       "$   $",
                       "     " ],
               
               "L" : [ "$    ",
                       "$    ",
                       "$    ",
                       "$    ",
                       "$    ",
                       "$    ",
                       "$$$$$",
                       "     " ],
               
               "I" : [ "$$$$$",
                       "  $  ",
                       "  $  ",
                       "  $  ",
                       "  $  ",
                       "  $  ",
                       "$$$$$",
                       "     " ],
               
               "S" : [ "$$$$$",
                       "$    ",
                       "$    ",
                       "$$$$$",
                       "    $",
                       "    $",
                       "$$$$$",
                       "     " ],
                       
               "F" : [ "$$$$$",
                       "$    ",
                       "$    ",
                       "$$$$$",
                       "$    ",
                       "$    ",
                       "$    ",
                       "     " ],
                       
                        
               "E" : [ "$$$$$",
                       "$    ",
                       "$    ",
                       "$$$$$",
                       "$    ",
                       "$    ",
                       "$$$$$",
                       "     " ],
                       
               "V" : [ "$   $",
                       "$   $",
                       " $ $ ",
                       " $ $ ",
                       " $ $ ",
                       "  $  ",
                       "  $  ",
                       "     " ],
                       
               "O" : [ "$$$$$",
                       "$   $",
                       "$   $",
                       "$   $",
                       "$   $",
                       "$   $",
                       "$$$$$",
                       "     " ],
                       
               "G" : [ "$$$$$",
                       "$    ",
                       "$    ",
                       "$  $$",
                       "$   $",
                       "$   $",
                       "$$$$$",
                       "     " ],
                       
                       
               "_" : [ "     ",
                       "     ",
                       "     ",
                       "     ",
                       "     ",
                       "     ",
                       "$$$$$",
                       "     " ],
                       
               "1" : [ "  $  ",
                       " $$  ",
                       "  $  ",
                       "  $  ",
                       "  $  ",
                       "  $  ",
                       "$$$$$",
                       "     " ],
                       
               "8" : [ "$$$$$",
                       "$   $",
                       "$   $",
                       "$$$$$",
                       "$   $",
                       "$   $",
                       "$$$$$",
                       "     " ] 
               }
               
for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + " ")
        
offset = WIDTH
while True:
    os.system("clear")
    for row in range(12):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
        offset -= 1
        if offset <=((len(message)+2)*6) * -1:
            offset = WIDTH
        time.sleep(0.125)
         