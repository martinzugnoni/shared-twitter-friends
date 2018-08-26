# Shared Twitter friends

Have you ever asked yourself "how many followers I share with my friends?". Quick and simple Python & Flask recipe to figure that out! 👏

## Preview

![image](https://user-images.githubusercontent.com/1155573/44632299-804eef00-a94e-11e8-9724-21e8627f779a.png)

## Want to try it youself?

The app runs on top of Python + Flask. To run it locally with your own account, follow the next few steps:

### 1) Fork the repo 👆

You will need to set up your own Twitter API keys and accounts name. As you don't have write permissions on this repo, you will need to fork it into your own account.

![image](https://user-images.githubusercontent.com/1155573/44632322-db80e180-a94e-11e8-93db-2e23f872b067.png)

### 2) Configure your Twitter API keys

In order to use the Twitter API to fetch account followers, you will need to authenticate yourself using your app's access key and token.

You don't have a Twitter API key yet? Start by checking https://apps.twitter.com/.

Once you have it, go to `app.py` file and change them accordingly: https://github.com/martinzugnoni/shared-twitter-friends/blob/master/app.py#L13-L16

![image](https://user-images.githubusercontent.com/1155573/44632331-2a2e7b80-a94f-11e8-9c36-70281961de8a.png)


### 3) List your friends' accounts

By default, the app is configured to use my personal friends' account. You will probably want to use yours.

You just need to replace these lines with your friends' Twitter usernames.
https://github.com/martinzugnoni/shared-twitter-friends/blob/master/app.py#L20-L29

### 4) Run the app

One of the best things about Flask, is its simplicity for writing and running a web app.

All you need to do is running `python app.py` in your preferred terminal, and visit `http://localhost:8080/` in your browser.

Make sure to have the libraries listed in `requirements.txt` installed in your local environment. If you don't, run `pip install -r requirements.txt`.

## Twitter API rate limits note

It's important to mention that, if you use accounts with a big amount of followers (>75.000), the app might take a long time to load.

The reason is Twitter API's rate limits. I'm using the `GetFollowerIDs` API method, which returns pages of 5000 account ids at max. As [explained here](https://python-twitter.readthedocs.io/en/latest/rate_limits.html), Twitter allows 15 API requests per 15 minutes. Meaning that, if all your listed accounts sum up to 75000 followers (15 requests, 5000 each), you will hit the API rate limit and the app will sleep for 15 minutes until the next request.

In most of the cases this wont't happen. But, if you use big influencers account you can easily reach >75000 followers.

That's all! 🙌
