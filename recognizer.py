import os
import time
import subprocess

class Recognizer():

    def recognize(self):
        print 'recording...'
        p1 = subprocess.call('rec record.wav rate 16k silence 1 0.1 3% 1 3.0 3%',shell=True)
        time.sleep(1)
        print 'recognizing...'
        recognized_text = subprocess.check_output('pocketsphinx_continuous -infile record.wav -lm models/5835.lm -dict models/5835.dic -logfn /dev/null',shell=True, stderr=subprocess.STDOUT)
        os.remove('record.wav')
        return recognized_text


if __name__ == "__main__":
    r = Recognizer()
    recognized_text = r.recognize()
    print recognized_text