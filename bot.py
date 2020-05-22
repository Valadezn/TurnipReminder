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
    
    
    if (todays_weekday == 6): # If it's Saturday
        # If it's 5am (Daisy Mae appears)
        # elif it's 11am (1 hr before daisy mae disappears)
        # elif it's 12pm (Daisy mae disappears)
        print("It's Sunday")
    elif (todays_weekday == 0): # If it's Monday
        # Write something like "happy monday!"
        
        # If it's 8am (open, new morning price)
        # elif 11am (1 hr before new noon price)
        # elif 12pm (new noon price)
        # elif 9pm (1 hr before closing)
        # elif 10pm (closed)
        pass
    elif (todays_weekday == 1): # If it's Tuesday
        pass
    elif (todays_weekday == 2): # If it's Wednesday
        pass
    elif (todays_weekday == 3): # If it's Thursday
        pass
    elif (todays_weekday == 4): # If it's Friday
        pass
    elif (todays_weekday == 5): # If it's Saturday 
        pass
    
    
    
if __name__ == '__main__':
    
    auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
    auth.set_access_token(credentials.access_token, credentials.access_token_secret)
    api = tweepy.API(auth)
    
    #api.update_status("test tweet")