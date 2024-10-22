
# 🍏 Nutrition Scale App

Welcome to the **Nutrition Scale App**! This Flask web application allows users to search for food items, view their nutritional information, and keep track of their daily food consumption. 🍽️

## 🚀 Features

- **Search for Food**: Enter the name of a food item to find its nutritional details.
- **Calculate Nutrition**: Get nutritional information based on the weight of the selected food item.
- **Daily Consumption Tracker**: Keep track of all the foods consumed in a day and see total nutrition.
- **Clear Daily Data**: Easily reset your daily consumption data.
- **User-Friendly Interface**: Built with Bootstrap for a clean and responsive design.

## :bookmark_tabs: Roadmap
- User Login
- Phone app
- ESP Scale integration
- Data Tracking

## 📜 License

This project is licensed under the [Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## 🔧 Technologies Used

- **Flask**: A lightweight web framework for Python.
- **Bootstrap**: For responsive UI components.
- **Requests**: To make API calls to the FatSecret API for food data.
- **dotenv**: For managing environment variables.

## ⚙️ Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/GerasimosKan/nutrition-scale-app.git
   cd nutrition-scale-app
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**: Create a `.env` file in the root directory with the following content:
   ```plaintext
   CLIENT_ID=your_client_id
   CLIENT_SECRET=your_client_secret
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the App**: Open your browser and go to `http://127.0.0.1:5000`.

## 🌟 Features

- **Search for Foods**: Easily search for food items using the FatSecret API.
- **Nutrition Calculation**: Input the weight of selected food items to calculate nutrition values.
- **Daily Consumption Tracker**: Keep track of daily food intake and total nutrition values.
- **Clear Day Button**: Reset your daily entries with a single click.
- **User-Friendly Interface**: Built with Bootstrap for a responsive design.

## 🛠️ Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **FatSecret API**: Provides access to a comprehensive food database and nutritional information.
- **HTML/CSS**: For front-end development and user interface.
- **Bootstrap**: For responsive and modern UI components.

## 📝 How to Run the Project

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/yourusername/nutrition-scale.git
   cd nutrition-scale
   ```
2. Install the required dependencies.
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables in a `.env` file using the provided example.
4. Run the Flask application.
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000/` to use the application.

## 👥 Contributing

Contributions are welcome! If you'd like to improve this project, please fork the repository and submit a pull request.

## 🤝 Acknowledgements

- Thanks to [FatSecret](https://www.fatsecret.com/) for providing the API for nutrition data.
- Inspired by community feedback and user needs.

Happy tracking! 🎉
