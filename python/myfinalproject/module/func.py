from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage,ImageSendMessage,StickerSendMessage,LocationSendMessage,AudioSendMessage

line_bot_api=LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

baseurl='https://dd939ef0b62f.ngrok.io/static/'

def sendText(event):
    try:
        message=TextSendMessage(text="Hello, my name is linebot1")
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤'))
        
def sendImage(event):
    try:
        message = ImageSendMessage(
            original_content_url=baseurl+'2.jpg',
            preview_image_url =  baseurl+'2.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤'))
def sendStick(event):
    try:
        message = StickerSendMessage(package_id='1',sticker_id='112')
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤'))
    
def sendPosition(event):
    try:
        message=LocationSendMessage(title='國立金門大學',address='金門縣金寧鄉大學路1號',latitude=24.44816,longitude=118.32252)
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤')) 
        
def sendAudio(event):
    try:
        message = AudioSendMessage(original_content_url=baseurl+'2.m4a',duration=49000 )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤'))    