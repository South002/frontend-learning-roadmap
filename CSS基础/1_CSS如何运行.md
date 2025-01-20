# CSS运行机制

## 基本概念

### 浏览器渲染流程
```mermaid
graph LR
    A[加载HTML] --> B[解析HTML]
    B --> C[创建DOM树]
    B --> D[加载CSS]
    D --> E[解析CSS]
    E --> |附加样式到DOM节点| C
    C --> F[显示]
    
    style A fill:#e4e4e4
    style B fill:#b8e6e6
    style C fill:#f8d0c3
    style D fill:#e4e4e4
    style E fill:#b8e6e6
    style F fill:#d4e6b5
```

<br>

![CSS渲染流程](https://developer.mozilla.org/zh-CN/docs/Learn_web_development/Core/Styling_basics/What_is_CSS/rendering.svg)

### DOM树结构
见习题1

### CSS解析规则
1. 浏览器遇到无法解析的CSS属性会跳过该属性
2. 遇到无法解析的选择器会跳过整个规则
3. 后面的样式会覆盖前面的样式

## 练习题

### 1. DOM结构解析
给定以下HTML代码:
```html
<div class="container">
  <h1>Title</h1>
  <p>Hello <span>World</span></p>
</div>
```
请画出其DOM树结构(用文本表示即可)

### 2. CSS解析行为预测
以下CSS代码在不同浏览器中会有什么表现?
```css
.box {
  colour: red;
  color: blue;
  width: 500px;
  width: calc(100% - 20px);
}
```

### 3. 代码补全练习
完成以下CSS代码,实现在新浏览器中宽度为90%,在旧浏览器中宽度为400px的效果:
```css
.container {
  /* 补全这里的代码 */
}
```

<details>
<summary>参考答案</summary>

1. DOM树结构:
```
DIV.container
├─ H1
|  └─ "Title"
├─ P
   ├─ "Hello"
   └─ SPAN
      └─ "World"
```

2. CSS解析行为:
- colour会被忽略(拼写错误)
- color: blue会生效
- 新浏览器会使用calc计算的宽度
- 旧浏览器会使用500px宽度

3. 代码补全:
```css
.container {
  width: 400px;
  width: calc(90%);
}
```
</details>