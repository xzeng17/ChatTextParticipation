# Chat Text Participation 

# Roster

$ python3 main.py init

Roster is downloaded from Lon-capa, under People->Users. Users' name, domain, netID, UID and email are extracted.  <br>

Each line represent one student. <br>
Sample format: "1		abc123	uiuc	123456789	a, bc	abc@illinois.edu"   <br>


# Update Roster

Replace the roster.txt file in assets folder <br>
repeat init step as in Roster so that you can get a new init.csv file <br>
Then execute update cmd <br>
$ python3 main.py update    <br>
Both concept_question_grades_XX20XX.csv and chat_grades_XXX20XX.csv will be updated base on the new roster. <br>

# Concept question

$ python3 main.py [cq] [filename] <br>
Ex: $ python3 main.py cq T1E.txt <br>

To load a concept question, download all graded student's grade from lon-capa       <br>
    ->Grades                                    <br>
    ->Content Grading                           <br>
    ->Select individual students to grade       <br>
    ->Check all and only view grades            <br>
    ->copy and paste                            <br>
    ->file in input folder                      <br>
Put the downloaded grades in txt file and place it in input folder  <br>

# Chat Participation
$ python3 main.py chat [first chat] [second chat]   <br>
Ex: $ python3 main.py chat chat_week1_1.txt chat_week1_2.txt

Because there are two sections of discussion, I hard coded the requirement for two file names <br>
Place the zoom recorded chat.txt under input file before run    <br>
<br>
<br>
Last edited: July 15 2021 <br>
