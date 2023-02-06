### condense review text so it can be itterated through faster by removing stop words from a string of text ###

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def remove_stop_words(text):
  # Split the text into a list of words
  words = text.split()
  
  # Get the list of stop words in English
  stop_words = stopwords.words('english')
  
  # Remove stop words from the list of words
  filtered_words = [word for word in words if word.lower() not in stop_words]
  
  filtered_text = ' '.join(filtered_words)
  
  return filtered_text


# Test the function
test_string = "Maybe they used to be good..The doctors we got to talk to seemed brilliant to be fair. The problem is how it is ran, how you are treated, disorganization, and wait for treatment.  DO not  go here for anything serious or bring your loved ones here. You will die waiting to be treated.  We were told to go to the emergency room to get my mom in for cancer.   22 hour wait...no joke to be seen..I thought it could only get better...I was wrong..She literally wound up on a ventilator at another hospital..luckily she came off of it...waiting to be scheduled for her first treatment..they were waiting on insurance approval which we were told at the beginning would not matter..They dont care about you...You are an experiment and they make you wait and wait and wait..Its inhumane what goes on here. I took my mother here because I heard they are the best..Don't make my mistake.."
test_string_short = remove_stop_words(test_string)


print(test_string)
print(len(test_string))
print(test_string_short)
print(len(remove_stop_words(test_string_short)))
print(len(remove_stop_words(test_string_short)) / len(test_string))