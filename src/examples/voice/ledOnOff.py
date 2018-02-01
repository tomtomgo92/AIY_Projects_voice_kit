import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import RPi.GPIO as GPIO

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('allumer')
    recognizer.expect_phrase('eteindre')

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
            if 'allumer' in text:
                GPIO.output(26,GPIO.HIGH)
            elif 'eteindre' in text:
                GPIO.output(26,GPIO.LOW)

if __name__ == '__main__':
    main()
    
    