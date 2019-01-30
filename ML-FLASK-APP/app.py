from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
from flask_material import Material
import numpy as np

from sklearn.externals import joblib

app = Flask(__name__)
Bootstrap(app)
Material(app)

@app.route('/')

def home():
    return render_template('home.html')


@app.route('/',methods=["POST"])

def analyze():

	if request.method == 'POST':
		
		size = request.form['BHK']
		balcony = request.form['BALCONY']
		bath = request.form['BATHROOM']
		area = request.form['AREA']
		sqft = request.form['SQFT']
		avail = request.form['AVAILABILITY']
		location = request.form['LOCATION']
		model_choice = request.form['MODEL']

		def fun_area(x):
			if area=='Carpet Area':
				return 1
			elif area=='Plot Area':
				return 3
			elif area=='Built_Up Area':
				return 2
			elif area=='Super Built_up Area':
				return 4

		def fun_avail(x):
			if avail=='Ready to move':
				return 1
			elif avail=='Available after may 2019':
				return 0

		def fun_loc(x):
			if location=='Whitefield':
				return 1252
			elif location=='Sarjapur Road':
				return 1039
			elif location=='Electronic City':
				return 417
			elif location=='Kanakpura Road':
				return 664
			elif location == 'Thanisandra':
				return 1148
			elif location == 'Yelahanka':
				return 1261
			elif location == 'Uttarahalli':
				return 1181
			elif location == 'Hebbal':
				return 869
			elif location == 'Marathahalli':
				return 277
			elif location == 'Raja Rajeshwari Nagar':
				return 566
			elif location == 'Hennur Road':
				return 690
			elif location == 'Bannerghatta Road':
				return 584
			elif location == '7th Phase JP Nagar':
				return 799
			elif location == 'Haralur Road':
				return 563
			elif location == 'Electronic City Phase II':
				return 1216
			elif location == 'Rajaji Nagar':
				return 381
			elif location == 'Bellandur':
				return 346
			elif location == 'KR Puram':
				return 530
			elif location == 'Electronics City Phase 1':
				return 514
			elif location == 'Yeshwanthpur':
				return 612

		
		lis1 = [fun_area(area),fun_loc(location),sqft,bath,balcony,size,fun_avail(avail)]
		clean_data=[float(i) for i in lis1]

		ex1 = np.array(clean_data).reshape(1,-1)
        
		if model_choice == 'Gradient Boosting':
			gb_model =joblib.load('data/gb.pkl')
			result_predict = gb_model.predict(ex1)
		elif model_choice == 'Random Forest':
			rf_model = joblib.load('data/rf.pkl')
			result_predict = rf_model.predict(ex1)


		result1 = round(result_predict[0],2) - 3.05
		result2 = round(result_predict[0],2) + 3.05







	return render_template('home.html',result_prediction =	round(result_predict[0],2),
							result_down = round(result1,2),result_up = round(result2,2),model=model_choice,
							location=location,avail=avail,area=area,
							size=size,balcony=balcony,sqft=sqft,bath=bath)
	

    
	



if __name__ == '__main__':
	app.run(debug=True)





