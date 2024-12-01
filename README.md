# public_deepL_proxy
Public DeepL Proxy for running Translating Extracted Text on ancientbrain.com

* Put your DeepL API key in the .json file under public_proxy/proxy/
* Create a password and place that password in the .json
* Install the requirements (by running *pip3 -r requirements.txt* in the public_proxy directory)
* Run the server using *python3 manage.py runserver*
* Note the address the server is running on
* On the ancientBrain page for extracting text and translating text, place the URL you noted in the above step in the deepL proxy api url input box and hit "set".
* In the box below, put in the *PASSWORD* that you set, *NOT* the deepL API key.
* All done. Hit "translate" on the website (so long as you have already extracted text to translate) to translate using Google, Microsoft, and DeepL.
