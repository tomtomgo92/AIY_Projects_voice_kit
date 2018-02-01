#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""
import logging
import os

import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import aiy.cloudspeech

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

    recognizer.expect_phrase('flo')
    recognizer.expect_phrase('Denis')    
    recognizer.expect_phrase('denis')
    recognizer.expect_phrase('florian')
    recognizer.expect_phrase('coding')

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
                if 'coding' in text.lower():
                    aiy.audio.say('En septembre 2017, ITESCIA ouvre une ecole du code : la Coding Factory by ITESCIA.')
                elif 'flo' in text.lower():
                    aiy.audio.say('je suis flo un codeur de la Coding Factory')
                elif 'denis' in text.lower():
                    os.system('aplay /home/pi/AIY-projects-python/src/sounds/ah.wav')
                elif 'homo' in text.lower():
                    os.system('aplay /home/pi/AIY-projects-python/src/sounds/ContreNature.wav')
                elif 'pokemon' in text.lower():
                    os.system('aplay /home/pi/AIY-projects-python/src/sounds/DavidLafarge.wav')
                else:
                    aiy.audio.say('Articule s\'iol te plait')
                print('You said', text)


if __name__ == '__main__':
    main()
