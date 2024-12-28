# JavaScript 调用栈进阶练习题

## 题目1: V8引擎架构
请解释 V8 引擎的主要组成部分及其作用,并用 mermaid 图表示它们之间的关系。

```mermaid
graph TD
    A[V8引擎] --> B[内存堆]
    A --> C[调用栈]
    B --> D[内存分配]
    C --> E[代码执行]
    A --> F[Web APIs]
    F --> G[DOM]
    F --> H[AJAX]
    F --> I[setTimeout]
```

## 题目2: 执行环境分析
分析以下代码在浏览器环境中的执行过程,包括调用栈和Web API的交互:

```javascript
console.log('开始');

setTimeout(() => {
    console.log('定时器1');
}, 0);

Promise.resolve().then(() => {
    console.log('Promise1');
});

setTimeout(() => {
    console.log('定时器2');
}, 0);

Promise.resolve().then(() => {
    console.log('Promise2');
});

console.log('结束');
```

## 题目3: 调用栈溢出优化
以下是一个可能导致栈溢出的递归代码,请优化它:

```javascript
function calculateFactorial(n) {
    if (n === 0) return 1;
    return n * calculateFactorial(n - 1);
}

console.log(calculateFactorial(10000));
```

## 题目4: 性能分析
以下代码可能会导致浏览器卡顿,请解释原因并提供优化方案:

```javascript
function processData(items) {
    for(let i = 0; i < items.length; i++) {
        // 复杂计算
        items[i] = items[i].toString(2).split('').reverse().join('');
    }
}

const largeArray = new Array(10000000).fill(1234567);
processData(largeArray);
```

## 题目5: 异常处理追踪
编写一个函数,能够准确捕获并输出完整的调用栈信息:

```javascript
function getStackTrace() {
    // 待实现
}

function func1() {
    func2();
}

function func2() {
    func3();
}

function func3() {
    getStackTrace();
}

func1();
```

## 参考答案

<details>
<summary>点击查看答案</summary>

### 答案1
V8引擎主要组成:
- 内存堆: 负责内存分配
- 调用栈: 负责执行代码
- Web APIs: 由浏览器提供的API接口
这些组件协同工作,共同构成了JavaScript的运行时环境。

### 答案2
输出顺序将会是:
```
开始
结束
Promise1
Promise2
定时器1
定时器2
```
原因:
1. 同步代码直接执行
2. Promise属于微任务,优先于宏任务执行
3. setTimeout回调会被放入宏任务队列

### 答案3
优化后的代码:
```javascript
function calculateFactorial(n) {
    let result = 1;
    while(n > 0) {
        result *= n;
        n--;
    }
    return result;
}
// 或使用尾递归优化
function factorial(n, accumulator = 1) {
    if (n === 0) return accumulator;
    return factorial(n - 1, n * accumulator);
}
```

### 答案4
优化方案:
```javascript
function processData(items) {
    // 使用分片处理
    const chunk = 1000;
    let index = 0;
    
    function process() {
        let count = 0;
        while(index < items.length && count < chunk) {
            items[index] = items[index].toString(2).split('').reverse().join('');
            index++;
            count++;
        }
        if (index < items.length) {
            setTimeout(process, 0);
        }
    }
    process();
}
```

### 答案5
实现方案:
```javascript
function getStackTrace() {
    const stack = new Error().stack;
    console.log(stack.split('\n').slice(1).map(line => line.trim()));
    return stack;
}
```

</details>

## 注意事项
- 理解调用栈与事件循环的关系
- 注意区分同步任务、微任务和宏任务
- 大量计算时要考虑分片处理
- 递归调用要注意优化和终止条件
- 异常处理要包含完整的调用栈信息

# JavaScript调用栈详解

## 1. 递归与尾递归对比 (题目3)

### 普通递归调用过程
```mermaid
sequenceDiagram
    participant Main
    participant factorial_5
    participant factorial_4
    participant factorial_3
    participant factorial_2
    participant factorial_1
    participant factorial_0

    Main->>factorial_5: calculateFactorial(5)
    factorial_5->>factorial_4: calculateFactorial(4)
    factorial_4->>factorial_3: calculateFactorial(3)
    factorial_3->>factorial_2: calculateFactorial(2)
    factorial_2->>factorial_1: calculateFactorial(1)
    factorial_1->>factorial_0: calculateFactorial(0)
    factorial_0-->>factorial_1: return 1
    factorial_1-->>factorial_2: return 1 * 1
    factorial_2-->>factorial_3: return 2 * 1
    factorial_3-->>factorial_4: return 3 * 2
    factorial_4-->>factorial_5: return 4 * 6
    factorial_5-->>Main: return 5 * 24
```

