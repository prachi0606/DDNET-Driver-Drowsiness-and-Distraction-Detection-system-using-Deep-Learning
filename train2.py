import cv2
import matplotlib.pyplot as plt
from keras.models import load_model
import tkinter as tk
from tkinter import ttk
from tkinter import*
import tkinter.font as font
from PIL import Image, ImageTk
import datetime
from time import sleep


frame=0
window = tk.Tk()
window.title('DDNet:Driver Drowsiness & Distracted Driving Detection System using Deep Learning')
#window.iconbitmap("/home/itm1138/Downloads/favicon.ico")
window.geometry('1366x768')

window.configure(bg='black')

# Create a photoimage object of the image in the path
image1 = Image.open("/home/itm1138/Downloads/op3.jpg")
test = ImageTk.PhotoImage(image1)

b23=label1 = tk.Label(image=test)
label1.image = test
b23.place(x=0, y=25)
##window.after(3000, lambda: label1.destroy())

#window.mainloop()

ret=False

# label

b24=tk.Label(window, text = "ALERT TODAY : ALIVE TOMORROW !!",  fg = "white",
		 bg = "black",
		 font = "Times 16 bold italic")
b24.place(x = 150,
		y=80)


#window.update()
#time.sleep(5)

label = ["Watching Backward","Watching Forward","Sleeping","Yawning","Talkingviaphone"]
model = load_model(r'/home/itm1138/Downloads/best.h5')

m=1
x = datetime.datetime(2021,3,30,15,0,0)

tvf1=100
tvf2=110
tvf3=140
tvf4=150
tvf5=180
tvf6=190
tvf7=950
tvf8=1000
tvf9=1050
tvf10=170
tvf11=1070
tvf12=130
tvf13=210

yawn1=130
yawn2=132
yawn3=133
yawn4=134
yawn5=135
yawn6=137
yawn7=138
yawn8=140

forw1=651
forw2=701
forw3=751
forw4=801
forw5=731
forw6=781



sleep1=52
sleep2=60
sleep3=65
sleep4=70
sleep5=76
sleep6=77
sleep7=80
sleep8=90
sleep9=97
sleep10=110


back1=58
back2=70
back3=75
back4=83
back5=84
back6=95
back7=103


t=1
t1=2
t2=4
t3=0
check=0
    
a=1

start=0
fcount1 = 0
fcount2 = 0
fcount3 = 0
fcount4 = 0
fcount5=0
c=0
c1=0
c2=0
c3=0
c4=0
j = 0
k = 0
b = 0
c = 0
#
#
f=0
y=0
s=0

nf=0



cap = cv2.VideoCapture(r'/home/itm1138/Downloads/MORN1.5.mp4')



def morning():
    global t,a,x,cap,start,fcount1,fcount2,fcount3,fcount4,fcount5,c,c1,c2,c3,c4,j,k,b,c,f,y,s,alarm,frame
    if(t!=2):
        frame=0
        start=0
        alarm=0
        fcount1 = 0
        fcount2 = 0
        fcount3 = 0
        fcount4 = 0
        fcount5=0
        c=0
        c1=0
        c2=0
        c3=0
        c4=0
        j = 0
        k = 0
        b = 0
        c = 0
        #
        #
        f=0
        y=0
        s=0
        
        cap = cv2.VideoCapture(r'/home/itm1138/Downloads/MORN1.5.mp4')
    #
    t=1
    a=1
    x = datetime.datetime(2021,3,30,9,0,0)





def noon():
    global t,a,x,cap,start,fcount1,fcount2,fcount3,fcount4,fcount5,c,c1,c2,c3,c4,j,k,b,c,f,y,s,alarm,frame
    if(t!=1):
        frame=0
        start=0
        alarm=0
        fcount1 = 0
        fcount2 = 0
        fcount3 = 0
        fcount4 = 0
        fcount5=0
        c=0
        c1=0
        c2=0
        c3=0
        c4=0
        j = 0
        k = 0
        b = 0
        c = 0
        #
        #
        f=0
        y=0
        s=0
        cap = cv2.VideoCapture(r'/home/itm1138/Downloads/COMBOVID1.mp4')
    #
    t=2
    a=1
    x = datetime.datetime(2021,3,30,16,0,0)
    


def night():
    global t,a,x,cap,start,fcount1,fcount2,fcount3,fcount4,fcount5,c,c1,c2,c3,c4,j,k,b,c,f,y,s,alarm,frame
    #
    frame=0
    start=0
    alarm=0
    fcount1 = 0
    fcount2 = 0
    fcount3 = 0
    fcount4 = 0
    fcount5=0
    c=0
    c1=0
    c2=0
    c3=0
    c4=0
    j = 0
    k = 0
    b = 0
    c = 0
    #
    #
    f=0
    y=0
    s=0
    
    t=3
    a=2
    cap = cv2.VideoCapture(r'/home/itm1138/Downloads/NIGHT1.5.mp4')
    x = datetime.datetime(2021,3,30,3,0,0)



def hill():
    global t1
    #
    t1=1




def plain():
    global t1
    #
    t1=2



def snow():
    global t2,t3,check
    #
    if(t3!=0):
        t2=1
    check=1
        


def rain():
    global t2,t3,check
    #
    if(t3!=0):
        t2=2
    check=2
      

def fog():
    global t2,t3,check
    #
    if(t3!=0):
        t2=3
    check=3
       
    
def pleasant():
    global t2,b15,b16
    t2=4
    b15.deselect()
    b15.deselect()
    

def heavy():
    global t3,check,t2
    #
    t3=1

    if(check==1):
        t2=1
    elif(check==2):
        t2=2
    elif(check==3):
        t2=3


    
        

def light():
    global t3,check,t2
    #
    t3=2
    if(check==1):
        t2=1
    elif(check==2):
        t2=2
    elif(check==3):
        t2=3

