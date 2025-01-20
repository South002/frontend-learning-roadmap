# HTML中的图片

## 基本概念

### img标签
`<img>` 是一个空元素,用于在网页中嵌入图片,需要两个基本属性:
- src: 指定图片的URL路径
- alt: 图片的替代文本描述

```mermaid
graph LR
    A[img标签] --> B[src属性]
    A --> C[alt属性]
    B --> D[相对路径]
    B --> E[绝对路径]
    C --> F[图片无法显示时的替代文本]
    C --> G[屏幕阅读器使用]
```

### 图片尺寸属性
- width: 图片宽度(像素)
- height: 图片高度(像素)

### figure和figcaption
用于为图片添加语义化的说明文字:
```mermaid
graph TD
    A[figure] --> B[img]
    A --> C[figcaption]
    B --> D[图片内容]
    C --> E[说明文字]
```

## 实践练习

### 练习1: 基础图片插入
补全下面的代码,插入一张图片并添加合适的alt文本:
```html
<___ src="images/cat.jpg" ___="一只正在睡觉的橘猫">
```

### 练习2: 添加图片说明
将下面的图片和说明文字改写为语义化的形式:
```html
<!-- 原代码 -->
<div>
  <img src="flower.jpg" alt="一朵红玫瑰">
  <p>春天盛开的玫瑰</p>
</div>

<!-- 请改写为使用figure和figcaption的形式 -->
```

### 练习3: 响应式图片尺寸
补全下面的代码,使图片在保持原始比例的情况下最大宽度为500px:
```css
img {
  max-___: 500px;
  ___: auto;
}
```

<details>
<summary>参考答案</summary>

练习1:
```html
<img src="images/cat.jpg" alt="一只正在睡觉的橘猫">
```

练习2:
```html
<figure>
  <img src="flower.jpg" alt="一朵红玫瑰">
  <figcaption>春天盛开的玫瑰</figcaption>
</figure>
```

练习3:
```css
img {
  max-width: 500px;
  height: auto;
}
```

</details>


# HTML中的图形和多媒体

## 基本概念

### CSS背景图片
使用 `background-image` 属性设置背景图片,主要用于装饰性图片。

```mermaid
graph LR
    A[背景图片] --> B[装饰性]
    A --> C[无语义]
    B --> D[CSS控制]
    C --> E[无alt文本]
    C --> F[屏幕阅读器无法识别]
```

### Canvas
提供2D图形绘制API,使用JavaScript控制。

### SVG
矢量图形格式,可无损缩放。

```mermaid
graph TD
    A[SVG优势] --> B[矢量图形]
    A --> C[可缩放]
    B --> D[线条]
    B --> E[曲线]
    B --> F[几何图形]
    C --> G[清晰度不损失]
```

### 音视频元素
- video: 视频播放
- audio: 音频播放

### WebRTC
实时通信技术,支持:
```mermaid
graph LR
    A[WebRTC] --> B[音频流]
    A --> C[视频流]
    A --> D[数据共享]
```

## 实践练习

### 练习1: CSS背景图片
补全CSS代码,为div设置背景图片并使其居中显示:
```css
div {
  ___-image: url("bg.jpg");
  ___-position: center;
  ___-repeat: no-repeat;
}
```

### 练习2: Canvas绘制
补全JavaScript代码,在canvas上绘制一个红色矩形:
```javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.___('2d');
ctx.___Style = 'red';
ctx.___Rect(10, 10, 100, 50);
```

### 练习3: 视频播放器
补全HTML代码,创建一个带控制条的视频播放器:
```html
<_____ controls>
  <source src="video.mp4" type="video/mp4">
  您的浏览器不支持视频播放
</___>
```

<details>
<summary>参考答案</summary>

练习1:
```css
div {
  background-image: url("bg.jpg");
  background-position: center;
  background-repeat: no-repeat;
}
```

练习2:
```javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
ctx.fillStyle = 'red';
ctx.fillRect(10, 10, 100, 50);
```

练习3:
```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  您的浏览器不支持视频播放
</video>
```

</details>