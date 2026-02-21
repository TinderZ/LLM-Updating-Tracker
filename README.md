![LLM Model Development Timeline](LLM模型路线图.png)  
*Image source: [A Survey of Reinforcement Learning for Large Reasoning Models](https://arxiv.org/abs/2509.08827)*

# LLM Model Tracker (Keep Updating~)

> [!TIP]
> **网页版已上线！** 访问更美观的在线时间轴：[https://tinderz.github.io/LLM-Tracker/](https://tinderz.github.io/LLM-Tracker/)

A tracker for the latest updates on Large Language Models from various companies.

<!-- LAST_UPDATED_START -->
*Last updated: 2026-02-21*
<!-- LAST_UPDATED_END -->

<!-- TABLE_START -->
| Company      | Model Version                      | Update Date | Improvements & Features                                      |
| :----------- | :--------------------------------- | :---------- | :----------------------------------------------------------- |
| Google<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro) | Gemini 3.1 Pro | 2026-02-19 | Gemini 3 系列升级后的“核心智能”模型，面向需要高级推理的复杂任务（如数据综合与复杂主题解释）；以预览版形式发布，并通过 Gemini API、Vertex AI、Gemini App 与 NotebookLM 等渠道逐步上线。 |
| Anthropic<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://www.anthropic.com/news/claude-sonnet-4-6) | Claude Sonnet 4.6 | 2026-02-17 | Sonnet 系列迄今最强升级：在编码、计算机使用（computer use）、长上下文推理、Agent 规划、知识工作与设计等方面全面提升；API 提供 1M token 上下文窗口（beta）；在 Claude.ai 默认模型，并保持与 Sonnet 4.5 相同定价。 |
| Alibaba<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://www.alibabacloud.com/blog/qwen3-5-towards-native-multimodal-agents_602894) | Qwen3.5（首发开源权重：Qwen3.5-397B-A17B；托管版：Qwen3.5-Plus） | 2026-02-17 | 官方发布 Qwen3.5，并开源首个模型权重 Qwen3.5-397B-A17B（原生视觉-语言模型）。采用混合架构（线性注意力 Gated Delta Networks + 稀疏 MoE），总参数 397B、单次激活 17B，强调推理效率与成本；覆盖推理、编程、Agent 能力与多模态理解等；语言/方言支持从 119 扩展到 201。官方托管模型 Qwen3.5-Plus 通过阿里云 Model Studio 提供，默认 1M 上下文，并带内置工具与自适应工具调用。 |
| ByteDance<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://seed.bytedance.com/en/blog/official-launch-of-seedance-2-0) | Doubao Large Model 2.0 / Seedance 2.0 / Seedream 5.0 Preview | 2026-02-14 | 字节跳动火山引擎在除夕夜发布豆包大模型 2.0，包含基础模型能力和企业级 Agent 功能的重大升级；同时发布 Seedance 2.0 音视频创作模型（支持文本/图片/音频/视频多模态输入，生成15秒带原生音频的高质量多镜头视频）和 Seedream 5.0 预览版图像创作模型。 |
| OpenAI<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://openai.com/index/introducing-gpt-5-3-codex-spark/) | GPT-5.3-Codex-Spark | 2026-02-12 | 面向 Codex 的实时编码超低延迟模型（研究预览）；运行在 Cerebras WSE-3 芯片上，可达 1000+ tokens/s，比 GPT-5.3-Codex 快约15倍；128k 上下文、仅限文本输入；面向 ChatGPT Pro 用户通过 Codex app/CLI/VS Code 扩展逐步开放。 |

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

