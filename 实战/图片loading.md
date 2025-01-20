# Vue Logo Loading动画实现方案

## 方案一：PNG序列实现

```html
<template>
  <div class="logo-loading">
    <img :src="currentFrame" alt="loading" />
  </div>
</template>

<script>
export default {
  name: 'LogoLoading',
  data() {
    return {
      currentFrameIndex: 0,
      totalFrames: 24, // 总帧数,根据实际图片数量调整
      animationInterval: null
    }
  },
  computed: {
    currentFrame() {
      // 根据实际图片路径调整
      return `/path/to/images/logo-${this.currentFrameIndex + 1}.png`
    }
  },
  mounted() {
    this.startAnimation()
  },
  beforeDestroy() {
    this.stopAnimation()
  },
  methods: {
    startAnimation() {
      this.animationInterval = setInterval(() => {
        this.currentFrameIndex = (this.currentFrameIndex + 1) % this.totalFrames
      }, 1000 / 30) // 30fps的播放速度
    },
    stopAnimation() {
      if (this.animationInterval) {
        clearInterval(this.animationInterval)
      }
    }
  }
}
</script>

<style scoped>
.logo-loading {
  width: 100px; /* 根据实际logo尺寸调整 */
  height: 100px;
}

.logo-loading img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
</style>
```

## 优化建议

### 1. 图片预加载
```html
methods: {
  preloadImages() {
    for (let i = 1; i <= this.totalFrames; i++) {
      const img = new Image()
      img.src = `/path/to/images/logo-${i}.png`
    }
  }
}
```

### 2. Sprite Sheet方案
```html
<template>
  <div class="logo-loading sprite-animation"></div>
</template>

<style scoped>
.sprite-animation {
  width: 100px;
  height: 100px;
  background: url('/path/to/sprite-sheet.png') 0 0 no-repeat;
  animation: play 0.8s steps(24) infinite;
}

@keyframes play {
  100% { background-position: -2400px 0; } /* 总宽度 = 单帧宽度 x 帧数 */
}
</style>
```

# Vue2 + TS Loading指令实现

## 创建loading指令文件
```typescript
// src/directives/loading.ts
import Vue from 'vue'
import LogoLoading from '@/components/LogoLoading.vue'

interface LoadingElement extends HTMLElement {
  instance?: any
  loadingElement?: HTMLElement
}

const createLoading = () => {
  // 创建一个包装器元素
  const loadingWrapper = document.createElement('div')
  loadingWrapper.style.cssText = `
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.9);
  `
  
  // 创建Loading组件实例
  const LoadingConstructor = Vue.extend(LogoLoading)
  const loadingInstance = new LoadingConstructor()
  loadingInstance.$mount()
  loadingWrapper.appendChild(loadingInstance.$el)
  
  return {
    wrapper: loadingWrapper,
    instance: loadingInstance
  }
}

export const MgmtLoading = {
  bind(el: LoadingElement) {
    // 确保元素可以定位
    if (getComputedStyle(el).position === 'static') {
      el.style.position = 'relative'
    }
  },
  
  update(el: LoadingElement, binding: any) {
    if (binding.value) {
      // 显示loading
      if (!el.loadingElement) {
        const { wrapper, instance } = createLoading()
        el.loadingElement = wrapper
        el.instance = instance
        el.appendChild(wrapper)
      }
    } else {
      // 隐藏loading
      if (el.loadingElement) {
        el.removeChild(el.loadingElement)
        el.instance.$destroy()
        el.loadingElement = undefined
        el.instance = undefined
      }
    }
  },
  
  unbind(el: LoadingElement) {
    // 清理工作
    if (el.instance) {
      el.instance.$destroy()
    }
    if (el.loadingElement) {
      el.removeChild(el.loadingElement)
    }
  }
}
```

## 注册指令
```typescript:src/main.ts
import Vue from 'vue'
import { MgmtLoading } from './directives/loading'

Vue.directive('mgmt-loading', MgmtLoading)
```

## 使用示例
```html
<template>
  <div class="container" v-mgmt-loading="isLoading">
    <!-- 内容 -->
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class MyComponent extends Vue {
  private isLoading = false

  async fetchData() {
    this.isLoading = true
    try {
      // 异步操作
      await someAsyncOperation()
    } finally {
      this.isLoading = false
    }
  }
}
</script>

<style scoped>
.container {
  min-height: 100px;
}
</style>
```

主要实现说明：
    创建了一个自定义指令v-mgmt-loading
    指令会在绑定元素上创建一个带有定位的遮罩层
    当值为true时显示loading，为false时移除loading
    使用了TypeScript接口来定义扩展的HTMLElement类型
    自动处理了元素的定位问题
    在组件销毁时自动清理资源

使用注意事项：
    确保绑定指令的元素有一定的高度
    如果需要自定义loading样式，可以修改createLoading函数中的样式配置
    可以根据需要在LoadingElement接口中添加更多的类型定义
    你可以根据实际需求调整loading的样式和行为。例如：
    修改背景色透明度
    添加动画过渡效果
    自定义loading组件的大小
    添加loading文字提示等