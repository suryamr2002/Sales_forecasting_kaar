from flask import Flask, request, render_template
import pickle
import pandas as pd


app = Flask(__name__)

# Load the trained model
with open('sales_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result.html')
def result():
    return render_template('result.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the HTML form
    month = int(request.form['month'])
    quarter = int(request.form['quarter'])
    year = int(request.form['year'])
    state_code = int(request.form['state_code'])
    category_code = int(request.form['category_code'])
    sub_category_code = int(request.form['sub_category_code'])

    # Create a new input for future sales prediction
    new_input = pd.DataFrame({'Month': [month], 'Quarter': [quarter], 'Year': [year], 'State Code': [state_code], 'Category Code': [category_code], 'Sub-Category Code': [sub_category_code]})
    future_sales = model.predict(new_input)[0]
    # Use the trained model to predict the sales for the next 12 months
    future_inputs = [new_input]
    for i in range(0, 12):
        future_month = i+1  
        future_quarter = int((month-1)/3)+1
        future_year = year 
        future_input = pd.DataFrame({'Month': [future_month], 'Quarter': [future_quarter], 'Year': [future_year], 'State Code': [state_code], 'Category Code': [category_code], 'Sub-Category Code': [sub_category_code]})
        future_inputs.append(future_input)
    sales_predictions = [(f"{inp.iloc[0]['Month']}/{inp.iloc[0]['Year']}", model.predict(inp)[0]) for inp in future_inputs]
    
    # Return the predicted sales as a response to the HTML form
    return render_template('index.html',prediction=f"Predicted sales for the future date: ${future_sales:.2f}", predictions=sales_predictions)

if __name__ == '__main__':
    app.run(debug=True)
