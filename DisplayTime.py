#prompt the user for input
seconds = eval(raw_input('Enter an integer for seconds:'))

#Get minutes and remaining seconds
mintues = seconds // 60         #Find mintues in seconds
remainingSeconds = seconds / 60         #Seconds remaining
print seconds,'seconds is',mintues, \
      'mintues and',remainingSeconds,'seconds'
