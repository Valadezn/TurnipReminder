'''
Created on May 20, 2020

@author: noemi
'''

from datetime import datetime
import tweepy, credentials



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
    current_datetime = datetime.now()
    todays_weekday = current_datetime.today().weekday() 
    
    boar_emoji = u"\U0001F417"
    money_emoji = u'\U0001F4B0'
    chart_emoji = u'\U0001F4C8'
    warning_emoji = u'\U0000FE0F'
    soon_sign_emoji = u'\U0001F51C'
    double_exclamation_emoji = u'\U0000FE0F'
    cross_mark_emoji = u'\U0000274C'
    
    
    if (todays_weekday == 6): # If it's Sunday
        if (current_datetime.hour == 5 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 5am (Daisy Mae appears)
            api.update_status(boar_emoji + 
                ": Good morning! It's Sunday, 5 AM. Daisy Mae is in town.\nDon't forget to buy turnips before she leaves at 12 PM!")
        
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and 
            current_datetime.second == 0):
            # elif it's 11am (1 hr before daisy mae disappears)
            api.update_status(boar_emoji + warning_emoji +
                ": It's Sunday, 11 AM. Daisy Mae will be leaving soon!!\nDon't forget to buy turnips before she leaves at 12 PM!")
        
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and 
            current_datetime.second == 0):
            # elif it's 12pm (Daisy mae disappears)
            api.update_status(boar_emoji + cross_mark_emoji +
                ": It's Sunday, 12 PM. Daisy Mae is gone for the week!\nTime to check on your turnip prices tomorrow or buy turnip next Sunday.")
    
    elif (todays_weekday == 0): # If it's Monday
        if (current_datetime.hour == 8 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 8am (open, new morning price)
            api.update_status(money_emoji + 
                ": Good morning! It's Monday, 8 AM. Don't forget to check on your morning turnip prices!")
        
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 11am (1 hr before new noon price)
            api.update_status(money_emoji + warning_emoji + 
                ": It's 11 AM. Your morning turnip prices end in one hour!!")
        
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 12pm (new noon price)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 12 PM. Check on your afternoon turnip prices before 10 PM!")
        
        elif (current_datetime.hour == 21 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 9pm (1 hr before closing)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 9 PM, one hour before Nook's Cranny closes. Check on your afternoon turnip prices before 10 PM!")
        
        elif (current_datetime.hour == 22 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 10pm (closed)
            api.update_status(money_emoji + cross_mark_emoji + 
                ": It's 10 PM, and Nook's Cranny has closed for the night. Turnip prices will update tomorrow at 8am!")
        

    elif (todays_weekday == 1): # If it's Tuesday
        if (current_datetime.hour == 8 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 8am (open, new morning price)
            api.update_status(money_emoji + 
                ": Good morning! It's Tuesday, 8 AM. Don't forget to check on your morning turnip prices!")
        
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 11am (1 hr before new noon price)
            api.update_status(money_emoji + warning_emoji + 
                ": It's 11 AM. Your morning turnip prices end in one hour!!")
        
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 12pm (new noon price)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 12 PM. Check on your afternoon turnip prices before 10 PM!")
        
        elif (current_datetime.hour == 21 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 9pm (1 hr before closing)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 9 PM, one hour before Nook's Cranny closes. Check on your afternoon turnip prices before 10 PM!")
        
        elif (current_datetime.hour == 22 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 10pm (closed)
            api.update_status(money_emoji + cross_mark_emoji + 
                ": It's 10 PM, and Nook's Cranny has closed for the night. Turnip prices will update tomorrow at 8am!")
    
    
    elif (todays_weekday == 2): # If it's Wednesday
        if (current_datetime.hour == 8 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 8am (open, new morning price)
            api.update_status(money_emoji + 
                ": Good morning! It's Wednesday, 8 AM. Don't forget to check on your morning turnip prices!")
        
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 11am (1 hr before new noon price)
            api.update_status(money_emoji + warning_emoji + 
                ": It's 11 AM. Your morning turnip prices end in one hour!!")
        
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 12pm (new noon price)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 12 PM. Check on your afternoon turnip prices before 10 PM!")
        
        elif (current_datetime.hour == 21 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 9pm (1 hr before closing)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 9 PM, one hour before Nook's Cranny closes. Check on your afternoon turnip prices before 10 PM!")
        
        elif (current_datetime.hour == 22 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 10pm (closed)
            api.update_status(money_emoji + cross_mark_emoji + 
                ": It's 10 PM, and Nook's Cranny has closed for the night. Turnip prices will update tomorrow at 8am!")
    
    
    elif (todays_weekday == 3): # If it's Thursday
        if (current_datetime.hour == 8 and current_datetime.minute == 0 and current_datetime.second == 0):
            # If it's 8am (open, new morning price)
            api.update_status(money_emoji + 
                ": Good morning! It's Thursday, 8 AM. Don't forget to check on your morning turnip prices!")
        
        elif (current_datetime.hour == 11 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 11am (1 hr before new noon price)
            api.update_status(money_emoji + warning_emoji + 
                ": It's 11 AM. Your morning turnip prices end in one hour!!")
        
        elif (current_datetime.hour == 12 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 12pm (new noon price)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 12 PM. Check on your afternoon turnip prices before 10 PM!")
        
        elif (current_datetime.hour == 21 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 9pm (1 hr before closing)
            api.update_status(money_emoji + double_exclamation_emoji + 
                ": It's 9 PM, one hour before Nook's Cranny closes. Check on your afternoon turnip prices before 10 PM!")
        
        elif (current_datetime.hour == 22 and current_datetime.minute == 0 and current_datetime.second == 0):
            # elif 10pm (closed)
            api.update_status(money_emoji + cross_mark_emoji + 
                ": It's 10 PM, and Nook's Cranny has closed for the night. Turnip prices will update tomorrow at 8am!")
    elif (todays_weekday == 4): # If it's Friday
        pass
    elif (todays_weekday == 5): # If it's Saturday 
        pass
    
    
    
if __name__ == '__main__':
    
    auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)
    api = tweepy.API(auth)
    
    #api.update_status("test tweet")