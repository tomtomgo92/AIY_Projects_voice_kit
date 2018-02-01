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

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

The Google Assistant Library can be installed with:
    env/bin/pip install google-assistant-library==0.0.2

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import RPi.GPIO as GPIO

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('light on')
    recognizer.expect_phrase('light off')

    button = aiy.voicehat.get_button()
    aiy.audio.get_recorder().start()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26,GPIO.OUT)

    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text = recognizer.recognize()
        if text is None:
            print('Sorry I did not hear you.')
        else:
            print('You said "', text,'"')
            if 'light on' in text:
                GPIO.output(26,GPIO.HIGH)
            elif 'light off' in text:
                GPIO.output(26,GPIO.LOW)

if __name__ == '__main__':
    main()
    
    