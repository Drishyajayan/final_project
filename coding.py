from flask import *
from src.dbconnection import *
from src.chatbot import *
from src.maincode_svm import predct
from src.newcnn import predict_cnn

app=Flask(__name__)

app.secret_key="sdfghj"


@app.route('/')
def login():
    # return render_template('index.html')
    return render_template('loginindex.html')


@app.route('/login1',methods=['post'])
def login1():
    uname=request.form['textfield']
    password=request.form['textfield2']
    qry="SELECT * FROM `login` WHERE `uname`=%s AND `password`=%s"
    val=(uname,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid");window.location="/"</script>'''
    elif res['utype']=='admin':
        session['lid']=res['lid']
        return '''<script>alert("welcome");window.location="/home"</script>'''
    elif res['utype']=='expert':
        session['lid']=res['lid']

        return '''<script>alert("welcome");window.location="/home1"</script>'''

    elif res['utype']=='user':
        session['lid']=res['lid']

        return '''<script>alert("welcome");window.location="/user_home"</script>'''
    else:
        return '''<script>alert("invalid");window.location="/"</script>'''

    return render_template('/expert/login.html')

@app.route('/add_exprert')
def add_exprert():
    return render_template('/admin/add exprert.html')

@app.route('/add_exprert1',methods=['post'])
def add_exprert1():
    name = request.form['textfield']
    place = request.form['textfield2']
    pin = request.form['textfield3']
    post = request.form['textfield4']
    email = request.form['textfield5']
    phone = request.form['textfield6']
    username = request.form['textfield7']
    password = request.form['textfield8']
    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'expert')"
    val=(username,password)
    id=iud(qry,val)
    qry1="INSERT INTO `expert` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(id),name,place,post,pin,email,phone)
    iud(qry1,val1)
    return '''<script>alert("Added");window.location="/view_expert"</script>'''

@app.route('/EDIT_exprert')
def EDIT_exprert():
    eid=request.args.get('id')
    session['eid']=eid
    qry="select * from expert where id=%s"
    res=selectone(qry,eid)

    return render_template('/admin/editexprert.html',val=res)

@app.route('/edit_exprert1',methods=['post'])
def edit_exprert1():
    name = request.form['textfield']
    place = request.form['textfield2']
    pin = request.form['textfield3']
    post = request.form['textfield4']
    email = request.form['textfield5']
    phone = request.form['textfield6']
    qry="UPDATE `expert` SET `name`=%s,`place`=%s,`post`=%s,`pin`=%s,`email`=%s,`phno`=%s WHERE `id`=%s"
    val=(name,place,post,pin,email,phone,session['eid'])
    iud(qry, val)
    return '''<script>alert("updated");window.location="/view_expert"</script>'''



@app.route('/deletetip',methods=['post','get'])
def deletetip():
    eid = request.args.get('id')
    qry="delete from tip where id=%s"
    iud(qry,eid)

    return '''<script>alert("deleted");window.location="/managetip"</script>'''


@app.route('/EDIT_tip')
def EDIT_tip():
    eid=request.args.get('id')
    session['exid']=eid
    qry="select * from tip where id=%s"
    res=selectone(qry,eid)
    return render_template('expert/edittip.html',val=res)



@app.route('/edittip',methods=['post'])
def edittip():
    tip = request.form['textarea']
    qry="UPDATE `tip` SET `tip`=%s WHERE `id`=%s"
    val=(tip,session['exid'])
    iud(qry, val)
    return '''<script>alert("updated");window.location="/managetip"</script>'''



@app.route('/deleteexprert1',methods=['post','get'])
def deleteexprert1():
    eid = request.args.get('id')
    qry="delete from expert where lid=%s"
    iud(qry,eid)
    qry="delete from login where lid=%s"
    iud(qry,eid)
    return '''<script>alert("deleted");window.location="/view_expert"</script>'''









@app.route('/reply')
def reply():
    id=request.args.get('id')
    session['Cid']=id
    return render_template('/admin/reply.html')

@app.route('/reply1',methods=['post'])
def reply1():
    reply = request.form['textfield2']
    qry="UPDATE `complaint` SET `reply`=%s WHERE `id`=%s"
    val=(reply,session['Cid'])
    iud(qry,val)
    return '''<script>alert("Sended");window.location="/view_complaints"</script>'''



@app.route('/view_complaints')
def view_complaints():
    qry="SELECT `complaint`.*,`user`.`fname`,`lname`  FROM `user` JOIN `complaint` ON `complaint`.`lid`=`user`.`lid`  WHERE `reply`='pending'"
    res=selectall(qry)
    return render_template('/admin/view complaints.html',val=res)

