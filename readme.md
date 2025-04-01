# URL Shortener Application

This is a simple URL shortener application built using **Flask** , **MySQL** , and **hashing techniques** . The application allows users to shorten long URLs and redirect to the original URL via the short URL. It also tracks the number of clicks for each short URL.

## Features

- **Shorten URLs** : Submit long URLs to generate short URLs.
- **Redirect to Original URL** : Access the original long URL by visiting the shortened URL.
- **Click Tracking** : Tracks how many times a shortened URL is clicked.

## Technologies Used

- **Flask** : A lightweight Python web framework for building web applications.
- **MySQL** : A relational database used to store mappings between long URLs and short URLs.
- **Python** : The primary programming language used for the backend.
- **HTML** : For frontend design (though not heavily styled).

## Requirements

The requirements for this project is listed in A file named as requirement.txt

to install it:

```
pip install -r requirements.txt

```

## Example

### Homepage:

- Enter a long URL in the form (e.g., `https://www.example.com`) and click the "Shorten" button.
- The response will be a shortened URL, e.g., `https://de/abc123`.

### Visiting Short URL:

- If you visit `http://localhost:5000/abc123`, it will redirect you to `https://www.example.com` and increase the "clicks" count in the database.
