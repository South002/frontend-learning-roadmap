# HTML5 表单验证基础

## 表单验证的两种方式

```mermaid
graph LR
    A[表单验证] --> B[Form表单提交]
    A --> C[Ajax无刷新提交]
```


## HTML5 原生表单验证特性

### 验证效果类型
1. 气泡提示
2. 边框变色
3. 自定义提示文本

### 基本案例展示

```mermaid
graph TD
    A[HTML5表单验证案例] --> B[Phone表单美化]
    A --> C[邮箱验证]
    A --> D[登录表单]
    A --> E[自定义提示气泡]
    
    B --> B1[必填红框]
    B --> B2[选填灰框]
    B --> B3[Focus蓝框]
    
    C --> C1[正确格式提示]
    C --> C2[错误格式提示]
    
    D --> D1[必填项标记]
    D --> D2[正确性验证]
    D --> D3[密码匹配验证]
```


## 练习题

### 题目1: 实现必填输入框的样式
补全以下CSS代码，实现必填输入框的红色边框效果：

```css
input {
    /* 补全代码：添加2px宽度的实线边框，颜色为#ff0000 */
}
```


### 题目2: 邮箱验证
补全以下HTML代码，为input添加邮箱验证：

```html
<input type="___" name="email" ___="请输入有效的邮箱地址">
```


### 题目3: JS表单验证
补全以下JavaScript代码，实现密码匹配验证：

```javascript
function validatePassword() {
    const password1 = document.getElementById('password1').value;
    const password2 = document.getElementById('password2').value;
    
    // 补全代码：判断两个密码是否相同，如果不同则返回false
    
}
```


<details>
<summary>参考答案</summary>

题目1:
```css
input {
    border: 2px solid #ff0000;
}
```


题目2:
```html
<input type="email" name="email" required="required">
```


题目3:
```javascript
function validatePassword() {
    const password1 = document.getElementById('password1').value;
    const password2 = document.getElementById('password2').value;
    
    return password1 === password2;
}
```

</details>