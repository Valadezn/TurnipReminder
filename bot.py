'''
TurnipReminder:

Twitter bot script that sends Twitter status updates via tweepy (Twitter API for Python) reminding
    users to check on Animal Crossing: New Horizon characters and turnip prices. 
'''

from datetime import datetime
from os import environ
import pytz, sys, time, tweepy

# TODO: Convert all times into GMT
# TODO: edit logic to include tweet status retrieval from text file

def updateTweet():
    """
    Function that tweets an appropriate message depending on what time it
        is and the day of the week
        
    Depending on the day and time, func sends a tweet reminding user
        to check on turnip prices, buy turnips, or sell turnips.
        
    Sunday -> Reminds to buy turnips
    Mon, Tue, Thur, Fri-> Reminds to check on prices 2x a day
    Wed -> Reminds to check on prices 2x a day & that it's halfway through 
        the week
    Sat -> Reminds to check prices 2x a day and that it's the last day
        to sell turnips before they turn rotten
        
    Parameter:
    None
    
    Returns:
    None
    
    """
    #current_datetime = datetime.now()
    #todays_weekday = current_datetime.today().weekday() 
    
    pst_timezone = pytz.timezone('America/Los_Angeles')
    current_datetime = datetime.now(pst_timezone)
    todays_weekday = current_datetime.today().weekday() 
    
    boar_emoji = u"\U0001F417"
    money_emoji = u'\U0001F4B0'
    chart_emoji = u'\U0001F4C8'
    warning_emoji = u'\U0000FE0F'
    soon_sign_emoji = u'\U0001F51C'
    double_exclamation_emoji = u'\U0000FE0F'
    cross_mark_emoji = u'\U0000274C'
    
    
    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_KEY = environ['ACCESS_KEY']
    ACCESS_SECRET = environ['ACCESS_SECRET']
    
    if (current_datetime.second == 0 and current_datetime.microsecond == 0):
        print("bot.py: Current day: {} --- Current time: {}:{}:{}:{}".format(todays_weekday, current_datetime.hour, current_datetime.minute, current_datetime.second, current_datetime.microsecond))
        sys.stdout.flush()
    
    
    if (todays_weekday == 6): # If it's Sunday
        if (current_datetime.hour == 5 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 5am (Daisy Mae appears)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(boar_emoji + 
                ": Good morning! It's Sunday, 5 AM. Daisy Mae is in town.\nDon't forget to buy turnips before she leaves at 12 PM!")
            print("sending tweet. sunday 5am")
            sys.stdout.flush()
            
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and 
            current_datetime.second == 0):
            # elif it's 11am (1 hr before daisy mae disappears)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(boar_emoji + warning_emoji +
                ": It's Sunday, 11 AM. Daisy Mae will be leaving soon!!\nDon't forget to buy turnips before she leaves at 12 PM!")
            print("sending tweet. sunday 11am")
            sys.stdout.flush()
            
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and 
            current_datetime.second == 0):
            # elif it's 12pm (Daisy mae disappears)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(boar_emoji + cross_mark_emoji +
                ": It's Sunday, 12 PM. Daisy Mae is gone for the week!\nTime to check on your turnip prices tomorrow or buy turnip next Sunday.")
            print("sending tweet. sunday 12pm")
            sys.stdout.flush()
            
    elif (todays_weekday == 0): # If it's Monday
        if (current_datetime.hour == 8 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 8am (open, new morning price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + 
                ": Good morning! It's Monday, 8 AM. Don't forget to check on your morning turnip prices!")
            print("sending tweet. monday 8am")
            sys.stdout.flush()
            
            
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 11am (1 hr before new noon price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + warning_emoji + 
                ": It's 11 AM. Your morning turnip prices end in one hour!!")
            print("sending tweet. monday 11am")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 12pm (new noon price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 12 PM. Check on your afternoon turnip prices before 10 PM!")
            print("sending tweet. monday 12pm")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 21 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 9pm (1 hr before closing)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 9 PM, one hour before Nook's Cranny closes. Check on your afternoon turnip prices before 10 PM!")
            print("sending tweet. monday 9pm")
            sys.stdout.flush()
            
        elif (current_datetime.hour == 22 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 10pm (closed)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + cross_mark_emoji + 
                ": It's 10 PM, and Nook's Cranny has closed for the night. Turnip prices will update tomorrow at 8am!")
            print("sending tweet. monday 10pm")
            sys.stdout.flush()

    elif (todays_weekday == 1): # If it's Tuesday GMT (Mon
        if (current_datetime.hour == 8 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 8am (open, new morning price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + 
                ": Good morning! It's Tuesday, 8 AM. Don't forget to check on your morning turnip prices!")
            print("sending tweet. tuesday 8am")
            sys.stdout.flush()
            
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and current_datetime.second == 0 and current_datetime.microsecond == 0):
            # elif 11am (1 hr before new noon price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + warning_emoji + 
                ": It's 11 AM. Your morning turnip prices end in one hour!!")
            print("sending tweet. tuesday 11am")
            sys.stdout.flush()
            time.sleep(5)
        
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 12pm (new noon price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 12 PM. Check on your afternoon turnip prices before 10 PM!")
            print("sending tweet. tuesday 12pm")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 21 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 9pm (1 hr before closing)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 9 PM, one hour before Nook's Cranny closes. Check on your afternoon turnip prices before 10 PM!")
            print("sending tweet. tuesday 9pm")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 5 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 10pm (closed) (Monday 10pm PST -> Tuesday 5am GMT)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + cross_mark_emoji + 
                ": It's 10 PM, and Nook's Cranny has closed for the night. Turnip prices will update tomorrow at 8am!")
            print("sending tweet. tuesday 10pm")
            sys.stdout.flush()
    
    elif (todays_weekday == 2): # If it's Wednesday
        if (current_datetime.hour == 8 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 8am (open, new morning price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + 
                ": Good morning! It's Wednesday, 8 AM. Don't forget to check on your morning turnip prices!")
            print("sending tweet. wednesday 8am")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 11am (1 hr before new noon price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + warning_emoji + 
                ": It's 11 AM. Your morning turnip prices end in one hour!!")
            print("sending tweet. wednesday 11am")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 12pm (new noon price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 12 PM. Check on your afternoon turnip prices before 10 PM!")
            print("sending tweet. wednesday 12pm")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 21 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 9pm (1 hr before closing)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 9 PM, one hour before Nook's Cranny closes. Check on your afternoon turnip prices before 10 PM!")
            print("sending tweet. wednesday 9pm")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 22 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 10pm (closed)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + cross_mark_emoji + 
                ": It's 10 PM, and Nook's Cranny has closed for the night. Turnip prices will update tomorrow at 8am!")
            print("sending tweet. wednesday 10pm")
            sys.stdout.flush()
            
    
    elif (todays_weekday == 3): # If it's Thursday
        if (current_datetime.hour == 8 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 8am (open, new morning price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + 
                ": Good morning! It's Thursday, 8 AM. Don't forget to check on your morning turnip prices!")
            print("sending tweet. thursday 8am")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 11am (1 hr before new noon price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + warning_emoji + 
                ": It's 11 AM. Your morning turnip prices end in one hour!!")
            print("sending tweet. thursday 11am")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 12pm (new noon price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 12 PM. Check on your afternoon turnip prices before 10 PM!")
            print("sending tweet. thursday 12am")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 21 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 9pm (1 hr before closing)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 9 PM, one hour before Nook's Cranny closes. Check on your afternoon turnip prices before 10 PM!")
            print("sending tweet. thursday 9pm")
            sys.stdout.flush()
            
        elif (current_datetime.hour == 22 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 10pm (closed)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + cross_mark_emoji + 
                ": It's 10 PM, and Nook's Cranny has closed for the night. Turnip prices will update tomorrow at 8am!")
            print("sending tweet. thursday 10pm")
            sys.stdout.flush()
            
    elif (todays_weekday == 4): # If it's Friday
        if (current_datetime.hour == 8 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 8am (open, new morning price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + 
                ": Good morning! It's Friday, 8 AM. Don't forget to check on your morning turnip prices!")
            print("sending tweet. friday 8am")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 11am (1 hr before new noon price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + warning_emoji + 
                ": It's 11 AM. Your morning turnip prices end in one hour!!")
            print("sending tweet. friday 11am")
            sys.stdout.flush()
            
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 12pm (new noon price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 12 PM. Check on your afternoon turnip prices before 10 PM!")
            print("sending tweet. friday 12pm")
            sys.stdout.flush()
            
        elif (current_datetime.hour == 21 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 9pm (1 hr before closing)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 9 PM, one hour before Nook's Cranny closes. Check on your afternoon turnip prices before 10 PM!")
            print("sending tweet. friday 9pm")
            sys.stdout.flush()
            
        elif (current_datetime.hour == 22 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 10pm (closed)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + cross_mark_emoji + 
                ": It's 10 PM, and Nook's Cranny has closed for the night. Tomorrow is the LAST DAY to sell your turnips if you haven't!")
            print("sending tweet. friday 10pm")
            sys.stdout.flush()
            
    elif (todays_weekday == 5): # If it's Saturday 
        if (current_datetime.hour == 8 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 8am (open, new morning price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + 
                ": Good morning! It's Friday, 8 AM. Make sure to sell your turnips today!!!")
            print("sending tweet. saturday 8am")
            sys.stdout.flush()
            
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 11am (1 hr before new noon price)
            
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + warning_emoji + 
                ": It's 11 AM. Your morning turnip prices end in one hour!!")
            print("sending tweet. saturday 11am")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 12pm (new noon price)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 12 PM. Check on your last afternoon turnip prices of the week before 10 PM!")
            print("sending tweet. saturday 12pm")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 21 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 9pm (1 hr before closing)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 9 PM, one hour before Nook's Cranny closes. DON'T FORGET TO SELL YOUR TURNIPS!!!")
            print("sending tweet. saturday 9pm")
            sys.stdout.flush()
        
        elif (current_datetime.hour == 22 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 10pm (closed)
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            api.update_status(money_emoji + cross_mark_emoji + 
                ": It's 10 PM, and Nook's Cranny has closed for the night. Daisy Mae will be selling turnips tomorrow.")
            print("sending tweet. saturday 10pm")
            sys.stdout.flush()
    
if __name__ == '__main__':
    print("Bot.py: Starting bot.py")
    sys.stdout.flush()
    while True:
        updateTweet()