@app.route('/view_expert')
def view_expert():
    qry="SELECT * FROM `expert`"
    res=selectall(qry)
    return render_template('/admin/view expert.html',val=res)

@app.route('/viewuser')
def viewuser():
    return render_template('/admin/viewuser.html')


@app.route('/add_dataset',methods=['post'])
def add_dataset():
    return render_template('/expert/add dataset.html')

@app.route('/add_dataset1', methods=['post'])
def add_dataset1():
    question=request.form['textfield23']
    ques=question.lower()
    print(ques,"======================")
    answer=request.form['textarea']
    qry=" INSERT INTO `datasets` VALUES(NULL,%s,%s)"
    val=(ques,answer)
    iud(qry,val)
    return '''<script>alert("Added");window.location="/question"</script>'''



@app.route('/ADD_TIP')
def ADD_TIP():
    qry = "SELECT * FROM `tip`"
    res = selectall(qry)
    return render_template('/expert/ADD TIP.html', val=res)

@app.route('/ADD_TIP1', methods=['post'])
def ADD_TIP1():
    tip=request.form['textarea']
    qry=" INSERT INTO `tip` VALUES(NULL,%s,%s)"
    val=(tip,session['lid'])
    iud(qry,val)
    return '''<script>alert("tip Added");window.location="/managetip"</script>'''

@app.route('/chat_view')
def chat_view():
    qry = "SELECT * FROM `user` "
    res = selectall(qry)
    return render_template('/expert/chat view.html',val=res)
@app.route('/vtip')
def vtip():
    qry="SELECT * FROM `tip` "
    res = selectall(qry)

    return render_template('/user/viewtip.html',val=res)

@app.route('/managetip')
def managetip():
    qry="SELECT * FROM `tip` WHERE exid=%s"
    res = selectall2(qry,session['lid'])

    return render_template('/expert/managetip.html',val=res)

@app.route('/question')
def question():
    qry = "SELECT * FROM `datasets`"
    res = selectall(qry)
    return render_template('/expert/question.html', val=res)



@app.route('/view_feedback')
def view_feedback():
    qry="SELECT `feedback`.*,`user`.`fname`,`lname`  FROM `user` JOIN `feedback` ON `feedback`.`lid`=`user`.`lid`"
    res=selectall(qry)
    print(res)
    return render_template('/expert/view feedback(expert).html',val=res)


@app.route('/view_user')
def view_user():
    qry="select * from user "
    res=selectall(qry)
    return render_template('/admin/viewuser.html',val=res)




@app.route('/view_user1')
def view_user1():
    qry="select * from user "
    res=selectall(qry)
    return render_template('/expert/view user.html',val=res)

@app.route('/home')
def home():
    return render_template('/admin/home.html')


@app.route('/home1')
def home1():
    return render_template('/expert/home1.html')


@app.route('/usercomplaint')
def usercomplaint():
    qry = "select * from complaint where lid=%s"
    res = selectall2(qry,session['lid'])
    return render_template('/user/COMPLAINT.html',val=res)

@app.route('/send_complaint',methods=['post'])
def send_complaint():
    return render_template('/user/send_complaint.html')





@app.route('/send_complaintt',methods=['post'])
def send_complaintt():
    comp=request.form['textfield']
    qry="INSERT INTO `complaint` VALUES(NULL,%s,%s,CURDATE(),'pending')"
    val=(session['lid'],comp)
    iud(qry,val)
    return '''<script>alert("success");window.location="/usercomplaint"</script>'''



@app.route('/deletetcomplaint',methods=['post','get'])
def deletetcomplaint():
    eid = request.args.get('id')
    qry="delete from complaint where id=%s"
    iud(qry,eid)

    return '''<script>alert("deleted");window.location="/usercomplaint"</script>'''



@app.route('/send_feedback')
def send_feedback():
    return render_template('/user/FEEDBACK.html')


@app.route('/send_feedbackk',methods=['post'])
def send_feedbackk():
    comp=request.form['textfield']
    qry="INSERT INTO `feedback` VALUES(NULL,%s,%s,CURDATE())"
    val=(session['lid'],comp)
    iud(qry,val)
    return '''<script>alert("success");window.location="/send_feedback"</script>'''
@app.route('/userfeedback')
def userfeedback():
    return render_template('/user/FEEDBACK.html')

@app.route('/userpredict')
def userpredict():
    return render_template('/user/PREDICT.html')

@app.route('/userregistration')
def userregistration():
    return render_template('reg_index.html')
