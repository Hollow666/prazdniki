import tkinter as tk
from tkinter import *
from tkinter import Button
from tkinter import messagebox as mb
from tkinter import Label
from tkinter import Entry


def button_click():
    global input
    try:
        god = int(input.get())
    except ValueError:
        mb.showerror('CRITICAL ERROR', 'Введите число!', font='Arial 10')
    else:
        vek = god // 100
        if vek+1 < 16:
            mb.showerror('CRITICAL ERROR', 'Введите год похже XVI века!')
            return
        else:
            raznica = 10
            for i in range(16, vek+1, 1):
                if i % 4 > 0:
                    raznica += 1
            label_raznica.config(text=f'Разнница между календарями: {raznica}')
            mod1 = (19 * (god % 19)) + 15
            mod2 = mod1 % 30
            a = mod2
            mod3 = 2*(god % 4)
            mod4 = 4*(god % 7)
            temp = mod3+mod4+(6*a)+6
            mod5 = temp % 7
            b = mod5
            if a + b > 9:
                dy = a + b - 9
                label_PU.config(text=f'Пасха: {dy} апреля.')
                dg = dy + raznica
                if dg > 30:
                    dg = dg - 30
                    label_PG.config(text=f'Пасха: {dg} мая.')
                    temp = dg - 7
                    if temp == 0:
                        label_VERB_U.config(text=f'Вербное воскресенье: {30 - raznica} апреля.')
                        label_VERB_G.config(text='Вербное воскресенье: 30 апреля.')
                    elif temp < 0:
                        label_VERB_U.config(text=f'Вербное воскресенье: {30 + temp - raznica} апреля.')
                        label_VERB_U.config(text=f'Вербное воскресенье: {30 + temp} апреля.')
                    elif temp > 0:
                        if temp - raznica == 0:
                            label_VERB_U.config(text='Вербное воскресенье: 30 апреля.')
                        if (temp - raznica) > 0:
                            label_VERB_U.config(text=f'Вербное воскресенье: {temp - raznica} мая.')
                        if (temp - raznica) < 0:
                            label_VERB_U.config(text=f'Вербное воскресенье: {30 + temp - raznica} апреля.')
                        label_VERB_G.config(text=f'Вербное воскресенье: {temp} мая.')
                    temp1 = dg + 40
                    temp1 = temp1 - 31
                    if temp1 < 30:
                        if temp1 - 1 - raznica > 0:
                             label_VOZ_U.config(text=f'Вознесение Христа: {temp1 - 1 - raznica} июня.')
                        if temp1 - 1 - raznica == 0:
                            label_VOZ_U.config(text=f'Вознесение Христа: 31 мая.')
                        if temp1 - 1 - raznica < 0:
                            label_VOZ_U.config(text=f'Вознесение Христа: {31 + (temp1 - 1 - raznica)} мая.')
                        label_VOZ_G.config(text=f'Вознесение Христа: {temp1 - 1} июня.')
                    if temp1 == 30:
                        label_VOZ_U.config(text=f'Вознесение Христа: {30 - 1 - raznica} июня.')
                        label_VOZ_G.config(text=f'Вознесение Христа: {30 - 1} июня.')
                    if temp1 > 30:
                        if temp1 == 1:
                            label_VOZ_U.config(text=f'Вознесение Христа: {30 - raznica}  июня.')
                            label_VOZ_G.config(text=f'Вознесение Христа: 30 июня.')
                        else:
                            if temp1 - 30 - 1 - raznica > 0:
                                label_VOZ_U.config(text=f'Вознесение Христа: {temp1 - 30 - 1 - raznica} июля.')
                            if temp1 - 30 - 1 - raznica == 0:
                                label_VOZ_U.config(text=f'Вознесение Христа: 30 июня.')
                            if temp1 - 30 - 1 - raznica < 0:
                                label_VOZ_U.config(text=f'Вознесение Христа: {30 + (temp1 - 30 - 1 - raznica)} июня.')
                            label_VOZ_G.config(text=f'Вознесение Христа: {temp1 - 30 - 1} июля.')
                    temp2 = dg + 50
                    temp2 = temp2 - 31
                    if temp2 > 30:
                        temp2 = temp2 - 30
                        if temp2 == 1:
                            label_TR_U.config(text=f'Троица: {30 - raznica} июня.')
                            label_TR_G.config(text='Троица: 30 июня.')
                        else:
                            if temp2 - 1 - raznica > 0:
                                label_TR_U.config(text=f'Троица: {temp2 - 1 - raznica} июля.')
                            if temp2 - 1 - raznica == 0:
                                label_TR_U.config(text=f'Троица: 30 июня.')
                            if temp2 - 1 - raznica < 0:
                                label_TR_U.config(text=f'Троица: {30 + (temp2 - 1 - raznica)} июня.')
                            label_TR_G.config(text=f'Троица: {temp2 - 1} июля.')
                    else:
                        if temp2 == 30:
                            label_TR_U.config(text=f'Троица: {30 - 1 - raznica} июня.')
                            label_TR_G.config(text=f'Троица: {30 - 1} июня.')
                        else:
                            if temp2 - 1 - raznica > 0:
                                label_TR_U.config(text=f'Троица: {temp2 - 1 - raznica} июня.')
                            if temp2 - 1 - raznica == 0:
                                label_TR_U.config(text=f'Троица: 31 мая.')
                            if temp2 - 1 - raznica < 0:
                                label_TR_U.config(text=f'Троица: {31 + (temp2 - 1 - raznica)} мая.')
                            label_TR_G.config(text=f'Троица: {temp2 - 1} июня.')
                    temp2 = dg + 50
                    temp2 = temp2 - 31
                    if temp2 > 30:
                        temp2 = temp2 - 30
                        if temp2 == 1:
                            label_DS_U.config(text=f'День Святого Духа: {30 + (1 - raznica)} июня.')
                            label_DS_G.config(text=f'День Святого Духа: 1 июля.')
                        else:
                            if temp2 - raznica > 0:
                                label_DS_U.config(text=f'День Святого Духа: {temp2 - raznica} июля.')
                            if temp2 - raznica == 0:
                                label_DS_U.config(text=f'День Святого Духа: 30 июня.')
                            if temp2 - raznica < 0:
                                label_DS_U.config(text=f'День Святого Духа: {30 + (temp2 - raznica)} июня.')
                            label_DS_G.config(text=f'День Святого Духа: {temp2} июля.')
                    else:
                        if temp2 == 30:      
                            label_DS_U.config(text=f'День Святого Духа: {30 - raznica} июня.')
                            label_DS_G.config(text=f'День Святого Духа: {30} июня.')
                        else:                   
                            if temp2 - raznica > 0:
                                label_DS_U.config(text=f'День Святого Духа: {temp2 - raznica} июня.')
                            if temp2 - raznica == 0:
                                label_DS_U.config(text=f'День Святого Духа: 31 мая.')
                            if temp2 - raznica < 0:
                                label_DS_U.config(text=f'День Святого Духа: {31 + (temp2 - raznica)} мая.')
                            label_DS_G.config(text=f'День Святого Духа: {temp2} июня.')
                else:
                    
                    textBox5.Text := inttostr (dg) + ' апреля.';
                    temp:=dg-7;
                    if temp=0 then
                        begin
                        textBox6.Text := inttostr (31-raznica) + ' марта.';
                        textBox7.Text := '31 марта.';
                        end;
                    if temp>0 then
                        begin
                        if (temp-raznica)=0 then
                        textBox6.Text := '31 марта.';
                        if (temp-raznica)>0 then
                        textBox6.Text := inttostr (temp-raznica) + ' апреля.';
                        if (temp-raznica)<0 then
                        textBox6.Text := inttostr (31+(temp-raznica)) + ' марта.';
                        textBox7.Text := inttostr (temp) + ' апреля.';
                        end;
                    if temp<0 then
                        begin
                        textBox6.Text := inttostr ((31+temp)-raznica) + ' марта.';
                        textBox7.Text := inttostr (31+temp) + ' марта.';
                        end;
                    temp1:=dg+40;
                    temp1:=temp1-30;
                    if temp1<31 then
                        begin
                        if temp1-1-raznica<0 then
                        textBox8.Text := inttostr (30+(temp1-1-raznica)) + ' апреля.';
                        if temp1-1-raznica=0 then
                        textBox8.Text := '30 апреля.';
                        if temp1-1-raznica>0 then
                        textBox8.Text := inttostr (temp1-1-raznica) + ' мая.';
                        textBox9.Text := inttostr (temp1-1) + ' мая.';
                        end;
                    if temp1=31 then
                        begin
                        textBox8.Text := inttostr (31-1-raznica) + ' мая.';
                        textBox9.Text := inttostr (31-1) + ' мая.';
                        end;
                    if temp1>31 then
                        begin
                        if temp1-31=1 then
                            begin
                            textBox8.Text := inttostr (31-raznica) + ' мая.';
                            textBox9.Text := '31 мая.';
                            end
                        else
                            begin
                            if temp1-31-1-raznica>0 then
                            textBox8.Text := inttostr (temp1-31-1-raznica) + ' июня.';
                            if temp1-31-1-raznica=0 then
                            textBox8.Text := '31 мая.';
                            if temp1-31-1-raznica<0 then
                            textBox8.Text := inttostr (31+(temp1-31-1-raznica)) + ' мая.';
                            textBox9.Text := inttostr (temp1-31-1) + ' июня.';
                            end;
                        end;
                    temp2:=dg+50;
                    temp2:=temp2-30;
                    if temp2>31 then
                        begin
                        temp2:=temp2-31;
                        if temp2=1 then
                            begin
                            textBox10.Text := inttostr (31-raznica) + ' мая.';
                            textBox11.Text := '31 мая.';
                            end
                        else
                            begin
                            if temp2-1-raznica>0 then
                            textBox10.Text := inttostr (temp2-1-raznica) + ' июня.';
                            if temp2-1-raznica=0 then
                            textBox10.Text := '31 мая.';
                            if temp2-1-raznica<0 then
                            textBox10.Text := inttostr (31+(temp2-1-raznica)) + ' мая.';
                            textBox11.Text := inttostr (temp2-1) + ' июня.';
                            end;
                        end
                    else
                        begin
                        if temp2=31 then
                            begin
                            textBox10.Text := inttostr (31-1-raznica) + ' мая.';
                            textBox11.Text := inttostr (31-1) + ' мая.';
                            end
                        else
                            begin
                            if temp2-1-raznica>0 then
                            textBox10.Text := inttostr (temp2-1-raznica) + ' мая.';
                            if temp2-1-raznica=0 then
                            textBox10.Text := '30 апреля.';
                            if temp2-1-raznica<0 then
                            textBox10.Text := inttostr (30+(temp2-1-raznica)) + ' апреля.';
                            textBox11.Text := inttostr (temp2-1) + ' мая.';
                            end;
                        end;
                    temp2:=dg+50;
                    temp2:=temp2-30;
                    if temp2>31 then
                        begin
                        temp2:=temp2-31;
                        if temp2=1 then
                            begin
                            textBox12.Text := inttostr (31+(1-raznica)) + ' мая.';
                            textBox13.Text := '1 июня.';
                            end
                        else
                            begin
                            if temp2-raznica>0 then
                            textBox12.Text := inttostr (temp2-raznica) + ' июня.';
                            if temp2-raznica=0 then
                            textBox12.Text := '31 мая.';
                            if temp2-raznica<0 then
                            textBox12.Text := inttostr (31+(temp2-raznica)) + ' мая.';
                            textBox13.Text := inttostr (temp2) + ' июня.';
                            end;
                        end
                    else
                        begin
                        if temp2=31 then
                            begin
                            textBox12.Text := inttostr (31-raznica) + ' мая.';
                            textBox13.Text := inttostr (31) + ' мая.';
                            end
                        else
                            begin
                            if temp2-raznica>0 then
                            textBox12.Text := inttostr (temp2-raznica) + ' мая.';
                            if temp2-raznica=0 then
                            textBox12.Text := '30 апреля.';
                            if temp2-raznica<0 then
                            textBox12.Text := inttostr (30+(temp2-raznica)) + ' апреля.';
                            textBox13.Text := inttostr (temp2) + ' мая.';
                            end;
                        end;
                    end;
                end;


