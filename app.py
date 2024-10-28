from flask import Flask, render_template,request,jsonify
import pickle

app=Flask(__name__)

@app.route("/")

def home():
    return render_template('index.html')

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method=="POST":
        preg=request.form.get('pregnancies')
        glu=request.form.get('glucose')
        bp=request.form.get('bloodPressure')
        sk=request.form.get('skinThickness')
        insulin=request.form.get('insulin')
        bmi=request.form.get('bmi')
        dpf=request.form.get('diabetesPedigreeFunction')
        age=request.form.get('age')
        print(preg,glu,bp,sk,insulin,bmi,dpf,age)
        with open('model.pickle','rb') as model_file:
            model=pickle.load(model_file)
        res= model.predict([[float(preg),float(glu),float(bp),float(sk),float(insulin),float(bmi),float(dpf),float(age)]])
        g=''
        if res[0]==1:
            g='Diabetic'
        else:
            g='Non Diabetic'
        return jsonify({'You are':[g]})
    
    else:
        return render_template('predict.html')



if __name__=='__main__':
    app.run(host='0.0.0.0',port=5050)