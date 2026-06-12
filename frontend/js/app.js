/* --- APPLICATION STATE METRICS TRACKER --- */
// Global session counters to maintain real-time telemetry state across dashboard updates
let totalCount = 0;
let positiveCount = 0;
let neutralCount = 0;
let negativeCount = 0;

/* --- DOM ELEMENT INTERACTION NODES --- */
// Capturing core interactive client-side element references for transaction inputs
const feedbackText = document.getElementById('feedback-text');
const runAnalysisBtn = document.getElementById('run-analysis');
const clearTextBtn = document.getElementById('clear-text');

// Capturing state metric score card containers for dynamic numerical rendering
const totalAnalyzedEl = document.getElementById('total-analyzed');
const posCountEl = document.getElementById('pos-count');
const neuCountEl = document.getElementById('neu-count');
const negCountEl = document.getElementById('neg-count');

// Capturing interface notification badges and visual rendering widgets
const sentimentBadge = document.getElementById('sentiment-badge');
const confidencePercentage = document.getElementById('confidence-percentage');
const progressCircle = document.getElementById('progress-circle');
const historyTableBody = document.getElementById('history-table-body');

/* --- ASYNC RUNTIME INFRASTRUCTURE LAYER --- */
// Registering active event interceptor for triggering backend model evaluations
runAnalysisBtn.addEventListener('click', async () => {
    // Extract token payload string and trim extraneous whitespace frames
    const text = feedbackText.value.trim();

    // Client-side validation gate to block null submissions
    if (!text) {
        alert("Please enter some text feedback to analyze!");
        return;
    }

    // Trigger visual pending transitions before network interface dispatch
    sentimentBadge.innerHTML = "ANALYZING...";
    confidencePercentage.innerHTML = "...";

    try {
        /* --- MICROSERVICE API NETWORK DISPATCH --- */
        // Executing non-blocking asynchronous payload transport over localized network loop
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });

        // Demarshalling binary network packets into structural JavaScript JSON literals
        const data = await response.json();
        
        // Handle explicit exceptions returned from backend processing channels
        if (data.error) {
            alert(data.error);
            sentimentBadge.innerHTML = "ERROR";
            return;
        }

        // Standardize returned string fields and provide static fallback vectors
        const detectedSentiment = data.sentiment ? data.sentiment.toLowerCase().trim() : 'neutral'; 
        const confidenceScore = data.confidence || '90%'; 

        // Update foundational telemetry display interfaces
        sentimentBadge.innerHTML = detectedSentiment.toUpperCase();
        confidencePercentage.innerHTML = confidenceScore;

        /* --- DYNAMIC STATE EVALUATION AND COUNTER MUTATION --- */
        // Isolated structural branches evaluating predictive responses to safely update metrics
        if (detectedSentiment === 'positive') {
            sentimentBadge.className = "sentiment-tag positive-text";
            if(progressCircle) progressCircle.style.backgroundColor = "rgba(16, 185, 129, 0.1)";
            
            positiveCount++;
            if(posCountEl) posCountEl.innerHTML = positiveCount;

        } else if (detectedSentiment === 'negative') {
            sentimentBadge.className = "sentiment-tag negative-text";
            if(progressCircle) progressCircle.style.backgroundColor = "rgba(239, 68, 68, 0.1)";
            
            negativeCount++;
            if(negCountEl) negCountEl.innerHTML = negativeCount;

        } else {
            sentimentBadge.className = "sentiment-tag neutral-text";
            if(progressCircle) progressCircle.style.backgroundColor = "rgba(107, 114, 128, 0.1)";
            
            neutralCount++;
            if(neuCountEl) neuCountEl.innerHTML = neutralCount;
        }

        // Increment cumulative global runtime statistics tracker
        totalCount++;
        if(totalAnalyzedEl) totalAnalyzedEl.innerHTML = totalCount;

        /* --- IMMUTABLE LOG APPEND MATRIX --- */
        // Capturing exact runtime performance metrics to write an explicit visual audit record
        const timestamp = new Date().toLocaleTimeString();
        const truncatedText = text.length > 50 ? text.substring(0, 50) + "..." : text;
        
        // Formulating dynamic transactional table row layout structure
        const newRow = `
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); color: #fff;">
                <td style="padding: 12px; font-size: 14px;">${timestamp}</td>
                <td style="padding: 12px; font-size: 14px; max-width: 250px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${truncatedText}</td>
                <td style="padding: 12px;"><span class="badge ${detectedSentiment}" style="padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold;">${detectedSentiment.toUpperCase()}</span></td>
                <td style="padding: 12px; font-size: 14px;">${confidenceScore}</td>
            </tr>
        `;
        
        // Dynamic DOM injection prepending the newest entry directly to the head of the log table
        if (historyTableBody) {
            historyTableBody.insertAdjacentHTML('afterbegin', newRow);
        }

    } catch (error) {
        // Network or infrastructure dependency breakdown trap logic
        console.error("Connection Error:", error);
        sentimentBadge.innerHTML = "ERROR";
        confidencePercentage.innerHTML = "OFFLINE";
    }
});

/* --- WORKSPACE RESET ROUTINE --- */
// Wipes context consoles clean and sets the core visual widgets back to neutral initialization parameters
clearTextBtn.addEventListener('click', () => {
    feedbackText.value = "";
    sentimentBadge.innerHTML = "NEUTRAL";
    confidencePercentage.innerHTML = "0%";
    sentimentBadge.className = "sentiment-tag";
    if(progressCircle) progressCircle.style.backgroundColor = "transparent";
});