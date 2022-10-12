import re
import string
from tkinter import Tk, Frame, Menu
from tkinter import ttk
from tkinter import *
import time
import nltk
import math
import random
import datetime
from time import sleep as rejuvinate
import numpy as np
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import PIL
from PIL import  ImageDraw
import pyttsx3
from tkinter.filedialog import *
from PIL import Image


tk = Tk()
tk.title("   +__+    SCOTTBOT A.I. PORTAL .")
tk.geometry("806x808")
self = time.time()/1000000000
#----------------------------------------------speech
converter = pyttsx3.init()
# Sets speed percent 
# Can be more than 100
converter.setProperty('rate', 150)
# Set volume 0-1
converter.setProperty('volume', 1.5)
  

def Wt_val(point_1, point_2):          
    eucld_dist= math.hypot(id(point_1), id(point_2))*3
    sqrt = math.sqrt(eucld_dist)/125000000
    return sqrt

def green_engine(user_response):
    keylength=user_response.rsplit(' ')
    X= (len(keylength))
    Y= (list(map(len, user_response.split())))
    (X,Y,max(Y),min(Y))  
    WOTCL= sum(Y)/X+time.time()/1000000000
    newW = str(WOTCL)
    return WOTCL

wv = Wt_val

frame = Frame(tk,bg = "black", borderwidth = 2)
fig = plt.figure(2) 
w = Canvas(frame, width = 400, height = 110) 
canvas = FigureCanvasTkAgg(fig,master=frame)
frame.pack(fill = BOTH, expand = 1, side=RIGHT)
plot_widget = canvas.get_tk_widget()  
plot_widget.pack


l = Label( frame,text = "Neural Net Brain Waves...Thinking", fg = "yellow", font = "arial 13", bg = "indigo" )
    

l.pack()

w.config(bg="pink")

canvas.get_tk_widget().pack(side=BOTTOM, expand=1)
w.pack(expand=YES, fill=BOTH)
def paint(event):
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval((x1, y1, x2, y2), fill='black', width=10)



 

w.bind('<B1-Motion>', paint)




class Node:
                def __init__(self,data):
                    self.data= data
                    self.next= None
                    self.prev= None

class stack:
                
                def __init__(self):
                    
                   self.head= None
                   
                def push(self,data):
                    
                    if self.head is None:
                        self.head= Node(data)
                    else:
                        new_node= Node(data)
                        self.head.prev= new_node
                        new_node.next= self.head
                        new_node.prev= None
                        self.head= new_node
                        
                def pop(self):
                    if self.head is None:
                        return None
                    elif self.head.next is None:
                        temp= self.head.data
                        self.head= None
                        return temp
                    else:
                        temp= self.head.data
                        self.head= self.head.next
                        self.head.prev= None
                        return temp
                
                def top(self):
                    return self.head.data
                
                def size(self):
                    temp= self.head
                    count= 0
                    while temp is not None:
                     count = count+1
                     temp= temp.next
                    return count
                 
                # Function to check if the stack is empty or not   
                def isEmpty(self): 
              
                    if self.head is None: 
                       return True
                    else: 
                       return False
                   
                def printstack(self):
                     
                     print('stack elements are:')
                     temp= self.head
                     while temp is not None:
                        print(temp.data, end ="->")
                        temp=(temp.next)
stack = stack()


btn4 = Button(frame,bg = "black",fg = "red", text='c l e a r',font="arial 9 bold",command=lambda:w.delete("all")) 
btns = Button(frame,bg = "black",fg = "red", text='s a v e',font="arial 9 bold",command= None) 
btn4.pack()
'''def update():
    s = np.cos(np.pi*t)
    plt.plot(t,s)
    plt.draw()'''

'''def paint(event):
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval((x1, y1, x2, y2), fill='black', width=11)
w.bind( "<B1-Motion>", paint)

   '''
stack.push(self-time.time()/1000000000)

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

