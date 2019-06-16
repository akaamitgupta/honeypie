# Convert Google Forms into API.

[![Build Status](https://travis-ci.org/akaamitgupta/honeypie.svg?branch=master)](https://travis-ci.org/akaamitgupta/honeypie)

#### Google Forms are awesome - so functional and flexible!

This service is an advanced version of the article [How to style Google Forms][1]. We have been using this trick to style our google forms to fit into our site's look and feel. And now the time is to think beyond just styling your google forms.

What if we can convert our Google Form into API so that we can easily grab validation errors given by form into a JSON format.

##### Enough talking lets code
```
curl -X POST \
    https://xgb5naiofi.execute-api.ap-south-1.amazonaws.com/api/google-forms \
    -H 'Content-Type: application/json' \
    -d '{
        "url": "https://docs.google.com/forms/u/1/d/e/1FAIpQLSfM54cLPNZk4mvMWTtiRWDUi2divL2cCtGG-byj05ttig1iVQ/formResponse",
        "inputs": {
                "entry.505110784": "some text",
                "entry.1915963433": "",
                "entry.948181294": "",
                "entry.700448681": "C"
        }
}
'

{
    "errors": "The given data was invalid.",
    "validations": {
        "entry.505110784": "Must be a number",
        "entry.1915963433": "This is a required question",
        "entry.948181294": "This is a required question"
    }
}
```

Here we can see an example of how it works. We need to hit a POST request to our API Gateway `https://xgb5naiofi.execute-api.ap-south-1.amazonaws.com/api/google-forms` along with the payload.

### Payload
`url` - The URL of our google form

`inputs` - contains the list of form fields as `name: value`

## How it works?
"Web Scraping!" Yeah, you heard it right. It just an old school web scraping.

We hit a `POST` request to the URL given by you of google forms and it returns the HTML in response then we parse it using very popular [BeautifulSoup][2] to fetch all the validation errors from the page. Click [here](app.py) to check the source code.


## Security

If you discover any security related issues, please email akaamitgupta@gmail.com instead of using the issue tracker.


[1]:https://morningstudio.com.au/blog/2013/06/how-to-style-google-forms
[2]:https://www.crummy.com/software/BeautifulSoup
