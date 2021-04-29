# myLMSC261

 # Final Project Documentation
 1. Summary of my project:
 For this final project, I did a series of two generative art pieces with a highlight of the concept of "randomness" using python mode processing. Python mode processing is able to show any visual arts and interactive arts. For more details of python mode of processing: https://py.processing.org/

 2. Motivation & Inspiration
 In short, I was inspired by my best friend who suffers from depression and was hoping to show her the world can be beautiful with and without colors and randomness.

 3. My thinking process & approach
 For the first piece, it's a black and white minimalist style of art that shows how particles move when we play music or listen to noise. It also symbolizes how each particle moves on earth in order to live. My approach to creating this piece is first getting inspiration from similar already existed pieces from github. The one that I chose to borrow some source code from is
 https://github.com/aaronpenne/generative_art/blob/master/allegory/allegory.pyde
 Since the concept of randomness is a big highlight of my project, I learned how to use the random.seed() function by looking it up on the internet. It is used to initialize the random number generator. The random number generator needs a number to start with (a seed value), to be able to generate a random number. This function is used in every piece of art in the series I created. For the first piece, I used the random.seed() function to make the result repeatable so that it creates a 3D effect.

 The next crucial function for this piece is the setup() function that is a part of the processing source code required to run a project. It sets the size, resolution, color, number of frames per second, stop drawing function, sets random value for python and processing, and initializes colors of the project.

 The draw() function is another critical function that basically sets how you want the art to be displayed. It saves the frame rates and location. It also keeps track of the time factor.

 As for the interactive/ generative part, because of the limitation of python processing, I wasn't able to ask the user to input a specific value. However, the user could pick a number value. By changing the random.seed value, the shape gets changed. Unfortunately it has to be done in the code writing section.

 As for the second piece of art in the series involves more colors. The color arrangement will be different every time you open it and that shows the beauty of randomness with colors.
 The source code of colors are from https://github.com/aaronpenne/generative_art/blob/master/blur_circles/blur_circles.pyde. This piece also uses the two critical functions setup() and draw() that are mentioned above. The special thing for this one is that the randomness shows up every time you open it. The colors would change their place every time.


 4. What could be improved
 I couldn't get the user input displayed like how it works in python just yet. Although it might be a processing thing, I will try to figure it out in the future.
