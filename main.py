from exchangeApi import get_supported_currency_codes, get_currency_conversions, convert_currencies
from cryptoExchange import get_cryptocurrency_values, get_all_assets
from tkinter import *
from PIL import ImageTk,Image 
import os
# You can just hit the play button on the top right and you will see the tkinter window appear
# you need to close it to run another one
# todo is to make it look better maybe? or to setup the crypto currency thing, up to you


def setup_currency_converter(window: Tk):
    greeting = Label(text="Currency Converter", bg="light cyan")
    greeting.pack()
    supported_currency_codes = list(get_supported_currency_codes())
    OPTIONS = supported_currency_codes #etc

    start_currencies = StringVar(window)
    start_currencies.set(OPTIONS[0]) # default value

    target_currencies = StringVar(window)
    target_currencies.set(OPTIONS[0])

    option_start = OptionMenu(window, start_currencies, *OPTIONS)
    option_start.pack()

    option_target = OptionMenu(window, target_currencies, *OPTIONS)
    option_target.pack()

    amount_label = Label(text="Amount", bg="light cyan")
    amount_label.pack()
    amount = Entry(window)
    amount.pack()

    target_amount_label = Label(text="No conversion")
    target_amount_label.pack()

    #def crypto():
     #   try:
      #      original_amount = float(amount.get())
       #     start_currency = start_currencies.get()
        #    target_currency = target_currencies.get()
         #   
          #  target_amount = convert_currencies(from_currency_amount=original_amount, from_currency_code=start_currency, to_currency_code=target_currency)
#
 #           target_amount_label.config(text=f'{original_amount} {start_currency} is equivalent to {target_amount} {target_currency}')
  #      except:
   #         target_amount_label.config(text="Invalid Number!")


    def convert():
        try:
            original_amount = float(amount.get())
            start_currency = start_currencies.get()
            target_currency = target_currencies.get()
            
            target_amount = convert_currencies(from_currency_amount=original_amount, from_currency_code=start_currency, to_currency_code=target_currency)

            target_amount_label.config(text=f'{original_amount} {start_currency} is equivalent to {target_amount} {target_currency}')
        except:
            target_amount_label.config(text="Invalid Number!")
    button = Button(window, text="Convert", command=convert, bg="light cyan")
    button.pack()

def main() -> None:
    # TODO: Uncomment the calls to demonstrate that the program runs (commented for easier debugging)

    

    

    # GUI
    window = Tk()
    window.geometry("600x600")
    window.configure(bg="light blue")

    canvas = Canvas(window, width = 300, height = 300)      
    canvas.pack()   
    welcome_message = Label(text="\nWelcome to Atlantis! We understand that you might be confused with \nthat many currencies going around here, but we got you! Use our app toconvert currencies :)\n", bg="light blue")
    welcome_message.pack()
    img= (Image.open("Python/currencyConverter/img/logo.png"))   
    resized_image= img.resize((250,250), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    # img = ImageTk.PhotoImage(Image.open("Python/currencyConverter/img/logo.png"))
    canvas.create_image(20,20, anchor=NW, image=new_image)   

    # ExchangeAPI
    setup_currency_converter(window)

    #TODO
    # Crypto Exchange
    #API_KEY = '36B1A396-8BCC-4F20-A809-271BF3BAD7E9'
    #url = "https://rest-sandbox.coinapi.io/v1/{endpoint_name}?apikey=%s" % API_KEY
    #headers = {}    
    #params = {
    # If not included in the url itself, we can pass the API key
    # to the params argument. Just uncomment the line below:
    #'api_key': API_KEY
    #}
    #res = get(url=url, headers=headers, params=params)  
    
    # print(get_all_assets())
    

    window.mainloop()

    
if __name__ == "__main__":
    main()