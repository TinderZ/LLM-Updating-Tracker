# LLM Model Updates Tracker (Keep Updating~)

A tracker for the latest updates on Large Language Models from various companies.

<!-- LAST_UPDATED_START -->
*Last updated: 2025-08-07*
<!-- LAST_UPDATED_END -->

<!-- TABLE_START -->
| Company      | Model Version                      | Update Date | Improvements & Features                                      |
| :----------- | :--------------------------------- | :---------- | :----------------------------------------------------------- |
| OpenAI | gpt-oss-120b, gpt-oss-20b | 2025-08-05 | Open-weight reasoning models (Apache 2.0 license). gpt-oss-120b (117B params) and gpt-oss-20b (21B params). |
| Anthropic | Claude Opus 4.1 | 2025-08-05 | Drop-in replacement for Opus 4, with hybrid reasoning and extended thinking. |
| Google DeepMind | Genie 3 | 2025-08-05 | Foundation world model that generates real-time interactive 3D environments from text prompts. Research preview. |
| Alibaba | Qwen3-Coder(480B-A35B-Instruct...) | 2025-07-23 |  |
| Alibaba | Qwen3-235B-A22B-2507 | 2025-07-22 |  |
| Moonshot | Kimi-K2 | 2025-07-12 |  |
| xAI | grok4, grok4-heavy | 2025-07-10 |  |
| Moonshot | Kimi-Research | 2025-06-20 |  |
| Google | gemini-2.5-flash-lite-preview-06-05 | 2025-06-18 |  |
| Moonshot | Kimi-Dev-72B | 2025-06-17 | 支持全球最长的上下文窗口，包括 100 万 tokens 输入、8 万 tokens 输出。 A Strong and Open-source Coding LLM for Issue Resolution |
| MiniMax | MiniMax-M1-80k/40k | 2025-06-11 |  |
| Google | gemini-2.5-pro-preview-06-05 | 2025-06-05 |  |
| Deepseek | deepseek-r1-0528 | 2025-05-28 |  |
| Google | gemini-2.5-flash-preview-05-20 | 2025-05-20 |  |
| Anthropic | claude-opus/sonnet-4-20250514 | 2025-05-14 |  |
| Google | gemini-2.5-pro-preview-05-06 | 2025-05-06 |  |
| Alibaba | Qwen3-235B-A22B | 2025-04-29 |  |
| OpenAI | o3-2025-04-16 | 2025-04-16 |  |
| OpenAI | chatgpt-4o-latest-20250326 | 2025-03-26 |  |

<!-- TABLE_END -->

## 🌟 Features

*   **Automatic Updates**: Automatically fetches the latest LLM updates from multiple sources daily via GitHub Actions.
*   **Structured Data**: All model information is stored in an easy-to-parse `scripts/data.json` file.
*   **Community-Driven**: Anyone is welcome to contribute new model information or improve the project.
*   **Clear Overview**: The table in the README provides an at-a-glance view of model release dynamics from major companies.

## ✍️ How to Contribute

We warmly welcome community contributions! You can participate in the following ways:

### 1. Add or Update Model Information

All model data is stored in the `scripts/data.json` file. If you find a new model release or incorrect information, please:

1.  **Fork this repository**
2.  **Modify `scripts/data.json`**: Add or update the corresponding model entry. Please ensure the JSON format is correct.
3.  **(Optional) Update the README**: Run the following command locally to update the table in the README.
    ```bash
    python scripts/update_readme.py
    ```
4.  **Submit a Pull Request**: We will review your contribution as soon as possible.

### 2. Add New Information Sources

Our automatic update script, `scripts/fetch_updates.py`, retrieves information via RSS feeds. If you have good information sources to recommend, you can:

*   Directly modify the `RSS_FEEDS` list in `scripts/fetch_updates.py` and submit a Pull Request.
*   Or, create an [Issue](https://github.com/your-username/your-repository/issues) and tell us the new RSS feed URL.

### 3. Report Issues or Suggest Improvements

If you encounter any problems or have any suggestions for improvement, feel free to submit an [Issue](https://github.com/your-username/your-repository/issues).

## 🤖 Automation

This repository uses GitHub Actions for automated updates.

This repository uses GitHub Actions for automated updates, managed by two separate workflows:

- `.github/workflows/fetch_data.yml`: Periodically fetches the latest model data by running `scripts/fetch_updates.py` and updates `scripts/data.json`.
- `.github/workflows/update_readme.yml`: Periodically updates the `README.md` table by running `scripts/update_readme.py` and creates a pull request with the changes.

## 📄 License

This project is open-sourced under the [MIT License](LICENSE).

