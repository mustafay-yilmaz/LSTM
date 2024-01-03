from tkinter import *
import predictf,webbrowser
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#010101"
FONT_NAME = "Courier"

entry_kelime = ""
entry_sayi = ""
logo2=""
logo = ""
button_bg = ""

github_logo = ""
linkdin_logo = ""
def choose_project():
    temizle()
    label = Label(text="Hangi projeyi kullanmak istiyorsunuz?",font=(FONT_NAME,30,"normal"),bg=YELLOW,fg=GREEN)
    canvas = Canvas(height=500,width=800,bg=YELLOW,highlightthickness=0)
    global logo2
    logo2 = PhotoImage(file="img/logoMavi.png")
    global logo
    logo = PhotoImage(file="img/logoPembe.png")
    ali_gpt_button = Button(command=ali_gpt_scene,bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)
    ali_gpt_button.config(text="Ali-Gpt")
    
    back_button = Button(command=ana_sayfa,bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)
    back_button.config(text="Geri Dön")
    
    m_gpt_button = Button(command=mustafaGpt_scene,bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)
    m_gpt_button.config(text="Mustafa-Gpt")
    canvas.create_image(100,250,image=logo)
    canvas.create_image(700,250,image=logo2)
    
    label.grid(column=1,row=1,columnspan=4)
    canvas.grid(column=1,row=2,columnspan=3) 
    ali_gpt_button.grid(column=1,row=3)
    m_gpt_button.grid(column=3,row=3)
    back_button.grid(column=2,row=4)
    
    
    
