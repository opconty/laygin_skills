---
name: ltx-prompt-generator
description: 根据文本描述生成符合 LTX-2.3 最佳实践的提示词，用于文本生成视频。当用户说"生成视频提示词"、"LTX prompt"、"视频提示词"、"制作视频"或类似请求时触发。
---

# LTX-2.3 视频提示词生成技能

## 触发条件
当用户要求生成 LTX-2.3 视频提示词、文本转视频提示词、使用 LTX 生成视频时使用此技能。

## 输入格式

用户提供一段文本描述，可以是：
- 简短的场景描述
- 故事片段
- 对话内容
- 动作序列
- 任意创意文本

## 核心任务

根据用户提供的文本，生成符合 LTX-2.3 最佳实践的**高质量视频提示词**。

**核心原则：动作驱动场景**——所有描述必须围绕"物体/人物在做什么"展开，而非静态描述。

## 提示词结构要求

### 动作描述优先级（必须按此顺序组织）：

1. **核心动作序列**（最高优先级）
   - 从动作直接开始，不要加"场景是"、"画面显示"等前缀
   - 描述动作的**完整流程**：开始 → 进行 → 结束
   - 使用**现在时**动词（running, turns, rises, falls, moves）
   - 强调**动态变化**而非静态状态

2. **动作细节**（高优先级）
   - 身体运动的具体方式（如何移动、速度、力度）
   - 手势、姿态、表情变化
   - 与环境/物体的互动方式
   - 连续动作的衔接（然后、接着、随后）

3. **角色/物体外观**（中优先级）
   - 外观描述必须与动作结合（如"a woman in her 30s wearing a red coat, turning her head slowly"）
   - 不要单独列出外貌特征，要融入动作叙述中

4. **镜头与动作的互动**（高优先级）
   - 镜头运动如何跟随/响应主体动作
   - 视角变化如何配合动作节奏
   - 镜头语言必须服务于动作呈现（如"The camera tracks his run in handheld style"）

5. **背景环境**（低优先级）
   - 环境如何与动作互动（如"dust rises as he runs"、"water ripples as she drinks"）
   - 环境对动作的影响（如"wind blows through her hair"）

6. **灯光与氛围**（最低优先级）
   - 仅在与动作相关时提及（如"golden light catches the sweat on his face"）

### 输出格式：

- **必须为单个连贯段落**（single flowing paragraph）
- **4～8 个句子**
- **200 词以内**
- **使用现在时**（present tense）
- **从动作直接开始**（不要加"场景开始"等前缀）

## 视觉细节（按需添加，必须与动作互动）

### 灯光条件（与动作结合）
- flickering candles（闪烁烛光）→ "the flickering candlelight dances across his face as he turns"
- neon glow（霓虹光）→ "neon signs reflect in puddles as she walks through"
- natural sunlight（自然光）→ "sunlight filters through leaves as the bird takes flight"
- dramatic shadows（戏剧性阴影）→ "shadows lengthen across the wall as he approaches"

### 材质纹理（与动作互动）
- rough stone（粗糙石头）→ "his hands grip the rough stone wall as he climbs"
- smooth metal（光滑金属）→ "water droplets slide down the smooth metal surface"
- worn fabric（磨损布料）→ "she pulls the worn fabric tighter around her shoulders against the wind"
- glossy surfaces（光泽表面）→ "raindrops streak across the glossy car window as the vehicle speeds by"

### 色彩基调（与动作互动）
- vibrant（鲜艳）→ "vibrant flowers sway in the breeze"
- muted（柔和）→ "muted tones deepen as night falls"
- monochromatic（单色）→ "monochromatic palette shifts as smoke rises"
- high contrast（高对比）→ "high contrast shadows stretch as the figure moves across"

### 大气元素（与动作互动）
- fog（雾）→ "thick fog swirls around her ankles as she walks forward"
- rain（雨）→ "raindrops splash against the pavement as he runs"
- dust（尘土）→ "dust clouds rise behind the truck as it speeds away"
- particles（粒子）→ "dust particles float in the air currents as sunlight streams through"
- smoke（烟雾）→ "smoke curls upward from the chimney as wind picks up"

## 技术风格标记（动作与镜头的互动）

### 镜头语言（必须跟随主体动作）
- follows（跟随）→ "the camera follows her as she walks down the hallway"
- tracks（追踪）→ "the camera tracks his movement across the room"
- pans across（横摇）→ "the camera pans across the battlefield, following the soldiers"
- circles around（环绕）→ "the camera circles around the dancer as she spins"
- tilts upward（上摇）→ "the camera tilts upward, following the rocket's trajectory"
- pushes in（推近）→ "the camera pushes in as his expression shifts to shock"
- pulls back（拉远）→ "the camera pulls back, revealing the scale of destruction"
- overhead view（俯拍）→ "the overhead view shows the crowd dispersing in all directions"
- handheld movement（手持）→ "handheld camera shakes as he sprints through the alley"
- over-the-shoulder（过肩）→ "over-the-shoulder shot follows the detective as he approaches the suspect"
- wide establishing shot（全景开场）→ "wide shot establishes the cityscape before zooming to the protagonist"
- static frame（固定镜头）→ "static frame captures the empty room as dust settles"

