import pyttsx3
engine = pyttsx3.init() # object creation

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate

filename = "Flickr8k.token.txt"


def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text


file = load_doc(filename)
captions = file.split('\n')

number = 100000

print("Started..")
for caption in captions[:-1]:
    img, caption = caption.split('\t')
    number += 1

##    print(caption)

    voices = engine.getProperty('voices')       #getting details of current voice

    engine.setProperty('voice', voices[0].id)  #Male Voice
    engine.save_to_file(caption, "./data/M_" + str(number) + ".wav")
    engine.runAndWait()

    engine.setProperty('voice', voices[1].id)  #Female Voice
    engine.save_to_file(caption, "./data/F_" + str(number) + ".wav")
    engine.runAndWait()

print(number)
print("Done")