root = tk.Tk()
root.title('Православные праздники')
root.geometry('400x450')


### Elements
input = Entry(root, font="Arial 10")
label_year = Label(root, text='Введите год:', font="Arial 10", justify=LEFT)
button = Button(root, text='Рассчитать', font="Arial 10", command=button_click)
label_raznica = Label(root, text='Разнница между календарями: ', font="Arial 10", justify=LEFT)
label_UK = Label(root, text='Юлианский календарь:', font="Arial 10 bold", justify=LEFT)
label_PU = Label(root, text='Пасха: ', font="Arial 10", justify=LEFT)
label_VERB_U = Label(root, text='Вербное воскресенье: ', font="Arial 10", justify=LEFT)
label_VOZ_U = Label(root, text='Вознесение Христа: ', font="Arial 10", justify=LEFT)
label_TR_U = Label(root, text='Троица: ', font="Arial 10", justify=LEFT)
label_DS_U = Label(root, text='День Святого Духа: ', font="Arial 10", justify=LEFT)
label_GK = Label(root, text='Григорианский календарь:', font="Arial 10 bold", justify=LEFT)
label_PG = Label(root, text='Пасха: ', font="Arial 10", justify=LEFT)
label_VERB_G = Label(root, text='Вербное воскресенье: ', font="Arial 10", justify=LEFT)
label_VOZ_G = Label(root, text='Вознесение Христа: ', font="Arial 10", justify=LEFT)
label_TR_G = Label(root, text='Троица: ', font="Arial 10", justify=LEFT)
label_DS_G = Label(root, text='День Святого Духа: ', font="Arial 10", justify=LEFT)
###


### Packing
input.pack()
label_year.pack()
button.pack()
label_raznica.pack()
label_UK.pack()
label_PU.pack()
label_VERB_U.pack()
label_VOZ_U.pack()
label_TR_U.pack()
label_DS_U.pack()
label_GK.pack()
label_PG.pack()
label_VERB_G.pack()
label_VOZ_G.pack()
label_TR_G.pack()
label_DS_G.pack()
###


input.place(x=120, y=13)
label_year.place(x=20, y=10)
button.place(x=280, y=9)
label_raznica.place(x=20, y=50)
label_UK.place(x=20, y=80)
label_PU.place(x=30, y=110)
label_VERB_U.place(x=30, y=140)
label_VOZ_U.place(x=30, y=170)
label_TR_U.place(x=30, y=200)
label_DS_U.place(x=30, y=230)
label_GK.place(x=20, y=260)
label_PG.place(x=30, y=290)
label_VERB_G.place(x=30, y=320)
label_VOZ_G.place(x=30, y=350)
label_TR_G.place(x=30, y=380)
label_DS_G.place(x=30, y=410)


root.mainloop()


