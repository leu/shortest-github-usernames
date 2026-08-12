Finds the shortest available usernames on GitHub

To run, first create a secret.txt file at the repository root, create a Personal access token (classic) in your GitHub settings, and place that token in the secret.txt file.

Create a Python venv, and install requirements.txt.

Then run main.py. The outputs will go into out/available.txt and out/taken.txt. These files will list GitHub usernames that are either available or taken.
