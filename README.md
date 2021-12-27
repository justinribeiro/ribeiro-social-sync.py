# ribeiro-social-sync.py (v2.0.0)

Sync Mastodon to Twitter nicely one-way. A very specific fork from [twoot.py](https://github.com/wtsnjp/twoot.py) (you should probably just use that!)

![example](https://user-images.githubusercontent.com/643503/147498591-a45ba050-e8b5-43d1-b664-060d087fcee3.png)

## What's the difference from Twoot.py?

I forked it because:

1. I wanted to use an access_token from my Mastodon instance instead of user/pass because 2FA
2. I only want Mastodon > Twitter
3. I wanted a link back to Mastodon (so people understand, that's where I am)

I have stripped this thing down; it does not have the nice setup that [twoot.py](https://github.com/wtsnjp/twoot.py) has, it is very specific to my setup, it is here so I both don't lose it and in case anyone else wants a more limited version.

## The config file
The twoot.py setup usually creates this file in the program name folder at your home directory (e.g., ~/.ribeiro-social-sync.py/default.config), so you'll have to create this yourself should you dare.

```
{
    "mastodon": {
      "client_id": "",
      "client_secret":"",
      "access_token": "",
      "api_base_url": ""
    },
    "twitter": {
      "consumer_key": "",
      "consumer_secret": "",
      "access_token": "",
      "access_token_secret": ""
    }
}
```

Other things you'll need:

1. Setup in your mastodon instance the require app (e.g., https://[YOUR-INSTANCE]/settings/applications/)
2. Setup an elevated app on Twitter (https://developer.twitter.com/en/portal/dashboard)

## The crontab
Every 15 minutes, check and sync as needed.

```
*/15 * * * * python3 /work/src/ribeiro-social-sync/ribeiro-social-sync.py --log=/home/justin/.ribeiro-social-sync.py/cron.log >> /home/justin/.ribeiro-social-sync.py/cron.log 2>&1
```

## License

This software is distributed under [the MIT license](./LICENSE) and was forked from Takuto ASAKURA ([wtsnjp](https://github.com/wtsnjp)) [twoot.py](https://github.com/wtsnjp/twoot.py) project.
