import os
import time
try:
    from selenium import webdriver
    from colorama import init, Fore
except ModuleNotFoundError:
    os.system('pip install selenium')
    from selenium import webdriver
    os.system('pip install colorama')
    from colorama import init, Fore

init(autoreset=False)
os.system("cls")

print(f"{Fore.WHITE}Welcome To {Fore.RED}Doragon Lite!")

username = input(f"\n{Fore.LIGHTYELLOW_EX}[USERNAME]: {Fore.WHITE}")
password = input(f"{Fore.LIGHTYELLOW_EX}[PASSWORD]: {Fore.WHITE}")

target = input(f"\n{Fore.GREEN}[TARGET]: {Fore.WHITE}")
report_choice = input(f"\n{Fore.RED}(1) Profile \n(2) Stories \n(3) Highlights\n\n{Fore.WHITE}[?] Option: {Fore.WHITE}")
report_options = input(f"\n{Fore.RED}Choose A Reason! \n\n{Fore.WHITE}(1) Spam \n(2) Suicide, self injury\n(3) Sale of illegal or regulated goods\n(4) Nudity or sexual activity \n(5) Hate speech or symbols\n(6) Violence or dangerous organizations\n(7) Bullying or harassment\n\n{Fore.GREEN}[?] Option: {Fore.WHITE}") 
web = webdriver.Chrome()
web.get("https://www.instagram.com/")

time.sleep(5)

User_Login = username
user = web.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
user.click()
time.sleep(1)
user.send_keys(User_Login)

time.sleep(2)

User_Pass = password
passwrd = web.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
passwrd.click()
time.sleep(1)
passwrd.send_keys(User_Pass)

time.sleep(5)
# login button
web.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
time.sleep(7)
# say no to save login.
try:
    web.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
    print(f"{Fore.GREEN}[LOGGED_IN]{Fore.WHITE} Successfully logged in.")
except:
    print(f"{Fore.RED}[ERROR]{Fore.WHITE} There was an issue with your login. Please try again.")
    time.sleep(3)
    quit()

time.sleep(3)
# enters target links
web.get(f"https://www.instagram.com/{target}")

def profile():
    while True:
        # Click Three Dots In The Profile
        time.sleep(5)
        try:    
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div/button').click()
        except:
            print(f"{Fore.RED}[ERROR]{Fore.WHITE} You have banned the user @{target}.")
            time.sleep(3)
            quit()
        time.sleep(5)
        # Clicks Report Account
        web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/button[3]').click()
        time.sleep(7)
        # Clicks It's posting content that shouldn't be on Instagram
        web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[2]').click()
        time.sleep(7)
        web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[1]').click()
        time.sleep(7)
        
        if report_options == "1":
            time.sleep(5)
            # Reports Account For Spam
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[1]').click()
            time.sleep(5)
            # Close
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
            time.sleep(5)

        elif report_options == "2":
            time.sleep(5)
            # Clicks Self-injury Report Option
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[3]').click()
            time.sleep(5)
            # Submit Self-injury Report Option
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/button').click()
            time.sleep(5)
            # Close
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
            time.sleep(5)

        elif report_options == "3":
            time.sleep(5)
            # CLicks The Report for Sale of Illegal or Regulated Goods
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[4]').click()
            time.sleep(5)
            # Clicks Report For Drugs
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[2]/label/div/input').click()
            time.sleep(5)
            # Submit Report
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button').click()
            time.sleep(5)
            # Close
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
            time.sleep(5)

        elif report_options == "4":
            time.sleep(5)
            # Clicks Nudity or sexual activity on the report option
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[5]').click()
            time.sleep(5)
            # Clicks Non-consensual intimate images option
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[3]/label/div/input').click()
            time.sleep(5)
            # Submit Report
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button').click()
            time.sleep(5)
            # Close
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
            time.sleep(5)

        elif report_options == "5":
            time.sleep(5)
            # Clicks Report For Hate-speech
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[6]').click()
            time.sleep(5)
            # Submit Report
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/button').click()
            time.sleep(5)
            # Close
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
            time.sleep(5)        
        
        elif report_options == "6":
            time.sleep(5)
            # Reports For Violence or dangerous organizations
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[7]').click()
            time.sleep(5)
            # Selects Dangerous organizations or individuals
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[4]/label/div/input').click()
            time.sleep(5)
            # Submits Report
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button').click()
            time.sleep(5)
            # Close
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
            time.sleep(5)
        
        elif report_options == "7":
            time.sleep(5)
            # Reports For Bullying
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[8]').click()
            time.sleep(5)
            # Clicks "Bullying Me"
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[1]').click()
            time.sleep(5)
            # Submit
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/button').click()
            time.sleep(5)
            # Close
            web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
            time.sleep(5)

