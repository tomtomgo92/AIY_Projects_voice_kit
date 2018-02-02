#!/usr/bin/env python3

"""A test of the Google CloudSpeech recognizer."""
import logging
import os

# Google imports
import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import aiy.cloudspeech

# Personal imports
from commands.parser import Parser

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


def main():
    aiy.i18n.set_language_code('fr-FR')
    print(aiy.i18n.get_language_code())
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    recognizer = aiy.cloudspeech.get_recognizer()

    # recognizer.expect_phrase('flo')
    # recognizer.expect_phrase('Denis')    
    # recognizer.expect_phrase('denis')
    # recognizer.expect_phrase('florian')
    # recognizer.expect_phrase('coding')

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()

    

    with aiy.audio.get_recorder():
        while True:
            status_ui.status('ready')
            print('Press the button and speak')
            button.wait_for_press()
            status_ui.status('listening')
            print('Listening...')
            text = recognizer.recognize()
            if not text:
                print('Sorry, I did not hear you.')
            else:
                app = Parser('src/commands/commands.lib')
                app.parse()
                commands = app.getCommands()
                actions = app.getActions()
                noMatches = 0
                for i in range(0, len(commands)):
                    if commands[i].startswith('sound->'):
                        if commands[i].replace('sound->', '').strip() in text.lower():
                            os.system('aplay /home/pi/AIY-projects-python/src/sounds/'+ actions[i].strip())
                            break
                    elif commands[i].strip() in text.lower():
                        aiy.audio.say(actions[i])
                        break
                    else:
                        noMatches = noMatches + 1
                if noMatches == len(commands):
                   aiy.audio.say('Articule s\'il te plait')
                print('You said', text)


if __name__ == '__main__':
    main()
