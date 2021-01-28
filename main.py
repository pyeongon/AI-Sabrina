import sys
import time
import random
import datetime

def slowprt(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.06)
        if char == ',':
            time.sleep(.3)
        if char in ".?!":
            time.sleep(.6)

exit_prompts = ["bye now!", "see you soon.", "goodbye.", "talk to you later, then."]
greet_prompts = ["hello. :)", "greetings, user.", "good morning, user.", "good afternoon, user.", "good evening, user."]
greetings = ["hello", "hi", "good morning", "good afternoon", "good evening"]

current_time = datetime.datetime.now()

def main():
    '''
    print("sabrina: ", end='')
    slowprt("greetings, user. i am sabrina, artifical not-very-intelligent intelligence.\n")
    print(" " * 9, end='')
    slowprt("i follow a very simple rule-based algorithm for deriving answers to your prompts, whatever they may be.\n")
    print(" " * 9, end='')
    slowprt("please be patient with me as i am constantly \"evolving\" to suit your needs.\n")

    print("sabrina: ", end='')
    slowprt("if at any point, you would like to exit the program, you can easily do so by typing\n")
    print(" " * 9, end='')
    slowprt("\"exitprgm\" into the given textspace.")

    print("sabrina: ", end='')
    slowprt("now then, where shall we begin?\n")
    '''

    while(True):
        ans = input("user: ")
        print("sabrina: ", end='')

        # exit case
        if ans == "exitprgm":
            slowprt(random.choice(exit_prompts) + '\n')
            sys.exit(0)

        # greetings
        if any(word in ans.lower() for word in greetings):
            fault = False
            time_of_day = "default"
            if "morning" in ans:
                time_of_day = "morning"
            elif "afternoon" in ans:
                time_of_day = "afternoon"
            elif "evening" in ans:
                time_of_day = "evening"
            # morning
            if 5 <= current_time.hour <= 12:
                if time_of_day in ["afternoon","evening"]:
                    fault = True
                    slowprt("it's not " + time_of_day + ", silly kid.\n")
                c = random.choice([0,1,2])
            # afternoon
            elif 13 <= current_time.hour <= 18:
                if time_of_day in ["morning","evening"]:
                    fault = True
                    slowprt("everyone has their own way of spelling \"afternoon\", but i've decided that your way is wrong.\n")
                c = random.choice([0,1,3])
            # evening
            elif 19 <= current_time.hour <= 23:
                if time_of_day in ["morning","afternoon"]:
                    fault = True
                    slowprt("hm.. wouldn't exactly call it \"" + time_of_day + "\" right now.\n")
                c = random.choice([0,1,4])
            # other
            else:
                c = random.randint(0,1)
            if not fault:
                slowprt(greet_prompts[c] + '\n')

main()
