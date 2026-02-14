![LLM Model Development Timeline](LLM模型路线图.png)  
*Image source: [A Survey of Reinforcement Learning for Large Reasoning Models](https://arxiv.org/abs/2509.08827)*

# LLM Model Tracker (Keep Updating~)

> [!TIP]
> **网页版已上线！** 访问更美观的在线时间轴：[https://tinderz.github.io/LLM-Tracker/](https://tinderz.github.io/LLM-Tracker/)

A tracker for the latest updates on Large Language Models from various companies.

<!-- LAST_UPDATED_START -->
*Last updated: 2026-02-14*
<!-- LAST_UPDATED_END -->

<!-- TABLE_START -->
| Company      | Model Version                      | Update Date | Improvements & Features                                      |
| :----------- | :--------------------------------- | :---------- | :----------------------------------------------------------- |
| Moonshot<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://kimi-k2.org/zh/blog/15-kimi-k2-thinking-zh) | Kimi-K2-Thinking | 2025-11-07 | 第一代原生支持"边思考，边使用工具"的Thinking Agent，标志着开源AI推理模型的重大突破，将进一步缩小与闭源顶级模型的性能差距。 |
| OpenAI | Sora2 | 2025-10-01 | Sora2 正式发布, 用于生成短视频。 |
| Anthropic<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://www.anthropic.com/news/claude-sonnet-4-5) | Claude-4.5-Sonnet | 2025-09-30 | Claude Sonnet 4.5 is the best coding model in the world. It's the strongest model for building complex agents. It’s the best model at using computers. And it shows substantial gains in reasoning and math. |
| ZhipuAI | GLM-4.6 | 2025-09-30 | 前脚DeepSeek更新到了V3.2，现在智谱又更新了——正式推出GLM-4.6，代码能力直接推到了国内最强。 |
| DeepSeek<br/>[![Blog](https://img.shields.io/badge/Blog-技术报告-blue?style=flat-square&logo=blogger)](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp/blob/main/DeepSeek_V3_2.pdf) | DeepSeek-V3.2-Exp | 2025-09-29 | 假期前一天，熟悉的节奏。 |

*注：README 仅展示最新的 5 条记录。查看完整历史，请访问 [网页版](https://tinderz.github.io/LLM-Model-Updates-Tracker/)。*
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

