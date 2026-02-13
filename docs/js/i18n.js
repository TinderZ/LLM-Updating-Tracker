/**
 * i18n — Internationalization module
 * Supports: zh (Chinese), en (English)
 */

const I18N = {
    zh: {
        title: 'LLM 模型更新追踪器',
        statsCompanies: '追踪厂商',
        statsModels: '模型总数',
        statsLatest: '最新更新',
        filterLicense: '许可类型',
        filterAll: '全部',
        filterOpen: '开源',
        filterClosed: '闭源',
        filterCompany: '厂商筛选',
        noResults: '没有匹配的结果',
        footerText: 'LLM Model Updates Tracker — 持续追踪前沿 AI 模型动态',
        blogLink: '技术博客',
        openSource: '开源',
        closedSource: '闭源',
        unknown: '未知',
    },
    en: {
        title: 'LLM Model Updates Tracker',
        statsCompanies: 'Companies',
        statsModels: 'Total Models',
        statsLatest: 'Latest Update',
        filterLicense: 'License Type',
        filterAll: 'All',
        filterOpen: 'Open Source',
        filterClosed: 'Closed Source',
        filterCompany: 'Filter by Company',
        noResults: 'No matching results',
        footerText: 'LLM Model Updates Tracker — Tracking cutting-edge AI model releases',
        blogLink: 'Blog',
        openSource: 'Open Source',
        closedSource: 'Closed',
        unknown: 'Unknown',
    }
};

class I18nManager {
    constructor() {
        this.lang = localStorage.getItem('llm-tracker-lang') || 'zh';
    }

    get(key) {
        return (I18N[this.lang] && I18N[this.lang][key]) || key;
    }

    toggle() {
        this.lang = this.lang === 'zh' ? 'en' : 'zh';
        localStorage.setItem('llm-tracker-lang', this.lang);
        this.applyToDOM();
        return this.lang;
    }

    setLang(lang) {
        this.lang = lang;
        localStorage.setItem('llm-tracker-lang', this.lang);
        this.applyToDOM();
    }

    applyToDOM() {
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            const text = this.get(key);
            if (text) el.textContent = text;
        });
        // Update html lang attribute
        document.documentElement.lang = this.lang === 'zh' ? 'zh-CN' : 'en';
        // Update lang toggle button text
        const langBtn = document.getElementById('langToggle');
        if (langBtn) {
            const label = langBtn.querySelector('.lang-label');
            if (label) label.textContent = this.lang === 'zh' ? 'EN' : '中';
        }
    }
}

// Export singleton
const i18n = new I18nManager();
