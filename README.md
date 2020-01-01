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

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
1. Need start python stripe server before running Vue web page
open Console command window
```
cd ~/workspace/vue/huaxia/server
source env/bin/activate
python app.py
```
2. Start web server
```
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
