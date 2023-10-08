# <p align="center"> *CarCollection* </p>
### <p align="center"> The app allows the user to browse different cars, including their price, category, year, type, and model. The user can create, edit, or delete cars at any time. He/ She can also edit or delete his/ her profile. </p>
## Solution:
### 1. **Models**
#### CarCollectionUser
- `Email`
- `Password`
#### Profile
- `First Name`
- `Last Name`
- `User`
#### Car
- `Brand`
- `Model`
- `Year`
- `Car image`
- `Car price`
### 2. **Structure**
#### Navigation Bar
- `CarCollection button` that leads to the home page
- `Add Car button` that leads to the pet add page
- `Login button` that leads to the login page (visible only to unauthenticated users)
- `Register button` that leads to the register page (visible only to unauthenticated users)
- `Profile button` that leads to the user profile details page (visible only to authenticated users)
#### Registration Page
- `Email`
- `Password`
#### Login Page
- `Email`
- `Password`
- When a user is logged in he/she is redirected to the Home page
#### Profile Details Page
- `Edit button`
- `Delete button`
- `Total number of cars`
#### Profile Edit Page
- `Email`
- `First Name`
- `Last Name`
#### Profile Delete Page
- `Are you sure you want to delete your profile?`
-  If the user clicks on the "Yes" button the profile is deleted, and all the user's photos, cats and likes as well, and the user is redirected to the Home page
#### Car Add Page
#### Car Details Page
#### Car Edit Page
#### Car Delete Page




