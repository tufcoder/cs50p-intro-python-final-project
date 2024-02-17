# LoL Draft SIM

#### Video Demo <URL HERE>

#### Description: 

That's my final project in CS50 Introduction to Programming with Python.

It's a League of Legends draft simulator.

The program gets the "champions.json" via Riot API with the list of all the champions in the game and write a file with the data.

If the file not exists, it's created. If the file exists, the program checks if the content is updated, if not, rewrite the file.

The draft occours in the console, so feel free to practice typing 🙂⌨️

When typing a champion name in the picks or bans, the program should output some champions names based in what you input after press ENTER. For example, typing "ve" or "VE" or "vE" or "Ve" outputs something like above:

Are you are trying to choose: Belveth ?
Are you are trying to choose: Draven ?
Are you are trying to choose: Evelynn ?
Are you are trying to choose: Graves ?
Are you are trying to choose: Ivern ?
Are you are trying to choose: Riven ?
Are you are trying to choose: Veigar ?
Are you are trying to choose: Velkoz ?
Are you are trying to choose: Vex ?

All champions that the name contains the literal "ve" case-insensitive.

In the end of the draft, a file called draf_sim_YYYYmmddHmSf.csv is created in a temp folder with the draft resume.