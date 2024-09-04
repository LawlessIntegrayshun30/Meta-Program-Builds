# user_interface.py

from flask import Flask, request, render_template
from main import Main

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        wallet_address = request.form.get('wallet_address')
        email_address = request.form.get('email_address')
        
        # Define the wallets and emails here
        # This is a placeholder for the actual wallets and emails
        wallets = {"wallet1": "key1", "wallet2": "key2"}
        emails = {"email1": "password1", "email2": "password2"}

        # Instantiate the Main class
        main = Main(wallets, emails)

        # Run the main function and get the result
        result = main.main(wallet_address, email_address)
        
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
