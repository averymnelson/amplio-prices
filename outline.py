import mysql.connector
# needs to be hooked up to where you are hosting database not necessarily mysql
from datetime import datetime
# update time
import numpy
# perform math

def format_input(partnum):
    # clean input (probably just trimming, not much to do here)
    # locate and save database entry in sample on program
    # let user know if the record was found successfully
    pass
        
def clean_record():
    # param: record saved in main
    # call update prev, set others to None
    pass
    
def web_scraping(partnum):
    # calls to big sites if no api. put script in another file to update easier
    # https://www.mc-mc.com	
    # https://www.radwell.com
    pass

def api_calls(partnum):
    # calls to any others needed that do have api. preferred. in another file for update ease
    # none that I saw worth it, could be worth setting up amazon. 
    pass

def update_auction(partnum):
    # ebay call for past sales return latest sale or average of sales made in the last month
    # https://developer.ebay.com/api-docs/buy/marketplace-insights/overview.html 
    # item_sales resource for items sold in last 90 days. 
    pass

def update_prev():
    # move current average to previous average, update date last checked.
    # using sample update to age the records
    pass

def average_price():
    # average results of scrapes and api for retail. ebay or other good sites for auction. 
    # consider weights of average so more reliable sites are more important
    # depending on volume of sites included may be worth calculating std deviation to remove outliers.
    pass

def percent_change():
    # results of current average to previous average update
    # just a pull from sample saved on a given iteration to show relative change 
    pass

def print_results():
    # clean and format
    # write to db
    pass

def main():
    # user entry, UI. 
    curr_rec = None
    # set up for parallel run? if this is done need semaphore/mutex for a given record to ensure its only being edited once
    partnum = ""
    # update partnum to match user input
    format_input(partnum)
    if curr_rec is not None:
        update_prev()
        web_scraping(partnum)
        api_calls(partnum)
        update_auction(partnum)
        average_price()
        percent_change()
        print_results()
    pass

if __name__ == "__main__":
    main()