from time import sleep
def printt(string, delay):
  for i in str(string):
    print(i, end="", flush = True)
    sleep(delay)
  print('')
printt('This string will be "typed" out letter by letter.\nPretty cool, right?', 0.05)
printt(f'Here is an example of typing out an integer\n{1234}\n', 0.08)
printt(f'And a float: {1.234}', 0.08)




