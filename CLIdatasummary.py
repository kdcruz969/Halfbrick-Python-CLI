import pandas
import matplotlib.pyplot as plt

def summarise(csv):
    df = pandas.read_csv(csv)
    
    #Classes for coloured text
    class txtcolour:
        RED = "\033[1;31;40m"
        GREEN = "\033[1;32;40m"
        YELLOW = "\033[1;33;40m"
        DEFAULT = "\033[0m"
    
    #remove row limit
    pandas.set_option('max_rows', None)
    head = df.describe()
    
    option = int
    
    #submenu for data summaries
    def menu():
        print(txtcolour.GREEN + "Please enter a number corresponding to one of the three program functions:")
        print("1. Player Data \n2. Installation Data \n3. Device Usage Data \n4. Recent Logins per Hour \n5. Exit" + txtcolour.DEFAULT)
        
        #check for valid input
        while True:
            try:
                option = int(input("Please enter option:"))
                #check if int is between 1 and 4
                if option <1 or option >5:
                    raise ValueError
                break
            except ValueError:
                print (txtcolour.RED + "Please enter a number from 1 to 5!" + txtcolour.DEFAULT)  

        #display player data        
        if option == 1:
            playerCount = df.groupby(['user_pseudo_id'])['user_pseudo_id'].size()       
            playerNo = len(playerCount)
            duplicates = df[df.duplicated(['user_pseudo_id'], keep=False)]
            countryPlayers = df.groupby(['geo_country'], dropna=False)['user_pseudo_id'].size()
            ad_tracking = df.groupby(['is_limited_ad_tracking'])['user_pseudo_id'].size()
        
            print("Number of Active Players: \n" + str(playerNo))
            print("Number of Active Players per Country: \n" + str(countryPlayers))
            print("Number of Players with Limited Ad Tracking: \n" +str(ad_tracking))
            
            input(txtcolour.GREEN + "Please press enter to continue..." + txtcolour.DEFAULT)
            menu()
            
        #display installation and version data
        elif option == 2:
            tech_details = df.groupby(['sku', 'app_version', 'device_os', 'device_os_version'])['user_pseudo_id'].size()
            print("Install Version Details: \n" + str(tech_details))
            input(txtcolour.GREEN + "Please press enter to continue..." + txtcolour.DEFAULT)
            menu()
        
        #display brand data
        elif option == 3:
            category_details = df.groupby(['device_category'])['user_pseudo_id'].size()
            brand_details = df.groupby(['device_brand_name'])['user_pseudo_id'].size()
            
            print("Device Usage: \n" + str(category_details))
            print("Brands: \n" + str(brand_details))
            print(txtcolour.GREEN + "For specific models, please enter a Device Category and Brand Name. To return, type exit " + txtcolour.DEFAULT)
            
            category = str
            brand_name = str
            
            while True:
                try:
                    category = input("Please enter a Device Category (or exit):")
                    #check if category is mobile or tablet
                    if category not in ['mobile', 'tablet', 'exit']:
                        raise ValueError
                    break
                except ValueError:
                    print (txtcolour.RED + "That is not a valid category, please try again..." + txtcolour.DEFAULT)
                
            if category == 'exit':
                False               
            else:    
                while True:
                    try:
                        brand_name = input("Please enter a brand:")
                        
                        search = df[(df['device_category'] == category) & (df['device_brand_name'] == brand_name)].groupby(['device_model_name']).size()
                        print("Results:\n" +str(search))
                        input(txtcolour.GREEN + "Please press enter to continue..." + txtcolour.DEFAULT)
                        break
                    except ValueError:
                        print (txtcolour.RED + "Invalid brand for chosen category, please try again..." + txtcolour.DEFAULT)                            
            menu()
         
        #plot logins per hour  
        elif option == 4:
            print(txtcolour.YELLOW + "Generating plot for logins per hour")
            
            dftime = pandas.read_csv(csv, parse_dates = True, index_col = ['timestamp_raw'])
            plt.figure(figsize=(12,12))
            dftime.resample('H').size().plot()
            
            plt.title('Logins per Hour')
            plt.ylabel('No. of Logins')
            plt.savefig("logindata")
            
            print("Done! Please check folder for plot image!" + txtcolour.DEFAULT)
            menu()
            
        else:
            return
        
    menu()
