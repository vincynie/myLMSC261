Scratch Read Me

# Description of my game
1.This game is made to train the multi tasking skills that the left hand and right hand each follows different instructions but functions simultaneously.
2.The left hand is in charge of making sure that the star keeps bouncing up and down; the right hand is in charge of keeping the llama away from the star with the four arrows.

# Decisions made while creating the game
1.First, I chose three sprites I like: llama, star, and Gobo. Then, I chose the background.

2.I wanted to interact the two sprites out of the three. Thus, I chose the llama and the star. I made the star moving randomly forever. However, when it touches the llama, in this case the condition of grey color, it makes a sound. Thus, I needed a forever loop with a if statement in it.

3.The llama just moves to the left, right, up or down when arrows with different directions are pressed. By achieving this goal, I just made four different blocks to change the X, horizontal change, and Y, vertical change. I also add a voice of a descriptive sentence to specify what I want the player to do.

4.The Gobo is a cute character that I wanted to make it bounce up and down without stop. Thus, I started with making a new variable called Y speed, which represents at what speed it would bounce, or how much does it change vertically each time. I first set the variable to a fixed value, the bouncing speed, and made it start from a location I wanted it to start. Then I made a loop saying that it changes by that speed. However, bouncing up and down means that it not only moves upward but downward. Thus, I also made the variable to change by a negative number. Moreover, I didn't want the Gobo to just bounce by itself, but with some interaction to the player. Thus, I included a if statement inside the loop I created saying if the the mouse is clicked, then let it bounce, otherwise make the pop sound to remind the player to make it bounce continuously. I also added a voice to tell the player what I want him or her to do for this character.
