/**
 * app.js — Core logic for LLM Model Updates Tracker
 * Handles: data loading, company/license filtering, timeline rendering
 */

// ============================================================
// Company metadata: brand colors + icon file mapping
// ============================================================
const COMPANY_META = {
    'OpenAI':         { color: '#10a37f', icon: 'openai.svg' },
    'Anthropic':      { color: '#d97757', icon: 'anthropic.svg' },
    'Google':         { color: '#4285f4', icon: 'gemini-color.svg' },
    'Google DeepMind':{ color: '#4285f4', icon: 'gemini-color.svg' },
    'Meta':           { color: '#1d65c1', icon: 'meta-color.svg' },
    'DeepSeek':       { color: '#4d6bfe', icon: 'deepseek-color.svg' },
    'Deepseek':       { color: '#4d6bfe', icon: 'deepseek-color.svg' },
    'Alibaba':        { color: '#ff6a00', icon: 'qwen-color.svg' },
    'Moonshot':       { color: '#5856d6', icon: 'moonshot.svg' },
    'xAI':            { color: '#1da1f2', icon: 'grok.svg' },
    'ByteDance':      { color: '#325ab4', icon: 'bytedance-color.svg' },
    'ZhipuAI':        { color: '#3859ff', icon: 'zhipu-color.svg' },
    'Tencent':        { color: '#07c160', icon: 'tencent-color.svg' },
    'MiniMax':        { color: '#6c5ce7', icon: 'minimax-color.svg' },
    'Mistral':        { color: '#FA520F', icon: 'mistral-color.svg' },
};

// Normalize company names for grouping (e.g., "Deepseek" -> "DeepSeek")
function normalizeCompany(name) {
    const map = {
        'deepseek': 'DeepSeek',
        'google deepmind': 'Google DeepMind',
    };
    return map[name.toLowerCase()] || name;
}

function getCompanyMeta(company) {
    const normalized = normalizeCompany(company);
    return COMPANY_META[normalized] || COMPANY_META[company] || { color: '#666', icon: null };
}

// ============================================================
// Application State
// ============================================================
const state = {
    allData: [],
    selectedCompanies: new Set(),   // empty = show all
    selectedLicense: 'all',         // 'all' | 'open_source' | 'closed_source'
};

// ============================================================
// Data Loading
// ============================================================
async function loadData() {
    try {
        const res = await fetch('data.json');
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const data = await res.json();

        // Normalize dates to YYYY-MM-DD
        data.forEach(item => {
            const parts = item.update_date.split('-');
            if (parts.length === 3) {
                item.update_date = `${parts[0]}-${parts[1].padStart(2, '0')}-${parts[2].padStart(2, '0')}`;
            }
        });

        // Sort by date descending
        data.sort((a, b) => b.update_date.localeCompare(a.update_date));
        state.allData = data;
        return data;
    } catch (err) {
        console.error('Failed to load data:', err);
        return [];
    }
}

// ============================================================
// Stats
// ============================================================
function updateStats(filtered) {
    const companies = new Set(filtered.map(d => normalizeCompany(d.company)));
    document.getElementById('statCompanies').textContent = companies.size;
    document.getElementById('statModels').textContent = filtered.length;
    if (filtered.length > 0) {
        document.getElementById('statLatest').textContent = filtered[0].update_date;
    } else {
        document.getElementById('statLatest').textContent = '-';
    }
}

// ============================================================
// Company Filter Buttons
// ============================================================
function buildCompanyFilters() {
    const container = document.getElementById('companyFilters');
    container.innerHTML = '';

    // Gather unique companies preserving order of first appearance
    const seen = new Set();
    const companies = [];
    for (const item of state.allData) {
        const name = normalizeCompany(item.company);
        if (!seen.has(name)) {
            seen.add(name);
            companies.push(name);
        }
    }

    companies.forEach(company => {
        const meta = getCompanyMeta(company);
        const btn = document.createElement('button');
        btn.className = 'company-btn';
        btn.dataset.company = company;
        btn.style.setProperty('--company-color', meta.color);

        // Icon
        if (meta.icon) {
            const img = document.createElement('img');
            img.className = 'company-icon';
            img.src = `icons/${meta.icon}`;
            img.alt = company;
            img.width = 18;
            img.height = 18;
            img.onerror = function () {
                // Fallback: replace with colored circle with initial
                const span = document.createElement('span');
                span.className = 'company-icon';
                span.style.cssText = `
                    display:inline-flex;align-items:center;justify-content:center;
                    width:18px;height:18px;border-radius:4px;font-size:0.65rem;
                    font-weight:700;color:#fff;background:${meta.color};flex-shrink:0;
                `;
                span.textContent = company.charAt(0);
                this.replaceWith(span);
            };
            btn.appendChild(img);
        } else {
            const span = document.createElement('span');
            span.className = 'company-icon';
            span.style.cssText = `
                display:inline-flex;align-items:center;justify-content:center;
                width:18px;height:18px;border-radius:4px;font-size:0.65rem;
                font-weight:700;color:#fff;background:${meta.color};flex-shrink:0;
            `;
            span.textContent = company.charAt(0);
            btn.appendChild(span);
        }

        const label = document.createElement('span');
        label.textContent = company;
        btn.appendChild(label);

        btn.addEventListener('click', () => toggleCompanyFilter(company, btn));
        container.appendChild(btn);
    });
}

