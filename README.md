# LLM Model Updates Tracker

A tracker for the latest updates on Large Language Models from various companies.

*Last updated: 2024-07-24*

| Company      | Model Version                      | Update Date | Improvements & Features                                      |
| :----------- | :--------------------------------- | :---------- | :----------------------------------------------------------- |
| Alibaba      | Qwen3-Coder(480B-A35B-Instruct...) | 07月23日    |                                                              |
| Alibaba      | Qwen3-235B-A22B-2507               | 07月22日    |                                                              |
| Moonshot     | Kimi-K2                            | 07月12日    |                                                              |
| xAI (Grok)   | grok4, grok4-heavy                 | 07月10日    |                                                              |
| Moonshot     | Kimi-Research                      | 06月20日    |                                                              |
| Google       | gemini-2.5-flash-lite-preview-06-05| 06月18日    |                                                              |
| Moonshot     | Kimi-Dev-72B                       | 06月17日    | 支持全球最长的上下文窗口，包括 100 万 tokens 输入、8 万 tokens 输出。 A Strong and Open-source Coding LLM for Issue Resolution |
| MiniMax      | MiniMax-M1-80k/40k                 | 06月11日    |                                                              |
| Google       | gemini-2.5-pro-preview-06-05       | 06月05日    |                                                              |
| Deepseek     | deepseek-r1-0528                   | 05月28日    |                                                              |
| Google       | gemini-2.5-flash-preview-05-20     | 05月20日    |                                                              |
| Anthropic    | claude-opus/sonnet-4-20250514      | 05月14日    |                                                              |
| Google       | gemini-2.5-pro-preview-05-06       | 05月06日    |                                                              |
| Alibaba      | Qwen3-235B-A22B                    | 04月29日    |                                                              |
| OpenAI       | o3-2025-04-16                      | 04月16日    |                                                              |
| OpenAI       | chatgpt-4o-latest-20250326         | 03月26日    |                                                              |


## How to Maintain

This repository is maintained using a Python script that generates this README file from a structured JSON data file.

1.  **Add New Data**: To add a new model update, open `scripts/data.json` and add a new JSON object to the list. Make sure to follow the existing format.

2.  **Update the README**: Run the following command from your project's root directory:

    ```bash
    python scripts/update_readme.py
    ```

    This will regenerate the table in this `README.md` file based on the latest data.

3.  **Commit and Push**: Commit both the updated `scripts/data.json` and the newly generated `README.md` to your GitHub repository.

### Automation with GitHub Actions

For fully automated updates, you can set up a GitHub Actions workflow. Create a file named `.github/workflows/update_readme.yml` with a configuration that runs the `scripts/update_readme.py` script on every push to the main branch.