@app.route('/userexpert')
def userexpert():
    qry="select * from expert"
    res=selectall(qry)
    return render_template('/user/VIEWEXPERT.html',val=res)


@app.route('/usereg',methods=['get','post'])
def usereg():

        fname = request.form['textfield']
        lname = request.form['textfield2']
        age = request.form['textfield3']
        gender = request.form['radiobutton']
        place = request.form['textfield5']
        post = request.form['textfield6']
        pin = request.form['textfield7']
        phno = request.form['textfield8']
        email = request.form['textfield9']
        username = request.form['textfield10']
        password = request.form['textfield11']
        qry="INSERT INTO `login` VALUES(NULL,%s,%s,'user')"
        val=(username,password)
        id=iud(qry,val)
        qry1="INSERT INTO `user` VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(str(id),fname,lname,age,gender,place,post,pin,phno,email)
        iud(qry1,val)
        return '''<script>alert("Registered");window.location="/"</script>'''

@app.route('/userfeed',methods=['get','post'])
def userfeed():

        feedback = request.form['textfield']

        qry="INSERT INTO `feedback` VALUES(NULL,%s,%s,curdate())"
        val=(session['lid'],feedback)
        iud(qry,val)

        @app.route('/home1')
        def home1():
            return render_template('/expert/home1.html')

        return '''<script>alert("feedback added ");window.location="/"</script>'''
@app.route('/user_home')
def user_home():
    return render_template('/userindex.html')

@app.route('/predict')
def predict():
    return render_template('/user/PREDICT.html')
@app.route('/predict1',methods=['post'])
def predict1():
    Age = request.form['textfield']
    Gender = request.form['select']
    ChestPainType = request.form['select2']
    BP = request.form['textfield5']
    Cholesterole = request.form['textfield6']
    FastingBS= request.form['textfield2']
    ECG = request.form['select3']
    HeartRate = request.form['textfield8']
    Excercise = request.form['select4']
    Oldeak = request.form['textfield11']
    STSlope = request.form['select5']

@app.route('/complaint')
def complaint():
        return render_template('/complaint.html')

# @app.route('/complaint')
# def complaint():
#         return render_template('user/compla.html')



# ////////////e_chat////////////////////////////////////////////


@app.route("/chat2")
def chatsp():
    pid=request.args.get('uid')
    print(pid,"==============================")
    session['pid']=pid
    qry="SELECT * FROM `user` WHERE `lid`=%s"
    res=selectone(qry,pid)


    print(res)


    qry="    SELECT * FROM `chat` WHERE `from`=%s AND `to`=%s OR `from`=%s AND `to`=%s "
    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)
    print(res1)

    print(res)

    fname=res['fname']
    lname=res['lname']
    return render_template("expert/chat2.html",data=res1,fname=fname,lname=lname,fr=str(session['lid']))



@app.route('/send',methods=['post'])
def sendchat():
    message=request.form['textarea']
    to_id = session['pid']
    from_id = session['lid']
    qry="insert into chat values(null,%s,%s,%s,CURDATE())"
    val=(from_id,to_id,message)
    iud(qry,val)


    return redirect("chatss")
@app.route("/chatss")
def chatss():
    pid=session['pid']
    qry="SELECT * FROM `user` WHERE `lid`=%s"
    res=selectone(qry,pid)
    qry="    SELECT * FROM `chat` WHERE `from`=%s AND `to`=%s OR `from`=%s AND `to`=%s "
    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)
    fname=res['fname']
    lname=res['lname']
    return render_template("/expert/chat2.html",data=res1,fname=fname,lname=lname,fr=session['lid'])



# ////////////e_chat////////////////////////////////////////////




# ////////////u_chat////////////////////////////////////////////


@app.route("/chat21")
def chatsp1():
    pid=request.args.get('uid')
    print(pid,"==============================")
    session['pid']=pid
    qry="SELECT * FROM `expert` WHERE `lid`=%s"
    res=selectone(qry,pid)


    sprint(res)


    qry="    SELECT * FROM `chat` WHERE `from`=%s AND `to`=%s OR `from`=%s AND `to`=%s "
    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)
    print(res1)

    print(res)

    name=res['name']
    # lname=res['lname']
    return render_template("user/chat21.html",data=res1,name=name,fr=session['lid'])



@app.route('/send1',methods=['post'])
def sendchat1():
    message=request.form['textarea']
    to_id = session['pid']
    from_id = session['lid']
    qry="insert into chat values(null,%s,%s,%s,CURDATE())"
    val=(from_id,to_id,message)
    iud(qry,val)


    return redirect("chatss1")
