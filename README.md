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
- The registering user **key**
- Corresponding route **key**
- Trip date
- Actual duration (hours)
- Number of people that participated
- Group experience (beginers, experienced, mixed)
- Weather (good, neutral, bad)
- Difficulty felt

## 3. TODO
- [x] [Auth](###5.1-Auth)
- [x] [Route list](###5.2-Route-list)
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
- [x] Add `Itineraire` class in `models.py` (see [2.](##2.-App-Description)) 
- [x] Add a few routes
- [x] Create a view in `views.py` that gets the routes and returns the appropriate HTML template
- [x] Set the url to `itineraires/`
- [x] Set the redirect value here if the login successes
- [x] Create the HTML template
- [x] Have `@login_required()` (or equivalent)
- [x] Have something just enough nice-looking

### 5.3 Trip from Route
- [ ] Add `Sortie` class in `models.py`
- [ ] Add a few trips
- [ ] Create a view `sorties` that gets the trips
- [ ] The view must be at `/sorties/<route id>`
- [ ] Create template
- [ ] Create a link to see/modify the trip
- [ ] Create a button to add a trip
- [ ] Have `@login_required()` (or equivalent)
- [ ] Have something just enough nice-looking

### 5.4 Trip visual
- [ ] Create a view `sortie` to visualise a trip
- [ ] The view must be at `sortie/<trip id>`
- [ ] Create template
- [ ] Have `@login_required()` (or equivalent)
- [ ] Have something just enough nice-looking

### 5.5 Create trip
- [ ] Create a view `nouvelle_sortie`
- [ ] Redirect to the trip visual once it's created
- [ ] The view must be at `/nouvelle_sortie/`
- [ ] Have `@login_required()` (or equivalent)
- [ ] Have something just enough nice-looking

### 5.6 Edit trip
- [ ] Create a view `modif_sortie` that will summon the entry modification form
- [ ] Redirect to the trip visual once it's saved
- [ ] Adapt the previous template for modification
- [ ] Have `@login_required()` (or equivalent) + must be restricted to the user that created this trip
- [ ] Have something just enough nice-looking

### 5.7 Navigation ?
- [ ] Implement a navigation system, menu ?

### 5.x Extra ideas 
- [ ] Refine the template for `login.html`
- [ ] Better style for every page obviously
- [ ] Setup a password changing template/system ?
- [ ] English and french version using html ?
- [ ] Favicons
- [ ] Have a button "save and continue edit" in the creation/modification of a trip
