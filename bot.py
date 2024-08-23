from config import
import telebot
import openai

chatStr = ""

def ChatModal(prompt): 
    global chatStr
    openai.api_key = OPENAI_KEY
    chatStr += f"Immortal: {prompt}\nFriday: "
    response = openai.Completion.create(
                   model="text-davinci-003",
                   prompt=chatStr,
                   temperature=1,
                   max_token=256,
                   top_p=1,
                   frequency_penalty=0,
                   presence_penalty=0
                   )
    print(response)      
    chatStr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text']
    
bot = telebot.Telebot(BOT_API)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Hello Welcome To Immortal's Bot I'm Friday How Can I Help")


@bot.message_handler()
def chat(message): 
    try: 
       reply = ChatModal(message.text)
    except Exception as e:
        print(e): 
        bot.reply_to(message,e)
        

print("bot started...")
bot.polling()
