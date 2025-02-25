#Prediction using Neural Network
import cv2
import matplotlib.pyplot as plt
from keras.models import load_model
label = ["Watching Backward","Watching Forward","Sleeping","Yawning","Talkingviaphone"]
model = load_model(r'D:\DDNet\best.h5')

#  Testing Dataset(On which videos are running well)

# Watching Backward
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Backwards\Daylight\ab.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Backwards\Daylight\pb.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Backwards\Daylight\rb.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Other\Daylight\pf4.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Backwards\Daylight\sb.mp4')
#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Backwards\Night\psb.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Backwards\Night\rbb.mp4')

# Watching Forward
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Forward\Daylight\a.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Forward\Daylight\p.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Forward\Daylight\sr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Other\Daylight\pf1.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Other\Daylight\pf2.mp4')
#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Forward\Night\rs.mp4')(sometimes shows talking via phone, only working video in night dataset)
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Other\Night\ps2el.mp4')(small video and sametimes shows yawing)

# Sleeping
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Sleeping\Daylight\a.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Sleeping\Daylight\pr.mp4')(plz everyone see this video)(at ending time shows some variation)
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Sleeping\Daylight\r.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Sleeping\Daylight\rf.mp4')( a very little fluctuation in labels)
#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Sleeping\Night\rs.mp4')

# Talking via phone
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Talking via phone\Daylight\r.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Other\Daylight\pf5.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Talking via phone\Daylight\pc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Talking via phone\Daylight\rfs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Talking via phone\Daylight\a.mp4')
#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Talking via phone\Night\m.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Talking via phone\Night\ps.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Talking via phone\Night\rbs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Talking via phone\Night\rs.mp4')

#Yawning
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Yawning\Daylight\sc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Other\Daylight\pf6.mp4') #only this can be shown in jatayu
# in these videos the eyes are closed then is showing yawning and sometime wactching forward)
#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Yawning\Night\m.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Yawning\Night\mf.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Yawning\Night\ps.mp4')


#  Testing Dataset(On which videos are not running well)

# Watching Backward
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Other\Daylight\pf3.mp4')(sometimes shows yawning)
#Night

# Watching Forward
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Forward\Daylight\rf.mp4')(showing talking via phone)

#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Other\Night\ps1el.mp4')(very small video and sometimes shows yawning whenever mouth open)
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Forward\Night\mbg.mp4')(showing yawning when driver is talking)
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Forward\Night\psc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Forward\Night\mm.mp4')

# Other Videos
#Daylight
#Night

# Sleeping
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Other\Daylight\pf7.mp4')(sometimes shows talking via phone)
#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Sleeping\Night\mb.mp4')( showing wactching backward and sometimes yawning)
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Sleeping\Night\mf.mp4')(showing every other label)
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Sleeping\Night\mm.mp4')(showinh batching backward)

# Talking via phone
#Night

# Yawning
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Yawning\Daylight\pn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Yawning\Daylight\r.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Yawning\Daylight\rc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Yawning\Daylight\rs.mp4')
## in every video not even a single time predicting yawing mostly watching forward and sometimes talking via phone)

#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Testing Dataset\Yawning\Night\rs.mp4')


#  Training Dataset(On which videos are running well)

# Watching Backward
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\ac.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\ac2.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\ar.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\ar2.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\ar3.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\gr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\mcs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\ms.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\pc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\pr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\pr2.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\rn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\sc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Daylight\sn.mp4')
#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Night\km.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Night\kn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Night\psc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Night\rbc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Night\rc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Night\rn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Night\xm.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Night\xn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Night\xs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Night\ym.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Backwards\Night\yn.mp4')

# Watching Forward
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\ac.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\an.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\an2.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\ar.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\ar2.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\as.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\gr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\mcs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\mr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\pc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\pr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\rc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\rn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\rr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\sc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Daylight\sn.mp4')
#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\km.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\kn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\psm.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\psn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\pss.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\rbc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\rbn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\rbr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\rc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\rn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\xm.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\xn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\yn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Forward\Night\ys.mp4')

# Sleeping
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\ar.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\as.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\gn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\gr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\mcs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\ms.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\pn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\ps.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\rc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\rr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\sn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\sr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Daylight\ss.mp4')
#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\km.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\psc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\psm.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\psn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\pss.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\rbc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\rbn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\rbs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\rc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\rn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\xm.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\yn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Sleeping\Night\ys.mp4')

# Talking via phone
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\ac.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\ar.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\gc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\gs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\mcs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\ms.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\pn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\pr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\rc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\rr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\sc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\sn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Daylight\sr.mp4')
#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\km.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\kn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\psc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\psm.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\psn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\rbc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\rbn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\rc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\rn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\xm.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\xn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\xs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\yn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\ys.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\ysm.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Talking via phone\Night\ysm2.mp4')

# Yawning
#Daylight
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Daylight\ac.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Daylight\an.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Daylight\ar.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Daylight\gn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Daylight\gr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Daylight\mcs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Daylight\mr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Daylight\ms.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Daylight\sn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Daylight\sr.mp4')
#Night
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\kn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\kn2.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\psc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\pss.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\rbc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\rbn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\rbr.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\rc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\rfc.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\rfn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\rfs.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\rn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\yn.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\yn2.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\ys.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\ys2.mp4')
#cap = cv2.VideoCapture(r'D:\DDNet\Training Dataset\Yawning\Night\ys3.mp4')

#  Training Dataset(On which videos are not running well)

# Watching Backward
#Daylight

#Night

# Watching Forward
#Daylight

#Night

# Sleeping
#Daylight

#Night

# Talking via phone
#Daylight

#Night

# Yawning
#Daylight

#Night


while True:
    _, samp = cap.read()
    #samp = cv2.rotate(samp, cv2.ROTATE_90_CLOCKWISE)
    #samp = cv2.rotate(samp, cv2.ROTATE_90_COUNTERCLOCKWISE)
    image = cv2.resize(samp, (100,100))
    image = image.astype("float")
    image= image.reshape(1, 100, 100, 3)
    answer = model.predict(image)
    i = answer.argmax(axis=1)[0]
    font = cv2.FONT_HERSHEY_SIMPLEX 
  
    # Use putText() method for 
    # inserting text on video 
    cv2.putText(samp,  
                label[int(i)],
                (50, 50),  
                font, 1,  
                (0, 0, 255),  
                3,  
                cv2.LINE_4) 
    image = cv2.resize(samp, (100,100))    
    cv2.imshow('video', samp) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap.release() 
cv2.destroyAllWindows() 


