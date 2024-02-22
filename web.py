import speech_recognition as am
import webbrowser
import os
import time


a = ['aaa', 'abb', 'cac', 'fad', 'dae', 'saf', 'amg', 'ssh', 'eai', 'awj', 'ark', 'atl', 'yam', 'uan', 'iao', 'oap', '6aq', 'tar', 's4a', 'rta',
     'tua', 'gva', 'nwa', 'xva', 'fya', 'hza', 'ja', 'kb', 'rc', 'ud', 're', 'od', 'pc', 'dq', 'dr', 'hs', 'rt', 'yu', 'iv', 'yw', 'ox', 'ty', 'uz']

# for i in range(0, 17):
#     webbrowser.open(f"https://www.bing.com/search?q={a[i]}&FORM=ANAB01&PC=HCTS")
#     time.sleep(0.4)


for i in range(17, 34):
    webbrowser.open(f"https://www.bing.com/search?q={a[i]}&FORM=ANAB01&PC=HCTS")
    time.sleep(0.4)
