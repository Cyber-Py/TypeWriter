# How to create a "TypeWriter"

Have you ever seen those programs, in which the output is "typed" out? Like, each letter is printed out one by one? If you have, and would want to know how to make it? Well you have ended up in the right place!



Ok, no more talking; let's get right to the code.

So first of all, we need to import the modules:

```py
from time import sleep
```
> ##### One module, actually

Now, we need to define our function; I have named it `printt()`, but you can name it whatever you want:
```py
def printt(string, delay):
  # Our code will go here
  # Our code will go here
  # Our code will go here
```

>
###### If you have noticed so far but don't know, the `string` in the brackets of our defined function, that is a parameter. It is uesd as a placeholder for whatever we qant variables/string/numbers. Same for the `delay`. Delay pauses the `print` function for a certain amount of time so it makes it look like a "typewriter"

Ok, so far, we have our modules imported and our function defined. Now we can actually start coding.

So, we need a `for` loop to print out every letter.

I will be using the letter `i` for every character in the string and `string` as the string/variable to be "typed" out
```py
def printt(string, delay):
  for i in str(string):
      # Our code will go here
      # Our code will go here
      # Our code will go here      
```

Next we will put this:
```py
def printt(string, delay):
  for i in str(string):
    print(i, end="", flush = True)
    sleep(delay)
```
If you're stumped as to what `end`, and `flush` are, they are actually parameters for the `print` function. While you're coding, hover your mouse over the `print` function and it will show this:

![print(*values: object, sep: Optional[Text]=..., file: Optional[_Writer]=..., flush: bool=...) -> None](https://storage.googleapis.com/replit/images/1623958494856_21cabdf7e060682043683b0933acc4af.png)

These parameters are actually optional, so you won't need to put them to use the `print` function.
We put the `end` parameter there without anything in the quotation marks to indicate there is no end, so it keeps on printing from the line before, and `flush`, I honestly dont understand it still. 

EDIT: `flush` is when you print something to the console text gets built up over time, but the new text isn't constantly rendered on the screen, instead its regularly "flushed" to the screen.
But `printt()` prints stuff to the console faster than it can render text, so by putting `flush = True` in your print statement you're forcing it to render the text in time.

Thanks to [@Dunce](https://replit.com/@Dunce) for heling me out for `flush`


The `sleep()` function is from the `time` module, and is used to "pause" the code for a few seconds. Here, `sleep()` "pauses" the program for 0.05 seconds.

So far we have this:
```py
from time import sleep
def printt(string, delay):
  for i in str(string):
    print(i, end="", flush = True)
    sleep(delay)
```
Next, we add a `print()` statement to print a new line after the string is typed out:

```py
from time import sleep
def printt(string, delay):
  for i in str(string):
    print(i, end="", flush = True)
    sleep(delay)
  print('')
  # Not Inside the for loop, or it will mess the program
```
## AND WE ARE DONE!

That's it. I know its simple, but it's worth it as it makes the program less "dull"
***

Please check out my [Racing Simulator](https://replit.com/talk/share/Racing-Sim/141553)

***

> Please give me more ideas on what to code, I don't have no more ideas.

***

# That's it for this Tutorial and see you in my next post; Bye!