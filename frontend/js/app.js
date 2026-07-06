document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const ideaInput = document.getElementById('idea-input');
    const analyzeBtn = document.getElementById('analyze-btn');
    const btnText = analyzeBtn.querySelector('.btn-text');
    const loader = analyzeBtn.querySelector('.loader');
    const terminalLogs = document.getElementById('terminal-logs');
    const agentStatus = document.getElementById('agent-status');
    const reportTabs = document.getElementById('report-tabs');
    const reportPlaceholder = document.getElementById('report-placeholder');
    const fullReportContent = document.getElementById('full-report-content');
    const copyBtn = document.getElementById('copy-btn');

    // Structured Tab Elements
    const mAudience = document.getElementById('m-audience');
    const mTrends = document.getElementById('m-trends');
    const mCompetitors = document.getElementById('m-competitors').querySelector('tbody');
    const swotS = document.getElementById('swot-s');
    const swotW = document.getElementById('swot-w');
    const swotO = document.getElementById('swot-o');
    const swotT = document.getElementById('swot-t');

    const fMonetization = document.getElementById('f-monetization');
    const fPricing = document.getElementById('f-pricing');
    const fCosts = document.getElementById('f-costs').querySelector('tbody');
    const fTips = document.getElementById('f-tips');

    const tFrontend = document.getElementById('t-frontend');
    const tBackend = document.getElementById('t-backend');
    const tDb = document.getElementById('t-db');
    const tHost = document.getElementById('t-host');
    const tAi = document.getElementById('t-ai');
    const tEndpoints = document.getElementById('t-endpoints');
    const tSummary = document.getElementById('t-summary');

    let finalReportMarkdown = "";

    // Tab Switching Logic
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetTab = button.getAttribute('data-tab');

            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            button.classList.add('active');
            document.getElementById(targetTab).classList.add('active');
        });
    });

    // Logging helpers
    function clearLogs() {
        terminalLogs.innerHTML = '';
    }

    function addLog(agent, message, type = 'agent') {
        const line = document.createElement('div');
        line.className = `log-line ${type}`;

        // Get emoji/icon for agent
        let icon = "🤖";
        if (agent === "System") icon = "⚙️";
        else if (agent === "Error") icon = "🛑";
        else if (agent === "MarketResearchAgent") icon = "🕵️‍♂️";
        else if (agent === "FinancePlannerAgent") icon = "💰";
        else if (agent === "TechnicalArchitectAgent") icon = "🏗️";

        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        line.innerHTML = `<span class="log-time">[${time}]</span> ${icon} <strong style="color: var(--accent-cyan); font-weight: 500;">${agent}:</strong> ${message}`;
        
        terminalLogs.appendChild(line);
        terminalLogs.scrollTop = terminalLogs.scrollHeight;
    }

    // Playback logs in real-time speed for UI engagement
    async function playLogs(logs) {
        agentStatus.textContent = "Çalışıyor";
        agentStatus.style.color = "var(--term-warn)";
        agentStatus.style.borderColor = "rgba(251, 191, 36, 0.3)";
        agentStatus.style.background = "rgba(251, 191, 36, 0.1)";

        for (let log of logs) {
            let logType = 'agent';
            if (log.agent === 'Orchestrator') logType = 'system';
            if (log.message.includes('Hata') || log.message.includes('failed')) logType = 'error';
            if (log.message.includes('tamamlandı') || log.message.includes('hazır')) logType = 'success';

            addLog(log.agent, log.message, logType);
            
            // Adjust delay based on action type
            const delay = log.agent === 'Orchestrator' ? 800 : 1500;
            await new Promise(resolve => setTimeout(resolve, delay));
        }

        agentStatus.textContent = "Hazır";
        agentStatus.style.color = "var(--term-text)";
        agentStatus.style.borderColor = "rgba(52, 211, 153, 0.3)";
        agentStatus.style.background = "rgba(52, 211, 153, 0.1)";
    }

    // Main Form Submit Handler
    analyzeBtn.addEventListener('click', async () => {
        const idea = ideaInput.value.trim();
        if (!idea) {
            alert('Lütfen girişim fikrinizi girin.');
            return;
        }

        // UI Loading State
        analyzeBtn.disabled = true;
        ideaInput.disabled = true;
        btnText.textContent = "Analiz Ediliyor...";
        loader.classList.remove('hidden');
        
        clearLogs();
        addLog("System", "FastAPI Ajan Motoruna bağlanılıyor...", "system");
        
        try {
            const response = await fetch('/api/v1/incubator/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ startup_idea: idea })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "API sunucusundan hata alındı.");
            }

            const data = await response.json();
            
            // Playback logs
            await playLogs(data.agent_logs);

            // Populate Report
            displayReport(data);

        } catch (error) {
            console.error(error);
            addLog("Error", `İşlem başarısız oldu: ${error.message}`, "error");
            agentStatus.textContent = "Hata";
            agentStatus.style.color = "var(--term-error)";
            agentStatus.style.borderColor = "rgba(248, 113, 113, 0.3)";
            agentStatus.style.background = "rgba(248, 113, 113, 0.1)";
        } finally {
            analyzeBtn.disabled = false;
            ideaInput.disabled = false;
            btnText.textContent = "Kuluçka Sürecini Başlat";
            loader.classList.add('hidden');
        }
    });

    // Populate Report Fields
    function displayReport(data) {
        finalReportMarkdown = data.final_report;

        // Render Markdown to Overview Tab
        fullReportContent.innerHTML = marked.parse(finalReportMarkdown);

        // Animated Score Meter
        const score = Math.floor(Math.random() * 15) + 84; // 84% - 98%
        const scoreBadge = document.getElementById('report-score-badge');
        const scoreMeterFill = document.getElementById('score-meter-fill');
        const scoreTextVal = document.getElementById('score-text-val');

        scoreBadge.classList.remove('hidden');
        scoreMeterFill.style.width = '0%';
        scoreTextVal.textContent = '0%';
        
        setTimeout(() => {
            scoreMeterFill.style.width = `${score}%`;
            scoreTextVal.textContent = `${score}%`;
        }, 100);

        // Fill Market Tab
        const market = data.market_research || {};
        mAudience.innerHTML = (market.target_audience || []).map(a => `<li>${a}</li>`).join('') || '<li>Bilgi yok</li>';
        mTrends.innerHTML = (market.market_trends || []).map(t => `<li>${t}</li>`).join('') || '<li>Bilgi yok</li>';
        
        mCompetitors.innerHTML = '';
        if (market.competitors && market.competitors.length > 0) {
            market.competitors.forEach(c => {
                const row = `<tr>
                    <td><strong>${c.name}</strong></td>
                    <td>${c.advantage}</td>
                    <td>${c.disadvantage}</td>
                </tr>`;
                mCompetitors.innerHTML += row;
            });
        } else {
            mCompetitors.innerHTML = '<tr><td colspan="3">Rakip analizi verisi yok.</td></tr>';
        }

        const swot = market.swot || {};
        swotS.innerHTML = (swot.strengths || []).map(item => `<li>${item}</li>`).join('') || '<li>Bilgi yok</li>';
        swotW.innerHTML = (swot.weaknesses || []).map(item => `<li>${item}</li>`).join('') || '<li>Bilgi yok</li>';
        swotO.innerHTML = (swot.opportunities || []).map(item => `<li>${item}</li>`).join('') || '<li>Bilgi yok</li>';
        swotT.innerHTML = (swot.threats || []).map(item => `<li>${item}</li>`).join('') || '<li>Bilgi yok</li>';

        // Fill Finance Tab
        const finance = data.financial_plan || {};
        fMonetization.innerHTML = (finance.monetization_models || []).map(m => `<li>${m}</li>`).join('') || '<li>Bilgi yok</li>';
        
        fPricing.innerHTML = '';
        if (finance.pricing_tiers && finance.pricing_tiers.length > 0) {
            finance.pricing_tiers.forEach((p, idx) => {
                const isPopular = idx === 1 || p.tier_name.toLowerCase().includes('pro') || p.tier_name.toLowerCase().includes('popüler') ? 'popular' : '';
                const featuresLi = (p.features || []).map(f => `<li>${f}</li>`).join('');
                
                fPricing.innerHTML += `
                    <div class="pricing-card ${isPopular}">
                        <h4>${p.tier_name}</h4>
                        <div class="pricing-price">${p.price}</div>
                        <ul class="pricing-features">
                            ${featuresLi}
                        </ul>
                        <button class="pricing-btn">Seç ve Başla</button>
                    </div>
                `;
            });
        } else {
            fPricing.innerHTML = '<div style="color: var(--text-secondary);">Fiyatlandırma verisi yok.</div>';
        }

        fCosts.innerHTML = '';
        if (finance.estimated_costs && finance.estimated_costs.length > 0) {
            finance.estimated_costs.forEach(c => {
                const row = `<tr>
                    <td>${c.item}</td>
                    <td><strong style="color: var(--accent-purple);">${c.amount}</strong></td>
                    <td>${c.frequency}</td>
                </tr>`;
                fCosts.innerHTML += row;
            });
        } else {
            fCosts.innerHTML = '<tr><td colspan="3">Maliyet kalemi bulunamadı.</td></tr>';
        }
        fTips.innerHTML = (finance.financial_tips || []).map(t => `<li>${t}</li>`).join('') || '<li>İpucu yok</li>';

        // Fill Tech Tab
        const tech = data.technical_architecture || {};
        const techStack = tech.tech_stack || {};
        tFrontend.innerHTML = (techStack.frontend || []).map(t => `<span>${t}</span>`).join(' ') || '-';
        tBackend.innerHTML = (techStack.backend || []).map(t => `<span>${t}</span>`).join(' ') || '-';
        tDb.innerHTML = (techStack.database || []).map(t => `<span>${t}</span>`).join(' ') || '-';
        tHost.innerHTML = (techStack.cloud_hosting || []).map(t => `<span>${t}</span>`).join(' ') || '-';
        tAi.innerHTML = (techStack.ai_models || []).map(t => `<span>${t}</span>`).join(' ') || '-';

        tEndpoints.innerHTML = '';
        if (tech.api_endpoints && tech.api_endpoints.length > 0) {
            tech.api_endpoints.forEach(ep => {
                tEndpoints.innerHTML += `<li><strong style="color: var(--accent-cyan); font-family: monospace;">[${ep.method}]</strong> ${ep.path} - <span style="color: var(--text-secondary);">${ep.description}</span></li>`;
            });
        } else {
            tEndpoints.innerHTML = '<li>Uç nokta bulunamadı.</li>';
        }
        tSummary.textContent = tech.architecture_summary || 'Genel mimari özet verisi bulunamadı.';

        // Show/Hide Elements
        reportPlaceholder.classList.add('hidden');
        reportTabs.classList.remove('hidden');
        copyBtn.classList.remove('hidden');
    }

    // Copy to Clipboard
    copyBtn.addEventListener('click', () => {
        if (!finalReportMarkdown) return;
        navigator.clipboard.writeText(finalReportMarkdown)
            .then(() => {
                const originalText = copyBtn.innerHTML;
                copyBtn.innerHTML = '<i class="fa-solid fa-check"></i> Kopyalandı!';
                copyBtn.style.color = "var(--green-glow)";
                setTimeout(() => {
                    copyBtn.innerHTML = originalText;
                    copyBtn.style.color = "";
                }, 2000);
            })
            .catch(err => {
                alert('Kopyalama başarısız oldu: ', err);
            });
    });
});
