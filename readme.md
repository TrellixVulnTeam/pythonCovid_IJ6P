# Python Vaccination Managment App [P.V.M.A]
## _Using Firebase and Kivy_

This Application has the following feautures For the Public User
- Sign up an account with their personal information (e.g., name, age, ID, phone, postcode,
address, etc.),
- Login to enter/update medical history, Covid-19 status (i.e., under-quarantine or normal)
and occupations.
- Login to check their appointment date, time and location.
- Login to R.S.V.P to the assigned appointment (i.e., yes or no).

For administrator, login to:
- Categorize the public users into high-risk or low-risk based on their medical history.
- Categorize the public users into priority ranking (1 to 5, with higher the value higher priority)
based on their occupations.
- Create vaccination centers: location and capacity per hour (i.e., how many individuals can be
vaccinated in an hour).
- Set appointment for public users by assigning vaccination center with specific date and time.
- Sort the public users according to their postcode, age, Covid-19 status, priority, group, etc.
- Generate the list of assigned appointments for a vaccination center and sorted by date and
time, containing users’ name, ID, RSVP, phone and risk group.

Extra's
- To auto-categorize the public users into high-risk and low-risk group based on medical
history and priority ranking based on occupation.
- To store all available data in persistent storage [Firebase]
- Graphical user interface. [For User App]



### Please Follow instructions to run the Application
## installation [Mac & Windows] *Rquires Python 3*

```sh
pip install virtualenv
```

## [Windows]

For User App

```sh
kivy_venv\Scripts\activate
python main.py
```

For production environments...

```sh
kivy_venv\Scripts\activate
python admin.py
```
## [Mac]

For User App

```sh
kivy_venv/bin/activate
python main.py
```

For production environments...

```sh
kivy_venv/bin/activate
python admin.py
```
