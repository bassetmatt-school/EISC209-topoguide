# Individual Web Project

## 1. Objective
The goal is to use the tutorial knowledge to build an app. <br>
The app **Topguide** will enable users to share their hiking trips on some routes. Each route can have 0,1 or several trips related. <br>
The app is bound to be evolutive, but in the individual part it will implement only the elements details in [2.](##2.-App-Description)
## 2. App Description
The app will feature a list of routes which will have the following attributes :
- Title
- Starting point
- Description
- Initial height
- Min height
- Max height
- Positive cumulated elevation gain
- Negative cumulated elevation gain
- Estimated duration (hours)
- Difficulty (from 1 to 5)

A trip will consist in the following ones :
- The registering user
- Corresponding route
- Trip date
- Actual duration (hours)
- Number of people that participated
- Group experience (beginers, experienced, mixed)
- Weather (good, neutral, bad)
- Difficulty felt

## 3. TODO
- [x] [Auth](###5.1-Auth)
- [ ] [Route list](###5.2-Route-list)
- [ ] [Trip from Route](###5.3-Trip-from-Route)
- [ ] [Trip visual](###5.4-Trip-visual)
- [ ] [Create trip](###5.5-Create-trip)
- [ ] [Edit trip](###5.6-Edit-trip)
- [ ] [Navigation ?](###5.7-Navigation-?)

## 4. Git
This document is on git, should be okay

## 5. Project details
### 5.1 Auth
- [x] Use the `User` class from `django` (see [this](https://docs.djangoproject.com/fr/4.0/topics/auth/default/))
- [x] Use the integrated url management
- [x] Write template in `templates/registration/`
- [x] Setup `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL`
- [ ] Add `@login_required()` on every view
### 5.2 Route list
- [x] Add `itineraire` class in `models.py` (see [2.](##2.-App-Description)) 
- [x] Add a few routes
- [x] Create a view in `views.py` that gets the routes and returns the appropriate HTML template
- [x] Set the url to `itineraires/`
- [x] Set the redirect value here if the login successes
- [x] Create the HTML template
- [ ] Have something just enough nice-looking

### 5.3 Trip from Route
### 5.4 Trip visual
### 5.5 Create trip
### 5.6 Edit trip
### 5.7 Navigation ?
- [ ] Menu

### 5.x Extra ideas 
- [ ] Refine the template for `login.html`
- [ ] Setup a password changing template/system ?
- [ ] English and french version using html ?
- [ ] Favicons