@app.route("/chatss1")
def chatss1():
    pid=session['pid']
    qry="SELECT * FROM `expert` WHERE `lid`=%s"
    res=selectone(qry,pid)
    qry="SELECT * FROM `chat` WHERE `from`=%s AND `to`=%s OR `from`=%s AND `to`=%s "
    val=(session['lid'],session['pid'],session['pid'],session['lid'])
    res1=selectall2(qry,val)
    name=res['name']
    print(res1)
    # lname=res['lname']
    return render_template("/user/chat21.html",data=res1,name=name,fr=str(session['lid']))



# ////////////u_chat////////////////////////////////////////////

# ////////////////////////chat_bot////////////////////////////
@app.route('/insertchatbot',methods=['post'])
def insertchatbot():
    question = request.form['textarea']
    qus=question.lower()
    print(qus)
    # lid = request.form['lid']
    # print(lid)

    res = cb(qus)
    # emo=sent(qus)
    qry = "INSERT INTO `chatbot` VALUES(NULL,%s,%s,%s)"
    val=(session['lid'],qus,res)
    iud(qry,val)
    return redirect('/response')


@app.route('/response')
def response():

    qry="SELECT `question` FROM `datasets`"
    res=selectall(qry)
    lid=[]
    for i in res:
        lid.append(i['question'])
    qry = "SELECT question,uid,answers FROM `chatbot` WHERE `uid`=%s"
    # val=(session['lid'])
    s = selectall2(qry,session['lid'] )
    print(s,"kkkkkkkkkkkkkkkkk")
    return render_template("/bot.html",data=s,fr=session['lid'],languages=lid)










@app.route('/predictfn')
def predictfn():
    return render_template('user/predctn.html',res="")


@app.route('/predict_fn',methods=['get','post'])
def predict_fn():
    print(request.form)
    age=request.form['textfield']
    Gender= request.form['radiobutton']
    ChestPainType=request.form['select2']

    BP=request.form['textfield3']
    Cholesterole=request.form['textfield7']
    FastingBloodSugar=request.form['textfield6']
    ECG=request.form['select3']
    HeartRate=request.form['textfield8']
    Exercise=request.form['select4']
    oldpeak=request.form['textfield11']
    STSlope=request.form['select5']

    val=[age,Gender,ChestPainType,BP,Cholesterole,FastingBloodSugar,ECG,HeartRate,Exercise,oldpeak,STSlope]
    re = predct([val])
    print(re)

    return render_template('user/predctn.html', res=re[0])

@app.route('/predict_by_ecg',methods=['get','post'])
def predict_by_ecg():
    if request.method=="POST":
        print(request.files)
        img = request.files['filef']
        img.save(r"D:\project\src\static\a.jpg")
        res=predict_cnn(r'static\a.jpg')
        print(res)
        if res==0:
            result="Fibrillation"
            des = "This label may indicate the presence of atrial fibrillation, which is a rapid and irregular beating of the heart's upper chambers (atria). Atrial fibrillation can lead to an increased risk of stroke and other complications."
        elif res==1:
            result="Myocardial Infarction"
            des="This label could represent ECG patterns associated with acute myocardial infarction or heart attack. It indicates the presence of abnormalities in the ECG resulting from a blockage in the coronary arteries, which leads to inadequate blood supply to the heart muscle."
        elif res==2:
            result="Normal"
            des="This label represents a normal ECG pattern, indicating a healthy heart without any significant abnormalities. It serves as a reference for comparison with abnormal ECG patterns."
        elif res==3:
            result="Block"
            des="The Q label may indicate the presence of conduction blockages or abnormalities, such as a bundle branch block or AV block. These conditions disrupt the normal electrical conduction in the heart."
        elif res==4:
            result="Supraventricular"
            des="This label can refer to various supraventricular arrhythmias, which are abnormal heart rhythms originating from the upper chambers (atria) of the heart. Examples include atrial tachycardia or atrial flutter."
        else:
            result="Ventricular"
            des="The V label indicates the presence of ventricular arrhythmias, which are abnormal heart rhythms originating from the lower chambers (ventricles) of the heart. Examples include ventricular tachycardia or ventricular fibrillation."
        return render_template('user/ecg_result.html',res=result,des1=des)
    return render_template('user/predecg.html')

@app.route('/deletechat',methods=['post','get'])
def deletetchat():
    eid = request.args.get('id')
    qry="delete from datasets where id=%s"
    iud(qry,eid)

    return '''<script>alert("deleted");window.location="/question#a"</script>'''
















# ////////////////////////////////chat_bot/////////////
app.run(debug=True,port=1234)












