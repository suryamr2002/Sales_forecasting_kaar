# Sales_forecasting_kaar
## 🛍️ Sales Prediction Web App

The Sales Prediction Web Application, built using Flask, offers a powerful predictive tool for estimating sales figures on forthcoming dates. The core functionality revolves around leveraging a meticulously trained machine learning model. This model, carefully developed and fine-tuned, utilizes historical sales data to forecast future sales with a high degree of accuracy.

## 📦 Installation

Clone the repository: `https://github.com/suryamr2002/Sales_forecasting_kaar.git`


## 🚀 Usage

To run the web app, run the following command in your terminal:

```python app.py```


Once the app is running, you can access it in your browser at `http://localhost:5000/`.

## 🧑‍💻 Development

To make changes to the web app, you can edit the `app.py` file and the templates in the `templates/` directory.

To train a new machine learning model, you can run the `train_model.py` script.

## 🤝 Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.


---

## Code Explanation

The Flask app has three routes:

1. `/` - renders the `index.html` template, which contains a form for user input.
2. `/result.html` - renders the `result.html` template, which contains the predicted sales for the future date.
3. `/predict` - handles the form submission, gets the input values from the HTML form, uses a trained machine learning model to predict the sales for the next 12 months, and returns the predicted sales as a response to the HTML form.

The `train_model.py` script is used to train the machine learning model. The trained model is saved as a pickle file (`sales_prediction_model.pkl`) and loaded in the Flask app using the `pickle.load()` method.

## Jupyter notebook

The Jupyter notebook `Sales_forecasting.ipynb` contains the code for training the machine learning model. It uses the pandas library to load the dataset and preprocess it. Then it uses the sklearn library to split the dataset into training and testing sets and train a Random Forest Regressor model on the training data. Finally, it evaluates the model on the testing data and saves the trained model as a pickle file (`sales_prediction_model.pkl`).


---

## 📊 Dataset

The machine learning model was trained on a sales dataset obtained from Kaggle. The dataset includes information about the date, state, product category, sub-category, product name, and sales amount for each transaction.

---

Thank you for reading! If you have any questions or feedback, please let me know.
