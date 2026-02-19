![LLM Model Development Timeline](LLM模型路线图.png)  
*Image source: [A Survey of Reinforcement Learning for Large Reasoning Models](https://arxiv.org/abs/2509.08827)*

# LLM Model Tracker (Keep Updating~)

> [!TIP]
> **网页版已上线！** 访问更美观的在线时间轴：[https://tinderz.github.io/LLM-Tracker/](https://tinderz.github.io/LLM-Tracker/)

A tracker for the latest updates on Large Language Models from various companies.

<!-- LAST_UPDATED_START -->
*Last updated: 2026-02-19*
<!-- LAST_UPDATED_END -->

<!-- TABLE_START -->
| Company      | Model Version                      | Update Date | Improvements & Features                                      |
| :----------- | :--------------------------------- | :---------- | :----------------------------------------------------------- |
| ByteDance<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0) | Doubao Large Model 2.0 / Seedance 2.0 / Seedream 5.0 Preview | 2026-02-14 | 字节跳动火山引擎在除夕夜发布豆包大模型 2.0，包含基础模型能力和企业级 Agent 功能的重大升级；同时发布 Seedance 2.0 音视频创作模型（支持文本/图片/音频/视频多模态输入，生成15秒带原生音频的高质量多镜头视频）和 Seedream 5.0 预览版图像创作模型。 |
| OpenAI<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://openai.com/index/introducing-gpt-5-3-codex-spark/) | GPT-5.3-Codex-Spark | 2026-02-12 | 面向 Codex 的实时编码超低延迟模型（研究预览）；运行在 Cerebras WSE-3 芯片上，可达 1000+ tokens/s，比 GPT-5.3-Codex 快约15倍；128k 上下文、仅限文本输入；面向 ChatGPT Pro 用户通过 Codex app/CLI/VS Code 扩展逐步开放。 |
| Google<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-deep-think/) | Gemini 3 Deep Think (Major Upgrade) | 2026-02-12 | Gemini 3 Deep Think 推理模式重大升级，面向科学/研究/工程难题；采用并行推理同时探索多种假设；在学术基准上表现优异（Humanity's Last Exam 48.4%，ARC-AGI-2 84.6%，Codeforces Elo 3455）；在 Gemini App 向 Google AI Ultra 订阅者开放，并首次通过 API 提供早期访问。 |
| MiniMax<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://www.minimaxi.com/news/minimax-m25) | M2.5 | 2026-02-12 | 230B 总参数 MoE 架构（约 10B 激活），性能接近 GPT-5.2 和 Claude Opus 4.6，成本仅为后者的 1/20。在编程、工具调用与搜索、办公等场景达到 SOTA 表现，优化了复杂任务拆解与思考 token 消耗，任务处理速度显著提升。 |
| ZhipuAI<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://z.ai/blog/glm-5) | GLM-5 | 2026-02-12 | 智谱AI新一代旗舰基座，面向 Agentic Engineering 设计。744B 参数 MoE（40B 激活），28.5T 预训练数据。完全基于华为昇腾芯片与 MindSpore 训练，集成 DeepSeek Sparse Attention。SWE-bench Verified 达 77.8%，权重以 MIT 许可开源。 |

<!-- TABLE_END -->

## 🌟 Features

*   **Intelligent AI Fetching**: Automatically searches and extracts the latest LLM updates daily using LLM (OpenAI/Perplexity) + Web Search.
*   **Web Dashboard**: A beautiful, interactive timeline to explore model updates with filtering and language support.
*   **Structured Data**: All model information is stored in a clean `docs/data.json` file.
*   **Automation**: Managed entirely by GitHub Actions for zero-maintenance updates.

## ✍️ How to Contribute

We warmly welcome community contributions! You can participate in the following ways:

### 1. Add or Update Model Information

All model data is stored in the `docs/data.json` file. If you find a new model release or incorrect information, please:

1.  **Fork this repository**
2.  **Modify `docs/data.json`**: Add or update the corresponding model entry. Please ensure the JSON format is correct.
3.  **(Optional) Update the README**: Run the following command locally to update the table in the README.
    ```bash
    python scripts/update_readme.py
    ```
4.  **Submit a Pull Request**: We will review your contribution as soon as possible.

### 2. Report Issues or Suggest Improvements

If you encounter any problems or have any suggestions for improvement, feel free to submit an [Issue](https://github.com/TinderZ/LLM-Model-Updates-Tracker/issues).

## 🤖 Automation

This repository uses GitHub Actions for automated updates, managed by two separate workflows:

- `.github/workflows/fetch_data.yml`: Periodically searches for the latest model data using AI and updates `docs/data.json`.
- `.github/workflows/update_readme.yml`: Periodically updates the `README.md` table to show the latest entries.


## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

