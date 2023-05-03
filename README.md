# Sales_forecasting_kaar
## 🛍️ Sales Prediction Web App

This is a Flask web application that uses a trained machine learning model to predict sales for a future date based on user input.

## 📦 Installation

1. Clone the repository: `git clone https://github.com/your-username/sales-prediction-web-app.git`
2. Install the required packages: `pip install -r requirements.txt`

## 🚀 Usage

To run the web app, run the following command in your terminal:

python app.py


Once the app is running, you can access it in your browser at `http://localhost:5000/`.

## 🧑‍💻 Development

To make changes to the web app, you can edit the `app.py` file and the templates in the `templates/` directory.

To train a new machine learning model, you can run the `train_model.py` script.

## 🤝 Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Code Explanation

The Flask app has three routes:

1. `/` - renders the `index.html` template, which contains a form for user input.
2. `/result.html` - renders the `result.html` template, which contains the predicted sales for the future date.
3. `/predict` - handles the form submission, gets the input values from the HTML form, uses a trained machine learning model to predict the sales for the next 12 months, and returns the predicted sales as a response to the HTML form.

The `train_model.py` script is used to train the machine learning model. The trained model is saved as a pickle file (`sales_prediction_model.pkl`) and loaded in the Flask app using the `pickle.load()` method.

## 📊 Dataset

The machine learning model was trained on the [Superstore Sales Dataset](https://community.tableau.com/s/article/Superstore-Sales), which contains sales data for a fictional superstore in the United States. The dataset includes information about the date, product category, and sales amount for each transaction.

---

Thank you for reading! If you have any questions or feedback, please let me know.
