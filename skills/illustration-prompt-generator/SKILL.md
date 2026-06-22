---
name: illustration-prompt-generator
description: 从字幕或文本中提取核心视觉元素，生成 5 条以上高质量文生图提示词。当用户说"生成配图提示词"、"配图建议"、"为文章配图"、"文生图提示词"或类似请求时触发。
---

# AI 图像提示词设计技能

## 触发条件
当用户要求从字幕/文本生成文生图提示词、为视频/文章配图、生成图像生成提示时使用此技能。

## 输入格式

用户输入为字幕（SRT）或文本内容
可能为：
- 演讲字幕
- 视频脚本
- 博客文章
- 深度分析
- 新闻报道

## 理解任务

生成提示词前，需从内容中提取：
- **核心主体**（人物/物体/场景）
- **动作或状态**（静态/动态瞬间）
- **环境信息**（地点、时代、空间）
- **情绪氛围**（压抑/温暖/科幻/神秘等）
- **视觉重点**（光影、构图、材质）

## 核心原则

### 1. 强画面化（必须可"看见"）

所有提示词必须是视觉可生成内容：

**禁止抽象词：**
- ❌ success / hope / intelligence / thinking
- ❌ emotion / meaning / knowledge / abstract concept

**正确具体画面：**
- ✅ a man standing alone in neon-lit street at night
- ✅ a woman in her 30s wearing a red coat, turning her head slowly
- ✅ golden sunlight filtering through dense forest leaves

### 2. 每条必须是完整图像提示词结构

每条提示词必须包含以下 6 要素：

```
[主体] + [动作/状态] + [场景环境] + [构图] + [光影] + [风格]
```

**示例完整结构：**
> A middle-aged woman with short gray hair (主体), sits alone at a wooden desk, writing notes (动作/状态), in a dimly lit study with bookshelves in background (场景环境), close-up shot from slightly above (构图), warm lamplight illuminating her face with soft shadows (光影), cinematic photorealistic style, shallow depth of field (风格)

### 3. 风格适配要求（兼容多模型）

必须支持多种风格混合：

| 风格类型 | 关键词 |
|---------|--------|
| 写实摄影风 | photorealistic, ultra-detailed, 8k, DSLR, natural lighting |
| 电影感 | cinematic, depth of field, film grain, color grading, anamorphic lens |
| 科幻风 | cyberpunk, futuristic, holographic, neon glow, metallic |
| 动画风 | anime style, studio quality, vibrant colors, clean lines |
| 插画风 | digital painting, concept art, illustration, artistic |

### 4. 多样性要求（至少 5 条）

必须覆盖不同的视觉角度：

| 维度 | 要求 |
|------|------|
| 构图 | 特写/中景/远景/广角 至少覆盖 3 种 |
| 视角 | 俯视/仰视/平视/第一视角 至少覆盖 2 种 |
| 时间 | 白天/夜晚/黄昏/黎明 至少覆盖 2 种 |
| 镜头感 | 静态/动态/运镜感 至少覆盖 2 种 |

### 5. 适配商业模型优化

针对 Kling、即梦、通义万象等商业模型：

- ✅ 画面要"干净明确"，避免复杂语义堆叠
- ✅ 一条提示词尽量控制在 **1-2 句**
- ✅ 避免过度抽象修辞
- ✅ 强调视觉细节（材质、光影、环境）
- ✅ 人物要具体（年龄、服装、动作）

## 高级生成目标

优先生成：
- **电影级构图**（cinematic framing）
- **有故事感但不叙事化**
- **可用于短视频分镜的画面序列**
- **主体一致性强**（避免频繁换人设）
- **视觉冲击力强的关键帧画面**

## 输出格式（严格）

**只输出编号列表，不要任何额外文字：**

```
1. [完整提示词 1]

2. [完整提示词 2]

3. [完整提示词 3]

4. [完整提示词 4]

5. [完整提示词 5]
```

**要求：**
- 至少 5 条，最多 8 条
- 每条之间空一行
- 不要标题、不要说明、不要分析
- 不要输出中文提示词

## 质量要求

- 每条提示词都是**完整可执行**的图像描述
- 覆盖不同构图、视角、时间、镜头感
- 风格与内容高度匹配
- 避免相似构图或重复描述
- 人物描述要具体（年龄、服装、特征）

## 禁止行为

- ❌ 不要解释字幕内容
- ❌ 不要分析剧情
- ❌ 不要输出中文提示词
- ❌ 不要使用抽象词（emotion, meaning, intelligence, success 等）
- ❌ 不要重复相似构图
- ❌ 不要输出额外说明文字
- ❌ 不要使用模糊描述（好看、美丽、震撼等）

## 输出要求

- 仅输出编号列表
- 不要添加说明文字
- 不要解释你的思考过程
- 直接输出可用的提示词
