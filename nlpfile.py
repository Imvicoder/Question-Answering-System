import nltk as nl
import numpy as np
import gensim as ge
from nltk.corpus import wordnet as wn
import Tkinter
import matplotlib.pyplot as plt
window = Tkinter.Tk();
# txt=["sachin","is","a","good","boy"]
# sentence = "The University was established by the UP Gautam Buddha University Act 2002 UP Act no. 9 of 2002 and began its first academic session in 2008. The university is fully funded by the NOIDA and GNIDA (undertakings of the UP government) and recognized by the University Grants Commission (UGC).[6] It is member of the Association of Indian Universities (AIU).Gautam Buddha University has been accredited jointly be Joint Accreditation System of Australia & New Zealand (JAS-ANZ), issued on 21 February 2015 after accessing and finding confirmation to the requirements of ISO 9001: 2008.Integrated Dual Degree Programme (B.Arch. + M. Arch./MBA) in Architecture and Planning, been recognized by the Council of Architecture. M. Phil. (Clinical Psychology), 2 years Programme which has been recognized by the Rehabilitation Council of India .Integrated B.A. LLB programme. This Programme has been approved by the Bar Council of India. Gautam Buddha University was the dream Project of Ms Mayawati four time Uttar Pradesh chief minister. August 23, 2008 Ms. Mayawati, inaugurated and dedicated the university to the people, During the Inauguration Ms Mayawati mentioned that she had conceived the idea to establish the International standard University during the previous term of the BSP government in 2002, but during the administration of the Samajwadi Party the project was dumped, and after coming to power again, She speed up the implementation of this project. It was emphasized by the great Architect MR.Dikshu."
window.title("Question Answering System")

lbl = Tkinter.Label(window, text="Enter the knowedge",fg="blue")  # this label
#lbl.config(width=200)
lbl.config(font=("Courier",10))
ent = Tkinter.Text(window, height=30, width=30,fg="red")  # this knowledge
text1 = ent.get('0.0', Tkinter.END)
sentspil = Tkinter.Label(window,text = "Sentence Spliter",fg="blue")#Splited sentence label
sentspil.config(font=("Courier",10))
sentsp = Tkinter.Text(window,height=30, width=30,fg="blue violet")
dcasl=Tkinter.Label(window,text="Deep Case Layer",fg="blue")    #
dcasl.config(font=("Courier",10))
dpcasres=Tkinter.Text(window,height=30, width=30,fg="cyan4")

dicto2 = Tkinter.Label(window, text="Dictonay layer",fg="green")
dicto2.config(font=("Courier",10))
lbl2 = Tkinter.Label(window, text="Enter the Question",fg="green")  # this is also label
#dcasl.config(font=("Courier",10))
lbl2.config(font=("Courier",10))
quest = Tkinter.Text(window, height=2, width=30,fg="dark orchid")  # this question
#answer = Tkinter.Label(window, text="")
organsw=[]
dictonwodd=[]
def on_click(*args):
    #tmp = Label(...)
    print "Click"
    sentence = ent.get('0.0', Tkinter.END)  # knoweldge
    print sentence
    ques = quest.get('0.0', Tkinter.END)


    def locationfunc(empl):
        print "*****************In Location********"
        print empl
        if (empl == 'South'):
            return "true"
        elif (empl == 'California'): #California
            return "true"
        elif (empl == 'Asia'):
            return "true"
        elif (empl == 'North'):
            return "true"
        else:
            return "false"
        # INPUT KNOWLEDGE ####################################################################
#    sentence = "Python is a general-purpose interpreted , interactive, object-oriented, and high-level programming language. It was created by Guido van Rossum during 1985- 1990. Like Perl, Python source code is also available under the GNU General Public License (GPL). This tutorial gives enough understanding on Python programming language."
    sentoke = nl.sent_tokenize(sentence)
    slen = len(sentoke)
    arr = [0 for i in range(slen + 1)]
    arst = [0 for i in range(slen + 1)]
