# Convert Google Forms into API.
#### Google Forms are awesome - so functional and flexible!

This service is advance version of the artile [How to style Google Forms][1]. We have been using this trick to style our google forms to fit into our site's look and feel. And now the time is to think beyond just styling your google forms.

What if we can convert our google form into API so that we can easlily grab valiation errors given by form into a json format.

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

Here we can see example of how it works. We need to hit a POST request to our API Gateway `https://xgb5naiofi.execute-api.ap-south-1.amazonaws.com/api/google-forms` along with the payload.

### Payload
`url` - The URL of our google form

`inputs` - contains the list of form fields as `name: value`


## Security

If you discover any security related issues, please email akaamitgupta@gmail.com instead of using the issue tracker.


[1]:https://morningstudio.com.au/blog/2013/06/how-to-style-google-forms/