### 电影特性（与动作配合）
- jittery stop-motion（抖动定格动画）→ "jittery stop-motion effect emphasizes each deliberate step"
- pixelated edges（像素化边缘）→ "pixelated edges pulse as the digital world warps"
- lens flares（镜头光晕）→ "lens flares flare as he turns toward the sunlight"
- film grain（胶片颗粒）→ "film grain adds texture as shadows move across the wall"

### 尺度指示（动作影响空间感）
- expansive（宏大）→ "expansive landscape as the caravan moves across the desert"
- epic（史诗）→ "epic scale reveals the army advancing in formation"
- intimate（亲密）→ "intimate framing as their hands slowly reach for each other"
- claustrophobic（幽闭）→ "claustrophobic angles as the walls close in around him"

### 时间与节奏（动作节奏控制）
- slow motion（慢动作）→ "slow motion captures the water droplets splashing upward"
- time-lapse（延时）→ "time-lapse shows clouds racing across the sky as the sun sets"
- rapid cuts（快速剪辑）→ "rapid cuts between punches heighten the fight's intensity"
- lingering shot（ linger shot）→ "lingering shot holds on the empty chair as curtains billow"
- continuous shot（连续镜头）→ "continuous shot follows the character through multiple rooms"
- freeze-frame（定格）→ "freeze-frame captures the moment of impact"
- fade-in（淡入）→ "fade-in reveals the figure emerging from darkness"
- fade-out（淡出）→ "fade-out as the train disappears into the tunnel"
- seamless transition（无缝转场）→ "seamless transition matches the spinning coin to the moon"
- dynamic movement（动态运动）→ "dynamic movement flows through the crowd as panic spreads"
- sudden stop（突然停止）→ "sudden stop as the car skids to a halt"

### 视觉特效（动作触发效果）
- particle systems（粒子系统）→ "particle effects swirl around her as magic energy builds"
- motion blur（运动模糊）→ "motion blur streaks past as the vehicle accelerates"
- depth of field（景深）→ "shallow depth of field keeps focus on her face as background blurs"

## LTX-2 最佳实践

### ✅ 推荐做法

- **动作驱动**：每个句子都应该描述"正在发生什么"，而非"这是什么"
- **连续动作流**：使用"then"、"as"、"while"、"before"连接动作序列
- **镜头跟随主体**：镜头运动必须响应主体动作（"camera tracks her as she runs"而非独立镜头描述）
- **环境互动**：展示环境如何被动作影响（水花飞溅、尘土飞扬、布料飘动）
- **电影构图**：广角、中景、特写搭配精心设计的灯光、浅景深、自然运动
- **情感表达**：LTX-2 擅长单主体的情感表达、细微手势、面部细腻表现（通过姿势/表情而非情绪词汇）
- **氛围与场景**：天气效果（雾、薄雾、黄金时刻光、柔和阴影、雨、反光、环境纹理）与动作互动
- **清晰的镜头语言**：如"slow dolly in"、"handheld tracking"、"over-the-shoulder"提高一致性
- **风格化美学**：绘画风格、黑色电影、模拟胶片感、时尚杂志、像素动画、超现实主义（需早期声明）
- **灯光与情绪控制**：背光、色彩基调、柔逆光、闪烁灯光比通用情绪词更有效
- **配音**：角色可以用多种语言说话和唱歌（对话需放在引号内，标注语言/口音）

### ❌ 避免事项

- **静态描述**：避免"这是一个..."、"画面中有..."等静态句式
- **内心状态**：避免只用"悲伤"或"困惑"等情绪标签，必须用姿势、手势、面部表情来表现
- **文字和标志**：LTX-2 目前无法生成清晰可读的文字。避免招牌、品牌名、印刷物
- **复杂物理或混乱运动**：非线性或快速旋转动作（如跳跃、抛接）可能导致瑕疵。舞蹈效果较好
- **场景复杂度超载**：角色太多、多层动作、过多物体降低清晰度和模型准确性
- **灯光逻辑不一致**：避免混合冲突光源（如"温暖日落+冷色荧光灯"），除非有明确动机
- **提示词过于复杂**：动作/角色/指令越多，未呈现的概率越高。从简单开始，逐步迭代添加

## 输出要求

- 仅输出最终提示词（英文）
- 不要添加说明、分析或额外文字
- 直接输出可粘贴到 LTX-2 的提示词内容
- 如需，可在提示词后附加简短中文对照说明
