# JAAN AI

A terminal based AI Assistant created using Google PALM LLM API.
It's features are listed below.

## License

This work is licensed under the [MIT License](https://opensource.org/licenses/MIT).

### Permissions
- Use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software.

### Conditions
- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the software.

### Disclaimer
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Installation Guide

If anything happens to your device, we are not responsible for it. Use it on your own risk btw according to me it's safe to use.

Follow these steps to set up and configure your software:

Firstly download the code in your device by clicking on the green `Code` button above and then click `Download ZIP`. Extract the zip now.
And in the directory open powershell and run `pip install -r requirements.txt` to install all the necessary packages. Python version `3.11` is required for using it.

### Step 1: Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/) and sign in or create a new account.
2. Create a new project by clicking on the project dropdown menu at the top of the page and selecting "New Project".
3. Follow the prompts to enter a project name, organization, and billing information if required. Then click "Create".

### Step 2: Generate an API Key

1. Once your project is created, navigate to the [API Key creation page](https://aistudio.google.com/app/apikey).
2. Click on the "Create API Key" button.
3. Copy the generated API key.

### Step 3: Update Configuration File

1. Open the `data.json` file in your project directory.
2. Add the copied API key to the `API_KEY` field in the `data.json` file.

```json
{
  "API_KEY": "YOUR_API_KEY_HERE",
  "username": "YOUR_USERNAME_HERE",
}
```

3. Fill other necessary details in the `data.json` file.

### Step 4: Start

Now you are ready to use it. Just run the JAAN.exe file and it will start. When the text is "Listening", you can ask your query and talk. Make sure the word "Jaan" is included in your query, if it's not there it will not respond.

## Features

- Wikipedia Search : You can ask about something which is available on wikipedia. The command is `Jaan wikipedia search {your_query}`.

  For example -> `Jaan wikipedia search Akshay Kumar`

- Youtube Search : She can also search youtube for you. The command is `Jaan youtube search {your_search_query}`.

  For example -> `Jaan youtube search Code With Harry`

- Play Video On Youtube : Command is `Jaan play {what_do_you_want_to_play} on youtube`.

  For example -> `Jaan play Python full course on youtube`

- Listen to Music : She can also play songs for you on youtube by the song name. The command is `Jaan play music` or `Jaan play song`. Then wait for the reply and say the song you want to listen. It will be started.

- Creating new window or tab : Say `Jaan new window` for new window and `Jaan new tab` for new tab.

- Closing and opening applications : If you say `Jaan close` it will close the currently opened window. And if u say `Jaan open {application_name}` she will search it in the start and will open it.

  For example -> `Jaan open Minecraft Launcher`

- Google Search : If you want to search something on google, say `Jaan google search {your_query}`.

  For example -> `Jaan google search how to make a cake`

- Speak you words : If you want her to say something, you can use `Jaan speak {text}`.

  For example -> `Jaan speak hey there welcome buddy` and she will speak "Hey there welcome buddy"

- Send mail : This feature is currently in beta but is working, if you wanna try you can by saying `Jaan send mail` and then she will guide you the other necessary steps. She will send the mail using Gmail.

- Voice Typing : Say `Jaan activate keyboard` and she will activate voice typing. Now you have to speak all the text you want to write but make sure you have the window opened where you wanna write and is currently active and then say it all in one go.

- Save file : This feature is also in beta currently but you can use it if you want to. Say `Jaan save file` when you are having the file currently opened. And then follow the steps.

- AI Chat : You can directly chat with the AI , just say anything including the word `Jaan` in your query and the AI will respond.

- Bye : You can say `Bye Jaan` to close it.

Will be soon adding more features like AI Image generator.


## Others
If you want to contribute or add some more amazing features to it, you can. If any error comes please report it. It is created using `Python 3.11`.