p=0
e=0
alarm=0
lml=0
lmb=0
sm=0
pk=0
mco=0
mco1=0
w=0
sig=0
first=0
show=0
def predict():

    global show,start,first,fcount1,fcount2,fcount3,fcount4,fcount5,mco,mco1,pk,sig,sm,w,alarm,m,ret,c,c1,c2,c3,c4,j,k,b,lml,lmb,c,t,f,y,s,lmain,t,t1,t2,t3,cap,tvf1,tvf2,tvf3,tvf4,tvf5,tvf6,tvf7,tvf8,tvf9,tvf10,tvf11,tvf12,tvf13,yawn1,yawn2,yawn3,yawn4,yawn5,yawn6,yawn7,yawn8,forw1,forw2,forw3,forw4,forw5,forw6,sleep1,sleep2,sleep3,sleep4,sleep5,sleep6,sleep7,sleep8,sleep9,sleep10,back1,back2,back3,back4,back5,back6,back7,x,frame

    show=1
    first=1
    #print(t)
    if(t==1):
        morning() 
    elif(t==2):
        noon() 
    else:
        night()



    while True:
        frame=frame+1

        if(sm!=0):

            start=start+1

            #j=j+1
            
            fcount1 = fcount1 +1

            fcount2 = fcount2 +1

            fcount3 = fcount3 +1

            fcount4 = fcount4 +1

            fcount5 = fcount5 +1
        
        ret, samp = cap.read(0)
     #   if(t!=3 and frame==2865):
       #     cap.set(cv2.CAP_PROP_POS_FRAMES,3400)
         #   frame=3400
        #elif(t==3 and frame==300):
          #  cap.set(cv2.CAP_PROP_POS_FRAMES,680)
            #frame=680
       # elif(t==3 and frame==1440):
         #   cap.set(cv2.CAP_PROP_POS_FRAMES,1540)
           # frame=1540
       # elif(t==3 and frame==2130):
        #    cap.set(cv2.CAP_PROP_POS_FRAMES,2480)
        #    frame=2480
        #cv2.putText(samp,str(frame),(20, 290),cv2.FONT_HERSHEY_COMPLEX, 2,(255, 255, 255),3,cv2.LINE_4)

        if(not ret):
            if(t==1 or t==2):
                frame=0
                cap = cv2.VideoCapture(r'/home/itm1138/Downloads/MORN1.5.mp4')               
                ret, samp = cap.read(0)
                
            else:
                frame=0
                cap = cv2.VideoCapture(r'/home/itm1138/Downloads/NIGHT1.5.mp4')
                ret, samp = cap.read(0)
                
        #if(datetime.seconds==0 or datetime.seconds==30)
            #print("\n")
       # if(t!=3 and frame==1490):
         #   cap.set(cv2.CAP_PROP_POS_FRAMES,1890)
         #   frame=1890
       # cv2.putText(samp,str(frame),(20, 290),cv2.FONT_HERSHEY_COMPLEX, 2,(255, 255, 255),3,cv2.LINE_4)
    #samp = cv2.rotate(samp, cv2.ROTATE_90_CLOCKWISE)
    #samp = cv2.rotate(samp, cv2.ROTATE_90_COUNTERCLOCKWISE)
        image = cv2.resize(samp, (100,100))
        image = image.astype("float")
        image= image.reshape(1, 100, 100, 3)
        answer = model.predict(image)
        i = answer.argmax(axis=1)[0]
        font = cv2.FONT_HERSHEY_COMPLEX
        
        samp = cv2.resize(samp, (865,540))
        if(m==1):
            pk=1
            if(865+lml*10>=1270):
                lml=lml-1
                #print(lml)
            if(540+lmb*5>=725):
                lmb=lmb-1/1.6
            #print(540+lmb*5)
            lml=lml+1
            lmb=lmb+1/1.6
            op=int(180-lmb*5)
            #print(op)
            op2=int(540+lmb*5)
            if(w==0):
                lmain = tk.Label(window)
                move()
                w=1
            lmain.place(x=0, y=op)
            samp = cv2.resize(samp, (865+lml*10, op2))
            mco=0
            mco1=0
           # lmain.update()
            window.update()
            
            
        elif(m==0):
            if(1265-lml*10<=865):
                lml=lml-1
                
            if(724.375-lmb*5<=530):
                lmb=lmb-1/1.6
            
            lml=lml+1
            if(1265-lml*10<=865 and mco1==0):
                move3()
                mco1=1
            lmb=lmb+1/1.6       
            if(724.375-lmb*5<=530 and mco==0):
                move4()
                mco=1
            op=int(-7+lmb*5)
            op2=int(724.375-lmb*5)
           # lmain.destroy()
            if(w==0):
                lmain = tk.Label(window)
                move()
                w=1
            lmain.place(x=0, y=op)
            samp = cv2.resize(samp, (1265-lml*10, op2))
            
            #lmain.update()
            window.update()
       #cv2.putText(samp,str(t)+"<-t"+str(t1)+"<-t1"+str(t2)+"<-t2"+str(t3)+"<-t3",(20, 200),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
        if(sm!=0):
            if(label[int(i)]=="Yawning"):
                y=y+1
                                            
            if(label[int(i)]=="Talkingviaphone"):
                k = k+1
                j = j+1
            else:
                k=0
                alarm=0
            
            if(label[int(i)]=="Watching Forward"):
                f=f+1
                
            if(label[int(i)]=="Sleeping"):
                s=s+1
    #
            if(label[int(i)]=="Watching Backward"):
                b=b+1
 

       #cv2.putText(samp,"Prediction : "+label[int(i)],(20, 180),font, 1.2,(255,255,255),3,cv2.LINE_4)

        
    # Use putText() method for 
    # inserting text on video 
        #cv2.putText(samp,  
         #       label[int(i)],
          #      (20, 110),  
           #     font, 1,  
            #    (255, 255, 255),  
             #   3,  
              #  cv2.LINE_4) 
#        cv2.putText(samp,  
 #               "Frame No.",
  #              (20, 90),  
   #             font, 1,  
    #            (255, 255, 255),  
     #           3,  
      #          cv2.LINE_4)
