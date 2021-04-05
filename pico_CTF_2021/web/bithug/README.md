# Bithug

1. You probably noticed that code treats you as admin if you access it internally (127.0.0.1) which means `SSRF`
2. There is a feature for WebHooks which can help you with that.
3. You need to send a request internally to _/<user>.git to make you a collaborator
4. Figure out what is the payload that makes a user collaborator of a repository (use wire shark to capture git push)
5. Make sure you follow all instructions on "user" tab of repository on how to add collaborator
6. Get the payload in binary and get the content type needed
7. The payload must be base64 of binary stream
8. use curl to create a webhook with custom payload and contentType
9. The url for the webhook is annoying as it filters out ports and localhost. Create a custom web server that does 307 redirect to 127.0.0.1/_/user.git/x-git...
10. Add the webhook using curl
11. Do a random push request to trigger webhook
12. magicccc

## Step1: Intuition

- Request from 127.0.0.1 are treated as admin and hence have access to all apis
- That means if we can make the server send a request to itself (SSRF) we can get it do whatever we want
- There is a features called webhooks, which makes a post request to said url with said body when you trigger it by doing git push
- The webhook is created using api, it needs to values: body and contentType
- The url for webhook is filtered, you cannot enter localhost ip or ports.
- But you need to send request to 127.0.0.1:1823/<api url> to make it work
- Anyhow, there is an intended way to add collaborator, create a repo go to "users" you'll see instructions to add user as collaborator (need to follow exact instructions)

## Step2: Plan

- The flag is hidden in a secret repo at `_/username.git`
- The plan is to add yourself as contributor to that repo so you can access it
- See how collaborator is added to a sample repo and mimic the request using webhook
- You will need exact payload that's sent to the server when you push the collaborator addition commit

## Step3: Getting the Payload

- You'll need Wireshark
- create a repo randomly on instance
- git clone that repo locally
- follow instructions to add collaborator but don't push it yet
- Turn on capture for wireshark
- git push
- You'll notice a post request to instance with content-type: x-git......
- Also remember path to which it pushes
- Copy the contentType to a file (to remember)
- Copy the payload as escaped string, Wireshark will give you copy of all request so you'll need to do some cleaning here. Once copied look for a patter "\x30\x30" from which the real payload starts, also check wireshark `data` tab
- Clean the payload format it'll have line break, create a single string thats like "\x30\x30...................."
- convert the byte stream payload from above to base64
- That will be your payload

## Step4: Figuring out URL

- As mentioned you cannot have 127.0.0.1:1823 as URL for webhook due to filters
- Create a webserver using flask or php and host it online
- the server should do a 307 redirect to http://127.0.0.1:1823/_/username.got/git-packet..... (you saw this path in wireshark)
- Use the url of your webserver for webhook

## Step5: Adding webhook

- You can't directly add it because we need a special contentType that is like /x-git......
- copy user-token cookie for we will send cURL request with it
- find the url of webhooks api (user chrome devtools to see the request when you create a dummy webhook)
- create a curl request with user-token cookie so your authorized and your payload should be in same structure as you noticed with dummy i. e {url: , body: , contentType}
- For url use your URL that you have created, body is your base64 string you created and contentType is what you copied from wireshark that looks like /git-packet something

## Step6: Magicccccc

- Now you have set the trap, Time to trigger it
- clone the repo for which you have added the webhook
- create a random commit like adding "# 69" to readme
- git push

## Step7: THE FLAG

- Go to instanceURL/\_/username.git
  Note: When I means <user>.git i mean your username like admin.git, applies to all places I mentioned it.