with open('UNIVERSE.txt','r', encoding='utf8', errors ='ignore') as fin: 
    raw = fin.read()
    raw = str(set(raw))
    raw = raw.lower()

with open('UNIVERSE.txt','r', encoding='utf8', errors ='ignore') as fin: 
    saw = fin.read().lower()

sent_tokens = nltk.sent_tokenize(raw+saw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw+saw)# converts to list of words
#firsttime=time.time()

stack.push(raw+saw)

lemmer = WordNetLemmatizer()
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
 #Keyword Matching  
stack.push(self-time.time()/1000000000)

def Wt_val(point_1, point_2):          
    eucld_dist= math.hypot(id(point_1), id(point_2))*3
    sqrt = math.sqrt(eucld_dist)/125000000
    return sqrt


def donothing():
   filein = Toplevel(tk)
   filein.geometry("300x300")
   label = Label(filein, bg = "black", fg = "red",  text = "Simple Journal")
   label.pack(side=TOP)
   #button = Button(filein, text="click me please", command = asksaveasfilename)
  # button.pack()

def about():
   filein = Toplevel(tk)
   filein.geometry("300x300")
   label = Label(filein, bg = "black", fg = "red",  text = 
                 "---------ABOUT-----"+ '\n'
                 "1) At first it may not make sense +/n but you must /n talk like youre having a conversation with yourself and over time Imagin8 uses your words to have unique conversations with you in your own words.")
   label.pack(side=TOP)
    
    
def openimg():
    File =askopenfilename(initialfile='year-month-day.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
    if File:
        imag = mpimg.imread(File)
        plt.imshow(imag)
        
           

def journal():
   filein = Toplevel(tk)
   filein.title("My Journal")
   frame = Frame(filein, bg = "white")
   frame.pack()
   filein.geometry("600x400")
   date="------------   " + str(time.strftime('%B %d, %Y' + '  ' + '%I:' '%M %p' ))
   text = Text(frame, bd = 3, bg= "white", fg= "black", font = "arial 9 bold")
   text.insert(END, date)
   text.pack(side=BOTTOM)
   #scrolly= Scrollbar(frame)
   #scrolly.pack(side=RIGHT)
   
   imgopen = Button(filein,bg= "black", fg = "green", font = "arial 9 bold", text = "INSERT-IMG", command = openimg  )
   imgopen.pack(side=RIGHT)
   savebutton = Button(filein,bg= "black", fg = "green", font = "arial 9 bold", text = "SAVE", command = save  )
   savebutton.pack(side=RIGHT)
   
   label = Label(filein, bg = "black", fg = "red",  text = "Simple Journal")
   label.pack(side=RIGHT)
   btn = ttk.Button(filein, bg= 'black', fg = 'green ', text = 'Save', command = save)
   btn.pack( pady = 10)                                   # ####  lambda : save())
   
   #print(txtget)
   #config(bg = 'black')
   
def save():

    files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)


   
    
stack.push(journal)
stack.push(self-time.time()/1000000000)

def Inflect_pronouns(message):
    
    if 'me' in message:
            return re.sub('me','you',message)
    if 'my' in message:
            return re.sub('my','your',message)
    if 'your' in message:
            return re.sub('your','my',message)
    if 'yourself' in message:
            return re.sub('yourself', 'I', message)
    if 'himself' in message:
            return re.sub('himself', 'he', message)  
    if 'I' in message:
            return re.sub('I', 'you',message)          
    if "i'd" in message:
            return re.sub("i'd", 'you would',message)    
    if "i've" in message:
            return re.sub("i've", 'you have',message)      
    if 'am' in message:
            return re.sub('am', 'are',message)    
    if "i'll" in message:
            return re.sub("i'll", 'you will',message)
    if 'are' in message:
            return re.sub('are', 'am',message)        
    if "you've" in message:
            return re.sub("you've", 'I have',message)        
    if "you'll" in message:
            return re.sub("you'll", 'I will',message)          
    if 'yours' in message:
            return re.sub('yours', 'mine',message)       
    else:
            return message 