def linkac(site,kisi):
    if(site == "github"):
        if(kisi == "ali"):
            webbrowser.open_new("https://github.com/Alidari")
        else:
            webbrowser.open_new("https://github.com/wassapman")
    else:
        if(kisi == "ali"):
            webbrowser.open_new("https://www.linkedin.com/in/ali-dar%C4%B1-a56ab6222?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
        else:
            webbrowser.open_new("https://www.linkedin.com/in/mustafa-y%C3%BCksel-y%C4%B1lmaz-02451b227?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")        


def generate_text(label,projeName,kelime=""):
    if(projeName == "auto"):
        kelime = entry_kelime.get()
        try:
            kelime_sayi = int(entry_sayi.get())
            kelime_sayi -= 1
        except:
            kelime_sayi=7
        generated_text = predictf.predict_cumle(1,projeName,kelime,kelime_sayi)
    else:
        generated_text = predictf.predict_cumle(1,projeName,kelime)[0][0]  
    label.config(text=generated_text)
     
     
def temizle():
    widgets = window.winfo_children()
    for widget in widgets:
            widget.destroy()
            
            
def whats_scene():
    temizle()
    whats_text = "Projemiz Doğal Dil İşleme algoritması olan LSTM algoritmasını kullanarak, \
    makine öğrenmesi sayesinde rastgele Türkçe kelime ve cümle üretebilmektedir.\
    Projemizde LSTM algoritması modelinin iç yapısı detaylı şekilde açıklanıp kullanılmaktadır ve hazır model ile manuel hazırlanmış model \
    çalıştırılıp doğruluk, kayıp ve karmaşıklık gibi değerleri karşılaştırılmaktadır. 2 adet veri seti kullanılmıştır. \
    İlk veri seti Oğuz Atay’ın Tutunamayanlar kitabından alınmış olup toplam 963 cümle bulunmaktadır. İkinci veri setinde 5749 cümle bulunmaktadır.\
    ALİ-GPT, manuel olarak hazırlanmış lstm modelidir ve rastgele cümleler üretir. MUSTAFA-GPT ise hazır model kullanılarak üretilmiş olup verdiğiniz\
    kelimeye göre cümleler üretir"
    label_main = Label(text="NEDİR?",font=(FONT_NAME,40,"normal"),bg=YELLOW,fg=GREEN)
    label = Label(text=whats_text,font=(FONT_NAME,10,"normal"),bg=YELLOW,fg=RED,wraplength=400)
    
    back_button = Button(command=ana_sayfa,bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)
    back_button.config(text="Geri Dön <--")
    
    label_main.grid(column=1,row=1,pady=50)
    label.grid(column=1,row=2,pady=50)
    back_button.grid(column=1,row=3,pady=10)
    

def ali_gpt_scene():
    temizle()
    label = Label(text="ALİ-GPT",font=(FONT_NAME,40,"normal"),bg=YELLOW,fg=GREEN)
    canvas = Canvas(height=500,width=500,bg=YELLOW,highlightthickness=0)
    global logo
    logo = PhotoImage(file="img/logoPembe.png")
    canvas.create_image(250, 250, image=logo)
    
    generate_text_label = Label(text="Henüz bir cümle oluşturmadınız",font=(FONT_NAME,10,"normal"),bg=YELLOW,fg=PINK,wraplength=300)
    generate_button = Button(command=lambda:generate_text(generate_text_label,"manuel"),bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)
    back_button = Button(command=choose_project,bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)
    back_button.config(text="Geri Dön")
    generate_button.config(text="Cumle Olustur")
    label.grid(column=1,row=0)
    canvas.grid(column=1,row=1)
    generate_text_label.grid(column=1,row=2)
    generate_button.grid(column=1,row=3)
    back_button.grid(column=1,row=4)
    
    
    
def mustafaGpt_scene():
    temizle()
    label = Label(text="Mustafa-GPT",font=(FONT_NAME,40,"normal"),bg=YELLOW,fg=GREEN)
    canvas = Canvas(height=500,width=500,bg=YELLOW,highlightthickness=0)
    global logo
    logo = PhotoImage(file="img/logoMavi.png")
    canvas.create_image(250, 250, image=logo)
    
    generate_text_label = Label(text="Henüz bir cümle oluşturmadınız",font=(FONT_NAME,10,"normal"),bg=YELLOW,fg=PINK,wraplength=300)
    global entry_kelime
    entry_kelime = Entry(width=30)
    entry_kelime.insert(0,"Bir kelime gir")
    
    global entry_sayi
    entry_sayi = Entry(width=30)
    entry_sayi.insert(0,"Kelime sayisini giriniz")
    
    generate_button = Button(command=lambda:generate_text(generate_text_label,"auto"),bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)
    back_button = Button(command=choose_project,bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)
    back_button.config(text="Geri Dön")
    generate_button.config(text="Cumle Olustur")
    label.grid(column=1,row=0)
    canvas.grid(column=1,row=1)
    generate_text_label.grid(column=1,row=2)
    entry_kelime.grid(column=0,row=4)
    entry_sayi.grid(column=0,row=5)
    generate_button.grid(column=1,row=3)
    back_button.grid(column=1,row=6)
        
    # Add widgets or elements to the new scene
def creators_scene():
    temizle()
    label = Label(text="YAPIMCILAR",font=(FONT_NAME,40,"normal"),bg=YELLOW,fg=GREEN)
    label_cr = Label(text="Ali Darı ve Mustafa Yüksel Yılmaz",font=(FONT_NAME,25,"normal"),bg=YELLOW,fg=RED)
    
    global github_logo
    github_logo = PhotoImage(file="img/github.png")
    global linkdin_logo
    linkdin_logo = PhotoImage(file="img/linkdin.png")
    
    a_github_button =  Button(command=lambda:linkac("github","ali"),bg=YELLOW,image=github_logo, bd=0, compound=CENTER,relief=FLAT)
    m_github_button =  Button(command=lambda:linkac("github","mustafa"),bg=YELLOW,image=github_logo, bd=0, compound=CENTER,relief=FLAT)
    a_linkdin_button =  Button(command=lambda:linkac("linkdin","ali"),bg=YELLOW,image=linkdin_logo, bd=0, compound=CENTER,relief=FLAT)
    m_linkdin_button =  Button(command=lambda:linkac("linkdin","mustafa"),bg=YELLOW,image=linkdin_logo, bd=0, compound=CENTER,relief=FLAT)
    
    label_contact = Label(text="İletişim",font=(FONT_NAME,15,"normal"),bg=YELLOW,fg=BLACK)
    label_ali = Label(text="Ali Darı",font=(FONT_NAME,15,"normal"),bg=YELLOW,fg=PINK)
    label_mustafa = Label(text="Mustafa Yüksel \nYılmaz",font=(FONT_NAME,15,"normal"),bg=YELLOW,fg=PINK)    
    
    
    
    back_button = Button(command=ana_sayfa,bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)
    back_button.config(text="Geri Dön")
    
    label.grid(column=2, row=1,pady=20)
    label_cr.grid(column=2, row=2,pady=20)
    label_contact.grid(column=2, row=3,pady=20)

    label_ali.grid(column=0, row=4, columnspan=2,pady=20)

    a_github_button.grid(column=0, row=5, padx=10,pady=20)
    a_linkdin_button.grid(column=1, row=5, padx=10,pady=20)

    label_mustafa.grid(column=3, row=4,columnspan=2,pady=20)
    m_github_button.grid(column=3, row=5, padx=10,pady=20)
    m_linkdin_button.grid(column=4, row=5, padx=10,pady=20)

    back_button.grid(column=2, row=6,pady=20)

    
def ana_sayfa():
    temizle()
    global button_bg
    button_bg = PhotoImage(file="img/buttonBg.png")

    start_button = Button(command=choose_project,bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)
    whats_button = Button(command=whats_scene,bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)
    creators_button = Button(command=creators_scene,bg=YELLOW,image=button_bg, bd=0, compound=CENTER,relief=FLAT)

    start_button.config(text="Başla",font=("Arial", 10))
    whats_button.config(text="Nedir?",font=("Arial", 10))
    creators_button.config(text="Yapımcılar",font=("Arial", 10))


    label = Label(text="M&A-GPT",font=(FONT_NAME,40,"normal"),bg=YELLOW,fg=GREEN)


    canvas = Canvas(height=500,width=500,bg=YELLOW,highlightthickness=0)

    global logo
    logo = PhotoImage(file="img/logoMavi.png")

    canvas.create_image(250,250,image=logo)



    canvas.grid(column=1,row=1,pady=10)
    whats_button.grid(column=1,row=3,pady=10)
    creators_button.grid(column=1,row=4,pady=10)
    start_button.grid(column=1,row=2,pady=10)
    label.grid(row=0,column=1)



window = Tk()
window.title("M&A-GPT")
window.config(padx=100,pady=100,bg=YELLOW)
ana_sayfa()

window.mainloop()
