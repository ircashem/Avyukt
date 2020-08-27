# Avyukt - Exploitation Framework (Beta Version)
Avyukt is a Exploitation Framework which can be used to generate Malicious Payloads and exploit Windows OS. For now, I have only released a Beta Version. More updated features
and better payloads are going to be added soon in the final version.

# General Info about the Framework
Avyukt is a Framework which can generate Malicious Payloads for getting remote access on Windows Computers

The Framework is still under Developement and I am just releasing a Beta Version of it right now

**Please keep in mind that my Framework nor me is going to be responsible for Illegal Purposes, This is only made for Penetration Testing Purpose for White-Hat Hackers**

**I have not added the WebCam Streamer for Avyukt Payloads for now as you must have seen it in the video tutorial as the WebCam streamer is not stable for everyone right now, I will surely release it in the next Version.**

`Framework Version : 1.1.0 (Beta)`

`Developer : Vedant-Bhalgama`

`Framework Testers : Vedant-Bhalgama and GOWTHAM-OFFICIAL-PGN`

# Setting Up Avyukt
To use the Framework, You can simply download it as a ZIP File or you can clone it using this command

`git clone https://github.com/Vedant-Bhalgama/Avyukt.git`

Now, You need to direct to the directory `Avyukt_Setup` to run the setup.py file.

Simply type this command to run the setup

`python ./setup.py`

![Capture](https://user-images.githubusercontent.com/67494275/90950281-ad670700-e46d-11ea-8f8f-270600a620b9.PNG)

# Getting Started with Avyukt
To start the Framework, You need to run this command

`python ./Avyukt.py`

You will see a menu like this

![Capture](https://user-images.githubusercontent.com/67494275/90904157-89afac80-e3ec-11ea-8e71-e3e3db914f26.PNG)

If you run the Framework for the first time, Directory called `Output` will be created

To Generate **Malicious Payload**, Type 1

To use **Listeners**, Type 2

To use **Help**, Type 3

To **Exit Framework**, Type 4

# Evasion 
You will get a view like this when you enter the Evasion Menu

![Capture](https://user-images.githubusercontent.com/67494275/90950360-2cf4d600-e46e-11ea-9273-002bb921f4dc.PNG)

Please remember that the Framework is still under Beta Developement, More Upgrades and Updates are going to come soon

**For the best results, Please use 1st payload or In-Built Avyukt Payloads as they are the best in Bypassing Anti-Virus. New implementations are going to be added soon**

For Eg. I was to use the 1st Payload, Simply type `1` or any other number in the menu you wanna use

After you choose the payload you want to use, You will have to enter values for `Name`, `LHOST` and `LPORT`. After you have given values for these parameters, You simply have to choose `y` or `n` if you have to add icon to the Executable which will be generated. `Please note only .ico files are supported`. After you enter the values you have to give the raw python script path which will be generated in the `Output` Folder. Simple type `Output/<your scriptname.py>`. Now, You have to enter the path to the `.ico` file and the Framework will do the rest.

![Capture](https://user-images.githubusercontent.com/67494275/90959231-5a19a680-e4b7-11ea-90db-5fe2bc62ba31.PNG)

# Handlers
You will see a view like this after you enter the Handler Menu

![Capture](https://user-images.githubusercontent.com/67494275/90950451-2b77dd80-e46f-11ea-90da-de2fdee3c237.PNG)

What is Avyukt Handler?
  * Avyukt Handler is the Default Handler for the In-Built Avyukt Payloads which were Programmed by me
  * Payloads like `python/Avyukt/reverse_tcp` are compatible with Avyukt Handler
  
What is NetCat Handler?
  * NetCat is a very popular tool which you must be knowing.
  * There are some payloads in the Framework which require NetCat as a listener

What is Metasploit?
  * Come on man, You must be knowing about Metasploit, I dont have to tell it!
  
# Features of Avyukt Payload
Here are some of the features which are found in the default Avyukt Payloads
  * Screenshot Ability
  * Upload Files
  * Download Files
  * Webcam Hacking and streaming live (I have not added it in this release as it is not stable, I will add it in the next update)
  * Execute any System Command (notepad.exe or any other system command)

# Suggestion Form
Having Ideas for Framework? Don't be shy! Submit them here 

`https://docs.google.com/forms/d/1YKYxLAYj0R0P5TS3bnnPkdGVKZuiS6rrWCLgH_2Kzao/edit`

# Video Tutorial for Framework 
`coming soon ;)`

# Special Thanks To
   * `GOWTHAM-OFFICIAL-PGN`
   * `Diego Perez`
   * `Zaid Sabih`