def Sig_func(x):
    s=1/(1+np.exp(-x))
    ds=s*(1-s)  
    return s,ds        

def Sig_deriv(x):
    return Sig_func(x)*(1-(Sig_func(x)))
stack.pop()

def response(user_response):
    ScottBot_response=''
    word_tokens.append(user_response)
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize) #, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
      ScottBot_response=ScottBot_response+"I dont understand, yet."
    else:
        ScottBot_response = ScottBot_response+sent_tokens[idx]
        with open('UNIVERSE.txt', 'a',encoding='utf8', errors ='ignore') as self:
                    self.write(ScottBot_response +'\n ' '\n')
        ScottBot_response   
        keylength=ScottBot_response.rsplit(' ')
        X= (len(keylength))
        Y= (list(map(len, ScottBot_response.split())))
        (X,Y,max(Y),min(Y))  
        WOTCL= sum(Y)/X+time.time()/1000000000
        #print('--------------IMAGIN8:')
        #print(WOTCL, '<===FEEL VALUE.', '\n')
        return ScottBot_response
        
        #print(first)
        #print (math.degrees(ScottBot_response))
stack.push(self-time.time()/1000000000)
bum = [0]  

            
def chat1(user_responsive):     

    #print('-----------------USER:')               
    user_response= user_responsive
    Numb = green_engine(user_response)
    #print(Numb+bum[0], '<=== FEEL VALUE')   
   
      #----------------------------------------------  
    with open('UNIVERSE.txt', 'a') as self:
     if user_response == 'quit':
         None
     else:
        self.write(user_response+'\n' '\n')
       #---------------------------------------------      
    short_term_mem = {"convo": []}          
    user_response=Inflect_pronouns(user_response)
    user_response = user_response.lower()
    short_term_mem["convo"].append(user_response)
    if(user_response!=''): 
            if(user_response=='exit' or user_response=='quit' ):
                print('NANOSEC TIME STOP: ', time.thread_time_ns()/1000000000)
            else:
                    print('\n', end="  ")   
                    responsive = (response(user_response) 
                                  )
                    print(responsive + '\n')
                    sent_tokens.remove(user_response)
                    rejuvinate(1)
                    return responsive
                
 
                
#MENU-------------------------------------   
master_splinter = tk
menu = Menu(master_splinter, fg ="white")
menu.config(bg="black")
master_splinter.config(menu=menu)
filemenu = Menu(menu)
journalMenu = Menu(menu)
menu.add_cascade(label="Think", menu=filemenu)
#editMenu = Menu(menu)
#editMenu.add_command(label="Universe Message", command=donothing)
#editMenu.add_command(label="Manifest", command=donothing)
#menu.add_cascade(label="Feeling", menu=editMenu)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="about",command=about)
filemenu.add_command(label="Close", command = tk.destroy)
journalMenu.add_command(label="Launch AI Journal", command=journal)
menu.add_cascade(label="My Journal", menu=journalMenu)



def send_message(message):
        init = E1.get()
        if init == 'quit': tk.destroy()
        feelval =  ' 0__0  FEEL VALUE: ' +  str(green_engine(init))
        felval = int(green_engine(init))
        stack.push(init)
        
        