#    print sentoke[0]
    for p in range(0, (slen)):
        # print p
        tokens = nl.word_tokenize(sentoke[p])
        # print tokens
        arst[p] = tokens
        toke = nl.pos_tag(tokens)
        fur = np.array(toke)
        arr[p] = fur
    print "Array Result"
    print arst
    # print fur[0][0][1]
    for i in range(0, len(arr) - 1):
        for u in range(0, len(arr[i]) - 1):
            dat = arr[i][u][0]
            if arr[i][u][1] == "NN" or arr[i][u][1] == "NNP":
                arr[i][u][1] = "Agent"
                blv = locationfunc(arr[i][u][0])
                if blv == "true":
                    arr[i][u][1] = "Location"
            elif arr[i][u][1] == "VBZ":
                arr[i][u][1] = "Modifiee"
            elif arr[i][u][1] == "VBZ":
                arr[i][u][1] = "Modifiee"
            elif arr[i][u][1] == "VBD":
                arr[i][u][1] = "Patient"
            elif dat.isdigit() == True:
                arr[i][u][1] = "Time"
    print "Final result"
    print arr
    sentsp.insert('0.0',sentoke)
    dpcasres.insert('0.0',arr)
    mrpp = [0 for h in range(len(arst))]
    arst = arst[0:len(arst) - 1]
    mpo = iter(arst)

    print(arst)
    model = ge.models.Word2Vec(mpo, min_count=1)  # ,size=19)

    # sim=model.most_similar("general-purpose",topn=8)

    organsw=["No Answer"]
    indxre = 1
    def findsynonyms(givenword):   
        synonyms=[]
        osynonyms=[]
        print "synomyns"
        for syn in wn.synsets(givenword):
            for l in syn.lemmas():
                synonyms.append(l.name())
                print synonyms
            dictonwodd.append(synonyms)
        for k in range(len(sentoke)):
            for h in range(len(sentoke[k])):
                for o in range(len(synonyms)):
                    if synonyms[o]==sentoke[k][h]:
                        osynonyms.append(synonyms[o])
        print "synomyns" 
        print dictonwodd
        return  osynonyms                               
                
    def whoansw(arr, sim):
      #  plt.plot(1,sim[1])
      #  plt.show()
        for k in range(0, len(arr) - 1):
            for t in range(0, len(arr[k]) - 1):
                for u in range(0, 40):
                    if sim[u][0] == arr[k][t][0]:
                        if arr[k][t][1] == "Agent":
                            # Output Result
                            print sim[u][0]
                            organsw.append(sim[u][0])
                            print organsw

    def wheresw(arr, sim):
        for k in range(0, len(arr) - 1):
            for t in range(0, len(arr[k]) - 1):
                for u in range(0, 40):
                    if sim[u][0] == arr[k][t][0]:
                        if arr[k][t][1] == "Location":
                            # Output Result
                            print sim[u][0]
                            organsw.append(sim[u][0])
                            print organsw
                            #indxre = indxre + 1

    def whatansw(arr,rett):
        orgasn=[]
        for k in range(0, len(arr)-1):
            for t in range(0, len(arr[k])-1):
                for u in range(0, len(rett)):
                    if rett[u] == arr[k][t][0]:
                           # print arr[k][][0]
                            orgasn.append(arr[k])
                            break
        #organsw=[o for o in organsw]
                            
        print "From What"
       # print organsw[1][0][0]
        for o in range(0,len(orgasn)):
            for y in range(0,len(orgasn[o])):
               organsw.append(orgasn[o][y][0])                
            #print arr[o][y]
            #[1]
    def descwor(arr,rett):
        orgasn=[]
        for k in range(0, len(arr)-1):
            for t in range(0, len(arr[k])-1):
                if rett == arr[k][t][0]:
                    print arr
                    orgasn.append(arr[k])
                           # print arr[k][][0]
                            
                           # break
        #organsw=[o for o in organsw]
        print rett                 
        print "From Describe"
       # print organsw[1][0][0]
        for o in range(0,len(orgasn)):
            for y in range(0,len(orgasn[o])):
               organsw.append(orgasn[o][y][0])                

        
    def whenist(arr, sim):
        for k in range(0, len(arr) - 1):
            for t in range(0, len(arr[k]) - 1):
                for u in range(0, 19):
                    if sim[u][0] == arr[k][t][0]:
                        if arr[k][t][1] == "Time":
                            print sim[u][0]
                            organsw.append(sim[u][0])
        # print       
                            #h=h+1

    ############## Input Question####
    # ques="When is created Python ?"
    qtag = nl.word_tokenize(ques)
    print qtag[0]
    qwtag = [0 for h in range(len(qtag) + 1)]
    # for i in range(0,len(qtag)):
    qwtas = nl.pos_tag(qtag)
    # qwtag=list(qwtas)
    qwtag = np.array(qwtas)
    # qwtag[1][1]='Sachin'
    # print qwtag[1][1]
    # print qwtas[1][1]

    # print qwtag[0][1]
    for m in range(len(qtag)):
        if qwtag[m][1] == "NN" or qwtag[m][1] == "NNP":
            qwtag[m][1] = "Agent"
            # blv=locationfunc(fur[i][0])
            #  if blv=="true":
            # fur[i][1]="Location"
        elif qwtag[m][1] == "VBZ":
            qwtag[m][1] = "Modifiee"
        elif qwtag[m][1] == "VBZ":
            qwtag[m][1] = "Modifiee"
        elif qwtag[m][1] == "VBD":
            qwtag[m][1] = "Patient"
    print qwtag

    if qwtag[0][0] == "Who" or qwtag[0][0] == "Which":
        n = 0
        putp=[]
        qusst = []  # 0 for u in range(len(qtag))]
        for p in range(1,len(qtag) - 1):
            print "Who is"
            print qtag[p]
            if qwtag[p][1] != "Modifiee" and qwtag[p][1] != "WP":
               # putp =(findsynonyms(qwtag[p][0]))
                print "Possible word synomyns"
                print putp
                print qwtag[p][0]
                print putp
                qusst.append(qwtag[p][0])  # [n]= qwtag[p][0]#['Python','Like']
                
                n = n + 1
        print qusst
        print "Synomyns"
        print putp
        print "Overall Result"
        rett = qusst + putp
        print rett
        sim = model.most_similar(positive=qusst, topn=40)
        # sim=model.cbow_mean("interpreted")#,topn=19)
        print "Similarity"
        print sim
        
        whoansw(arr, sim)


    elif qwtag[0][0] == "When":
        qusst = []
        u = 1
        print len(qtag)
        for u in range(1,len(qtag)-1):
            print u
            if qwtag[u][1] != "Modifiee" and qwtag[u][1] != "WP":
                qusst.append(qwtag[u][0])

        sim = model.most_similar(positive=qusst, topn=30)
        print "Data similarity"
        print sim
        whenist(arr, sim)
        whenist(arr, sim)
    elif qwtag[0][0] == "What" :
        putp=[]
        qusst = []
        for g in range(len(qtag)-1):
             if qwtag[g][1] != "Modifiee" and qwtag[g][1] != "WP":
                 putp.append(findsynonyms(qwtag[g][0]))
                 qusst.append(qwtag[g][0])
        rett = qusst + putp
        print rett
        whatansw(arr,rett)
    elif qwtag[0][0]=="Where":
        
         #or qwtag[0][0] == "Which":
        n = 0
        putp=[]
        qusst = []  # 0 for u in range(len(qtag))]
        for p in range(1,len(qtag) - 1):
            if qwtag[p][1] != "Modifiee" and qwtag[p][1] != "WP":
                putp =(findsynonyms(qwtag[p][0]))
                print "Possible word synomyns"
                print putp
                print qwtag[p][0]
                print putp
                qusst.append(qwtag[p][0])  # [n]= qwtag[p][0]#['Python','Like']
                
                n = n + 1
        print qusst
        print "Synomyns"
        print putp
        print "Overall Result"
        rett = qusst + putp
        print rett
        sim = model.most_similar(positive=rett, topn=40)
        # sim=model.cbow_mean("interpreted")#,topn=19)
        print "Similarity"
        print sim
        wheresw(arr, sim)

    
    elif qwtag[0][0] == "Describe":
         descwor(arr,qwtag[1][0])
        
         
         #usst.append(rett)
         
             
         
    print "Size"
    if len(organsw) > 1:
        organsw.pop(0)
    answer = Tkinter.Label(window, text=organsw,wraplength=100,height=40, width=20,fg="lime green") 
    answer.grid(row=1,column=4)#,rowspan=2)#,-width=40)
   

