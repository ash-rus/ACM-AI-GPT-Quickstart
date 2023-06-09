# GPT API Quickstart - Python example app

This is an example GPT Chat model project, based on the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd ACM-AI-GPT-Quickstart
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/Scripts/activate
   ```
5. Upgrade pip (if needed)

   ```bash
   $ pip install --upgrade pip
   ```
   
6. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```
   (Close and reopen your project if it doesn't work)
   
7. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```
   
8. Add your [API key](https://beta.openai.com/account/api-keys) to the `.env` file.

9. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
