为了使团队介绍在不同屏幕尺寸下都能良好显示，我们需要对CSS进行优化，实现图片和文字的自适应布局。以下是修改后的代码：
主要改进点：

1. 添加了标题和职业信息的结构化标签，便于SEO和语义化
2. 使用flex布局的自适应特性：
flex: 1; min-width: 0; 让文字区域能够自适应剩余空间
flex-shrink: 0; 防止图片在空间不足时被压缩
3. 媒体查询适配：
在768px以下屏幕，布局变为垂直排列
文字居中对齐，图片下方显示
在480px以下屏幕，进一步优化字体大小和图片尺寸
4. 响应式图片：在小屏幕上图片会自适应宽度并保持比例

这样修改后，在手机竖屏查看时，图片会在上方，文字内容会完整显示在下方，避免了文字被挤压或超出屏幕的问题。

```html
<div style="display: flex; align-items: flex-start; gap: 1.5rem; margin: 1.2em 0;">
  <img src="/images/zhanglaijun.png" width="170" height="227" style="border-radius:6px; box-shadow:0 3px 8px rgba(0,0,0,0.1); flex-shrink: 0;">
  <div style="flex: 1; min-width: 0;">
    <h3 style="margin: 0 0 0.5rem 0; font-size: 1.1em;">张来军</h3>
    <p style="margin: 0 0 0.5rem 0; color: #666; font-weight: 500;">商务运营专家</p>
    <p style="margin: 0; line-height: 1.6; font-size: 0.95em;">
      曾任职百度等数家头部互联网公司，参与团购行业的"百团大战"，熟悉互联网平台的市场营销、商务管理、地面推广、活动运营、客户服务；有AI、云计算等数字产品，以及传统行业、实体产品和农村市场的推广经验，多次从0到1创业的丰富经历。
    </p>
  </div>
</div>

<style>
  @media (max-width: 768px) {
    div[style*="display: flex"] {
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
    
    div[style*="display: flex"] img {
      width: 150px !important;
      height: auto !important;
      max-width: 100%;
      margin-bottom: 1rem;
    }
    
    div[style*="display: flex"] div {
      flex: none;
      width: 100%;
    }
    
    div[style*="display: flex"] h3 {
      text-align: center;
    }
    
    div[style*="display: flex"] p {
      text-align: center;
    }
  }
  
  @media (max-width: 480px) {
    div[style*="display: flex"] img {
      width: 130px !important;
    }
    
    div[style*="display: flex"] h3 {
      font-size: 1em;
    }
    
    div[style*="display: flex"] p {
      font-size: 0.9em;
      line-height: 1.5;
    }
  }
</style>
```

请求将他们放入主题模板中，共享给有需要的页面。

