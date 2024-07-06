import pickle
from flask import Flask, render_template, request, url_for
print('hello world')
#object creation
app=Flask(__name__)
model=pickle.load(open('model.pkl', 'rb'))
#url
@app.route("/")
def index():
    return render_template('Index.html')
#to open new page we will give new end point

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = model.predict([[int(request.form.get('temperature'))]])
    output = round(prediction[0], 2)
    return render_template('Index.html',prediction_text=f'Total amount in Rs {output}/-')


if __name__=='__main__':
    app.run(debug=True)