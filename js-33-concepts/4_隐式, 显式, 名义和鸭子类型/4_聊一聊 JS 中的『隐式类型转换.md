
# JavaScript 隐式类型转换详解

## 什么是隐式类型转换?

隐式类型转换是JavaScript在运算时,自动将操作数转换为期望的数据类型的过程。

## 主要转换规则

```mermaid
graph TD
    A[隐式类型转换规则] --> B[算术运算转换]
    A --> C[条件判断转换]
    A --> D[对象转换]
    
    B --> B1[数字运算: - * / %]
    B --> B2[加法运算: +]
    
    C --> C1[Boolean转Number]
    C --> C2[String转Number]
    
    D --> D1[valueOf]
    D --> D2[toString]
```

### 1. 算术运算符转换
- `-`, `*`, `/`, `%`: 操作数转为数字
  - `undefined` -> `NaN`
  - `null` -> `0`
  - `true` -> `1`
  - `false` -> `0`
  - `string` -> 按数字语法解析,失败则`NaN`
- `+`: 
  - 有字符串则进行字符串连接
  - 无字符串时:
    - `undefined` + `undefined` = `NaN`
    - `null` + `null` = `0`
    - `true` + `true` = `2`
    - `false` + `false` = `0`

### 2. 条件判断转换(==)
```mermaid
graph LR
    A[条件判断] --> B[Boolean vs Any]
    B --> B1[Boolean先转Number]
    A --> C[Number vs String]
    C --> C1[String转Number]
    A --> D[Object vs Any]
    D --> D1[调用valueOf]
    D1 --> D2[如果还是对象则调用toString]
```
```mermaid
graph TD
    A[条件判断==] --> B[Boolean vs 任意值]
    B --> B1[Boolean先转Number]
    B1 --> B2[继续按其他规则比较]
    
    A --> C[Number vs String]
    C --> C1[String转Number后比较]
    
    A --> D[String vs Boolean]
    D --> D1[都转为Number后比较]
    
    A --> E[Object vs 任意值]
    E --> E1[调用valueOf]
    E1 --> E2{是原始值?}
    E2 -->|是| E3[按原始值规则比较]
    E2 -->|否| E4[调用toString]
    E4 --> E5[按String规则比较]
    
    A --> F[null vs undefined]
    F --> F1[直接返回true]
    
    style B1 fill:#f9f,stroke:#333
    style C1 fill:#f9f,stroke:#333
    style D1 fill:#f9f,stroke:#333
    style E1 fill:#f9f,stroke:#333
```
具体规则:
1. `null == undefined` 结果为 `true`
2. 如果一个是 Boolean,先转 Number
3. 如果一个是 String,一个是 Number,String 转 Number
4. 如果一个是 Object,先调用 valueOf(),如果结果还是对象则调用 toString()

例子:
```js
[] == false   // true, 过程: [] -> "" -> 0 == 0
[1] == true   // true, 过程: [1] -> "1" -> 1 == 1
["0"] == false // true, 过程: ["0"] -> "0" -> 0 == 0
```

### 3. 对象转换规则
当对象需要转换为原始值时,会按以下顺序调用:

```mermaid
graph TD
    A[对象转换] --> B[valueOf]
    B --> C{是否为原始值?}
    C -->|是| D[返回结果]
    C -->|否| E[toString]
    E --> F{是否为原始值?}
    F -->|是| D
    F -->|否| G[TypeError]
```

例子:
```js
let obj = {
  valueOf() { return 100 },
  toString() { return '200' }
}
console.log(obj + 1)    // 101 (使用valueOf)
console.log(`${obj}`)   // "200" (显式调用toString)
```

## 练习题

### 1. 补全代码
```js
// 实现一个函数,判断输入值是否为假值
function isFalsy(val) {
  // 补全代码
}

console.log(isFalsy(""))  // true
console.log(isFalsy(1))   // false
console.log(isFalsy({}))  // false
```

### 2. 判断输出
```js
let result = 1 + "2" + 3;
// result的值是什么?
```

### 3. 补全代码
```js
// 实现一个函数,将任意值转换为数字
function toNumber(val) {
  // 补全代码,不能直接使用Number()函数
}

console.log(toNumber("123")) // 123
console.log(toNumber(true)) // 1
console.log(toNumber({})) // NaN
```

<details>
<summary>参考答案</summary>

1. isFalsy实现:
```js
function isFalsy(val) {
  return !val;
}
```

2. result的值是"123"
因为从左到右运算:
- 1 + "2" = "12"
- "12" + 3 = "123"

3. toNumber实现:
```js
function toNumber(val) {
  return val - 0;
}
```

</details>