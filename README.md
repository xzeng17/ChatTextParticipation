# Chat Text Participation 

# Roster

$ python3 main.py init

Roster is downloaded from Lon-capa, under People->Users. Users' First name, Last name, netID, UID and email are extracted.  <br>

Each line represent one student. <br>
Sample format: "1		abc123	uiuc	123456789	a, bc	abc@illinois.edu"   <br>


# Concept question

$ python3 main.py [cq] [filename] <br>
Ex: $ python3 main.py cq T1E.txt <br>

To load a concept question, download all graded student's grade from lon-capa       <br>
    Grades->Content Grading->Select individual students to grade->Check all and only view grades->copy and paste->remove all headings that involves starnge characters->file in input folder    <br>
Put the downloaded grades in txt file and place it in input folder  <br>

# Chat Participation
$ python3 main.py chat [first chat] [second chat].txt
Ex: $ python3 main.py chat chat_week1_1.txt chat_week1_2.txt

Because there are two sections of discussion, I hard coded the requirement for two file names <br>
Place the zoom recorded chat.txt under input file before run    <br>
<br>
<br>
Last edited: June 20 2021 <br>
