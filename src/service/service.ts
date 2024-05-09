
import axios from 'axios';
import { ElMessage } from 'element-plus';
// 创建axios实例
const service = axios.create({
  // baseURL: process.env.VUE_APP_BASE_API, 
  baseURL: '/',
  timeout: 5000000
});

// 请求拦截器
service.interceptors.request.use(
  config => {
    console.log(config, '请求拦截------');
    return config;
  },
  error => {
    // 请求错误处理
    console.log(error); // for debug
    Promise.reject(error);
  }
);

// 响应拦截器
service.interceptors.response.use((res) => {
  console.log(res, '---------');
  let resJson = res.data
  if (resJson !== 200) {
    let code = resJson.code
    switch (code) {
      case 1:
        ElMessage({
          message: resJson.errmsg,
          type: 'error'
        });
        break;
      default:
        break;
    }
  } else {
    return res.data;
  }
  // ElMessage({
  //   message: resJson.msg,
  //   type: 'success'
  // });
  return res.data
},
  error => {
    console.log('err' + error);
    ElMessage({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    });
    return Promise.reject(error);
  }
);

export default service;
