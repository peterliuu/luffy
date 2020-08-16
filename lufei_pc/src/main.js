// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import settings from "./settings";
Vue.config.productionTip = false
//Vue.prototype.$xxx 设置全局变量, 每个vue中都可以使用
Vue.prototype.$settings = settings;
// elementUI 导入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 调用插件
Vue.use(ElementUI);

//导入css初始化
import '../static/css/reset.css'
import axios from 'axios'; // 从node_modules目录中导入包
// false 阻止ajax发送请求时附带cookie
axios.defaults.withCredentials = false;

Vue.prototype.$axios = axios; // 把对象挂载vue中
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})