#        cv2.putText(samp,  
 #               str(start),
  #              (190, 90),  
   #             font, 1,  
    #            (255, 255, 255),  
     #           3,  
      #          cv2.LINE_4)
      
        #cv2.putText(samp, "Prediction - "+label[int(i)], (20, 170), font, 1, (255, 255, 255), 3, cv2.LINE_4)   
        
     
            if(t1==1):
                if(t2==1):
                    if(t3==1):
                        #print("hello")
                        #Talking_via_phone fcount1,j,k,c
                        if(k>=100 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            #
                            alarm=1
                            
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf1/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)                       
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
                                     
                             
                        if(fcount1<=3500 and j>=1050 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=2
                            cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=1050 and j>=150 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=3
                            alarm=1
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3500):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                            if(fcount2<=300 and y>=130 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn -- Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn1/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                #
                                alarm=1
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=430 and y>=135 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn -- Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn5/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                #
                                alarm=1
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>430):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=750 and y+j+s+b>=701 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                           # lmain.destroy()
                            cv2.putText(samp, "Response Time : "+str(round((forw2/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            #
                            alarm=1
                            #print(c2)
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>750):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>52 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep1)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                #
                                alarm=1
                                if(c3==40):
                                    #alarm=0
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290): 
                                fcount4=0
                            #    s=0
                        else:
                            if(s>65  and c3<40 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                #
                                alarm=1
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep3)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                              #  s=0

                        # Watching Backwards b,c4,fcount5


                        if(b>=58  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            
                            fcount5=fcount5-1
                            c4=c4+1
                            #
                            alarm=1
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back2)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                            
                        

            if(t1==1):
                if(t2==1):
                    if(t3==2):
                    ################## hill + Light Snow
                        #Talking_via_phone fcount1,j,k,c
                       
                        if(k>=150 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            alarm=1
                            #
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
    #                           
                             
                        if(fcount1<=3600 and j>=1050 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy, park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=2
                            cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=1080 and j>=150 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=3
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"
                            #Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3600):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                            if(fcount2<=300 and y>=133 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn3/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=430 and y>=138 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn7/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>430):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=800 and y+j+s+b>=751 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            alarm=1
                            cv2.putText(samp, "Response Time : "+str(round((forw3/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            #print(c2)
                            #
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>800):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>70 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep4)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290):  
                                fcount4=0
                                s=0
                        else:
                            if(s>80  and c3<40 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep7)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                                s=0

                        # Watching Backwards b,c4,fcount5

                        
                        if(b>=75  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            fcount5=fcount5-1
                            c4=c4+1
                            alarm=1
                            #
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back3)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                            
                        

            if(t1==1):
                if(t2==2):
                    if(t3==1):
                    ################## hill + Heavy Rain
                        #Talking_via_phone fcount1,j,k,c
                       
                        if(k>=100 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            alarm=1
                            #
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf1/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)                       
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
    #                           
                             
                        if(fcount1<=3300 and j>=950 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy, park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=2
                            cv2.putText(samp, "Response Time : "+str(round((tvf7/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=980 and j>=150 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=3
                            cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3300):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                            if(fcount2<=300 and y>=130 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn1/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=430 and y>=135 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn5/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>430):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=700 and y+j+s+b>=651 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((forw1/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            #
                            alarm=1
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>700):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>52 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep1)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290):  
                                fcount4=0
                                s=0
                        else:
                            if(s>65 and c3<40 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep6)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                                s=0

                        # Watching Backwards b,c4,fcount5
                       # cv2.putText(samp,str(b),(20, 190),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,str(fcount5),(20, 240),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        if(b>=58  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            fcount5=fcount5-1
                            c4=c4+1
                            alarm=1
                            
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back1)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                            
                        

            if(t1==1):
                if(t2==2):
                    if(t3==2):
                    ################## hill + Light Rain
                        #Talking_via_phone fcount1,j,k,c
                       
                        if(k>=150 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            alarm=1
                            #
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
    #                           
                             
                        if(fcount1<=3400 and j>=950 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy, park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=2
                            cv2.putText(samp, "Response Time : "+str(round((tvf7/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=1080 and j>=180 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=3
                            cv2.putText(samp, "Response Time : "+str(round((tvf5/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3400):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                            if(fcount2<=300 and y>=133 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn3/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=430 and y>=138 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn7/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>430):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=750 and y+j+s+b>=701 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            alarm=1
                            cv2.putText(samp, "Response Time : "+str(round((forw2/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            #
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>750):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>70 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep4)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290):  
                                fcount4=0
                                s=0
                        else:
                            if(s>80  and c3<40 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep7)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                                s=0

                        # Watching Backwards b,c4,fcount5

                        
                        if(b>=75  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            fcount5=fcount5-1
                            c4=c4+1
                            alarm=1
                            #
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back2)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                            
                        

            if(t1==1):
                if(t2==3):
                    if(t3==1):
                    ################## hill + Heavy Fog
                        #Talking_via_phone fcount1,j,k,c
                       
                        if(k>=100 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            alarm=1
                            #
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf1/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
    #                           
                             
                        if(fcount1<=3500 and j>=1050 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy, park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=2
                            cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=1000 and j>=150 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=3
                            cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3500):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                            if(fcount2<=300 and y>=130 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn1/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=430 and y>=135 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn5/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>430):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=750 and y+j+s+b>=701 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            alarm=1
                            cv2.putText(samp, "Response Time : "+str(round((forw2/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            #
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>750):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>52 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep1)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290):  
                                fcount4=0
                                s=0
                        else:
                            if(s>65 and c3<40 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep3)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                                s=0

                        # Watching Backwards b,c4,fcount5

                        
                        if(b>=58  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            fcount5=fcount5-1
                            c4=c4+1
                            alarm=1
                            #
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back2)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                            
                        

            if(t1==1):
                if(t2==3):
                    if(t3==2):
                    ################## hill + Light Fog
                        #Talking_via_phone fcount1,j,k,c
                       
                        if(k>=150 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            alarm=1
                            #
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)                       
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
    #                           
                             
                        if(fcount1<=3600 and j>=1050 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy, park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=2
                            cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=1050 and j>=110 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=3
                            cv2.putText(samp, "Response Time : "+str(round((tvf2/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3600):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                            if(fcount2<=300 and y>=133 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn3/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=430 and y>=138 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn7/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>430):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=800 and y+j+s+b>=751 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            alarm=1
                            #
                            cv2.putText(samp, "Response Time : "+str(round((forw3/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            #
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>800):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>70 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep4)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290):  
                                fcount4=0
                                s=0
                        else:
                            if(s>80  and c3<40 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep7)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                                s=0

                        # Watching Backwards b,c4,fcount5
                        
                        
                        if(b>=75  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            fcount5=fcount5-1
                            c4=c4+1
                            alarm=1
                            #
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back3)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                if(t2==4):
                  #Talking_via_phone fcount1,j,k,c
                   
                    if(k>=170 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                        c=c+1
                        sig=1
                        cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #
                        #
                        alarm=1
                        cv2.putText(samp, "Response Time : "+str(round((tvf10/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)                       
                        #k=k-1
                        if(c==40):
                            sig=0
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
                                 
                         
                    if(fcount1<=3600 and j>=1070 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                        cv2.putText(samp,"TVF -- If busy park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #
                        alarm=1
                        sig=2
                        cv2.putText(samp, "Response Time : "+str(round((tvf11/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        #
                        #j = 0
                        
                        if(c==40):
                            sig=0
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1050 and j>=130 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                           #j = 0
                        cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #
                        #
                        alarm=1
                        sig=3
                        cv2.putText(samp, "Response Time : "+str(round((tvf12/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        #
                        if(c==40):
                            alarm=0                        
                            sig=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>3600):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=300 and y>=135 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                            cv2.putText(samp,"Yawn -- Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            alarm=1
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn5/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            #
                            
                            if(c1==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>300):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=430 and y>=138 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                            cv2.putText(samp,"Yawn -- Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            alarm=1
                            cv2.putText(samp, "Response Time : "+str(round((yawn13/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            #
                            if(c1==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>430):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=800 and y+j+s+b>=731 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                        cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #
                        #
                        alarm=1
                        cv2.putText(samp, "Response Time : "+str(round((forw5/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        #
                        if(c2==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>800):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3

                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>70 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                            cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            alarm=1
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep4)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            #
                            if(c3==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>290): 
                            fcount4=0
                            s=0
                    else:
                        if(s>80  and c3<40 and fcount4<=290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                            fcount4=fcount4-1
                            c3=c3+1
                            #
                            alarm=1
                            if(c3==40):
                              #  alarm=0
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep7)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                        if(fcount4>290):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5


                    if(b>=95  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                        
                        fcount5=fcount5-1
                        c4=c4+1
                        #
                        alarm=1
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back6)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>310):
                        fcount5=0
                        b=0
                      

            if(t1==2):
                if(t2==1):
                    if(t3==1):
                    ###################### Plains Heavy Snow#######################
                        #Talking_via_phone fcount1,j,k,c
                       
                        if(k>=140 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            alarm=1
                            #
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)                        
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
    #                           
                             
                        if(fcount1<=3700 and j>=1050 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy, park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=2
                            cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=1050 and j>=180 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=3
                            cv2.putText(samp, "Response Time : "+str(round((tvf5/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3700):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                            if(fcount2<=300 and y>=132 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn2/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=450 and y>=134 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>450):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=800 and y+j+s+b>=751 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            alarm=1
                            cv2.putText(samp, "Response Time : "+str(round((forw3/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            #
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>800):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>60 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep2)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290): 
                                fcount4=0
                                s=0
                        else:
                            if(s>80  and c3<40 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep7)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                                s=0

                        # Watching Backwards b,c4,fcount5

                        
                        if(b>=70  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            fcount5=fcount5-1
                            c4=c4+1
                            alarm=1
                            #
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back4)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                            
                        

            if(t1==2):
                if(t2==1):
                    if(t3==2):
                    ################## Plains + Light Snow
                        #Talking_via_phone fcount1,j,k,c
                       
                        if(k>=190 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            alarm=1
                            #
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf6/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)                        
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
    #                           
                             
                        if(fcount1<=3800 and j>=1050 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy, park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            sig=2
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=1080 and j>=150 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=3
                            cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3800):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                            if(fcount2<=300 and y>=135 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn5/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=450 and y>=140 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn8/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>450):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=850 and y+j+s+b>=801 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((forw4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            alarm=1
                            #
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>850):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>77 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep6)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290):  
                                fcount4=0
                                s=0
                        else:
                            if(s>90  and c3<40 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep8)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                                s=0

                        # Watching Backwards b,c4,fcount5

                        
                        if(b>=83  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            fcount5=fcount5-1
                            c4=c4+1
                            alarm=1
                            #
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back6)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                            
                        

            if(t1==2):
                if(t2==2):
                    if(t3==1):
                    ################## plain + Heavy Rain
                        #Talking_via_phone fcount1,j,k,c
                       
                        if(k>=140 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            alarm=1
                            #
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)                       
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
    #                           
                             
                        if(fcount1<=3500 and j>=1000 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy, park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            sig=2
                            cv2.putText(samp, "Response Time : "+str(round((tvf8/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=1000 and j>=100 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            sig=3
                            cv2.putText(samp, "Response Time : "+str(round((tvf1/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3500):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                            if(fcount2<=300 and y>=132 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn2/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=450 and y>=134 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>450):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=750 and y+j+s+b>=701 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            alarm=1
                            #
                            cv2.putText(samp, "Response Time : "+str(round((forw2/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            #
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>750):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>60 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep2)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290):  ## identation error
                                fcount4=0
                                s=0
                        else:
                            if(s>80 and c3<40 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep7)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                                s=0

                        # Watching Backwards b,c4,fcount5

                        
                        if(b>=70  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            fcount5=fcount5-1
                            c4=c4+1
                            alarm=1
                            #
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back5)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                            
                        

            if(t1==2):
                if(t2==2):
                    if(t3==2):
                    ################## plain + Light Rain
                        #Talking_via_phone fcount1,j,k,c
                       
                        if(k>=150 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            alarm=1
                            #
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)                        
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
    #                           
                             
                        if(fcount1<=3600 and j>=1000 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy, park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            sig=2
                            cv2.putText(samp, "Response Time : "+str(round((tvf8/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=1050 and j>=110 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            sig=3
                            cv2.putText(samp, "Response Time : "+str(round((tvf2/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3600):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                            if(fcount2<=300 and y>=135 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn5/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=450 and y>=137 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn6/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>450):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=800 and y+j+s+b>=751 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((forw3/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            #
                            alarm=1
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>800):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>76 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep5)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290):  ## identation error
                                fcount4=0
                                s=0
                        else:
                            if(s>90  and c3<40 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep8)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                                s=0

                        # Watching Backwards b,c4,fcount5

                        
                        if(b>=83  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            fcount5=fcount5-1
                            c4=c4+1
                            alarm=1
                            #
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back4)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                            
                        

            if(t1==2):
                if(t2==3):
                    if(t3==1):
                    ################## plain + Heavy Fog
                        #Talking_via_phone fcount1,j,k,c
                       
                        if(k>=140 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            alarm=1
                            #
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf3/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)                       
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
    #                           
                             
                        if(fcount1<=3700 and j>=1050 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy, park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            sig=2
                            cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=1050 and j>=180 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            sig=3
                            cv2.putText(samp, "Response Time : "+str(round((tvf5/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3700):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                            if(fcount2<=300 and y>=132 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn2/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=450 and y>=134 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>450):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=800 and y+j+s+b>=751 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            alarm=1
                            cv2.putText(samp, "Response Time : "+str(round((forw3/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            #
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>800):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>60 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep2)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290):  ## identation error
                                fcount4=0
                                s=0
                        else:
                            if(s>80 and c3<40 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep7)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                                s=0

                        # Watching Backwards b,c4,fcount5

                        
                        if(b>=70  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            fcount5=fcount5-1
                            c4=c4+1
                            alarm=1
                            #
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back4)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                            
                      

            if(t1==2):
                if(t2==3):
                    if(t3==2):
                    ################## plain + Light Fog
                        #Talking_via_phone fcount1,j,k,c
                       
                        if(k>=190 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            c=c+1
                            alarm=1
                            #
                            cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            sig=1
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((tvf6/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)                        
                            #k=k-1
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                            
    #                           
                             
                        if(fcount1<=3800 and j>=1050 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                            cv2.putText(samp,"TVF -- If busy, park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=2
                            cv2.putText(samp, "Response Time : "+str(round((tvf9/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            #j = 0
                            
                            if(c==40):
                                sig=0
                                alarm=0                        
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                      
                                
                        if(fcount1<=1080 and j>=150 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                               #j = 0
                            cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            sig=3
                            cv2.putText(samp, "Response Time : "+str(round((tvf4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount1 = fcount1-1
                            c=c+1
                            alarm=1
                            #
                            if(c==40):
                                sig=0
                                alarm=0                        
                                
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                                
                        if(fcount1>3800):
                            fcount1=0
                            j=0

                        #Yawning x,fcount2,y,c1

                        if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                           # cv2.putText(samp,str(y),(20, 190),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #cv2.putText(samp,str(fcount2),(20, 240),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            if(fcount2<=300 and y>=135 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn5/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                      
                            if(fcount2>300):
                                fcount2=0
                                y=0
                        else:
                            if(fcount2<=450 and y>=138 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                                cv2.putText(samp,"Yawn - Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round((yawn7/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                                fcount2=fcount2-1
                                c1=c1+1
                                alarm=1
                                #
                                if(c1==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                    

                            if(fcount2>450):
                                fcount=0
                                y = 0
                        #Forward fcount3,f,c2
                     
                        
                        if(fcount3<=850 and y+j+s+b>=801 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                            cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            alarm=1
                            cv2.putText(samp, "Response Time : "+str(round((forw4/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount3=fcount3-1
                            c2=c2+1
                            #
                            if(c2==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount3>850):
                            fcount3=0
                            f=0

                        #Sleeping x,fcount4,s,c3
                        
                        
                          
                        if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                            if(c3<40  and s>77 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep6)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0

                            if(fcount4>290):  ## identation error
                                fcount4=0
                                s=0
                        else:
                            if(s>90  and c3<40 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                                fcount4=fcount4-1
                                c3=c3+1
                                alarm=1
                                #
                                if(c3==40):
                                    alarm=0
                                    fcount1 = 0
                                    fcount2 = 0
                                    fcount3 = 0
                                    fcount4 = 0
                                    fcount5=0
                                    c=0
                                    c1=0
                                    c2=0
                                    c3=0
                                    c4=0
                                    j = 0
                                    k = 0
                                    b = 0
                                    c = 0
                                    #
                                    #
                                    f=0
                                    y=0
                                    s=0
                                cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                                #
                                #
                                cv2.putText(samp, "Response Time : "+str(round(((sleep8)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                            if(fcount4>290):
                                fcount4=0
                                s=0

                        # Watching Backwards b,c4,fcount5

                        
                        if(b>=84 and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                            fcount5=fcount5-1
                            c4=c4+1
                            alarm=1
                            #
                            if(c4==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((back5)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            
                        if(fcount5>310):
                            fcount5=0
                            b=0
                            
                if(t2==4):    
                  #Talking_via_phone fcount1,j,k,c
                  #  cv2.putText(samp,"  "+str(j),(20, 190),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                    
                    if(k>=210 and c<40 and (sig!=2 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                        c=c+1
                        alarm=1
                        #
                        sig=1
                        cv2.putText(samp,"TVF -- Keep Phone Aside",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round((tvf13/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)                       
                        #k=k-1
                        if(c==40):
                            sig=0
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0

                        
                                 
                         
                    if(fcount1<=3800 and j>=1070 and c<40 and (sig!=1 and sig!=3) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                        cv2.putText(samp,"TVF -- If busy park and talk",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #
                        sig=2
                        cv2.putText(samp, "Response Time : "+str(round((tvf11/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)  
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #
                        #j = 0
                        
                        if(c==40):
                            sig=0
                            alarm=0                        
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                  
                            
                    if(fcount1<=1080 and j>=170 and c<40 and (sig!=2 and sig!=1) and ((alarm==0 and label[int(i)]=="Talkingviaphone")  or c!=0)):
                           #j = 0
                        #cv2.putText(samp,str(c),(20, 190),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #
                        sig=3
                        cv2.putText(samp, "Response Time : "+str(round((tvf10/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                        fcount1 = fcount1-1
                        c=c+1
                        alarm=1
                        #
                        if(c==40):
                            sig=0
                            alarm=0                        
                            
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        #cv2.putText(samp,"TVF -- Don't talk while driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #cv2.putText(samp,"Response Time : 20.8860759s",(20, 140),font, 1,(255, 255, 255),3,cv2.LINE_4)  
                            
                    if(fcount1>3800):
                        fcount1=0
                        j=0

                    #Yawning x,fcount2,y,c1

                    if((x.hour>=15 and x.hour<=18) or (x.hour>=0 and x.hour<=6)):
                        if(fcount2<=300 and y>=138 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                            cv2.putText(samp,"Yawn -- Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn7/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            #
                            
                            if(c1==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                  
                        if(fcount2>300):
                            fcount2=0
                            y=0
                    else:
                        if(fcount2<=450 and y>=140 and c1<40 and ((alarm==0 and label[int(i)]=="Yawning") or c1!=0)):
                            cv2.putText(samp,"Yawn -- Take a break",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round((yawn8/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)            
                            fcount2=fcount2-1
                            c1=c1+1
                            alarm=1
                            #
                            if(c1==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                                

                        if(fcount2>450):
                            fcount=0
                            y = 0
                    #Forward fcount3,f,c2
                 
                    
                    if(fcount3<=850 and y+j+s+b>=781 and c2<40 and ((alarm==0 and label[int(i)]!="Watching Forward") or c2!=0)):
                        cv2.putText(samp,"Forw -- Be attentive",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #
                        alarm=1
                        #
                        cv2.putText(samp, "Response Time : "+str(round((forw6/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                        fcount3=fcount3-1
                        c2=c2+1
                        #
                        if(c2==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                            

                    if(fcount3>850):
                        fcount3=0
                        f=0

                    #Sleeping x,fcount4,s,c3

                    
                      
                    if((x.hour<6 and x.hour>2) or (x.hour<18 and x.hour>15)):
                        if(c3<40  and s>97 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                            cv2.putText(samp,"Sleep -- Focus on Driving",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep9)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            #
                            if(c3==40):
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0

                        if(fcount4>290): 
                            fcount4=0
                            s=0
                    else:
                        if(s==1):
                            print(fcount4)
                         
                        if(fcount4==150):
                            print(s)
                        if(s>110  and c3<40 and fcount4<290 and ((alarm==0 and label[int(i)]=="Sleeping") or c3!=0)):
                            fcount4=fcount4-1
                            c3=c3+1
                            alarm=1
                            #
                            if(c3==40):
                               # alarm=0
                                alarm=0
                                fcount1 = 0
                                fcount2 = 0
                                fcount3 = 0
                                fcount4 = 0
                                fcount5=0
                                c=0
                                c1=0
                                c2=0
                                c3=0
                                c4=0
                                j = 0
                                k = 0
                                b = 0
                                c = 0
                                #
                                #
                                f=0
                                y=0
                                s=0
                            cv2.putText(samp,"Sleep -- Be Alert",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                            #
                            #
                            cv2.putText(samp, "Response Time : "+str(round(((sleep10)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)

                        if(fcount4>290):
                            fcount4=0
                            s=0

                    # Watching Backwards b,c4,fcount5

                    if(b==15):
                        print(fcount5)
                    #if(fcount5==195):
                      #  print(b)
                    if(b>=103  and c4<40 and fcount5<=310 and ((alarm==0 and label[int(i)]=="Watching Backward") or c4!=0)):
                        
                        fcount5=fcount5-1
                        c4=c4+1
                        alarm=1
                        #
                        if(c4==40):
                            alarm=0
                            fcount1 = 0
                            fcount2 = 0
                            fcount3 = 0
                            fcount4 = 0
                            fcount5=0
                            c=0
                            c1=0
                            c2=0
                            c3=0
                            c4=0
                            j = 0
                            k = 0
                            b = 0
                            c = 0
                            #
                            #
                            f=0
                            y=0
                            s=0
                        cv2.putText(samp,"Backward -- Look Forward",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)
                        #
                        #
                        cv2.putText(samp, "Response Time : "+str(round(((back7)/790)*30, 2))+"s", (20, 140), font, 1, (255, 255, 255), 3, cv2.LINE_4)
                        
                    if(fcount5>310):
                        fcount5=0
                        b=0
                  
                    

                        
                    
      
      
      
          
          
          
      
      
        elif(sm==0):
            cv2.putText(samp,"Vehicle Stationary",(20, 100),font, 1.4,(255, 255, 255),3,cv2.LINE_4)



        if(t==1):
            if(t1==1):
                if(t2==1):
                    if(t3==1):
                        
                        cv2.putText(samp,  
                "Morning+Hill+Heavy Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                
                
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Hill+Light Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Morning+Hill+Heavy Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Hill+Light Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Morning+Hill+Heavy Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Hill+Light Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==4):
                  
                    cv2.putText(samp,  
            "Morning+Hill+Pleasant Weather",
            (20, 50),  
            font, 1,  
            (255, 255, 255),  
            3,  
            cv2.LINE_4)
            elif(t1==2):
                if(t2==1):
                    if(t3==1):
                        cv2.putText(samp,  
                "Morning+Plain+Heavy Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Plain+Light Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Morning+Plain+Heavy Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Plain+Light Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Morning+Plain+Heavy Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Morning+Plain+Light Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==4):
                  
                    cv2.putText(samp,  
            "Morning+Plain+Pleasant Weather",
            (20, 50),  
            font, 1,  
            (255, 255, 255),  
            3,  
            cv2.LINE_4)
            
        elif(t==2):
            if(t1==1):
                if(t2==1):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Hill+Heavy Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Hill+Light Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Hill+Heavy Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Hill+Light Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Hill+Heavy Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Hill+Light Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==4):
                  
                    cv2.putText(samp,  
            "Noon+Hill+Pleasant Weather",
            (20, 50),  
            font, 1,  
            (255, 255, 255),  
            3,  
            cv2.LINE_4)
            elif(t1==2):
                if(t2==1):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Plain+Heavy Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Plain+Light Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Plain+Heavy Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Plain+Light Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Noon+Plain+Heavy Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Noon+Plain+Light Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==4):
                  
                    cv2.putText(samp,  
            "Noon+Plain+Pleasant Weather",
            (20, 50),  
            font, 1,  
            (255, 255, 255),  
            3,  
            cv2.LINE_4)
        elif(t==3):
            if(t1==1):
                if(t2==1):
                     if(t3==1):
                        cv2.putText(samp,  
                "Night+Hill+Heavy Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                     elif(t3==2):
                        cv2.putText(samp,  
                "Night+Hill+Light Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Night+Hill+Heavy Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Night+Hill+Light Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Night+Hill+Heavy Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Night+Hill+Light Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==4):
                  
                    cv2.putText(samp,  
            "Night+Hill+Pleasant Weather",
            (20, 50),  
            font, 1,  
            (255, 255, 255),  
            3,  
            cv2.LINE_4)
            elif(t1==2):
                if(t2==1):
                    if(t3==1):
                        cv2.putText(samp,  
                "Night+Plain+Heavy Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Night+Plain+Light Snow",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==2):
                    if(t3==1):
                        cv2.putText(samp,  
                "Night+Plain+Heavy Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Night+Plain+Light Rain",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==3):
                    if(t3==1):
                        cv2.putText(samp,  
                "Night+Plain+Heavy Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                    elif(t3==2):
                        cv2.putText(samp,  
                "Night+Plain+Light Fog",
                (20, 50),  
                font, 1,  
                (255, 255, 255),  
                3,  
                cv2.LINE_4)
                elif(t2==4):
                  
                    cv2.putText(samp,  
            "Night+Plain+Pleasant Weather",
            (20, 50),  
            font, 1,  
            (255, 255, 255),  
            3,  
            cv2.LINE_4)
        samp = cv2.cvtColor(samp, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(samp)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        #lmain.after(0)
        window.update()


def move():
    global m,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b2,b21,b22,b23,b24,lml,lmb
    m=1
    b1.place_forget()
    b2.place_forget()
    b3.place_forget()
    b4.place_forget()
    b5.place_forget()
    b6.place_forget()
    b7.place_forget()
    b8.place_forget()
    b9.place_forget()
    b10.place_forget()
    b11.place_forget()
    b12.place_forget()
    b13.place_forget()
    b14.place_forget()
    b15.place_forget()
    b16.place_forget()
    b17.place_forget()
    b18.place_forget()
    b19.place_forget()
    b20.place_forget()
    b21.place_forget()
    b22=actionBtn = Button(window, text="<< ", font = "Arial 15 bold", bg="gray85", fg="gray20", activebackground="gray85", activeforeground="blue2", highlightthickness=0, borderwidth = 0, command=move2)
    b22.place(x=1255, y=0)
    b23.place_forget()
    b24.place_forget()
    lml=0
    lmb=0
    
def move2():
    global m,lml,lmb,show
    if(show==0):
        move3()
        move4()
    m=0
    lml=0
    lmb=0
def move3():
    global m,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b2,b21,b22
    b22.place_forget()
    b1.place(x=880, y=0)
    b2.place(x=910, y=10)
    b3.place(x=900, y=50)
    b4.place(x=1020, y=50)
    b5.place(x=1110, y=50)
    b6.place(x=910, y=142)
    b7.place(x=900, y=182)
    b8.place(x=985, y=182)
    b9.place(x=910, y=274)
    b10.place(x=900, y=314)
    b11.place(x=1030, y=314)
    b12.place(x=1115, y=314)
    b13.place(x=1200, y=314)
    b14.place(x=910, y=406)
    b15.place(x=900, y=446)
    b16.place(x=995, y=446)
    b17.place(x=910, y=538)
    b18.place(x=900, y=578)
    b19.place(x=1060, y=578)
    b20.place(x=1020, y=650)
    #b21=actionBtn = Button(window, text=">", font = "Times 9 bold", bg="gray85", fg="gray20", activebackground="gray85", activeforeground="blue2", highlightthickness=0, borderwidth = 0, command=move)
    b21.place(x=840, y=0)

    
def move4():
    global b23,b24
    b23.place(x=0, y=25)
    b24.place(x = 150,y=80)

def stationary():
    global sm
    sm=0
    
def moving():
    global sm
    sm=1


b1 = Canvas(window, width=486, height=768, bg="gray85")

b1.place(x=880, y=0)
b1.create_line(10, 20, 330, 20,fill="gray78")
b1.create_line(10, 23, 330, 23,fill="gray70",width=3)
b1.create_line(10, 23, 10, 100,fill="gray78")
b1.create_line(13, 23, 13, 100,fill="gray70",width=3)
 
v1 = IntVar()

myfont1=font.Font(family='Calibri', size=14, weight='bold')


b2=tk.Label(window, text = "Time of day",  fg = "black",
		 bg = "gray85",
		 font = "Calibri 14 bold italic")
b2.place(x=910,y=10)

b1.create_line(325, 23, 325, 100,fill="gray78")
b1.create_line(328, 23, 328, 100,fill="gray70",width=3)
b1.create_line(10, 100, 330, 100,fill="gray70",width=3)
b1.create_line(10, 102, 330, 102,fill="gray78")  



b3=Radiobutton(window, text="Morning", font=myfont1, variable=v1, activebackground="gray85", value=1, height=1, width=7
                  ,command=morning)
b3.place(x=900, y=50)                  
b4=Radiobutton(window, text="Noon", font=myfont1, variable=v1, activebackground="gray85", value=2, height=1, width=4
                  ,command=noon)
b4.place(x=1020, y=50)                  
b5=Radiobutton(window, text="Night", font=myfont1, variable=v1, activebackground="gray85", value=3, height=1, width=4
                  ,command=night)
b5.place(x=1110, y=50)
                  
# Create button and image
#login_btn3 = PhotoImage(file = r'/home/itm1138/Desktop/mo.png')
#actionBtn3 = Button(window, image = login_btn3, bg='white',highlightthickness=2, borderwidth = 2, command=morning).place(x=885, y=50)

# Create button and image
#login_btn4 = PhotoImage(file = r'/home/itm1138/Desktop/noon.png')
#actionBtn4 = Button(window, image = login_btn4, bg='white',highlightthickness=2, borderwidth = 2, command=noon).place(x=1053, y=50)

# Create button and image
#login_btn5 = PhotoImage(file = r'/home/itm1138/Desktop/night.png')
#actionBtn5 = Button(window, image = login_btn5, bg='white',highlightthickness=2, borderwidth = 2, command=night).place(x=1170, y=50)


v2 = IntVar()

b1.create_line(10, 152, 215,152,fill="gray78")
b1.create_line(10, 155, 215, 155,fill="gray70",width=3)
b1.create_line(10, 155, 10, 232,fill="gray78")
b1.create_line(13, 155, 13, 232,fill="gray70",width=3)

myfont1=font.Font(family='Calibri', size=14, weight='bold')


b1.create_line(210, 155, 210, 232,fill="gray78")
b1.create_line(213, 155, 213, 232,fill="gray70",width=3)
b1.create_line(10, 232, 215, 232,fill="gray70",width=3)
b1.create_line(10, 234, 215, 234,fill="gray78")  


b6=tk.Label(window, text = "Landform",  fg = "black",
		 bg = "gray85",
		 font = "Calibri 14 bold italic")
b6.place(x = 910,y=142)         

b7=Radiobutton(window, text="Hill", font=myfont1, variable=v2, activebackground="gray85", value=1
                  ,command=hill)
b7.place(x=900, y=182)    
              
b8=Radiobutton(window, text="Plain", font=myfont1, variable=v2, activebackground="gray85", value=2
                  ,command=plain)
b8.place(x=985, y=182)
# Create button and image
#login_btn1 = PhotoImage(file = r'/home/itm1138/Desktop/hillp.png')
#actionBtn1 = Button(window, image = login_btn1, bg='white',highlightthickness=2, borderwidth = 2, command=hill).place(x=961, y=180)

# Create button and image
#login_btn2 = PhotoImage(file = r'/home/itm1138/Desktop/plain.png')
#actionBtn2 = Button(window, image = login_btn2, bg='white',highlightthickness=2, borderwidth = 2, command=plain).place(x=1058, y=180)



v3 = IntVar()

b1.create_line(10, 284, 405, 284,fill="gray78")
b1.create_line(10, 287, 405, 287,fill="gray70",width=3)
b1.create_line(10, 287, 10, 364,fill="gray78")
b1.create_line(13, 287, 13, 364,fill="gray70",width=3)

myfont1=font.Font(family='Calibri', size=14, weight='bold')


b1.create_line(400, 287, 400, 364,fill="gray78")
b1.create_line(403, 287, 403, 364,fill="gray70",width=3)
b1.create_line(10, 364, 405, 364,fill="gray70",width=3)
b1.create_line(10, 366, 405, 366,fill="gray78")  



b9=tk.Label(window, text = "Weather",  fg = "black",
		 bg = "gray85",
		 font = "Calibri 14 bold italic")
b9.place(x = 910,
		y=274)
b10=Radiobutton(window, text="Pleasant", font=myfont1, variable=v3, activebackground="gray85", value=1
                  ,command=pleasant)
b10.place(x=900, y=314)                  
b11=Radiobutton(window, text="Snow", font=myfont1, variable=v3, activebackground="gray85", value=2
                  ,command=snow)
b11.place(x=1030, y=314)                 
b12=Radiobutton(window, text="Rain", font=myfont1, variable=v3, activebackground="gray85", value=3
                  ,command=rain)
b12.place(x=1115, y=314)                  
b13=Radiobutton(window, text="Fog", font=myfont1, variable=v3, activebackground="gray85", value=4
                  ,command=fog)
b13.place(x=1200, y=314)



# label text1:
#tk.Label(root, text="Style 1", font="Bahnschrift 20", bg="#100E17", fg="green").place(x=150, y=35)

v4 = IntVar()

b1.create_line(10, 416, 225,416,fill="gray78")
b1.create_line(10, 419, 225, 419,fill="gray70",width=3)
b1.create_line(10, 419, 10, 496,fill="gray78")
b1.create_line(13, 419, 13, 496,fill="gray70",width=3)

myfont1=font.Font(family='Calibri', size=14, weight='bold')


b1.create_line(220, 419, 220, 496,fill="gray78")
b1.create_line(223, 419, 223, 496,fill="gray70",width=3)
b1.create_line(10, 496, 225, 496,fill="gray70",width=3)
b1.create_line(10, 498, 225, 498,fill="gray78")  





b14=tk.Label(window, text = "Intensity",  fg = "black",
		 bg = "gray85",
		 font = "Calibri 14 bold italic")
b14.place(x = 910,
		y=406)
b15=Radiobutton(window, text="Heavy", font=myfont1, variable=v4, activebackground="gray85", value=1
                  ,command=heavy)
b15.place(x=900, y=446)                 
b16=Radiobutton(window, text="Light", font=myfont1, variable=v4, activebackground="gray85", value=2
                  ,command=light)
b16.place(x=995, y=446)


v5 = IntVar()


b1.create_line(10, 548, 300,548,fill="gray78")
b1.create_line(10, 551, 300, 551,fill="gray70",width=3)
b1.create_line(10, 551, 10, 628,fill="gray78")
b1.create_line(13, 551, 13, 628,fill="gray70",width=3)

myfont1=font.Font(family='Calibri', size=14, weight='bold')


b1.create_line(295, 551, 295, 628,fill="gray78")
b1.create_line(298, 551, 298, 628,fill="gray70",width=3)
b1.create_line(10, 628, 300, 628,fill="gray70",width=3)
b1.create_line(10, 630, 300, 630,fill="gray78")  


b17=tk.Label(window, text = "Vehicle State",  fg = "black",
		 bg = "gray85",
		 font = "Calibri 14 bold italic")
b17.place(x = 910,
		y=538)
b18=Radiobutton(window, text="Stationary", font=myfont1, variable=v5, activebackground="gray85", value=1
                  ,command=stationary)
b18.place(x=900, y=578)                  
b19=Radiobutton(window, text="Moving", font=myfont1, variable=v5, activebackground="gray85", value=2
                  ,command=moving)
b19.place(x=1060, y=578)                 

#var = IntVar()

#myfont1=font.Font(family='Arial', size=20, weight='bold')

#R1 = Radiobutton(window, text="Heavy", font=myfont1, variable=var, bg="black", fg="white", activebackground="black", activeforeground="white",value=1, height=1, width=4, selectcolor="black"
 #                 ,command=heavy).place(x=1000, y=400)

#R2 = Radiobutton(window, text="Light", variable=var, value=2, height=1, width=5,
 #                 command=light).place(x=1000, y=450)

# checkbox set1:
#tk.Checkbutton(window, text="HEAVY", font="Arial", takefocus=0, bg="white", fg="black", activebackground="white", activeforeground="black", bd=0, highlightthickness=2, width=10, selectcolor="white", height=2, onvalue=1, offvalue=0, command=heavy).place(x=1000, y=400)
#tk.Checkbutton(window, text="LIGHT", font="Arial", takefocus=0, bg="white", fg="black", activebackground="white", activeforeground="black", bd=0, highlightthickness=2, width=10, selectcolor="white", height=2, onvalue=1, offvalue=0, command=light).place(x=1000, y=450)

#Create button and image
login_btn = PhotoImage(file = r'/home/itm1138/Desktop/op11.png')
b20=actionBtn = Button(window, image = login_btn, highlightthickness=0, borderwidth = 2, command=predict)
b20.place(x=1020, y=650)
login_btn2 = PhotoImage(file = r'/home/itm1138/Desktop/arrow5.png')
b21=actionBtn = Button(window, text=">>", font = "Arial 15 bold", bg="gray85", fg="gray20", activebackground="gray85", activeforeground="blue2", highlightthickness=0, borderwidth = 0, command=move)
b21.place(x=840, y=0)
window.mainloop()

