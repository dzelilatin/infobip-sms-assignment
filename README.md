# Infobip SMS Script Assignment

This is a simple Python script built for the Infobip Solution Engineer assignment.

The program reads a list of phone numbers and sender IDs from a `messages.csv` file, sends a text message to each number using the Infobip SMS API, and then saves the results (like the official `messageId` and delivery status) into a new `messages_output.csv` file.

---

### What's in Here?

* `send_sms.py`: The main Python script that does all the work.
* `messages.csv`: This is where you put the numbers you want to text. You need to fill in the `SenderId` and `MSISDN` columns yourself.
* `.env`: A file to keep your secret API Key and Base URL safe. **This is not included in the repo on purpose!**
* `.gitignore`: Tells Git to ignore the `.env` file so I don't accidentally share my secrets.
* `messages_output.csv`: The file that the script creates with all the results.

---

### How to Get it Running

**1. Set up the project:**
First, clone the repository to your computer and navigate into the folder.
```bash
git clone [https://github.com/dzelilatin/infobip-sms-assignment.git](https://github.com/dzelilatin/infobip-sms-assignment.git)
cd infobip-sms-assignment
```

**2. Install the necessary libraries:**
This script needs a couple of Python packages to work. You can install them with this command:
```bash
pip install requests python-dotenv
```

**3. Create your `.env` file:**
You'll need to create a file named `.env` in the main folder. This is where you'll put your secret keys from Infobip. The script will read them from here.
```
API_KEY=your_infobip_api_key_goes_here
BASE_URL=https://your_infobip_base_url_goes_here
```

**4. Edit `messages.csv`:**
Open up the `messages.csv` file and add the phone numbers you want to send messages to. Remember to use the international format for the `MSISDN` column!

**5. Run the script!**
Now, just run the script from your terminal:
```bash
python send_sms.py
```

You'll see a `messages_output.csv` file pop up in your folder with the results from the API. Done!