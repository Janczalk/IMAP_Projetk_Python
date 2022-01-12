from tkinter import *
import smtplib

#testowac na https://mail.yandex.ru/?ncrnd=7110&uid=1545774597#message/178173660257845250
#mial: janekpapajek@yandex.ru
#haslo:Trudnehaslo123


#glowny ekran
master = Tk()
master.title('Custom Python Email App')

#okienko
Label(master, text="Aplikacja SMTP", font=('Calibri',15)).grid(row=0, sticky=N)
Label(master, text="Wypelnij ponizsze pola aby wyslac maila", font=('Calibri',11)).grid(row=1,sticky=N,padx=5)

Label(master, text="Email", font=('Calibri',11)).grid(row=2, sticky=W, padx=5)
Label(master, text="Haslo", font=('Calibri',11)).grid(row=3, sticky=W, padx=5)
Label(master, text="Do", font=('Calibri',11)).grid(row=4, sticky=W, padx=5)
Label(master, text="Temat", font=('Calibri',11)).grid(row=5, sticky=W, padx=5)
Label(master, text="Tresc", font=('Calibri',11)).grid(row=6, sticky=W, padx=5)
Label(master, text="Server", font=('Calibri',11)).grid(row=7, sticky=W, padx=5)
Label(master, text="Port", font=('Calibri',11)).grid(row=8, sticky=W, padx=5)

Notif = Label(master, text="", font=('Calibri', 11), fg="red")
Notif.grid(row=11, sticky=S, padx=5)

#funkcje

def send():
    uzytkownik = temp_uzytkownik.get()
    haslo = temp_haslo.get()
    do_kogo = temp_odbiorca.get()
    temat = temp_temat.get()
    tresc = temp_tresc.get()
    smtp = temp_smtp.get()
    port = temp_port.get()

    #code, msg = server.ehlo()
    if uzytkownik=="" or haslo=="" or do_kogo=="" or temat=="" or tresc=="" or smtp=="" or port=="":
        Notif.config(text="Uzupelnij wszystkie pola!", fg="red")
        return
    else:
        wiadomosc = 'Subject: {}\n\n{}'.format(temat, tresc)
        server = smtplib.SMTP_SSL(smtp, port)
        #server.starttls()
        server.login(uzytkownik, haslo)
        server.sendmail(uzytkownik, do_kogo, wiadomosc)
        Notif.config(text="Wiadomosc zostala wyslana", fg="green")


def reset():
    wprowadzUzytkownika.delete(0, 'end')
    WprowadzHaslo.delete(0, 'end')
    wprowadzOdbiorce.delete(0, 'end')
    wprowadzTemat.delete(0, 'end')
    wprowadzTresc.delete(0, 'end')
    wprowadzSMTP.delete(0,'end')
    #wprowadzPort.delete(0,'end')


#dane
temp_uzytkownik = StringVar()
temp_haslo = StringVar()
temp_odbiorca = StringVar()
temp_temat = StringVar()
temp_tresc = StringVar()
temp_smtp = StringVar()
temp_port = IntVar()


#Wprowadzanie danych
wprowadzUzytkownika = Entry(master, textvariable=temp_uzytkownik)
wprowadzUzytkownika.grid(row=2, column=0)
WprowadzHaslo = Entry(master, show="*", textvariable=temp_haslo)
WprowadzHaslo.grid(row=3, column=0)
wprowadzOdbiorce = Entry(master, textvariable=temp_odbiorca)
wprowadzOdbiorce.grid(row=4, column=0)
wprowadzTemat = Entry(master, textvariable=temp_temat)
wprowadzTemat.grid(row=5, column=0)
wprowadzTresc = Entry(master, textvariable=temp_tresc)
wprowadzTresc.grid(row=6, column=0)
wprowadzSMTP = Entry(master, textvariable=temp_smtp)
wprowadzSMTP.grid(row=7, column=0)
wprowadzPort = Entry(master, textvariable=temp_port)
wprowadzPort.grid(row=8, column=0)


#przyciski
Button(master, text="Wyslij", command=send).grid(row=9, sticky=W, pady=15, padx=5)
Button(master, text="Resetuj", command=reset).grid(row=9, sticky=W, padx=60, pady=60)

master.mainloop()

