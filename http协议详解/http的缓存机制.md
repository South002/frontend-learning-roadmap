# 浏览器缓存机制详解

## 目录
- [浏览器缓存机制详解](#浏览器缓存机制详解)
  - [目录](#目录)
  - [概述](#概述)
  - [缓存过程分析](#缓存过程分析)
  - [强制缓存](#强制缓存)
  - [协商缓存](#协商缓存)
  - [总结](#总结)

## 概述

浏览器缓存机制是基于HTTP缓存机制实现的。在分析之前,我们需要了解HTTP报文的基本结构:

1. HTTP请求(Request)报文结构:
```mermaid
graph LR
A[请求行] --> B[HTTP头]
B --> C[请求报文主体]
```

2. HTTP响应(Response)报文结构:
```mermaid
graph LR
A[状态行] --> B[HTTP头]
B --> C[响应报文主体] 
```

## 缓存过程分析

浏览器缓存的基本流程如下:

```mermaid
flowchart TD
    A[浏览器发起HTTP请求] --> B{是否有缓存?}
    B -->|是| C{缓存是否过期?}
    B -->|否| D[向服务器请求]
    C -->|是| D
    C -->|否| E[使用缓存]
    D --> F[存入缓存]
```

## 强制缓存

强制缓存主要通过以下两个HTTP头部字段控制:

1. Expires(HTTP 1.0)
2. Cache-Control(HTTP 1.1)

其中Cache-Control的优先级更高,主要取值包括:

- public: 所有内容都将被缓存
- private: 只有客户端可以缓存
- no-cache: 需要经过协商缓存验证
- no-store: 不使用任何缓存
- max-age=xxx: xxx秒后失效

```mermaid
flowchart TD
    A[请求] --> B{是否有Cache-Control?}
    B -->|是| C{检查max-age是否过期}
    B -->|否| D{检查Expires}
    C -->|未过期| E[使用缓存]
    C -->|已过期| F[协商缓存]
    D -->|未过期| E
    D -->|已过期| F
```

## 协商缓存

协商缓存主要通过以下两对HTTP头部字段控制:

1. Last-Modified/If-Modified-Since
2. ETag/If-None-Match(优先级更高)

```mermaid
flowchart TD
    A[协商缓存] --> B{是否有ETag?}
    B -->|是| C{ETag是否匹配?}
    B -->|否| D{检查Last-Modified}
    C -->|匹配| E[返回304]
    C -->|不匹配| F[返回200]
    D -->|文件未修改| E
    D -->|文件已修改| F
```

## 总结

浏览器缓存完整流程:

```mermaid
flowchart TD
    A[浏览器请求] --> B{强制缓存是否生效?}
    B -->|是| C[使用缓存]
    B -->|否| D{协商缓存是否生效?}
    D -->|是| E[返回304]
    D -->|否| F[返回200]
    E --> C
    F --> G[更新缓存]
```

<br>

![原文图片](https://github.com/shfshanyue/Daily-Question/assets/53259809/18f43f9c-e85a-44ae-bf38-5382c66bbdf8)

<br>

缓存位置:
- from memory cache: 内存缓存,读取快但进程关闭后失效
- from disk cache: 硬盘缓存,读取较慢但可持久保存

[原文链接](https://mp.weixin.qq.com/s/d2zeGhUptGUGJpB5xHQbOA)