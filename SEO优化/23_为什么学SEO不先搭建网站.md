# SEO第一印象规则

## 基本概念

第一印象规则是百度蜘蛛首次爬取网站时的评估机制。这个规则会影响网站后续的排名表现。

```mermaid
graph TD
A[百度蜘蛛首次爬取] --> B{评估网站质量}
B -->|优质| C[正面评估]
B -->|劣质| D[负面评估]
C --> E[提高后续排名权重]
D --> F[降低后续排名权重]
style A fill:#f9f,stroke:#333
style B fill:#bbf,stroke:#333
style C fill:#bfb,stroke:#333
style D fill:#fbb,stroke:#333
```


## 重要性

1. 决定网站未来排名走向
2. 影响百度对网站的信任度
3. 影响后续内容的评估标准

## 优化建议
```mermaid
flowchart LR
A[前期准备] --> B[域名选择]
B --> C[服务器选择]
C --> D[TDK优化]
D --> E[整体优化]
E --> F[网站上线]
```


## 常见错误

1. 未经优化就上线网站
2. 频繁修改核心要素(如TDK)
3. 分散式优化而非一次性优化

## 练习题

### 1. 网站优化顺序题
请将以下优化步骤按正确顺序排列:
A. 网站上线
B. SEO规则学习
C. 域名购买
D. 整体优化
E. 服务器选择

### 2. JavaScript实现SEO检测工具
完成以下代码,实现一个简单的TDK检测函数:

```javascript
function checkTDK(title, description, keywords) {
    const result = {
        titleValid: false,
        descriptionValid: false,
        keywordsValid: false
    };
    
    // 补充代码：检查title长度是否在10-60个字符之间
    
    // 补充代码：检查description长度是否在50-160个字符之间
    
    // 补充代码：检查keywords是否包含3-5个关键词
    
    return result;
}
```

### 3. 实现域名评估函数
完成以下代码,实现一个简单的域名评估函数:

```javascript
function evaluateDomain(domainName) {
    // 补充代码：检查域名长度是否合适(建议5-15个字符)
    
    // 补充代码：检查是否包含连字符(不建议)
    
    // 补充代码：检查是否全为字母或数字
}
```

<details>
<summary>参考答案</summary>

### 题目1答案:
正确顺序: B -> C -> E -> D -> A

### 题目2答案:
```javascript
function checkTDK(title, description, keywords) {
    const result = {
        titleValid: false,
        descriptionValid: false,
        keywordsValid: false
    };
    
    result.titleValid = title.length >= 10 && title.length <= 60;
    
    result.descriptionValid = description.length >= 50 && description.length <= 160;
    
    result.keywordsValid = keywords.split(',').length >= 3 && keywords.split(',').length <= 5;
    
    return result;
}
```

### 题目3答案:
```javascript
function evaluateDomain(domainName) {
    const length = domainName.length >= 5 && domainName.length <= 15;
    
    const hasHyphen = domainName.includes('-');
    
    const isAlphaNumeric = /^[a-zA-Z0-9]+$/.test(domainName);
    
    return {
        isValid: length && !hasHyphen && isAlphaNumeric,
        issues: {
            length,
            hasHyphen,
            isAlphaNumeric
        }
    };
}
```
</details>