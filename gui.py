import tkinter as tk
from tkinter import *
from pycoingecko import CoinGeckoAPI
from PIL import Image, ImageFont, ImageDraw

window = Tk()

window.geometry('200x200')

window.title("Cryptoblades Calculator")

lbl = Label(window, text="3* Blade Price")
lbl1 = Label(window, text="4* Blade Price")
lbl2 = Label(window, text="5* Blade Price")
lbl3 = Label(window, text="4 Chars Lvl 1")
lbl4 = Label(window, text="Gas fee BNB")
lbl5 = Label(window, text="3* gain/fight")
lbl6 = Label(window, text="4* gain/fight")
lbl7 = Label(window, text="5* gain/fight")

txt = Entry(window,width=10)
txt1 = Entry(window,width=10)
txt2 = Entry(window,width=10)
txt3 = Entry(window,width=10)
txt4 = Entry(window,width=10)
txt5 = Entry(window,width=10)
txt6 = Entry(window,width=10)
txt7 = Entry(window,width=10)

txt.grid(column=1, row=0)
txt1.grid(column=1, row=1)
txt2.grid(column=1, row=2)
txt3.grid(column=1, row=3)
txt4.grid(column=1, row=4)
txt5.grid(column=1, row=5)
txt6.grid(column=1, row=6)
txt7.grid(column=1, row=7)

lbl.grid(column=0, row=0)
lbl1.grid(column=0, row=1)
lbl2.grid(column=0, row=2)
lbl3.grid(column=0, row=3)
lbl4.grid(column=0, row=4)
lbl5.grid(column=0, row=5)
lbl6.grid(column=0, row=6)
lbl7.grid(column=0, row=7)

def clicked():
    three_star_price = float(txt.get()) * price_skill
    four_star_price = float(txt1.get()) * price_skill
    five_star_price = float(txt2.get()) * price_skill
    four_chars = float(txt3.get()) * 4 * price_skill
    gas = float(txt4.get()) * price_bnb * 864
    write_3_star(three_star_price, four_chars, gas)
    write_4_star(four_star_price, four_chars, gas)
    write_5_star(five_star_price, four_chars, gas)


#SCRIPT START
cg = CoinGeckoAPI()
dict_skill = cg.get_price(ids='CryptoBlades', vs_currencies='usd')
dict_bnb = cg.get_price(ids='Binance Coin', vs_currencies='usd')

for key, value in dict_skill.items() :
    for k, v in value.items():
        price_skill = float(v)

for key, value in dict_bnb.items() :
    for k, v in value.items():
        price_bnb = float(v)

test = txt1.get()



def write_3_star(three_star_price, four_chars, gas,):
    my_image = Image.open('resources/3_star_Build_black_empty.png')
    title_font = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 70)
    title_font2 = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 20)
    title_font3 = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 13)
    title_font4 = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 15)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((450, 290), "$" +str(int(803 * (float(txt5.get()) * price_skill) - gas)), (250, 250, 250),font=title_font)  # Monthly Earnings
    image_editable.text((165, 483), "$" + str(round(three_star_price, 2)), (10, 10, 10), font=title_font2)         # 3* blade
    image_editable.text((165, 510), "$" + str(round(four_chars, 2)), (10, 10, 10), font=title_font2)               # 4 chars lvl 1
    image_editable.text((165, 535), "$" + str(round(gas, 2)), (10, 10, 10), font=title_font2)                      # Gas fees
    image_editable.text((580, 455), "803", (10, 10, 10), font=title_font2)                                         # Good player wpm
    image_editable.text((677, 460), str(int(803 * (float(txt5.get()) * price_skill))), (10, 10, 10),font=title_font4)          # Good player epm
    image_editable.text((740, 460), str(int(803 * (float(txt5.get()) * price_skill) * 2)), (10, 10, 10),font=title_font4)      # Good player epm x2
    image_editable.text((580, 485), "734", (10, 10, 10), font=title_font2)                                         # Avg player wpm
    image_editable.text((677, 485), str(int(734 * (float(txt5.get()) * price_skill))), (10, 10, 10),font=title_font4)          # Avg player epm
    image_editable.text((740, 485), str(int(734 * (float(txt5.get()) * price_skill) * 2)), (10, 10, 10),font=title_font4)      # Avg player epm x2
    image_editable.text((706, 545), str(round(price_skill, 2)), (10, 10, 10), font=title_font3)                    # Skill price
    my_image.save('3_star.png')


