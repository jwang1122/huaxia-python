# huaxia

## Project Creation
```
vue --version
npm install @vue/cli -g
cd ~/workspace/vue
vue create huaxia
cd huaxia
npm run serve
npm install vuetify --save
npm install --save axios vue-router
```
add following line in public/index.html
    <script type="text/javascript" src="https://js.stripe.com/v2/"></script>


## Project setup
```
npm install
```

### Run this application
1. Need start python stripe server before running Vue web page
open Console command window
```
cd ~/workspace/vue/huaxia/server
conda deactivate
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
npm install --save vuex
cd workspace/vue/huaxia
npm run serve
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