### 尾递归调用过程
```mermaid
sequenceDiagram
    participant Main
    participant factorial_5
    participant factorial_4
    participant factorial_3
    participant factorial_2
    participant factorial_1
    participant factorial_0

    Main->>factorial_5: factorial(5, 1)
    factorial_5->>factorial_4: factorial(4, 5)
    factorial_4->>factorial_3: factorial(3, 20)
    factorial_3->>factorial_2: factorial(2, 60)
    factorial_2->>factorial_1: factorial(1, 120)
    factorial_1->>factorial_0: factorial(0, 120)
    factorial_0-->>Main: return 120
```
```mermaid
graph TD
    subgraph "普通递归的栈帧"
        A1[factorial5] --> A2[factorial4]
        A2 --> A3[factorial3]
        A3 --> A4[factorial2]
        A4 --> A5[factorial1]
        A5 --> A6[factorial0]
    end

    subgraph "尾递归的栈帧,复用栈帧"
        B1[factorial5,acc=1] 
        B2[factorial4,acc=5] 
        B3[factorial3,acc=20]
    end
```
```mermaid
sequenceDiagram
    participant 调用栈
    participant 尾递归函数
    
    Note over 调用栈: 栈帧大小保持为1
    调用栈->>尾递归函数: factorial(5,1)
    尾递归函数-->>调用栈: 替换为factorial(4,5)
    调用栈->>尾递归函数: factorial(4,5)
    尾递归函数-->>调用栈: 替换为factorial(3,20)
    调用栈->>尾递归函数: factorial(3,20)
    Note over 调用栈,尾递归函数: 持续复用同一个栈帧
```
```javascript
// 普通递归
function factorial1(n) {
    if (n === 0) return 1;
    return n * factorial1(n - 1);  // 需要等待子调用返回后再计算
}

// 尾递归
function factorial2(n, acc = 1) {
    if (n === 0) return acc;
    return factorial2(n - 1, n * acc);  // 直接返回递归调用，无需保存中间状态
}
```
## 2. 分片处理流程 (题目4)
![分片处理流程](https://static.oschina.net/uploads/space/2017/1213/104047_yNc9_2896879.png)
```mermaid
sequenceDiagram
    participant Main
    participant Process_1
    participant EventLoop
    participant Process_2
    participant Process_3

    Main->>Process_1: 处理前1000个元素
    Process_1->>EventLoop: setTimeout(process, 0)
    EventLoop->>Process_2: 处理1001-2000个元素
    Process_2->>EventLoop: setTimeout(process, 0)
    EventLoop->>Process_3: 处理2001-3000个元素
    Note over Process_3: 继续处理直到完成
```

```mermaid
graph TD
    A[主线程执行同步代码] --> B[检查微任务队列]
    B --> C[执行所有微任务]
    C --> D[检查宏任务队列]
    D --> E[执行一个宏任务]
    E --> B
```
```mermaid
sequenceDiagram
    participant 宏任务队列
    participant 微任务队列
    participant UI渲染

    宏任务队列->>宏任务队列: 执行当前宏任务
    宏任务队列->>微任务队列: 检查微任务
    loop 微任务处理
        微任务队列->>微任务队列: 执行所有微任务
    end
    微任务队列->>UI渲染: 执行UI渲染
    UI渲染->>宏任务队列: 取出下一个宏任务
```
```mermaid
sequenceDiagram
    participant 不分片
    participant 分片处理
    participant 用户交互

    Note over 不分片: 开始处理大量数据
    不分片->>不分片: 持续占用主线程
    用户交互--x不分片: ❌无法响应
    Note over 不分片: 完成所有处理

    Note over 分片处理: 处理第一块
    分片处理->>用户交互: ✅可以响应
    Note over 分片处理: 处理第二块
    分片处理->>用户交互: ✅可以响应
    Note over 分片处理: 处理第三块
```

## 3. 错误堆栈追踪 (题目5)

```mermaid
sequenceDiagram
    participant Main
    participant func1
    participant func2
    participant func3
    participant getStackTrace
    participant ErrorObject

    Main->>func1: 调用func1()
    func1->>func2: 调用func2()
    func2->>func3: 调用func3()
    func3->>getStackTrace: 调用getStackTrace()
    getStackTrace->>ErrorObject: new Error()
    ErrorObject-->>getStackTrace: 返回Error对象
    getStackTrace->>getStackTrace: 解析stack属性
    getStackTrace-->>func3: 返回堆栈信息
    func3-->>func2: 返回
    func2-->>func1: 返回
    func1-->>Main: 返回
```

## 关键点总结

1. **尾递归优化**
   - 避免保存中间计算结果
   - 减少内存使用
   - 防止栈溢出

2. **分片处理**
   - 将大任务分解为小任务
   - 通过事件循环调度执行
   - 避免阻塞主线程

3. **堆栈追踪**
   - 利用Error对象获取完整调用栈
   - 帮助调试和错误定位
   - 展示函数调用链路