def get_stories():
    while True:
        web.get(f"https://instagram.com/stories/{target}/")
        time.sleep(5)
        try:
            web.find_element_by_xpath("//button[text()='View story']").click()
        except:
            print(f"{Fore.RED}[ERROR]{Fore.WHITE} There was an error getting the stories.")
            time.sleep(3)
            
        time.sleep(5)
        break
def stories():
    while True:
        time.sleep(4)
        # story click
        get_stories()
    
        while True:
            try:
                time.sleep(2)
                # click three dots at stories
                web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/section/div/header/div[2]/div[2]/button[3]').click()
                # report inapropiate
                time.sleep(4)
                web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/button[1]').click()
                
                if report_choice == "1":
                    # Reports For Spam
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[1]').click()
                    # Close
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()

                elif report_options == "2":
                    # click suicide and self injury
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[8]').click()
                    # submit report
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/button').click()
                    # close button
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)
                
                elif report_options == "3":
                    # Reports for Sale of Illegal or regulated goods
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[5]').click()
                    # Click Drugs
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[2]/label/div/input').click()
                    # Click Submit
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button').click()
                    # Close
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)

                elif report_options == "4":
                    # Reports for Nudity
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[2]').click()
                    time.sleep(2)
                    # Selects Nudity Or Pornography
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[1]/label/div/input').click()
                    time.sleep(2)
                    # Submit
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button').click()
                    time.sleep(2)
                    # Close
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()    
                    time.sleep(5)

                elif report_choice == "5":
                    # Reports For Hate Speech
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[3]').click()
                    # Submit Report
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/button').click()
                    time.sleep(2)
                    # Close
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)

                elif report_choice == "6":
                    # Reports For Violence
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[4]').click()
                    # Selects Dangerous organizations
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[1]/label/div/input').click()
                    # Submit Report
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button').click()
                    time.sleep(2)
                    # Close
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)

                elif report_choice == "7":
                    # Reports For Bullying 
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[6]').click()
                    # Clicks Bullying "Me"
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[1]').click()
                    # Submit Report
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/button').click()
                    time.sleep(2)
                    # Close
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)
            except:
                break

def highlights():
    while True:

        web.get(f"https://instagram.com/{target}/")
        time.sleep(7)
        # click highlights
        web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[1]/div/div/div/ul/li[3]/div/div/div[1]').click()
        time.sleep(4)

        while True:
            try:
                time.sleep(2)
                # click 3 dots
                web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/header/div[2]/div[2]/button[3]').click()
                # report inappropriate
                time.sleep(4) 
                web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/button[1]').click()
                
                if report_choice == "1":
                    # Report For Spam
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]').click()
                    # Close
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)

                elif report_options == "2":
                    # click self-injury
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[8]').click()
                    # submit report
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/button').click()
                    # close
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)

                elif report_options == "3":
                    # Report For Sale Of Illegal or regulated goods
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[5]')
                    # Clicks Drugs
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[2]/label/div/input').click()
                    # Submit
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button').click()
                    # close
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)

                elif report_options == "4":
                    # Reports For Nudity
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[2]').click()
                    # Clicks Nudity Or Pornography
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[1]/label/div/input').click()
                    # Submit Report
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button').click()
                    # close
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)
                
                elif report_options == "5":
                    # Reports For Hate Speech
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[3]').click()
                    # Submit
                    time.sleep(2) 
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/button').click()
                    # close
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)
                
                elif report_options == "6":
                    # Report For Violence
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[4]').click()
                    # Clicks Dangerous organizations
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/fieldset/div[1]/label/div/input').click()
                    # Submit Report
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[6]/button').click()
                    # close
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)

                elif report_options == "7":
                    # Report For Bullying
                    time.sleep(3)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[6]').click()
                    # Reports For "Bullying Me
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[3]/button[1]')
                    # Submit Repor
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/button').click()
                    # close
                    time.sleep(2)
                    web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[4]/button').click()
                    time.sleep(5)
            except:
                break


if report_choice == "1":
    profile()
elif report_choice == "2":
    stories()
elif report_choice == "3":
    highlights()
else:
    print("Incorrect Choice.")
    time.sleep(2.5)
    quit()