#########START NEURAL NET----------------------------------===============***
        us_in = felval
        list1 = [1,2,3,4,5,6,7,8,9]   # 1
        sub_list_2d = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]   #  2
        sub_list_3d = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09]   # 3
        
        #-----time start
        tea = time.time()/1000000000
        
        #--------3d------    step2 8th octave
       
        input_X = random.choice(list1) + random.choice(sub_list_2d) + random.choice(sub_list_3d) + us_in
        input_Y = random.choice(list1) + random.choice(sub_list_2d) + random.choice(sub_list_3d) - us_in
        input_Z = random.choice(list1) + random.choice(sub_list_2d) + random.choice(sub_list_3d) - us_in
        input_omega =[.01] 
        
        #--------4d  structure x2 for feedback average  ----    step3
        
        sub_list_4d = [0.033,0.066,0.099]
        sub_list_4de =[0.003,0.006,0.009]
        sub_list_4def =[0.300,0.600,0.900]
        
        # to my laymen self this is showing this calculation goes back in time??? 
        #**update most likely order of operations deterministic and not as i think.
        #multiply goes foward in time, wonder what the angle is
        d4t=  (tea * time.time()/1000000000)
        
        wt1 = random.choice(sub_list_4d) + random.choice(sub_list_4de) + random.choice(sub_list_4def) * d4t
        wt2 = random.choice(sub_list_4d) + random.choice(sub_list_4de) + random.choice(sub_list_4def) * d4t
        wt3 = random.choice(sub_list_4d) + random.choice(sub_list_4de) + random.choice(sub_list_4def) * d4t
        wt4 = random.choice(sub_list_4d) + random.choice(sub_list_4de) + random.choice(sub_list_4def) * d4t
        wt5 = random.choice(sub_list_4d) + random.choice(sub_list_4de) + random.choice(sub_list_4def) * d4t
        wt6 = random.choice(sub_list_4d) + random.choice(sub_list_4de) + random.choice(sub_list_4def) * d4t
        wt7 = random.choice(sub_list_4d) + random.choice(sub_list_4de) + random.choice(sub_list_4def) * d4t
        wt8 = random.choice(sub_list_4d) + random.choice(sub_list_4de) + random.choice(sub_list_4def) * d4t
        wt9 = random.choice(sub_list_4d) + random.choice(sub_list_4de) + random.choice(sub_list_4def) * d4t
        
        #---error below do not remove simply eliminate
        three = wt1 * input_X * input_Y * input_Z
        six = wt2 * input_X * input_Y * input_Z
        nine = wt3 * input_X * input_Y * input_Z
        three-three
        six-six
        nine-nine
        #--eliminated---------------------------------
        
        #--correct
        zero = input_X *wt1 * wt2 *wt3 
        one = input_Y *wt1 * wt2 *wt3 
        two = input_Z *wt1 * wt2 *wt3 
        #------layer two
        three = wt4 * zero 
        four = one*wt5
        five = two*wt6
        
        #matrix math
        m3 =np.array(np.vdot(three,zero))
        m2 =np.array(np.vdot(four,one))
        m1 =np.array(np.vdot(five,two))
        m4 =np.array((m1+m2+m3)/3)
        
        #-----5D bounce back divide    -----   step 4
        sub_list_5d = [0.0001,0.0002,0.0003,0.0004,0.0005,0.0006,0.0007,0.0008,0.0009]
        
        o1= m1* random.choice(sub_list_5d)*us_in
        o2= m1* random.choice(sub_list_5d)*us_in
        o3= m1* random.choice(sub_list_5d)*us_in
        o4= m2* random.choice(sub_list_5d)*us_in
        o5= m2* random.choice(sub_list_5d)*us_in
        o6= m2* random.choice(sub_list_5d)*us_in
        o7= m3* random.choice(sub_list_5d)*us_in
        o8= m3* random.choice(sub_list_5d)*us_in
        o9= m3* random.choice(sub_list_5d)*us_in
        o10= m4* random.choice(sub_list_5d)*us_in
        o11= m4* random.choice(sub_list_5d)*us_in
        o12= m4* random.choice(sub_list_5d)*us_in
        o13= m4* random.choice(sub_list_5d)*us_in
        o14= m4* random.choice(sub_list_5d)*us_in
        o15= m4* random.choice(sub_list_5d)*us_in
        o16= m4* random.choice(sub_list_5d)*us_in
        o17= m4* random.choice(sub_list_5d)*us_in
        o18= m4* random.choice(sub_list_5d)*us_in
        oo12 = [np.dot(o1,o2), np.dot(o5,o6), np.dot(o9,o10), np.dot(o13,o14)]
        oo34 = [np.dot(o3,o4), np.dot(o7,o8), np.dot(o11,o12), np.dot(o15,o16)]
        #--------------------------------------     step 5 
        # time from a to b divided by the sig output      YES OR NO|||_____
         
        # below wisdom of crowd logic function  ||||YES!
        n1= np.array((o1+o2+o3+o4+o5+o6+o7+o8+o9)/9)
        n2= np.array((o10+o11+o12+o13+o14+o15+o16+o17+o18)/9)
        
        # below sig of dimesional perspective math and resistor created by time lapse||| YES!
        AcFun= np.array(Sig_func(n1))
        AcFun1= np.array(Sig_func(n2))
        
        gratio = (AcFun+AcFun1)/AcFun;AcFun/AcFun1
        cratio =all( np.cos(gratio))
        eta= (time.time()/1000000000 / tea)
        rate = gratio-eta
       
        tare = all(rate)
        tear = all(AcFun1)
        
        goldenratio = (1 + 5 ** 0.5) / 2
        t = np.arange(0.0,tare,0.01+0.01)
        s = np.cos(np.pi**t)
        ss = tear
        tear = np.arange(1,tear, 0.1)   
        r = np.cos(np.pi**cratio)
