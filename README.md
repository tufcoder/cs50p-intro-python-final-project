# LoL Draft SIM

#### Video Demo <https://youtu.be/lN9AF-YE_Ms>

#### Introduction:

* Project title: LoL Draft SIM
* Name: Oswaldo Guirra Pereira de Castro
* Github | edX: tufcoder | tufcastro
* City | County: São Paulo | Brazil 🇧🇷
* Date: 2024-02-19

#### Description: 

This is my final project for the CS50 Introduction to Programming with Python course.

It's a League of Legends draft simulator.

```txt
    __          __       ____             ______     _____ ______  ___
   / /   ____  / /      / __ \_________ _/ __/ /_   / ___//  _/  |/  /
  / /   / __ \/ /      / / / / ___/ __ `/ /_/ __/   \__ \ / // /|_/ / 
 / /___/ /_/ / /___   / /_/ / /  / /_/ / __/ /_    ___/ // // /  / /  
/_____/\____/_____/  /_____/_/   \__,_/_/  \__/   /____/___/_/  /_/   
```                                                               

The program gets the "champions.json" via Riot API with the list of all the champions in the game and write a file with the data.

If the file not exists, it's created. If the file exists, the program checks if the content is updated, if not, rewrite the file.

The draft occours in the console, so feel free to practice typing 🙂⌨️

When typing a champion name in the picks or bans, the program should output some champions names based in what you input after press ENTER. For example, typing "ve" or "VE" or "vE" or "Ve" and press ENTER outputs something like bellow:

Are you are trying to choose: Belveth ?
Are you are trying to choose: Draven ?
Are you are trying to choose: Evelynn ?
Are you are trying to choose: Graves ?
Are you are trying to choose: Ivern ?
Are you are trying to choose: Riven ?
Are you are trying to choose: Veigar ?
Are you are trying to choose: Velkoz ?
Are you are trying to choose: Vex ?

The draft is divided into two rounds of bans and picks.

1st bans round:
Blue, Red, Blue, Red, Blue, Red = 6 bans

1st picks round:
Blue, Red, Red, Blue, Blue, Red = 6 picks

2nd bans round:
Red, Blue, Red, Blue = 4 bans

2nd picks round:
Red, Blue, Blue, Red = 4 picks

Total champions banned: 10 bans
Total champions picked: 10 picks

In the end of the draft, a "csv" file is created in a temp folder with the draft resume.