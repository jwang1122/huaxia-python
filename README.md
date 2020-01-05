# huaxia
## Other documents
[Vue ReadMe.md](./src/ReadMe.md)
[Python ReadMe.md](./server/ReadMe.md)

## Project setup
```bash
// if download the project from GitHug
npm install
```
create a config.js file which include stripe publishable and secret keys as following format, replace xxxxx with your own keys.
```js
const STRIPE_PUBLIC_KEY = "pk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
const STRIPE_SECRET_KEY = "sk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

export default {
    STRIPE_PUBLIC_KEY:STRIPE_PUBLIC_KEY,
    STRIPE_SECRET_KEY:STRIPE_SECRET_KEY,
}
```

## Project Creation
```
vue --version
//if not install vue
npm install @vue/cli -g

// create project from scratch
cd ~/workspace/vue
vue create huaxia
cd huaxia
npm run serve
npm install vuetify --save
npm install --save axios vue-router
```
add following line in public/index.html
```html
    <script type="text/javascript" src="https://js.stripe.com/v2/"></script>
```


### Run this application
1. Need start python stripe server before running Vue web page
open Console command window
```
cd ~/workspace/vue/huaxia/server

// if in the different virtual environment such as (base)
conda deactivate

// if not under virtual environment (evn)
source env/bin/activate

python app.py
```
2. Start MongoDB server
Open command window
```
mongod
```
3. Start web server
Open command window
```
// if not install vuex yet
npm install --save vuex
cd workspace/vue/huaxia
npm run serve
```


## Run application job in background
1. start python server (fail to do this)
```bash
cd server
source env/bin/activate
python app.py & / Enter
jobs
fg
bg
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