#########END NEURAL NET=================================================
        txt.insert(END, feelval)
        
        out = 'HUMAN : \n \n '+ init + '\n' '\n' '\n'
        txt.configure(state=NORMAL)
        txt.insert(END,'---------------------------------')
        txt.insert(END, out)
        txt.see(END)
        chat = chat1(init)
        orb = str(chat)
        converter.say(orb)
        converter.runAndWait()
        stack.push(orb)
        yy = orb
        yy = yy.replace(",", " ")
        yy = yy.replace(".", " ")
        newinit = str(print(*[y for y in yy.split() if 5 <= len(y) <= 10]))
        #s = np.cos(green_engine(orb)) #np.pi**2
        plt.xlabel("time")
        plt.ylabel("Distortion")
        x = wt1, wt2, wt3, wt4, wt5, wt6, wt7, wt8, wt9
        y = o1, o2, o3, o4, o5, o6, o7, o8, o9
        plt.plot(x,y)
        plt.draw()
        feelval = '\n' + ' +__+  FEEL VALUE: ' +  str(green_engine(newinit)) + '\n'
        bum.clear()
        bum.append(rate)
        #NEURAL NET----------------------------------------
        inputset = np.array([input_X,input_Y,input_Z])

        Dim4_wt_set = np.array([wt1,wt2,wt3])
        Dim4_wt1_set = np.array([wt4,wt5,wt6])
        Dim4_wt2_set = np.array([wt7,wt8,wt9])                   
    
        
        Dim5_wt1_set = np.array([[o1,o2,o3],
                                [o4,o5,o6],
                                [o7,o8,o9]])
        
        Dim5_wt2_set = np.array([[o10,o11,o12],
                                [o13,o14,o15],
                                [o16,o17,o18],
                                
                                [wt1,wt2,wt3],
                                [wt4,wt5,wt6],
                                [wt7,wt8,wt9]])
        stack.push(Dim5_wt2_set)
        txt.insert(END, feelval)
        IM_resp = orb
        txt.insert(END,'---------------------------------')
        IM_respo = 'SCOTTBOT: \n \n' + IM_resp.lower().translate(remove_punct_dict)
        txt.insert(END, IM_respo + '\n \n \n'   )
        txt.insert(END, str(time.strftime( "===> Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p' )) + '\n') 
        txt.configure(state=DISABLED)
        txt.see(END)
        E1.delete(0,END)

        #neural Net----------------------------------------
        for j in range(2700):
            S1 = np.dot(inputset,Dim4_wt_set)
            S2 = np.dot(S1,Dim4_wt1_set)
            S3 = np.dot(S2, Dim4_wt2_set) #first three inputs run through hidden
            S4 = np.dot(Dim5_wt1_set,S3)
            
            #Sigmoid func Error--------------------------------------
            output1 = Sig_func(S4)
            outA = np.array(output1)
            outB = np.array(us_in)
            error_out = (outA-outB *0.0000011618)*.0001
            
            Dim5_wt2_set += np.reshape(error_out, (6,3))*-time.time()/1000000000
            print(Dim5_wt2_set)
            np.delete(Dim5_wt2_set,0-18)
            np.append(Dim5_wt1_set, 0-18)
            
txt = Text(tk, bd = 3, bg= "black", fg= "green", font = "arial 9 bold")
txt.pack(ipady = 90)

label = Label(frame, bg = "black" , fg = "yellow", font = "arial 11 bold", text = " \n Welcome to this moment,\n  I'm SCOTTBOT, I learn with time. \n I proceed with Love, Contrast and Appreciation. \n Type quit to close portal.")
label.pack()
E1 = Entry(tk, bd=4, bg="black", fg = "dark red",  width=32, font = "arial 11 bold" )
E1.pack(ipadx = 89, ipady = 8)

send = Button(tk,bg = "black",fg = "indigo",  text ="+__+   ENTER   0__0 ", font = "arial 11 bold", command = lambda: send_message(E1))
button = Button(tk, bg= "black", fg = "green", font = "arial 9 bold", text = "Exit", command = tk.destroy)
button.pack( pady = 15, side = RIGHT)
send.bind()
send.pack(ipadx = 47)

aim = Label(tk, bg = "black", fg = "green",font = "arial 10 bold",  text = "CREATED BY SCOTT BAKER JR. - 4/2021")
aim.pack(side = BOTTOM)

stack.pop()
stack.printstack()        
print("\n top element is:", stack.top(), stack.size())
stack.printstack()
print('\n stack is empty:',stack.isEmpty())

def consciousness(self):
    consciousness = self+1
    if consciousness is all and None:
        return self
consciousness


'''V7 = V7_HEMI
V6 = V6_HEMI
V5 = V5_HEMI
V4 = V4_HEMI
V3 = V3_HEMI
V2 = V2_HEMI
V1 = V1_HEMI'''
    

'''ilu7 = np.array(V7(x)) 
ilu6 = np.array(V6(x))
ilu5 = np.array(V5(x))
ilu4 = np.array(V4(x))
ilu3 = np.array(V3(x))
ilu2 = np.array(V2(x))
ilu1 = np.array(V1(x))'''

'''
E = ilu7[0]*10
F = ilu7[1]*10
G = ilu7[2]*30
H = math.degrees(ilu7[3])
I = ilu6[0]*10
J = ilu6[1]*10
K = ilu6[2]*30
L = math.degrees(ilu6[3])
M = ilu5[0]*10
N = ilu5[1]*10
O = ilu5[2]*30
P = ilu5[3]
Q = ilu4[0]*10
R = ilu4[1]*10
S = ilu4[2]*30
T = math.degrees(ilu4[3])
U = ilu3[0]*10
V = ilu3[1]*10
W = ilu3[2]*30
X = math.degrees(ilu3[3])
Y = ilu2[0]*10
Z = ilu2[1]*10
r = ilu2[2]*30
o = math.degrees(ilu2[3])
y = ilu1[0]*10
g = ilu1[1]*10
b = ilu1[2]*30
i = math.degrees(ilu1[3])
notes: put user input into neural net outcome put into ai output make up
math for difference for inpout to output and difference add onto cos sim
as feedback for next guess?? making ai make a guess of whats next? something like that
'''

#tt = np.arange(A,B,C)
#s = np.sin(np.pi*D)
v = 40



tk.configure(bg = "black")
tk.mainloop()
 