function toggleCompanyFilter(company, btn) {
    if (state.selectedCompanies.has(company)) {
        state.selectedCompanies.delete(company);
        btn.classList.remove('active');
    } else {
        state.selectedCompanies.add(company);
        btn.classList.add('active');
    }
    renderTimeline();
}

// ============================================================
// License Filter
// ============================================================
function initLicenseFilters() {
    document.querySelectorAll('.license-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.license-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            state.selectedLicense = btn.dataset.license;
            renderTimeline();
        });
    });
}

// ============================================================
// Filtering
// ============================================================
function getFilteredData() {
    let data = state.allData;

    // Company filter
    if (state.selectedCompanies.size > 0) {
        data = data.filter(item => state.selectedCompanies.has(normalizeCompany(item.company)));
    }

    // License filter
    if (state.selectedLicense !== 'all') {
        data = data.filter(item => item.license_type === state.selectedLicense);
    }

    return data;
}

// ============================================================
// Timeline Rendering
// ============================================================
function renderTimeline() {
    const filtered = getFilteredData();
    const timeline = document.getElementById('timeline');
    const emptyState = document.getElementById('emptyState');

    if (filtered.length === 0) {
        timeline.style.display = 'none';
        emptyState.style.display = 'flex';
        updateStats(filtered);
        return;
    }

    timeline.style.display = 'block';
    emptyState.style.display = 'none';

    // Group by date
    const groups = new Map();
    for (const item of filtered) {
        const date = item.update_date;
        if (!groups.has(date)) groups.set(date, []);
        groups.get(date).push(item);
    }

    // Build HTML
    let html = '';
    for (const [date, items] of groups) {
        html += `<div class="timeline-date-group">`;
        html += `<div class="timeline-date"><span class="timeline-date-text">${date}</span></div>`;
        html += `<div class="timeline-cards">`;
        for (const item of items) {
            html += renderModelCard(item);
        }
        html += `</div></div>`;
    }

    timeline.innerHTML = html;
    updateStats(filtered);
}

function renderModelCard(item) {
    const meta = getCompanyMeta(item.company);
    const normalized = normalizeCompany(item.company);

    // License badge
    let badgeClass = 'badge-unknown';
    let badgeText = i18n.get('unknown');
    if (item.license_type === 'open_source') {
        badgeClass = 'badge-open';
        badgeText = i18n.get('openSource');
    } else if (item.license_type === 'closed_source') {
        badgeClass = 'badge-closed';
        badgeText = i18n.get('closedSource');
    }

    // Icon html
    const iconHtml = meta.icon
        ? `<img class="card-company-icon" src="icons/${meta.icon}" alt="${normalized}" width="28" height="28"
            onerror="this.outerHTML='<span class=\\'card-company-icon-placeholder\\' style=\\'background:${meta.color}\\'>${normalized.charAt(0)}</span>'">`
        : `<span class="card-company-icon-placeholder" style="background:${meta.color}">${normalized.charAt(0)}</span>`;

    // Features (bilingual)
    const featuresKey = i18n.lang === 'zh' ? 'features_zh' : 'features_en';
    const featuresText = item[featuresKey] || item.features_zh || item.features_en || item.features || '';
    const features = featuresText
        ? `<p class="card-features">${escapeHtml(featuresText)}</p>`
        : '';

    // Blog link
    const blogLink = item.blog_url
        ? `<div class="card-footer">
            <a class="blog-link" href="${escapeHtml(item.blog_url)}" target="_blank" rel="noopener">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                <span data-i18n="blogLink">${i18n.get('blogLink')}</span>
            </a>
           </div>`
        : '';

    return `
    <div class="model-card" style="--card-accent: ${meta.color}">
        <div class="card-header">
            ${iconHtml}
            <div class="card-info">
                <div class="card-company-name">${escapeHtml(normalized)}</div>
                <div class="card-model-name">${escapeHtml(item.model_name)}</div>
            </div>
            <div class="card-badges">
                <span class="badge ${badgeClass}">${badgeText}</span>
            </div>
        </div>
        ${features}
        ${blogLink}
    </div>`;
}

function escapeHtml(str) {
    if (!str) return '';
    return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
}

// ============================================================
// Theme Toggle
// ============================================================
function initTheme() {
    const saved = localStorage.getItem('llm-tracker-theme');
    if (saved) {
        document.documentElement.setAttribute('data-theme', saved);
    }
    // Default is dark (set in HTML)

    document.getElementById('themeToggle').addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('llm-tracker-theme', next);
    });
}

// ============================================================
// Language Toggle
// ============================================================
function initLang() {
    // Apply saved language on load
    i18n.applyToDOM();

    document.getElementById('langToggle').addEventListener('click', () => {
        i18n.toggle();
        // Re-render timeline to update badge texts
        renderTimeline();
    });
}

// ============================================================
// Init
// ============================================================
async function init() {
    initTheme();
    initLang();
    initLicenseFilters();

    await loadData();
    buildCompanyFilters();
    renderTimeline();
}

document.addEventListener('DOMContentLoaded', init);
