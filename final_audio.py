import pyttsx3
import os

try:
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Expanded text with more grammatical errors and hesitations
    text = ("So umm.. I was uh, you know, just kind of, uh, sitting there thinking, like, about, umm, what I should do today, right? "
            "And, umm, I was like, maybe I could go to the, uh, store or something, but then I thought, umm, you know, like, do I really need anything? "
            "But then, uh, I remembered that I, umm, wanted to pick up some, uh, snacks or, umm, maybe some ice cream, right? "
            "But then I was, uh, kinda like, do I really want to go out, or should I just stay home and, umm, chill? "
            "So then I thought, maybe I could just, umm, order something online, but, like, what if the delivery takes too long? "
            "And then I was like, uh, you know, I could just make something at home, but, umm, I wasn’t really feeling it. "
            "So I was kinda just sitting there, uh, thinking about all of this and, umm, going back and forth in my mind. "
            "And, umm, I even texted my friend, like, asking what they were up to, but, umm, they didn’t respond right away, you know? "
            "So I just sat there for a bit longer, feeling a bit indecisive, like, I didn’t want to waste the day, but, umm, I wasn’t sure what to do. "
            "Eventually, I decided, uh, to just stay in and watch some TV, but, like, even then, I couldn’t really focus because I kept thinking about, umm, all the stuff I could have done, you know? "
            "So, umm, that's basically what happened, and, like, I guess I just need to be, uh, better at making decisions or something.")

    # Define file path to save
    file_path = os.path.join(os.getcwd(), 'speech_with_more_mistakes.wav')

    # Save speech to file
    engine.save_to_file(text, file_path)
    engine.runAndWait()

    print(f'File successfully saved as: {file_path}')
except Exception as e:
    print(f'An error occurred: {e}')
