# ใช้งาน text-to-speech โดยใช้ไลบารี่ gTTS
สคริปต์นี้ช่วยให้คุณใช้งานคำสั่ง ป้อนข้อความ และเปลี่ยนเป็นคำพูด ด้วยเสียงของสิริ โดยการป้อนข้อความที่ต้องการแล้วให้ gTTs save กลับเข้า directory แล้ว เล่นเสียงในไฟล์เหล่านั้น

## การใช้งานคำสั่ง และการกำหนด token
ใช้งานโดยคำสั่ง !speak แล้วตามด้วยข้อความที่ต้องการให้ gTTs พูด 
การกำหนด token นั้น อยู่ใน config\.env 
## ข้อกำหนดเบื้องต้น
- คุณต้องติดตั้ง packages : discord.py , gTTS, voiceclient โดยใช้คำสั่ง `pip install discord.py` `pip install gTTs` `pip install voiceclient`

## Dependencies
Python 3.7+
discord.py
gTTS
...

## ผู้จัดทำ
นาย ศธร สุขขัง (github: pondsan1412)
...

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.