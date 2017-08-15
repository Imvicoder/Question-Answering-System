import Tkinter
window = Tkinter.Tk();



window.title("hello world")

lbl = Tkinter.Label(window,text = "Enter the knowedge")#this label
ent = Tkinter.Text(window,height=10, width=30)           # this knowledge
sentspil = Tkinter.Label(window,text = "Sentence Spliter")#Splited sentence label
sentsp = Tkinter.Text(window,height=10, width=30)           # splited sentence result
dcasl=Tkinter.Label(window,text="Deep Case Layer")    #
dpcasres=Tkinter.Text(window,height=10, width=30)
dictor=Tkinter.Label(window,text="Dictonary Layer")
dictorna=Tkinter.Text(window,height=10, width=20)
text1 = ent.get('0.0', Tkinter.END)
lbl2 = Tkinter.Label(window,text = "Enter the Question")   # this is also label

quest = Tkinter.Text(window,height=1, width=30)                              # this question
def on_click(*args):
            
          sentence = ent.get('0.0', Tkinter.END) #knoweldge
          text2 = quest.get('0.0', Tkinter.END)  #question
         # print sentence  
btn = Tkinter.Button(window,text = "Get Answer",command=on_click)
answer = Tkinter.Label(window,text = "dfgdcbksjdbdjkbcjksbjkcbaskjbckjasbcjbkaksjbckajsbkcjbxaskjbckjasbkjcbaskjbcjkasbcjkasbkjcbasjkbckjasbckjasbkjcbasjk",wraplength=50)        # this is answer whic is calculated

lbl.grid(row=0,column=0)
ent.grid(row=1,column=0)
sentspil.grid(row=0,column=1)
sentsp.grid(row=1,column=1)
dcasl.grid(row=0,column=2)
dpcasres.grid(row=1,column=2)
dictor.grid(row=0,column=3)
dictorna.grid(row=1,column=3)
lbl2.grid(row=0,column=4)
quest.grid(row=1,column=4)
btn.grid(row=2,column=4)
answer.grid(row=3,column=4,rowspan=2)
#btn.pack()
#answer.pack()

#window.geometry("600x600+600+600")
window.mainloop()