def write_4_star(four_star_price, four_chars, gas):
    my_image = Image.open('resources/4_star_Build_empty.png')
    title_font = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 70)
    title_font2 = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 20)
    title_font3 = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 16)
    title_font4 = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 17)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((450, 290), "$" +str(int(803*(float(txt6.get())*price_skill)-gas)), (250, 250, 250), font=title_font)   #Monthly Earnings
    image_editable.text((165, 483), "$"+str(round(four_star_price, 2)), (10, 10, 10), font=title_font2)        #4* blade
    image_editable.text((165, 510), "$"+str(round(four_chars, 2)), (10, 10, 10), font=title_font2)             #4 chars lvl 1
    image_editable.text((165, 535), "$"+str(round(gas, 2)), (10, 10, 10), font=title_font2)                     #Gas fees
    image_editable.text((550, 460), "803", (10, 10, 10), font=title_font2)                                     #Good player wpm
    image_editable.text((687, 465), str(int(803*(float(txt6.get())*price_skill))), (10, 10, 10), font=title_font4)         #Good player epm
    image_editable.text((755, 465), str(int(803*(float(txt6.get())*price_skill)*2)), (10, 10, 10), font=title_font4)       #Good player epm x2
    image_editable.text((550, 490), "734", (10, 10, 10), font=title_font2)                                     #Avg player wpm
    image_editable.text((687, 495), str(int(734*(float(txt6.get())*price_skill))), (10, 10, 10), font=title_font4)         #Avg player epm
    image_editable.text((755, 495), str(int(734*(float(txt6.get())*price_skill)*2)), (10, 10, 10), font=title_font4)       #Avg player epm x2
    image_editable.text((709, 541), str(round(price_skill, 2)), (10, 10, 10), font=title_font3)                #Skill price
    my_image.save('4_star.png')


def write_5_star(five_star_price, four_chars, gas):
    my_image = Image.open('resources/5_star_Build_black_empty.png')
    title_font = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 70)
    title_font2 = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 20)
    title_font3 = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 16)
    title_font4 = ImageFont.truetype('resources/NotoSansJP-Bold.otf', 17)
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((450, 290), "$" +str(int(803*(float(txt7.get())*price_skill)-gas)), (250, 250, 250), font=title_font)   #Monthly Earnings
    image_editable.text((165, 483), "$"+str(round(five_star_price, 2)), (10, 10, 10), font=title_font2)        #5* blade
    image_editable.text((165, 510), "$"+str(round(four_chars, 2)), (10, 10, 10), font=title_font2)             #4 chars lvl 1
    image_editable.text((165, 535), "$"+str(round(gas, 2)), (10, 10, 10), font=title_font2)                    #Gas fees
    image_editable.text((550, 460), "803", (10, 10, 10), font=title_font2)                                     #Good player wpm
    image_editable.text((667, 458), str(int(803*(float(txt7.get())*price_skill))), (10, 10, 10), font=title_font4)         #Good player epm
    image_editable.text((740, 458), str(int(803*(float(txt7.get())*price_skill)*2)), (10, 10, 10), font=title_font4)       #Good player epm x2
    image_editable.text((550, 490), "734", (10, 10, 10), font=title_font2)                                     #Avg player wpm
    image_editable.text((667, 488), str(int(734*(float(txt7.get())*price_skill))), (10, 10, 10), font=title_font4)         #Avg player epm
    image_editable.text((740, 488), str(int(734*(float(txt7.get())*price_skill)*2)), (10, 10, 10), font=title_font4)       #Avg player epm x2
    image_editable.text((595, 538), str(round(price_skill, 2)), (10, 10, 10), font=title_font3)                #Skill price
    my_image.save('5_star.png')


btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=1, row=8)
window.mainloop()