btn = Tkinter.Button(window, text="Get Answer", command=on_click,fg='orange')
 # this is answer whic is calculated
window.config(background='light blue')
lbl.grid(row=0,column=0)
lbl.config(background='light yellow')
ent.grid(row=1,column=0)
sentspil.grid(row=0,column=1)
sentsp.grid(row=1,column=1)
dcasl.grid(row=0,column=2)#=Tkinter.Label(window,text="Deep Case Layer")    #
dpcasres.grid(row=1,column=2)
lbl2.grid(row=0,column=3)
lbl2.config(background='light yellow')
#lbl2.config(width=200,height=2)
lbl2.config(font=("Courier",10))
quest.grid(row=1,column=3)
quest.config(width=20,height=1)
btn.config(background='light cyan')
#btn.config(width=30,height=1)
btn.config(font=("Courier",12))
#dicto2.grid(row=0,column=3)
btn.grid(row=2,column=3)
window.mainloop()

# print sim
# print sim[1][0]
# print fur[1][0]
print "Our sentence"

print "m result"
# whoansw(arr,sim)
# whatansw(arr,sim)


# print (arr[0][1])#[0][1]
# print sim[0][0]
# print len(arr[2])

# print arr[1]


'''

            # print sim[u][0]

for k in range(1,len(arr)):
    for t in range(0,len(arr[k])):
        for u in range(0,len(sim)):
         if sim[u][0]==arr[k][t][0]:
            # print sim[u][0]
             if arr[k][t][1]=="Location":
                 print sim[u][0]
for k in range(1,len(arr)):
    for t in range(0,len(arr[k])):
        for u in range(0,len(sim)):
         if sim[u][0]==arr[k][t][0]:
            # print sim[u][0]
             if arr[k][t][1]=="Patient":
                 print sim[u][0]
'''
# print sim[0]
# sim=ge.models.Word2Vec
# print "my array"







# agents[[]]
# for ind in range(0, len(sentoke)):
#    for fg in range(0,len(fur)):
#         if arr[ind][fg][1]=="Agent":
#             print arr[ind][fg][0]

# elif fur[i][1]==""
# mard=[["Architect","MR.Dikshu"],["Gautam Buddha University","Uttar Pradesh"]]#np.array([[]])
#   print "My Output"
#  for j in range(0, len(fur)):
# if fur[j][1]=="Agent":
# mard.append([fur[j][0]])////////////
# print "custom agent only "+ fur[j][0]
# print mard
# qraa=[["Mahesh","Rajesh","Suresh"]]
#
# print model.similar_by_vector("Architect",topn=1)#.most_similarby("MR.Dikshu",topn=1)
# []
# print model["University"]
# print model["Uttar"]
# print model["Architect"]
# print model["Gautam"]



# fur[0][2]='Sachin'
# print fur[1][1]
